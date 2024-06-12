import streamlit as st
import requests

# Function to send user input to Flask backend and get chatbot response
def get_chatbot_response(user_input):
    response = requests.post(
        "http://127.0.0.1:5000/chat", 
        json={"message": user_input}
    )
    return response.json().get("response")

def main():
    st.title("Chatbot Interface")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    user_input_key = "user_input"

    user_input = st.text_input("You: ", key=user_input_key)

    if st.button("Send"):
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.conversation.append(("You", user_input))
            st.session_state.conversation.append(("Aneka", response))

    if st.session_state.conversation:
        for speaker, message in st.session_state.conversation:
            st.write(f"{speaker}: {message}")

if __name__ == "__main__":
    main()



