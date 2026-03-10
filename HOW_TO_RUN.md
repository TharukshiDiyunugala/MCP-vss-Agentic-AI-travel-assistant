# 🚀 HOW TO RUN - Complete Instructions

## Quick Start (2 Steps)

### For Web Interface (Recommended):
```powershell
pip install -r requirements.txt
python app.py
```
Then open: **http://localhost:5000**

### For CLI Demo:
```powershell
python main.py
```

---

## 📦 What You Just Got

Your project now has **TWO ways** to experience the MCP vs Agentic AI comparison:

### 1. 🌐 Interactive Web Interface (NEW!)
- **File**: `app.py`
- **Access**: http://localhost:5000
- **Features**:
  - Side-by-side chatbots
  - Real-time interaction
  - Visual comparison
  - Quick test queries

### 2. 📟 Command Line Demo (Original)
- **File**: `main.py`
- **Features**:
  - Quick execution
  - Detailed output
  - No browser needed

---

## 📂 Complete File Structure

```
e:\mcp vs agentic ai travel agent\
│
├── 🌐 WEB INTERFACE FILES
│   ├── app.py                    ← Flask backend server
│   └── static/
│       ├── index.html            ← Chat interface
│       ├── style.css             ← Modern styling
│       └── script.js             ← Chat functionality
│
├── 🤖 CORE AGENT FILES
│   ├── main.py                   ← CLI demo entrypoint
│   ├── models.py                 ← Data models
│   ├── tools.py                  ← Travel tools
│   ├── adapters.py               ← Mock providers
│   ├── mcp_agent_init.py         ← MCP initialization
│   ├── mcp_workflow.py           ← MCP workflow
│   ├── agentic_agent_init.py     ← Agentic initialization
│   └── agentic_workflow.py       ← Agentic workflow
│
├── 📚 DOCUMENTATION
│   ├── README.md                 ← Complete project docs
│   ├── WEB_GUIDE.md              ← Web interface guide
│   ├── QUICKSTART.txt            ← Quick reference
│   └── HOW_TO_RUN.md             ← This file!
│
└── ⚙️ CONFIGURATION
    ├── requirements.txt          ← Dependencies
    └── .gitignore               ← Git ignore rules
```

---

## 🎯 Step-by-Step: Web Interface

### Step 1: Install Dependencies
```powershell
cd "e:\mcp vs agentic ai travel agent"
pip install -r requirements.txt
```

**What this installs:**
- Flask (web framework)
- Flask-CORS (cross-origin support)

### Step 2: Start the Server
```powershell
python app.py
```

**You'll see:**
```
============================================================
🚀 MCP vs Agentic AI Travel Assistant - Web Interface
============================================================

📡 Server starting at: http://localhost:5000

🤖 Two agents ready:
   • MCP Agent: Protocol-based tool coordination
   • Agentic AI: Autonomous planning loop
```

### Step 3: Open Your Browser
Navigate to: **http://localhost:5000**

### Step 4: Interact with Both Agents!

**Try these:**
1. Click "✈️ Search Flights" - sends query to BOTH agents
2. Click "🏨 Search Hotels" - compare responses
3. Click "🗺️ Plan Trip" - see different planning approaches
4. Type your own queries in either chat box

### Step 5: Stop the Server
When done, press **Ctrl+C** in the terminal

---

## 🎯 Step-by-Step: CLI Demo

### Just Run It
```powershell
python main.py
```

**That's it!** 

You'll see:
1. MCP Agent architecture description
2. Agentic AI architecture description
3. MCP workflow execution
4. Agentic workflow execution

---

## 🔍 What Makes Them Different?

### MCP Agent (Blue) 
```
User: "Find flights to Singapore"
  ↓
MCP Protocol Tool Call
  ↓
search_flights(origin, destination, date)
  ↓
Structured JSON Response
  ↓
Result displayed
```

**Key Traits:**
- ✅ Fast and efficient
- ✅ Protocol-based
- ✅ Stateless
- ✅ Explicit tool calls visible

### Agentic AI (Purple)
```
User: "Find flights to Singapore"
  ↓
OBSERVE: Parse intent
  ↓
PLAN: Create subtasks
  ↓
ACT: Execute tools
  ↓
REFLECT: Evaluate results
  ↓
Response with reasoning
```

**Key Traits:**
- ✅ Reasoning visible
- ✅ Memory-aware
- ✅ Self-correcting
- ✅ Planning-focused

---

## 💬 Example Queries to Try

### Flight Searches
- "Find flights from Colombo to Singapore"
- "Search for flights to Tokyo"
- "Show me flight options"

### Hotel Searches  
- "Search hotels in Singapore"
- "Find accommodation in Tokyo"
- "I need a hotel"

### Trip Planning
- "Plan a trip to Tokyo"
- "Create an itinerary for Singapore"
- "I want to travel to Paris"

### General
- "What can you help me with?"
- "Tell me about yourself"
- "How do you work?"

---

## 🎨 Web Interface Features

