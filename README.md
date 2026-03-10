# MCP vs Agentic AI Travel Assistant

A comparison demonstration project showing the architectural differences between **Model Context Protocol (MCP)** and **Agentic AI** approaches for building a travel assistant application.

## 📋 Project Overview

This project implements two different architectures for a travel planning assistant:

1. **MCP Architecture**: 
   - Externalized tools with explicit JSON schemas
   - Protocol-level server/session handshake
   - Stateless tool calls coordinated through context
   - Pattern: `Request → Context → Tool Call → Structured Response`

2. **Agentic AI Architecture**:
   - Internal planner + memory + executor loop
   - Goal decomposition into subtasks
   - Iterative reasoning with reflection
   - Pattern: `Observe → Plan → Act → Reflect loop`

## 🎯 Key Features

- **Side-by-side comparison** of two modern AI agent architectures
- **Mock travel tools** for flight and hotel searches
- **Pluggable adapter pattern** for easy provider swaps
- **Structured workflows** demonstrating distinct reasoning patterns
- **Type-safe implementation** using Python dataclasses and type hints

## 🛠️ Project Structure

```
.
├── main.py                    # CLI demo - runs both architectures
├── app.py                     # Flask web server for chat interface
├── models.py                  # Shared data models (TravelRequest, WorkflowResult)
├── tools.py                   # Travel tool specifications and execution logic
├── adapters.py                # Tool adapter interfaces and mock implementations
├── mcp_agent_init.py         # MCP agent initialization
├── mcp_workflow.py           # MCP workflow runner
├── agentic_agent_init.py     # Agentic AI agent initialization
├── agentic_workflow.py       # Agentic AI workflow runner
├── static/                    # Web interface files
│   ├── index.html            # Main chat interface
│   ├── style.css             # Modern UI styling
│   └── script.js             # Chat functionality
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 📦 Requirements

- **Python 3.10+** (required for union type syntax `|`)
- **Flask 3.0+** and **Flask-CORS** (for web interface)
- No other external dependencies needed

## 🚀 Installation & Setup

### 1. Clone or download this project

```powershell
cd "e:\mcp vs agentic ai travel agent"
```

### 2. Verify Python version

```powershell
python --version
```

**Note**: Ensure you have Python 3.10 or higher. If not, download it from [python.org](https://www.python.org/downloads/).

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

This will install Flask and Flask-CORS for the web interface.

### 4. (Optional but Recommended) Use a virtual environment

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install dependencies in virtual environment
pip install -r requirements.txt
```

## ▶️ Running the Project

### Option 1: Interactive Web Interface (Recommended) 🌐

Run the Flask web server to access the dual chatbot interface:

```powershell
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

**Features of the web interface:**
- 💬 **Dual chat windows** - Compare MCP and Agentic AI side-by-side
- 🚀 **Quick action buttons** - Test common queries with one click
- 📊 **Real-time responses** - See how each architecture processes requests
- 🔄 **Reset conversations** - Start fresh anytime
- ℹ️ **Architecture info** - View detailed agent specifications

### Option 2: Command-Line Demo

Run the original CLI demo to see both architectures in action:

```powershell
python main.py
```

This will execute both agents with a sample travel request and display the results.

## 📊 Expected Output

### Web Interface Output:

When you run `python app.py` and open http://localhost:5000, you'll see:

- **Left Panel**: MCP Agent chatbot with blue theme
- **Right Panel**: Agentic AI chatbot with purple theme
- **Quick Actions**: Pre-configured test queries
- **Architecture Info**: Detailed comparison modal

You can:
1. Ask questions to either agent individually
2. Use quick action buttons to send the same query to both agents
3. Compare how each architecture processes and responds
4. View real-time differences in their reasoning approaches

### CLI Demo Output:

The program will display:

1. **MCP Agent Initialization** - Architecture description
2. **Agentic AI Agent Initialization** - Architecture description
3. **MCP Workflow Run** - Step-by-step execution with results
4. **Agentic Workflow Run** - Step-by-step execution with results

### Sample Output:
```
=== MCP Agent Initialization ===
{
  'agent': 'MCPTravelAssistant',
  'architecture': 'Model Context Protocol (MCP)',
  'tool_integration': 'External tools exposed via MCP server + JSON schemas',
  'reasoning_workflow': 'Model delegates actions as protocol tool calls',
  'task_pattern': 'Request -> Context -> Tool Call -> Structured Response',
  'tool_count': 2,
  'server_endpoint': 'mcp://travel-tools'
}

