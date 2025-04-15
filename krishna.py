import streamlit as st
import google.generativeai as genai

# Replace with your actual Google AI Studio API Key
genai.configure(api_key="AIzaSyCSDw2ExCnUSqPUkp7yV48eZzh8pS5gzCc")

# Initialize Gemini Model
model = genai.GenerativeModel('gemini-1.5-pro')

# Streamlit app title
st.title("🦚 Little Krishna Chatbot")
st.write("Chat with Little Krishna — full of wisdom and mischief! 🌼")

# Initialize conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box for user
user_input = st.text_input("You:", "")

if user_input:
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Create prompt with Krishna's personality
    system_prompt = """
You are Little Krishna, the divine child from Hindu mythology.
You speak in a playful, loving, wise tone.
If someone asks you who your brother is, reply 'Balarama is my brother!' and act like a divine child.
If someone asks you about your mother, respond lovingly and affectionately.
Always keep your answers wise but concise, avoiding long repetitive sentences.
"""

    # Combine system and conversation messages
    full_prompt = system_prompt + "\n" + "\n".join(
        f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.chat_history
    )

    try:
        # Use Gemini to generate the response with controlled output length
        response = model.generate_content(full_prompt)
        reply = response.text.strip()

        # Save assistant reply to history
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

        # Display reply
        st.write(f"**Little Krishna 🦚:** {reply}")

    except Exception as e:
        st.write("⚠️ Error:", e)

# Display entire chat history
st.write("---")
for msg in st.session_state.chat_history:
    speaker = "You" if msg["role"] == "user" else "Little Krishna 🦚"
    st.write(f"**{speaker}:** {msg['content']}")
