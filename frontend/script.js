const API_URL = "/chat/stream";

const logEl   = document.getElementById("chat-log");
const inputEl = document.getElementById("chat-input");
const btnEl   = document.getElementById("send-btn");

let lastBotMd = "";
let isStreaming = false;

function appendUser(message) {
  const div = document.createElement("div");
  div.className = "message user";
  div.innerHTML = `<strong>You:</strong> ${escapeHtml(message)}`;
  logEl.appendChild(div);
  scrollToBottom();
}

function escapeHtml(text) {
  const map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  };
  return text.replace(/[&<>"']/g, m => map[m]);
}

function renderBot(md) {
  let botDiv = logEl.querySelector(".message.bot:last-child");
  if (!botDiv) {
    botDiv = document.createElement("div");
    botDiv.className = "message bot";
    botDiv.innerHTML = `<strong>Shiva:</strong> <div class="bot-content"></div>`;
    logEl.appendChild(botDiv);
  }
  
  const contentDiv = botDiv.querySelector(".bot-content");
  
  // Simple: just use marked.js directly
  try {
    if (typeof marked !== 'undefined') {
      const html = marked.parse(md);
      contentDiv.innerHTML = html;
    } else {
      // Basic fallback
      const html = escapeHtml(md).replace(/\n/g, '<br>');
      contentDiv.innerHTML = html;
    }
  } catch (e) {
    contentDiv.innerHTML = escapeHtml(md).replace(/\n/g, '<br>');
  }
  
  scrollToBottom();
}

function scrollToBottom() {
  logEl.scrollTop = logEl.scrollHeight;
}

function setUIState(streaming) {
  isStreaming = streaming;
  btnEl.disabled = streaming;
  btnEl.textContent = streaming ? "..." : "Send";
  inputEl.disabled = streaming;
}

btnEl.addEventListener("click", async () => {
  const question = inputEl.value.trim();
  if (!question || isStreaming) return;

  appendUser(question);
  inputEl.value = "";
  lastBotMd = "";
  setUIState(true);

  try {
    const resp = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });

    if (!resp.ok) {
      renderBot("Network error. Please try again.");
      setUIState(false);
      return;
    }

    const reader = resp.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      
      buffer += decoder.decode(value, { stream: true });

      const chunks = buffer.split(/\n\n|\n(?=data:)/);
      buffer = chunks.pop() || "";

      for (let chunk of chunks) {
        chunk = chunk.trim();
        if (!chunk) continue;
        
        let content = "";
        
        if (chunk.startsWith("data:")) {
          content = chunk.replace(/^data:\s*/, "").trim();
          
          if (content === "[DONE]" || content === "DONE") {
            setUIState(false);
            return;
          }
          
          if (content.startsWith("{")) {
            try {
              const parsed = JSON.parse(content);
              content = parsed.content || parsed.message || parsed.text || parsed.delta || "";
            } catch (e) {
              // Use as-is
            }
          }
        } else if (chunk.startsWith("{")) {
          try {
            const parsed = JSON.parse(chunk);
            content = parsed.content || parsed.message || parsed.text || parsed.delta || "";
          } catch (e) {
            content = chunk;
          }
        } else {
          content = chunk;
        }
        
        if (content) {
          lastBotMd += content;
          renderBot(lastBotMd);
        }
      }
    }
    
    if (buffer.trim()) {
      let content = buffer.trim();
      if (content.startsWith("data:")) {
        content = content.replace(/^data:\s*/, "").trim();
      }
      if (content && content !== "[DONE]" && content !== "DONE") {
        lastBotMd += content;
        renderBot(lastBotMd);
      }
    }
    
  } catch (error) {
    renderBot("Connection error. Please try again.");
  } finally {
    setUIState(false);
  }
});

inputEl.addEventListener("keypress", (e) => {
  if (e.key === "Enter" && !e.shiftKey && !isStreaming) {
    e.preventDefault();
    btnEl.click();
  }
});