### 🖼️ Layout
- **Left Panel**: MCP Agent (Blue theme)
- **Right Panel**: Agentic AI (Purple theme)
- **Top**: Quick action buttons
- **Header**: Info and reset buttons

### ⚡ Quick Actions
Click these to send the same query to BOTH agents:
- **✈️ Search Flights**
- **🏨 Search Hotels**
- **🗺️ Plan Trip**
- **💡 Capabilities**

### 🔧 Controls
- **🔄 Reset Chat**: Clear all conversations
- **ℹ️ Info**: View architecture details

### 🎯 Watch For
- Different response structures
- Varying levels of detail
- Reasoning process vs direct execution
- Speed differences

---

## 📊 Sample Interaction

**Your Query:** "Find flights from Colombo to Singapore"

**MCP Response:**
```
✈️ MCP Flight Search

Protocol: Executed `search_flights` tool via MCP server

Result:
- Flight ID: FL-102
- Route: Colombo → Singapore  
- Date: 2026-04-15
- Price: $420
- Provider: mock-provider

*MCP approach: Direct tool call with structured response*
```

**Agentic AI Response:**
```
✈️ Agentic Flight Search

Observe: Analyzing your request for flight information

Plan: Breaking down into subtasks:
  1. Identify origin and destination
  2. Search available flights
  3. Rank by price and convenience

Act: Executed flight search tool

Result:
- Flight ID: FL-102
- Route: Colombo → Singapore
- Date: 2026-04-15
- Price: $420

Reflect: Found 1 option(s). Confidence: High ✓

*Agentic approach: Autonomous reasoning with self-reflection*
```

**Notice the difference?**
- MCP: Direct and efficient
- Agentic: Detailed reasoning process

---

## ❓ FAQ

### Q: Which interface should I use?
**A:** Web interface is recommended for interactive exploration. CLI is great for quick tests.

### Q: Do I need an API key?
**A:** No! This uses mock data for demonstration.

### Q: Can I add real APIs?
**A:** Yes! Edit `adapters.py` to add real flight/hotel APIs.

### Q: Why are responses pre-configured?
**A:** This is a demo focusing on architectural patterns, not live data.

### Q: Can I customize the agents?
**A:** Yes! Edit `app.py` to modify responses and behavior.

### Q: Does this use AI/LLM?
**A:** No, this demonstrates architecture patterns with mock responses.

---

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```powershell
pip install -r requirements.txt
```

### Problem: Can't access http://localhost:5000
**Solution:**
1. Verify Flask is running (`python app.py`)
2. Check if port 5000 is free
3. Try http://127.0.0.1:5000 instead

### Problem: Agents not responding in web interface
**Solution:**
1. Check browser console (F12)
2. Verify Flask server is running
3. Try refreshing the page

### Problem: "Address already in use"
**Solution:**
1. Another app is using port 5000
2. Stop it or change port in `app.py`:
   ```python
   app.run(debug=True, port=5001)  # Use different port
   ```

---

## 🎓 Learning Path

1. **Start with CLI** (`python main.py`)
   - Understand basic architecture differences
   - See complete workflow execution

2. **Explore Web Interface** (`python app.py`)
   - Interactive comparison
   - Real-time responses
   - Visual understanding

3. **Read the Docs**
   - [README.md](README.md) - Complete overview
   - [WEB_GUIDE.md](WEB_GUIDE.md) - Web interface details
   - Code files - Implementation details

4. **Experiment**
   - Modify queries
   - Change responses
   - Add new features

---

## 🚀 Next Steps

### As a Learner:
1. ✅ Run both interfaces
2. ✅ Compare the responses
3. ✅ Read the source code
4. ✅ Understand architectural differences

### As a Developer:
1. 🔧 Add real API integrations
2. 🔧 Enhance NLP capabilities
3. 🔧 Add more travel tools
4. 🔧 Implement user authentication
5. 🔧 Deploy to production

---

## 📞 Support

- **Documentation**: See [README.md](README.md)
- **Web Guide**: See [WEB_GUIDE.md](WEB_GUIDE.md)
- **Quick Start**: See [QUICKSTART.txt](QUICKSTART.txt)
- **GitHub**: [Repository](https://github.com/TharukshiDiyunugala/MCP-vss-Agentic-AI-travel-assistant)

---

## ✅ Quick Checklist

Before you start:
- [ ] Python 3.10+ installed
- [ ] In correct directory (`e:\mcp vs agentic ai travel agent`)
- [ ] Dependencies installed (`pip install -r requirements.txt`)

For web interface:
- [ ] Flask server running (`python app.py`)
- [ ] Browser open to http://localhost:5000
- [ ] Both chat panels visible

For CLI:
- [ ] Just run `python main.py`

---

**You're all set! Enjoy exploring MCP vs Agentic AI architectures!** 🎉

Choose your adventure:
- 🌐 **Web**: `python app.py` → http://localhost:5000
- 📟 **CLI**: `python main.py`
