# 🛠️ HighSpotMCP Roadmap: Step-by-Step Build Guide (with ChatGPT as Your Pair Programmer)

This is your hands-on buddy guide to building the HighSpotMCP project from scratch using **Visual Studio Code**. We're going slow and clear. You’ve got this.

---

## 🧱 STEP 1: PROJECT SETUP

### ✅ Create a new project folder
```bash
mkdir highspot-mcp-server
cd highspot-mcp-server
```

### ✅ Open in VS Code
```bash
code .
```

### ✅ Create a virtual environment
```bash
python -m venv .venv
```

### ✅ Activate the virtual environment
- macOS/Linux:
```bash
source .venv/bin/activate
```
- Windows:
```bash
.venv\Scripts\activate
```

---

## 📦 STEP 2: INSTALL DEPENDENCIES
```bash
pip install fastapi uvicorn python-dotenv requests
```

---

## 📄 STEP 3: CREATE KEY FILES

### 🔹 `main.py`
This is your FastAPI server (copy/paste from `Highspot Mcp Server` file in this project).

### 🔹 `.env`
Create this in the root of your project:
```
HIGHSPOT_API_KEY=your_base64_encoded_key_here
```

> 🔐 NOTE: Your API key is your Highspot email:password encoded in base64. Example: `echo -n 'email:password' | base64`

---

## 🧪 STEP 4: RUN YOUR SERVER
```bash
uvicorn main:app --reload
```
Open `http://127.0.0.1:8000/docs` in your browser — that’s your Swagger UI playground.

---

## 📡 STEP 5: CONNECT CLAUDE DESKTOP (LATER)
Once the server is working, we’ll configure Claude Desktop to call it using either `sse` or `stdio`. This comes in Phase 2.

---

## 📌 NEXT STEPS (after MVP is live)
- Add logging and error handling
- Implement token rotation
- Add draft publishing
- Add Docker support for deployment

---

## 💬 Use this roadmap as your checklist and journaling space. We'll build together!
