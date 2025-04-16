import os
import sys

# ✅ Ensure local path is included for `mcp` module before any imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import asyncio
import base64
import requests
from dotenv import load_dotenv
from typing import Optional, List
from pydantic import BaseModel
from mcp.server.fastmcp import FastMCP, Context



load_dotenv()

# Highspot API Config
HIGHSPOT_API_BASE = "https://api.highspot.com/v1.0"
HIGHSPOT_API_KEY = os.getenv("HIGHSPOT_API_KEY")
HIGHSPOT_API_SECRET = os.getenv("HIGHSPOT_API_SECRET")

# Combine key:secret and encode to base64
if HIGHSPOT_API_KEY and HIGHSPOT_API_SECRET:
    credentials = f"{HIGHSPOT_API_KEY}:{HIGHSPOT_API_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
else:
    encoded_credentials = ""

# Auth Header
HEADERS = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/json"
}

# MCP Server Init
mcp = FastMCP(
    "highspot-mcp",
    description="MCP server to integrate Claude Desktop with Highspot"
)

# Models
class SpotRequest(BaseModel):
    title: str
    description: Optional[str] = None
    visibility: str = "private"

class PageRequest(BaseModel):
    spot_id: str
    title: str
    description: Optional[str] = None

class ContentRequest(BaseModel):
    spot_id: str
    list_id: Optional[str] = None
    title: str
    url: str

class PermissionRequest(BaseModel):
    spot_id: str
    role: str
    users: List[str]

class PublishRequest(BaseModel):
    spot_id: str

# Claude-compatible tool endpoints
@mcp.tool()
async def authenticate(_: Context) -> dict:
    """Check Highspot authentication."""
    try:
        resp = requests.get(f"{HIGHSPOT_API_BASE}/me", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        return {
            "error": str(e),
            "encoded_auth_hint": encoded_credentials[:10] + "..." if encoded_credentials else "Missing or invalid env vars"
        }

@mcp.tool()
async def create_highspot_spot(ctx: Context, title: str, description: Optional[str] = None, visibility: str = "private") -> dict:
    """Create a new Highspot Spot."""
    payload = {
        "title": title,
        "description": description,
        "visibility": visibility
    }
    resp = requests.post(f"{HIGHSPOT_API_BASE}/spots", headers=HEADERS, json=payload)
    return resp.json()

@mcp.tool()
async def add_highspot_content(ctx: Context, spot_id: str, title: str, url: str, list_id: Optional[str] = None) -> dict:
    """Add a URL link as content to a Highspot Spot."""
    payload = {
        "type": "web_link",
        "url": url
    }
    metadata = {"title": title}
    if list_id:
        metadata["lists"] = [list_id]
    params = {"spot": spot_id, "metadata": metadata}
    resp = requests.post(f"{HIGHSPOT_API_BASE}/items", headers=HEADERS, params=params, json=payload)
    return resp.json()

@mcp.tool()
async def create_highspot_page(ctx: Context, spot_id: str, title: str, description: Optional[str] = None) -> dict:
    """Create a SmartPage in a Highspot Spot."""
    payload = {
        "type": "smartpage",
        "content": {
            "settings": {"kind": "Page"},
            "sections": [],
            "blocks": []
        }
    }
    params = {
        "spot": spot_id,
        "metadata": {
            "title": title,
            "description": description
        }
    }
    resp = requests.post(f"{HIGHSPOT_API_BASE}/items", headers=HEADERS, params=params, json=payload)
    return resp.json()

@mcp.tool()
async def status(_: Context) -> dict:
    """Returns status of the server."""
    return {"status": "HighSpotMCP running and Claude-compatible"}

# Entry Point
async def main():
    transport = os.getenv("TRANSPORT", "stdio")
    if transport == "sse":
        await mcp.run_sse_async()
    else:
        await mcp.run_stdio_async()

if __name__ == "__main__":
    asyncio.run(main())
