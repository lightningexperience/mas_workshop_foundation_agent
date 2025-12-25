# foundation_agent.py
# Version 1.1 — Same app as before, but now it resends earlier questions and answers

import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # Loads environment variables when running locally


def main():
    """
    Stage 0 — Foundation Agent (with conversation history)

    What this app does:
    - Shows a simple web page
    - Lets the user type a question
    - Sends the question to Groq
    - Shows Groq’s response

    What is new in this version:
    Every time the user asks a new question,
    the app sends the previous user questions
    and the previous Groq responses back to Groq again,
    along with the new question.
    """

    # ---------------------------------
    # Read the Groq API key
    # ---------------------------------
    # Heroku provides this value when the app runs.
    # It is not stored in GitHub.
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.error("GROQ_API_KEY not found in environment variables.")
        return

    # Create a connection to Groq
    client = Groq(api_key=groq_api_key)

    # ---------------------------------
    # Build the web page
    # ---------------------------------
    # Streamlit is only used to show text boxes and text on the page.
    st.title("Foundation Agent (Stage 0)")
    st.write(
        "This app sends your question to Groq and shows the response. "
        "It also resends earlier questions and earlier Groq responses "
        "so follow-up questions make sense."
    )

    # Sidebar controls
    st.sidebar.title("Customize Your Foundation Agent")
    system_prompt = st.sidebar.text_area(
        "System Prompt:",
        value="You are a helpful assistant."
    )
    model = st.sidebar.selectbox(
        "Choose Model:",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"],
    )

    # ---------------------------------
    # Store earlier questions and answers
    # ---------------------------------
    # Groq does NOT remember anything.
    # After Groq replies, it forgets the conversation.
    #
    # To make conversation work, this app saves:
    # - what the user asked before
    # - what Groq answered before
    #
    # These saved messages are sent again
    # every time the user asks a new question.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ---------------------------------
    # User input
    # ---------------------------------
    user_input = st.text_input("Ask me something:")

    if user_input:
        try:
            # ---------------------------------
            # Save the new user question
            # ---------------------------------
            # This does NOT go to Groq automatically.
            # We save it so we can send it ourselves.
            st.session_state.messages.append(
                {"role": "user", "content": user_input}
            )

            # ---------------------------------
            # Send messages to Groq
            # ---------------------------------
            # We send:
            # - the instructions (system prompt)
            # - all earlier user questions
            # - all earlier Groq responses
            # - plus the new question
            #
            # Groq only sees what we send here.
            # It does not remember anything on its own.
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt}
                ] + st.session_state.messages,
                temperature=0.7,
            )

            # Get Groq’s reply
            response = completion.choices[0].message.content

            # ---------------------------------
            # Save Groq’s reply
            # ---------------------------------
            # We save this so it can be sent again
            # if the user asks another question.
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )

            # Show the response on the page
            st.write("### Response:")
            st.write(response)

        except Exception as e:
            st.error(f"Error calling Groq API: {e}")


if __name__ == "__main__":
    main()
