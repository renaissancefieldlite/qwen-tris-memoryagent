const state = {
  chatId: null,
  chats: [],
  voice: {
    recognition: null,
    active: false,
    finalTranscript: "",
    basePrompt: "",
    silenceTimer: null,
  },
  audio: {
    recorder: null,
    stream: null,
    chunks: [],
    dataUrl: "",
  },
  speakReplies: false,
};

const els = {
  newChat: document.getElementById("newChat"),
  chatList: document.getElementById("chatList"),
  messages: document.getElementById("messages"),
  composer: document.getElementById("composer"),
  prompt: document.getElementById("prompt"),
  routeSelect: document.getElementById("routeSelect"),
  qwenStatus: document.getElementById("qwenStatus"),
  nemotronStatus: document.getElementById("nemotronStatus"),
  qwenCloudStatus: document.getElementById("qwenCloudStatus"),
  openClawStatus: document.getElementById("openClawStatus"),
  langchainStatus: document.getElementById("langchainStatus"),
  audioStatus: document.getElementById("audioStatus"),
  homeNodeStatus: document.getElementById("homeNodeStatus"),
  memoryStatus: document.getElementById("memoryStatus"),
  lastRecall: document.getElementById("lastRecall"),
  fetchUrl: document.getElementById("fetchUrl"),
  webFetch: document.getElementById("webFetch"),
  fetchResult: document.getElementById("fetchResult"),
  voiceBtn: document.getElementById("voiceBtn"),
  recordBtn: document.getElementById("recordBtn"),
  speakBtn: document.getElementById("speakBtn"),
  voiceStatus: document.getElementById("voiceStatus"),
  micPlayback: document.getElementById("micPlayback"),
};

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  const payload = await response.json();
  if (!response.ok || payload.ok === false) {
    throw new Error(payload.error || response.statusText);
  }
  return payload;
}

function renderEmpty() {
  els.messages.innerHTML = `
    <div class="empty-state">
      <h3>Qwen Tris is ready.</h3>
      <p>Chat first. Stable-state memory, LangChain RAG, and Qwen routing move underneath.</p>
    </div>
  `;
}

function renderMessages(messages = []) {
  if (!messages.length) {
    renderEmpty();
    return;
  }
  els.messages.innerHTML = messages
    .map((message) => `
      <div class="message ${escapeHtml(message.role)}">
        <span>${escapeHtml(message.role === "assistant" ? "Qwen Tris" : "You")}</span>
        <p>${escapeHtml(message.content)}</p>
        ${message.provider ? `<em>${escapeHtml(message.provider)} ${escapeHtml(message.route || "")}</em>` : ""}
      </div>
    `)
    .join("");
  els.messages.scrollTop = els.messages.scrollHeight;
}

function speakText(text) {
  if (!state.speakReplies || !window.speechSynthesis || !text) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text.slice(0, 900));
  utterance.rate = 0.96;
  utterance.pitch = 1.0;
  window.speechSynthesis.speak(utterance);
}

function renderChats() {
  if (!state.chats.length) {
    els.chatList.innerHTML = `<div class="empty-list">No chats yet.</div>`;
    return;
  }
  els.chatList.innerHTML = state.chats
    .map((chat) => `
      <div class="chat-row ${chat.id === state.chatId ? "active" : ""}">
        <button class="chat-item" data-chat-id="${escapeHtml(chat.id)}">${escapeHtml(chat.title)}</button>
        <button class="chat-delete" data-delete-chat-id="${escapeHtml(chat.id)}" title="Delete">x</button>
      </div>
    `)
    .join("");
}

function renderRecall(retrievals = [], evidence = []) {
  const parts = [];
  for (const item of retrievals) {
    parts.push(`
      <article>
        <strong>${escapeHtml(item.id)} / ${escapeHtml(item.kind)}</strong>
        <em>${escapeHtml(item.reason)}</em>
        <p>${escapeHtml(item.content)}</p>
      </article>
    `);
  }
  for (const item of evidence) {
    parts.push(`
      <article>
        <strong>${escapeHtml(item.id)}</strong>
        <em>${escapeHtml(item.source_ref)}</em>
        <p>${escapeHtml(item.title)} - ${escapeHtml(item.body)}</p>
      </article>
    `);
  }
  els.lastRecall.innerHTML = parts.join("") || `<div class="empty-list">No recall yet.</div>`;
}