=== Agentic AI Agent Initialization ===
{
  'agent': 'AgenticTravelAssistant',
  'architecture': 'Agentic AI',
  'tool_integration': 'Tools invoked by internal planner/executor decisions',
  'reasoning_workflow': 'Observe -> Plan -> Act -> Reflect loop',
  'task_pattern': 'Goal -> Subtasks -> Tool Actions -> Final Itinerary',
  'tool_count': 2,
  'max_iterations': 6
}

=== Next Step: MCP Workflow Run ===
{
  'architecture': 'MCP',
  'summary': 'Selected 1 flight option and 1 hotel option for Singapore. (flight=FL-102, hotel=HT-77)',
  'steps': [
    "MCP tool call -> search_flights {'origin': 'Colombo', 'destination': 'Singapore', 'date': '2026-04-15'}",
    "MCP tool call -> search_hotels {'city': 'Singapore', 'check_in': '2026-04-15', 'check_out': '2026-04-20'}",
    'MCP response synthesis from structured tool outputs'
  ]
}

=== Next Step: Agentic Workflow Run ===
{
  'architecture': 'Agentic AI',
  'summary': 'Draft itinerary ready for Singapore. Top picks: FL-102 + HT-77',
  'steps': [
    'Observe: parse user intent and constraints',
    "Plan: generated subtasks ['find best outbound flight', 'find central hotel near business district', 'merge into draft itinerary']",
    'Act: searched flights',
    'Act: searched hotels',
    'Reflect: confidence improved after tool evidence'
  ]
}
```

## 🔧 Customization

### Web Interface Queries

Ask the chatbots questions like:
- "Find flights from Colombo to Singapore"
- "Search hotels in Singapore"
- "Plan a trip to Tokyo"
- "What can you help me with?"

The agents will respond based on their architectural patterns:
- **MCP**: Direct protocol-based tool calls
- **Agentic AI**: Observe-Plan-Act-Reflect loop

### Modify CLI Travel Request

Edit the request in [main.py](main.py#L13-L18):

```python
request = TravelRequest(
    origin="Your City",
    destination="Your Destination",
    depart_date="YYYY-MM-DD",
    return_date="YYYY-MM-DD",
)
```

### Add Real API Integration

Replace `MockTravelToolsAdapter` in [adapters.py](adapters.py) with real API implementations:

```python
class RealTravelToolsAdapter:
    def search_flights(self, origin: str, destination: str, date: str):
        # Call real flight API
        pass
    
    def search_hotels(self, city: str, check_in: str, check_out: str):
        # Call real hotel API
        pass
```

## 🎓 Learning Goals

This project demonstrates:

1. **Architectural Patterns**: How MCP and Agentic AI differ in design
2. **Tool Integration**: Different approaches to external tool usage
3. **Workflow Orchestration**: Protocol-based vs. autonomous loop execution
4. **Type Safety**: Using Python's type system for robust code
5. **Adapter Pattern**: Clean separation between logic and external providers

## 📝 Notes

- This is a **demonstration project** focusing on architecture patterns
- Uses **mock data** - no real API calls are made
- Tools are intentionally simple to highlight architectural differences
- Both approaches produce similar results with different execution patterns

## 🤝 Contributing

Feel free to extend this project by:
- Adding more travel tools (car rentals, activities, etc.)
- Implementing real API integrations
- Adding error recovery strategies
- Implementing user preference learning
- Adding cost optimization logic

## 📄 License

This is a demonstration/educational project.

---

**Happy Coding!** 🚀✈️🏨
