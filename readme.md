# HighSpotMCP: Claude Desktop to Highspot Automation Server

## 🚀 What We're Building
A lightweight Python server that lets Claude Desktop automate actions in your Highspot instance via the Highspot API. This project bridges Claude’s structured document analysis capabilities with Highspot’s content management features.

### 🔧 Key Use Cases
- Upload a document into Claude Desktop
- Claude extracts structure and content
- Claude calls this MCP server
- This server creates Spots, SmartPages, and uploads content to Highspot automatically

### 🧩 Tech Stack
- **Python 3.12+**
- **FastAPI** for server endpoints
- **Highspot API** for content creation
- **Claude Desktop** as the client (via MCP tooling)

### 📦 Endpoints
| Endpoint          | Purpose                         |
|------------------|---------------------------------|
| `/authenticate`  | Confirm Highspot credentials    |
| `/create-spot`   | Create a new Highspot Spot      |
| `/create-page`   | Create a SmartPage in a Spot    |
| `/add-content`   | Add a URL/link as content       |
| `/set-permissions` | Share Spot with users/groups |
| `/publish-draft` | Mock: finalize a Spot draft     |
| `/status`        | Ping server for health          |

### 🛠️ Setup Instructions
Use the `ROADMAP.md` file for a complete walkthrough to build and run this locally.

### 📁 Directory Structure
```bash
highspot-mcp-server/
├── .env                # Your environment config
├── main.py             # Main server implementation
├── README.md           # This file
├── ROADMAP.md          # Step-by-step coding buddy guide
```

---

## ⚙️ Requirements
- API key from Highspot (base64 encoded user:password)
- Python 3.12+
- Visual Studio Code (or any IDE)
- `uvicorn`, `fastapi`, `python-dotenv`, `requests` libraries

---

## 💬 Want to Contribute?
This is a solo project guided by Claude or ChatGPT. PRs welcome if you’re following the vision 😎

---

## 🧠 Author
**shonesque** – [https://github.com/shonesque](https://github.com/shonesque)
## 🎖️ Certified by MCP Review
## 🔗 MCP Review Page - [https://mcpreview.com/mcp-servers/shonesque/hs-mcp-server](https://mcpreview.com/mcp-servers/shonesque/hs-mcp-server)