async function loadHealth() {
  const health = await api("/api/health");
  const providers = health.providers || {};
  els.qwenStatus.textContent = providers.qwen_local?.online ? "online" : "offline";
  els.nemotronStatus.textContent = providers.nemotron_local?.online ? "online" : "offline";
  els.qwenCloudStatus.textContent = providers.qwen_cloud?.online ? "online" : "key gate";
  const nemoClaw = providers.nemoclaw || providers.openclaw || {};
  els.openClawStatus.textContent = nemoClaw.online ? "online" : "not connected";
  els.langchainStatus.textContent = providers.langchain_rag?.online ? "online" : "fallback";
  els.audioStatus.textContent = providers.audio?.server_transcription ? "transcribe" : "browser";
  els.homeNodeStatus.textContent = providers.audio?.home_node_online ? "online" : "offline";
  els.memoryStatus.textContent = `${health.memory_count} memories`;
}

async function loadChats() {
  const payload = await api("/api/chats");
  state.chats = payload.chats || [];
  renderChats();
  if (!state.chatId && state.chats.length) {
    await loadChat(state.chats[0].id);
  }
}

async function loadChat(chatId) {
  state.chatId = chatId;
  renderChats();
  const payload = await api(`/api/messages?chat_id=${encodeURIComponent(chatId)}`);
  renderMessages(payload.messages || []);
}

async function sendMessage(event) {
  event.preventDefault();
  const message = els.prompt.value.trim();
  if (!message && !state.audio.dataUrl) return;
  els.prompt.value = "";
  const working = [...els.messages.querySelectorAll(".message")].map((node) => ({
    role: node.classList.contains("assistant") ? "assistant" : "user",
    content: node.querySelector("p")?.textContent || "",
  }));
  renderMessages([...working, { role: "user", content: message }, { role: "assistant", content: "Thinking through memory..." }]);
  try {
    const payload = await api("/api/chat", {
      method: "POST",
      body: JSON.stringify({
        chat_id: state.chatId,
        message,
        route: els.routeSelect.value,
        mic_audio_data: state.audio.dataUrl,
      }),
    });
    state.chatId = payload.chat_id;
    state.chats = payload.chats || state.chats;
    renderChats();
    renderMessages(payload.messages || []);
    renderRecall(payload.retrievals || [], payload.evidence || []);
    if (payload.response) speakText(payload.response);
    state.audio.dataUrl = "";
    els.micPlayback.hidden = true;
    els.micPlayback.removeAttribute("src");
    await loadHealth();
  } catch (error) {
    renderMessages([...working, { role: "user", content: message }, { role: "assistant", content: error.message }]);
  }
}

function recognitionCtor() {
  return window.SpeechRecognition || window.webkitSpeechRecognition || null;
}

function setVoiceStatus(text) {
  els.voiceStatus.textContent = text;
}

function clearVoiceTimer() {
  if (state.voice.silenceTimer) clearTimeout(state.voice.silenceTimer);
  state.voice.silenceTimer = null;
}

function stopVoice(manual = true) {
  clearVoiceTimer();
  if (state.voice.recognition) {
    try { state.voice.recognition.stop(); } catch (error) {}
  }
  state.voice.recognition = null;
  state.voice.active = false;
  els.voiceBtn.dataset.active = "false";
  els.voiceBtn.textContent = "Voice";
  if (manual) setVoiceStatus("Voice idle.");
}

function scheduleVoiceSend() {
  clearVoiceTimer();
  state.voice.silenceTimer = setTimeout(() => {
    setVoiceStatus("Pause detected. Sending voice command.");
    stopVoice(false);
    els.composer.requestSubmit();
  }, 1200);
}

function startVoice() {
  const Recognition = recognitionCtor();
  if (!Recognition) {
    setVoiceStatus("Voice command unavailable in this browser.");
    return;
  }
  stopVoice(false);
  const recognition = new Recognition();
  recognition.lang = "en-US";
  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.maxAlternatives = 1;
  state.voice.recognition = recognition;
  state.voice.active = true;
  state.voice.basePrompt = els.prompt.value.trim();
  state.voice.finalTranscript = "";
  els.voiceBtn.dataset.active = "true";
  els.voiceBtn.textContent = "Listening";
  setVoiceStatus("Listening. Pause to send.");

  recognition.onresult = (event) => {
    let interim = "";
    let sawFinal = false;
    for (let index = event.resultIndex; index < event.results.length; index += 1) {
      const piece = String(event.results[index][0].transcript || "").trim();
      if (!piece) continue;
      if (event.results[index].isFinal) {
        state.voice.finalTranscript = [state.voice.finalTranscript, piece].filter(Boolean).join(" ");
        sawFinal = true;
      } else {
        interim = [interim, piece].filter(Boolean).join(" ");
      }
    }
    els.prompt.value = [state.voice.basePrompt, state.voice.finalTranscript, interim].filter(Boolean).join(" ").trim();
    if (sawFinal) scheduleVoiceSend();
  };
  recognition.onerror = (event) => {
    stopVoice(false);
    setVoiceStatus(`Voice error: ${event.error || "unknown"}`);
  };
  recognition.onend = () => {
    const hadText = Boolean(els.prompt.value.trim());
    state.voice.recognition = null;
    state.voice.active = false;
    els.voiceBtn.dataset.active = "false";
    els.voiceBtn.textContent = "Voice";
    if (hadText) scheduleVoiceSend();
    else setVoiceStatus("Voice idle.");
  };
  recognition.start();
}

