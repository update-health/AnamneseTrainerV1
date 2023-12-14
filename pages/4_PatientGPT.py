from openai import OpenAI
import streamlit as st
import os

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "selectedPatient" not in st.session_state:
    st.session_state.selectedPatient

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
st.session_state.selectedPatient=st.selectbox("Wähle einen Patienten. Achtung: Das bisherige Gespräch wird zurückgesetz und ein neues beginnt",('Meier', 'Müller', 'Schulze'))

if prompt := st.chat_input("What is up?"+st.session_state.selectedPatient):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})