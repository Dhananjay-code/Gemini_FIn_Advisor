import streamlit as st
import base64
import os
from bot_engine import initialize_chat, get_chat_response_stream

# 1. Page Configuration
st.set_page_config(page_title="AI Financial Advisor", page_icon="🏦", layout="wide")

# 2. Advanced Cosmetic Styling Function
def apply_custom_style(image_file):
    if not os.path.exists(image_file):
        st.error(f"⚠️ Background image '{image_file}' not found in directory.")
        return

    with open(image_file, "rb") as f:
        data = f.read()
        bin_str = base64.b64encode(data).decode()

    st.markdown(f"""
        <style>
            /* 1. Global Background with a subtle dark tint for readability */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                            url("data:image/jpg;base64,{bin_str}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            
            /* 2. Fully Transparent Chat Bubbles */
            [data-testid="stChatMessage"] {{
                background-color: transparent !important;
                border: none !important;
                box-shadow: none !important;
            }}

            /* 3. Text Visibility: High-contrast white with double-shadowing */
            [data-testid="stChatMessage"] .stMarkdown p {{
                color: #ffffff !important;
                font-weight: 600;
                text-shadow: 2px 2px 8px rgba(0, 0, 0, 1), 
                             -1px -1px 2px rgba(0, 0, 0, 1);
                font-size: 1.15rem;
                line-height: 1.6;
            }}

            /* 4. Advisor Panel Sidebar Text styling */
            .sidebar-title {{
                color: #00FFCC !important; /* Neon cyan to pop against dark sidebar */
                font-size: 26px !important;
                font-weight: bold !important;
                text-shadow: 2px 2px 4px #000;
                margin-top: -20px;
            }}

            /* 5. Cleanup: Remove bottom bar gray background */
            [data-testid="stBottom"] > div {{
                background: transparent !important;
            }}
        </style>
    """, unsafe_allow_html=True)

# CALL THE STYLE FUNCTION (Change filename to your actual file)
apply_custom_style("my_image.jpg")

# 3. Sidebar for Production Meta-data
with st.sidebar:
    st.markdown('<p class="sidebar-title">💰 Advisor Panel</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.info("💡 **Focus:** Conservative wealth building.")
    st.metric(label="System Status", value="Online", delta="Stable")
    
    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_session = initialize_chat()
        st.rerun()

# 4. Initialize Chat Session & History
if "chat_session" not in st.session_state:
    st.session_state.chat_session = initialize_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🏦 AI Financial Advisor")
st.caption("Production-Ready Gemini Chatbot | Focus: Education & Budgeting")

# 5. Display Conversation History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input Logic with Streaming
if user_query := st.chat_input("Ask about savings, 401k, or budgeting..."):
    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Generate & Display Assistant Response
    with st.chat_message("assistant"):
        response_generator = get_chat_response_stream(st.session_state.chat_session, user_query)
        
        def stream_handler():
            if isinstance(response_generator, str):
                yield response_generator
                return
            
            for chunk in response_generator:
                if chunk.text:
                    yield chunk.text

        full_response = st.write_stream(stream_handler())
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})