async function startRecording() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia || !window.MediaRecorder) {
    setVoiceStatus("Audio recording unavailable in this browser.");
    return;
  }
  if (state.audio.recorder && state.audio.recorder.state === "recording") {
    state.audio.recorder.stop();
    return;
  }
  state.audio.stream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false });
  state.audio.chunks = [];
  const recorder = new MediaRecorder(state.audio.stream);
  state.audio.recorder = recorder;
  recorder.ondataavailable = (event) => {
    if (event.data && event.data.size) state.audio.chunks.push(event.data);
  };
  recorder.onstop = async () => {
    const blob = new Blob(state.audio.chunks, { type: recorder.mimeType || "audio/webm" });
    const reader = new FileReader();
    reader.onloadend = () => {
      state.audio.dataUrl = String(reader.result || "");
      els.micPlayback.src = URL.createObjectURL(blob);
      els.micPlayback.hidden = false;
      setVoiceStatus("Audio captured. Add text or press Send.");
    };
    reader.readAsDataURL(blob);
    if (state.audio.stream) {
      state.audio.stream.getTracks().forEach((track) => track.stop());
    }
    state.audio.stream = null;
    state.audio.recorder = null;
    els.recordBtn.textContent = "Record";
    els.recordBtn.dataset.active = "false";
  };
  recorder.start();
  els.recordBtn.textContent = "Stop";
  els.recordBtn.dataset.active = "true";
  setVoiceStatus("Recording audio.");
}

async function deleteChat(chatId) {
  await api("/api/chats/delete", {
    method: "POST",
    body: JSON.stringify({ chat_id: chatId }),
  });
  if (state.chatId === chatId) {
    state.chatId = null;
    renderEmpty();
  }
  await loadChats();
}

async function webFetch() {
  els.fetchResult.textContent = "Fetching...";
  try {
    const payload = await api("/api/web-fetch", {
      method: "POST",
      body: JSON.stringify({ url: els.fetchUrl.value }),
    });
    els.fetchResult.textContent = `Added ${payload.doc.title}`;
    await loadHealth();
  } catch (error) {
    els.fetchResult.textContent = error.message;
  }
}

els.newChat.addEventListener("click", () => {
  state.chatId = null;
  renderChats();
  renderEmpty();
  renderRecall();
  els.prompt.focus();
});

els.chatList.addEventListener("click", (event) => {
  const deleteButton = event.target.closest("[data-delete-chat-id]");
  if (deleteButton) {
    deleteChat(deleteButton.dataset.deleteChatId);
    return;
  }
  const chatButton = event.target.closest("[data-chat-id]");
  if (chatButton) loadChat(chatButton.dataset.chatId);
});

els.composer.addEventListener("submit", sendMessage);
els.prompt.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey && !event.isComposing) {
    event.preventDefault();
    els.composer.requestSubmit();
  }
});
els.webFetch.addEventListener("click", webFetch);
els.voiceBtn.addEventListener("click", () => {
  if (state.voice.active) stopVoice(true);
  else startVoice();
});
els.recordBtn.addEventListener("click", () => {
  startRecording().catch((error) => setVoiceStatus(`Audio error: ${error.message}`));
});
els.speakBtn.addEventListener("click", () => {
  state.speakReplies = !state.speakReplies;
  els.speakBtn.dataset.active = state.speakReplies ? "true" : "false";
  els.speakBtn.textContent = state.speakReplies ? "Speaking" : "Speak";
  if (!state.speakReplies && window.speechSynthesis) window.speechSynthesis.cancel();
});

renderEmpty();
renderRecall();
loadHealth();
loadChats();
