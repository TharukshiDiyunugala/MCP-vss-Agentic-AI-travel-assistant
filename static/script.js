// MCP vs Agentic AI - Professional Comparator UI

const API_BASE = "http://localhost:5000/api";

const mcpMessages = document.getElementById("mcpMessages");
const agenticMessages = document.getElementById("agenticMessages");
const mcpInput = document.getElementById("mcpInput");
const agenticInput = document.getElementById("agenticInput");
const mcpSend = document.getElementById("mcpSend");
const agenticSend = document.getElementById("agenticSend");
const resetBtn = document.getElementById("resetBtn");
const infoBtn = document.getElementById("infoBtn");
const infoModal = document.getElementById("infoModal");
const closeModal = document.querySelector(".close");

const metricTotalMessages = document.getElementById("metricTotalMessages");
const metricMcpLatency = document.getElementById("metricMcpLatency");
const metricAgenticLatency = document.getElementById("metricAgenticLatency");
const metricDualRuns = document.getElementById("metricDualRuns");

const metrics = {
    totalMessages: 0,
    dualRuns: 0,
    mcpLatencies: [],
    agenticLatencies: [],
};

document.addEventListener("DOMContentLoaded", () => {
    setupEventListeners();
    loadAgentInfo();
    updateMetricsUI();
});

function setupEventListeners() {
    mcpSend.addEventListener("click", () => sendMessage("mcp"));
    mcpInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage("mcp");
    });

    agenticSend.addEventListener("click", () => sendMessage("agentic"));
    agenticInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage("agentic");
    });

    resetBtn.addEventListener("click", resetConversation);

    infoBtn.addEventListener("click", () => {
        infoModal.style.display = "block";
        loadAgentInfo();
    });

    closeModal.addEventListener("click", () => {
        infoModal.style.display = "none";
    });

    window.addEventListener("click", (e) => {
        if (e.target === infoModal) {
            infoModal.style.display = "none";
        }
    });

    const actionButtons = document.querySelectorAll(".action-btn");
    actionButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const query = btn.dataset.query;
            sendMessageToBoth(query);
        });
    });
}

async function sendMessage(agent) {
    const input = agent === "mcp" ? mcpInput : agenticInput;
    const messagesContainer = agent === "mcp" ? mcpMessages : agenticMessages;
    const message = input.value.trim();

    if (!message) return;

    clearWelcomeMessage(messagesContainer);
    appendMessage(messagesContainer, message, "user");

    metrics.totalMessages += 1;
    updateMetricsUI();

    input.value = "";
    const typingId = showTypingIndicator(messagesContainer);

    const start = performance.now();

    try {
        const response = await fetch(`${API_BASE}/chat/${agent}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        });

        if (!response.ok) {
            throw new Error("Failed to get response");
        }

        const data = await response.json();
        const elapsed = Math.round(performance.now() - start);

        trackLatency(agent, elapsed);
        updateMetricsUI();

        removeTypingIndicator(messagesContainer, typingId);
        appendMessage(messagesContainer, data.response, "assistant");
    } catch (error) {
        console.error("Error:", error);
        removeTypingIndicator(messagesContainer, typingId);
        appendMessage(messagesContainer, "Service error: unable to process this request.", "assistant");
    }
}

function sendMessageToBoth(message) {
    metrics.dualRuns += 1;
    updateMetricsUI();

    mcpInput.value = message;
    agenticInput.value = message;

    sendMessage("mcp");
    sendMessage("agentic");
}

function clearWelcomeMessage(container) {
    const welcome = container.querySelector(".welcome-message");
    if (welcome) {
        welcome.remove();
    }
}

function appendMessage(container, text, role) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message message-${role}`;

    const bubbleDiv = document.createElement("div");
    bubbleDiv.className = "message-bubble";

    const contentDiv = document.createElement("div");
    contentDiv.className = "message-content";
    contentDiv.innerHTML = formatMessage(text);

    const timestamp = document.createElement("span");
    timestamp.className = "message-timestamp";
    timestamp.textContent = new Date().toLocaleTimeString();

    bubbleDiv.appendChild(contentDiv);
    bubbleDiv.appendChild(timestamp);
    messageDiv.appendChild(bubbleDiv);
    container.appendChild(messageDiv);

    container.scrollTop = container.scrollHeight;
}

function formatMessage(text) {
    let formatted = text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

    formatted = formatted.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    formatted = formatted.replace(/\n/g, "<br>");
    formatted = formatted.replace(/^- (.+)$/gm, "• $1");

    return formatted;
}

function showTypingIndicator(container) {
    const wrapper = document.createElement("div");
    wrapper.className = "message message-assistant";

    const indicator = document.createElement("div");
    indicator.className = "typing-indicator";
    indicator.innerHTML = `
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    `;

    const id = `typing-${Date.now()}`;
    wrapper.id = id;
    wrapper.appendChild(indicator);
    container.appendChild(wrapper);
    container.scrollTop = container.scrollHeight;

    return id;
}

function removeTypingIndicator(container, id) {
    const typingDiv = document.getElementById(id);
    if (typingDiv) {
        typingDiv.remove();
    }
}

async function resetConversation() {
    if (!confirm("Reset both conversations and metrics?")) {
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/reset`, { method: "POST" });
        if (!response.ok) {
            throw new Error("Reset failed");
        }

        location.reload();
    } catch (error) {
        console.error("Error resetting conversation:", error);
        alert("Reset failed. Please try again.");
    }
}

async function loadAgentInfo() {
    try {
        const response = await fetch(`${API_BASE}/info`);
        if (!response.ok) {
            throw new Error("Info endpoint failed");
        }

        const data = await response.json();

        const mcpInfo = document.getElementById("mcpInfo");
        const agenticInfo = document.getElementById("agenticInfo");

        mcpInfo.innerHTML = formatAgentInfo(data.mcp);
        agenticInfo.innerHTML = formatAgentInfo(data.agentic);
    } catch (error) {
        console.error("Error loading agent info:", error);
    }
}

function formatAgentInfo(info) {
    let html = "<div>";

    for (const [key, value] of Object.entries(info)) {
        const label = key.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

        if (typeof value === "object") {
            html += `<strong>${label}:</strong>`;
            html += `<pre>${JSON.stringify(value, null, 2)}</pre>`;
        } else {
            html += `<strong>${label}:</strong> ${String(value)}<br>`;
        }
    }

    html += "</div>";
    return html;
}

function trackLatency(agent, elapsedMs) {
    if (agent === "mcp") {
        metrics.mcpLatencies.push(elapsedMs);
    } else {
        metrics.agenticLatencies.push(elapsedMs);
    }
}

function average(values) {
    if (!values.length) return 0;
    const total = values.reduce((sum, n) => sum + n, 0);
    return Math.round(total / values.length);
}

function updateMetricsUI() {
    metricTotalMessages.textContent = String(metrics.totalMessages);
    metricDualRuns.textContent = String(metrics.dualRuns);
    metricMcpLatency.textContent = `${average(metrics.mcpLatencies)} ms`;
    metricAgenticLatency.textContent = `${average(metrics.agenticLatencies)} ms`;
}
