import google.generativeai as genai
import streamlit as st
import json
import pandas as pd
import os

x = os.getenv("API_KEY")
genai.configure(api_key = x)
model = genai.GenerativeModel('gemini-2.0-flash')

# Session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "step" not in st.session_state:
    st.session_state.step = 0
if "log" not in st.session_state:
    st.session_state.log = []
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# Logging function
def log_msg(message, sender="agent"):
    st.session_state.log.append({"sender": sender, "message": message})

# Gemini reply function
def get_reply(msg):
    response = st.session_state.chat.send_message(msg)
    reply = response.text
    log_msg(reply)
    return reply

# UI
st.title("🤖 AI Sales Agent")

# Display chat log
for entry in st.session_state.log:
    if entry["sender"] == "user":
        st.chat_message("user").markdown(entry["message"])
    else:
        st.chat_message("assistant").markdown(entry["message"])

# Conversation flow
prompts = [
    "Hello! I'm your AI Sales Agent. Can I know your name?",
    "Nice to meet you, {name}! Are you looking for a **phone** or a **SaaS plan**?",
    "What’s your budget in USD?",
    "Any specific feature you care about? (e.g., camera, storage, email)",
    "Do you have any concerns or questions?",
]

# Generate the current prompt
if st.session_state.step < len(prompts):
    prompt_template = prompts[st.session_state.step]
    current_prompt = prompt_template.format(**st.session_state.user_data)

    # Chat input
    user_input = st.chat_input(current_prompt)
    if user_input:
        log_msg(user_input, sender="user")

        if st.session_state.step == 0:
            st.session_state.user_data["name"] = user_input
        elif st.session_state.step == 1:
            st.session_state.user_data["need"] = user_input
            get_reply(f"The user is looking for {user_input}. Recommend a product with pricing and features.")
        elif st.session_state.step == 2:
            st.session_state.user_data["budget"] = user_input
            get_reply(f"The user has a budget of {user_input} dollars. Suggest suitable options for {st.session_state.user_data['need']}.")
        elif st.session_state.step == 3:
            st.session_state.user_data["feature"] = user_input
            get_reply(f"The user wants features like {user_input}. Suggest best products matching these preferences.")
        elif st.session_state.step == 4:
            st.session_state.user_data["objection"] = user_input
            get_reply(f"The user has '{user_input}' concern. Address it politely and convincingly.")
            get_reply("Thanks for the chat! We’ll follow up soon with more info.")

        st.session_state.step += 1
else:
    st.success("🎉 Chat completed. Thank you!")

    # Export log
    df = pd.DataFrame(st.session_state.log)
    name = st.session_state.user_data.get("name", "user")
    df.to_csv(f"{name}_chat.csv", index=False)
    with open(f"{name}_chat.json", "w") as f:
        json.dump(st.session_state.log, f, indent=2)