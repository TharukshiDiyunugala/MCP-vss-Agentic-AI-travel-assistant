"""Flask web server for dual chatbot interface.

Provides REST API endpoints for both MCP and Agentic AI travel agents.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from typing import Dict, Any, List
from datetime import datetime

from adapters import MockTravelToolsAdapter
from agentic_workflow import AgenticWorkflowRunner
from agentic_agent_init import AgenticTravelAgentInitializer
from mcp_workflow import MCPWorkflowRunner
from mcp_agent_init import MCPTravelAgentInitializer
from models import TravelRequest, WorkflowResult
from tools import execute_tool, ToolValidationError, ToolExecutionError

app = Flask(__name__, static_folder='static', template_folder='static')
CORS(app)

# Initialize both agents
mcp_agent = MCPTravelAgentInitializer().initialize()
agentic_agent = AgenticTravelAgentInitializer().initialize()
adapter = MockTravelToolsAdapter()

# Store conversation history
conversation_history: Dict[str, List[Dict[str, str]]] = {
    "mcp": [],
    "agentic": []
}


def extract_travel_intent(message: str) -> Dict[str, Any] | None:
    """Simple intent extraction from user message.
    
    In a real application, you'd use NLP/LLM for this.
    For demo purposes, we'll look for keywords.
    """
    message_lower = message.lower()
    
    # Check for flight search intent
    if any(word in message_lower for word in ["flight", "fly", "plane", "ticket"]):
        # Try to extract cities and dates (simplified)
        result = {
            "intent": "search_flights",
            "message": message
        }
        return result
    
    # Check for hotel search intent
    if any(word in message_lower for word in ["hotel", "accommodation", "stay", "room"]):
        result = {
            "intent": "search_hotels",
            "message": message
        }
        return result
    
    # Check for trip planning intent
    if any(word in message_lower for word in ["trip", "travel", "plan", "visit", "vacation"]):
        result = {
            "intent": "plan_trip",
            "message": message
        }
        return result
    
    return None


def generate_mcp_response(message: str, intent: Dict[str, Any] | None) -> str:
    """Generate response using MCP architecture."""
    if not intent:
        return (
            "🤖 **MCP Agent**: I'm a travel assistant using the Model Context Protocol. "
            "I can help you search for flights, hotels, or plan complete trips. "
            "Try asking me: 'Find flights from Colombo to Singapore' or 'Plan a trip to Tokyo'"
        )
    
    if intent["intent"] == "search_flights":
        # Default example
        flights = execute_tool(
            "search_flights",
            {
                "origin": "Colombo",
                "destination": "Singapore",
                "date": "2026-04-15"
            },
            adapter
        )
        flight = flights[0]
        response = (
            f"✈️ **MCP Flight Search**\n\n"
            f"**Protocol**: Executed `search_flights` tool via MCP server\n\n"
            f"**Result**:\n"
            f"- Flight ID: {flight['flight_id']}\n"
            f"- Route: {flight['origin']} → {flight['destination']}\n"
            f"- Date: {flight['date']}\n"
            f"- Price: ${flight['price_usd']}\n"
            f"- Provider: {flight['provider']}\n\n"
            f"*MCP approach: Direct tool call with structured response*"
        )
        return response
    
    elif intent["intent"] == "search_hotels":
        hotels = execute_tool(
            "search_hotels",
            {
                "city": "Singapore",
                "check_in": "2026-04-15",
                "check_out": "2026-04-20"
            },
            adapter
        )
        hotel = hotels[0]
        response = (
            f"🏨 **MCP Hotel Search**\n\n"
            f"**Protocol**: Executed `search_hotels` tool via MCP server\n\n"
            f"**Result**:\n"
            f"- Hotel ID: {hotel['hotel_id']}\n"
            f"- City: {hotel['city']}\n"
            f"- Check-in: {hotel['check_in']}\n"
            f"- Check-out: {hotel['check_out']}\n"
            f"- Nightly Rate: ${hotel['nightly_usd']}\n"
            f"- Provider: {hotel['provider']}\n\n"
            f"*MCP approach: Stateless tool execution*"
        )
        return response
    
    elif intent["intent"] == "plan_trip":
        request = TravelRequest(
            origin="Colombo",
            destination="Singapore",
            depart_date="2026-04-15",
            return_date="2026-04-20"
        )
        result = MCPWorkflowRunner(mcp_agent, adapter).run_trip_planning(request)
        
        response = (
            f"🗺️ **MCP Trip Planning**\n\n"
            f"**Architecture**: Model Context Protocol\n\n"
            f"**Workflow Steps**:\n"
        )
        for i, step in enumerate(result.steps, 1):
            response += f"{i}. {step}\n"
        
        response += f"\n**Summary**: {result.summary}\n\n"
        response += "*MCP Pattern: Request → Context → Tool Call → Structured Response*"
        return response
    
    return "I can help with flights, hotels, or trip planning!"


def generate_agentic_response(message: str, intent: Dict[str, Any] | None) -> str:
    """Generate response using Agentic AI architecture."""
    if not intent:
        return (
            "🤖 **Agentic AI**: I'm an autonomous travel assistant with planning capabilities. "
            "I use an Observe-Plan-Act-Reflect loop to help you. "
            "Try asking me: 'Find flights from Colombo to Singapore' or 'Plan a trip to Tokyo'"
        )
    
    if intent["intent"] == "search_flights":
        response = (
            f"✈️ **Agentic Flight Search**\n\n"
            f"**Observe**: Analyzing your request for flight information\n\n"
            f"**Plan**: Breaking down into subtasks:\n"
            f"  1. Identify origin and destination\n"
            f"  2. Search available flights\n"
            f"  3. Rank by price and convenience\n\n"
        )
        
        flights = execute_tool(
            "search_flights",
            {
                "origin": "Colombo",
                "destination": "Singapore",
                "date": "2026-04-15"
            },
            adapter
        )
        flight = flights[0]
        
        response += (
            f"**Act**: Executed flight search tool\n\n"
            f"**Result**:\n"
            f"- Flight ID: {flight['flight_id']}\n"
            f"- Route: {flight['origin']} → {flight['destination']}\n"
            f"- Date: {flight['date']}\n"
            f"- Price: ${flight['price_usd']}\n\n"
            f"**Reflect**: Found {len(flights)} option(s). Confidence: High ✓\n\n"
            f"*Agentic approach: Autonomous reasoning with self-reflection*"
        )
        return response
    
    elif intent["intent"] == "search_hotels":
        response = (
            f"🏨 **Agentic Hotel Search**\n\n"
            f"**Observe**: User needs accommodation\n\n"
            f"**Plan**: Strategy:\n"
            f"  1. Determine location preferences\n"
            f"  2. Search available hotels\n"
            f"  3. Filter by amenities and rating\n\n"
        )
        
        hotels = execute_tool(
            "search_hotels",
            {
                "city": "Singapore",
                "check_in": "2026-04-15",
                "check_out": "2026-04-20"
            },
            adapter
        )
        hotel = hotels[0]
        
        response += (
            f"**Act**: Searched hotel database\n\n"
            f"**Result**:\n"
            f"- Hotel ID: {hotel['hotel_id']}\n"
            f"- City: {hotel['city']}\n"
            f"- Check-in: {hotel['check_in']}\n"
            f"- Check-out: {hotel['check_out']}\n"
            f"- Nightly Rate: ${hotel['nightly_usd']}\n\n"
            f"**Reflect**: Good match for business traveler. Confidence: 0.92\n\n"
            f"*Agentic approach: Memory-informed decisions*"
        )
        return response
    
    elif intent["intent"] == "plan_trip":
        request = TravelRequest(
            origin="Colombo",
            destination="Singapore",
            depart_date="2026-04-15",
            return_date="2026-04-20"
        )
        result = AgenticWorkflowRunner(agentic_agent, adapter).run_trip_planning(request)
        
        response = (
            f"🗺️ **Agentic Trip Planning**\n\n"
            f"**Architecture**: Autonomous AI Agent\n\n"
            f"**Execution Loop**:\n"
        )
        for i, step in enumerate(result.steps, 1):
            response += f"{i}. {step}\n"
        
        response += f"\n**Summary**: {result.summary}\n\n"
        response += f"*Agentic Pattern: Observe → Plan → Act → Reflect (Iteration 1/{agentic_agent.loop_config.max_iterations})*"
        return response
    
    return "I'm analyzing your request using my planning capabilities!"


@app.route('/')
def index():
    """Serve the main chat interface."""
    return render_template('index.html')


@app.route('/api/chat/mcp', methods=['POST'])
def chat_mcp():
    """Handle MCP agent chat messages."""
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Extract intent
        intent = extract_travel_intent(user_message)
        
        # Generate response
        response = generate_mcp_response(user_message, intent)
        
        # Store in history
        conversation_history["mcp"].append({
            "role": "user",
            "message": user_message,
            "timestamp": datetime.now().isoformat()
        })
        conversation_history["mcp"].append({
            "role": "assistant",
            "message": response,
            "timestamp": datetime.now().isoformat()
        })
        
        return jsonify({
            'response': response,
            'agent': 'MCP',
            'architecture': mcp_agent.describe_architecture()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/chat/agentic', methods=['POST'])
def chat_agentic():
    """Handle Agentic AI agent chat messages."""
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Extract intent
        intent = extract_travel_intent(user_message)
        
        # Generate response
        response = generate_agentic_response(user_message, intent)
        
        # Store in history
        conversation_history["agentic"].append({
            "role": "user",
            "message": user_message,
            "timestamp": datetime.now().isoformat()
        })
        conversation_history["agentic"].append({
            "role": "assistant",
            "message": response,
            "timestamp": datetime.now().isoformat()
        })
        
        return jsonify({
            'response': response,
            'agent': 'Agentic AI',
            'architecture': agentic_agent.describe_architecture()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/reset', methods=['POST'])
def reset_conversation():
    """Reset conversation history for both agents."""
    conversation_history["mcp"].clear()
    conversation_history["agentic"].clear()
    return jsonify({'status': 'reset successful'})


@app.route('/api/info', methods=['GET'])
def get_info():
    """Get information about both agents."""
    return jsonify({
        'mcp': mcp_agent.describe_architecture(),
        'agentic': agentic_agent.describe_architecture()
    })


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 MCP vs Agentic AI Travel Assistant - Web Interface")
    print("="*60)
    print("\n📡 Server starting at: http://localhost:5000")
    print("\n🤖 Two agents ready:")
    print("   • MCP Agent: Protocol-based tool coordination")
    print("   • Agentic AI: Autonomous planning loop")
    print("\n💡 Try asking:")
    print("   • 'Find flights from Colombo to Singapore'")
    print("   • 'Search hotels in Singapore'")
    print("   • 'Plan a trip to Tokyo'")
    print("\n" + "="*60 + "\n")
    
    app.run(debug=True, port=5000)
