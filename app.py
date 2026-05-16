import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

# ── Page Config ──────────────────────────────────────────
st.set_page_config(page_title="AI Chatbot — Claude", page_icon="🤖", layout="centered")

# ── CSS ───────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Space+Mono&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; background: #0d0d14; color: #e2e8f0; }
.stApp { background: #0d0d14; }
.chat-user {
    background: linear-gradient(135deg, #1e3a5f, #0f3460);
    border-radius: 18px 18px 4px 18px; padding: 14px 18px;
    margin: 8px 0; max-width: 80%; margin-left: auto;
    border: 1px solid #1e4a7a; font-size: 0.92rem; line-height: 1.6;
}
.chat-ai {
    background: linear-gradient(135deg, #0d1f0d, #1a2e1a);
    border-radius: 18px 18px 18px 4px; padding: 14px 18px;
    margin: 8px 0; max-width: 85%;
    border: 1px solid #1a4a1a; font-size: 0.92rem;
    line-height: 1.6; color: #c8f0c8;
}
.lbl-bot { font-size:0.7rem; color:#00e5a0; letter-spacing:2px; text-transform:uppercase; margin-bottom:4px; }
.lbl-usr { font-size:0.7rem; color:#60a5fa; letter-spacing:2px; text-transform:uppercase; margin-bottom:4px; text-align:right; }
.title-main { font-family:'Space Mono',monospace; font-size:1.8rem; color:#00e5a0; font-weight:700; }
</style>
""", unsafe_allow_html=True)

# ── State ─────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Header ────────────────────────────────────────────────
st.markdown('<div class="title-main">🤖 AI Chatbot</div>', unsafe_allow_html=True)
st.caption("Powered by Claude AI (Anthropic) · Built with Streamlit")
st.divider()

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    persona = st.selectbox("🎭 Persona", ["Helpful Assistant","Data Science Tutor","Python Expert","Career Coach","Interview Prep"])
    max_tokens = st.slider("📝 Max Response", 256, 2048, 1024, 128)
    st.divider()
    st.markdown(f"**💬 Messages:** {len(st.session_state.messages)}")
    st.markdown(f"**🔄 Turns:** {len(st.session_state.messages)//2}")
    st.divider()
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.markdown("### 💡 Quick Ask")
    for q in ["Explain Machine Learning","Python vs JavaScript?","How to crack DS interviews?","Best AI projects for portfolio?"]:
        if st.button(q, key=q):
            st.session_state.messages.append({"role":"user","content":q})
            st.rerun()

PERSONAS = {
    "Helpful Assistant": "You are a helpful, friendly AI assistant.",
    "Data Science Tutor": "You are an expert Data Science tutor. Explain concepts clearly with examples.",
    "Python Expert": "You are a Python expert. Give clean, well-commented code examples.",
    "Career Coach": "You are a career coach for tech professionals. Give actionable advice.",
    "Interview Prep": "You are an interview coach. Help with DS/ML interview questions and answers.",
}

# ── Chat Display ──────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="lbl-usr">You</div><div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="lbl-bot">🤖 Claude AI</div><div class="chat-ai">{msg["content"]}</div>', unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    st.markdown(f'<div class="lbl-usr">You</div><div class="chat-user">{user_input}</div>', unsafe_allow_html=True)
    with st.spinner("🤖 Thinking..."):
        try:
            client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=max_tokens,
                system=PERSONAS.get(persona, PERSONAS["Helpful Assistant"]),
                messages=[{"role":m["role"],"content":m["content"]} for m in st.session_state.messages],
            )
            reply = response.content[0].text
            st.session_state.messages.append({"role":"assistant","content":reply})
            st.markdown(f'<div class="lbl-bot">🤖 Claude AI</div><div class="chat-ai">{reply}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Error: {e} — Check ANTHROPIC_API_KEY in .env")
