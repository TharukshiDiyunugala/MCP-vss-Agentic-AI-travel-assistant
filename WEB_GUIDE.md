# Web Interface Usage Guide

## 🌐 MCP vs Agentic AI - Interactive Chat Interface

This guide will help you get the most out of the dual chatbot web interface.

---

## 📖 Getting Started

### 1. Start the Server

```powershell
python app.py
```

You should see:
```
============================================================
🚀 MCP vs Agentic AI Travel Assistant - Web Interface
============================================================

📡 Server starting at: http://localhost:5000

🤖 Two agents ready:
   • MCP Agent: Protocol-based tool coordination
   • Agentic AI: Autonomous planning loop

💡 Try asking:
   • 'Find flights from Colombo to Singapore'
   • 'Search hotels in Singapore'
   • 'Plan a trip to Tokyo'

============================================================
```

### 2. Open the Interface

Navigate to **http://localhost:5000** in your web browser.

---

## 🎨 Interface Overview

### Left Panel: MCP Agent (Blue Theme)
- **Architecture**: Model Context Protocol
- **Approach**: Protocol-based, stateless tool calls
- **Pattern**: Request → Context → Tool Call → Response

### Right Panel: Agentic AI (Purple Theme)
- **Architecture**: Autonomous Agent
- **Approach**: Planning loop with reflection
- **Pattern**: Observe → Plan → Act → Reflect

---

## 💬 Using the Chatbots

### Individual Conversations

1. **Type a message** in either chat input box
2. **Press Enter** or click the **Send** button
3. Watch how that specific agent processes your request

### Simultaneous Comparison

Use the **Quick Action Buttons** to send the same query to both agents:
- **✈️ Search Flights** - Compare flight search approaches
- **🏨 Search Hotels** - Compare hotel search methods
- **🗺️ Plan Trip** - Compare complete trip planning
- **💡 Capabilities** - See what each agent can do

---

## 🔍 What to Look For

### MCP Agent Shows:
✓ **Explicit protocol calls** - "MCP tool call -> search_flights"
✓ **Structured payloads** - JSON-like request data
✓ **Direct execution** - Minimal reasoning overhead
✓ **Stateless operations** - No conversation memory

**Example Response:**
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

### Agentic AI Shows:
✓ **Planning steps** - "Observe", "Plan", "Act", "Reflect"
✓ **Subtask breakdown** - Goal decomposition
✓ **Reasoning process** - Why and how decisions are made
✓ **Self-reflection** - Confidence scores and quality checks

**Example Response:**
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

---

## 📊 Comparison Insights

| Aspect | MCP Agent | Agentic AI |
|--------|-----------|------------|
| **Execution Style** | Direct & efficient | Deliberate & thorough |
| **Visibility** | Technical (protocols) | Conceptual (reasoning) |
| **Response Time** | Faster | Slightly slower (more steps) |
| **Context Awareness** | Stateless | Memory-informed |
| **Transparency** | Tool calls visible | Thought process visible |
| **Best For** | Known workflows | Complex planning |

---

## 🎯 Test Scenarios

### Scenario 1: Simple Flight Search
**Query**: "Find flights from Colombo to Singapore"

**Compare**:
- How quickly each agent responds
- Structure of the response
- Amount of detail provided

### Scenario 2: Hotel Search
**Query**: "Search hotels in Singapore"

**Compare**:
- How each agent interprets the request
- What additional context they provide
- Their recommendation approach

### Scenario 3: Complete Trip Planning
**Query**: "Plan a trip to Tokyo"

**Compare**:
- How they break down the task
- Sequencing of operations
- Comprehensiveness of the plan

### Scenario 4: Capability Discovery
**Query**: "What can you help me with?"

**Compare**:
- How they describe themselves
- Clarity of capabilities
- Architectural explanation

---

## 🔧 Advanced Features

### Architecture Info Modal
Click the **ℹ️ Info** button to see:
- Complete agent specifications
- Tool registry details
- Configuration parameters
- Workflow patterns

### Reset Conversations
Click the **🔄 Reset Chat** button to:
- Clear all message history
- Start fresh conversations
- Reset both agents simultaneously

### Browser Console
Open browser DevTools (F12) to see:
- API request/response logs
- Performance metrics
- Debug information

---

## 💡 Tips for Best Experience

1. **Start Simple**: Try quick action buttons first
2. **Compare Side-by-Side**: Use the same query for both agents
3. **Read Carefully**: Notice the architectural differences
4. **Experiment**: Try different query phrasings
5. **Observe Patterns**: See consistency in agent behaviors

---

## 🚫 Limitations (Demo Mode)

This is a **demonstration** project with mock data:
- ❌ No real API calls to flight/hotel services
- ❌ Limited natural language processing
- ❌ Simplified intent extraction
- ❌ Pre-configured responses
- ✅ Perfect for understanding architectural patterns!

---

## 🛑 Stopping the Server

When you're done:
1. Go to the terminal running `python app.py`
2. Press **Ctrl+C**
3. The server will shut down gracefully

---

## 🐛 Troubleshooting

### Issue: Can't connect to http://localhost:5000
**Solution**: Make sure Flask server is running (`python app.py`)

### Issue: Agents not responding
**Solution**: 
1. Check browser console for errors (F12)
2. Verify server is running
3. Try resetting the conversation

### Issue: Responses look wrong
**Solution**: The agents use mock data - this is expected behavior!

### Issue: Page doesn't load
**Solution**: 
1. Check if port 5000 is available
2. Try a different browser
3. Clear browser cache

---

## 📚 Learn More

- Read [README.md](../README.md) for project overview
- Explore [app.py](../app.py) for backend logic
- Check [static/script.js](../static/script.js) for frontend code
- Review [models.py](../models.py) for data structures

---

## 🎓 Educational Value

This interface teaches:
1. **Architectural Patterns** - MCP vs Agentic AI
2. **Tool Integration** - Different approaches to external tools
3. **Workflow Design** - Stateless vs. stateful execution
4. **User Experience** - How architecture affects interactions
5. **API Design** - RESTful endpoints for AI agents

---

**Enjoy exploring the differences between MCP and Agentic AI architectures!** 🚀

For questions or improvements, check the [GitHub repository](https://github.com/TharukshiDiyunugala/MCP-vss-Agentic-AI-travel-assistant).
