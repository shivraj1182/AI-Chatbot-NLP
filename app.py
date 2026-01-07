"""Streamlit Web Application for AI Chatbot"""

import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.chatbot import ChatBot

# Page configuration
st.set_page_config(
    page_title="AI Chatbot - NLP",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main { max-width: 800px; }
    .chat-message { padding: 10px; margin: 5px 0; border-radius: 5px; }
    .user-message { background-color: #e3f2fd; }
    .bot-message { background-color: #f3e5f5; }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = ChatBot('data/intents.json')

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Title and description
st.title("🤖 AI Chatbot powered by NLP")
st.markdown("Welcome! I'm an intelligent chatbot built using Natural Language Processing techniques.")

# Sidebar information
with st.sidebar:
    st.header("About")
    st.info("""
    **AI Chatbot using NLP**
    - Built with: Python, NLTK, spaCy, TensorFlow
    - Deployment: Streamlit
    - Capabilities: Intent Classification, Response Generation
    """)
    
    st.header("Features")
    st.markdown("""
    - 📝 Intent-based conversation
    - 🧠 NLP preprocessing
    - ⚡ Real-time responses
    - 💬 Multi-turn conversations
    """)
    
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get chatbot response
    bot_response = st.session_state.chatbot.chat(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    # Rerun to display new messages
    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Powered by AI and NLP | Version 1.0.0</p>
    <p><a href='https://github.com/shivraj1182/AI-Chatbot-NLP'>GitHub Repository</a></p>
</div>
""", unsafe_allow_html=True)
