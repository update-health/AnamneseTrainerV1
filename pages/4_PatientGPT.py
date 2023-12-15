from openai import OpenAI
import streamlit as st
import os
import pandas as pd

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-1106-preview"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "case_dict" not in st.session_state:
    # 1. Laden der Excel-Datei und Extrahieren der Fallbeispiele
    df = pd.read_excel('/workspaces/patientgptlit/pages/Fallbeispiele.xlsx')

    # Fallbeispiele extrahieren
    cases = df["Zusammenfassung"].tolist()
    details = df["Details"].tolist()

    # Fallbeispiele als ein Wörterbuch für einfachen Zugriff
    st.session_state.case_dict = dict(zip(cases, details))

if "selectedPatient" not in st.session_state:
    st.session_state.selectedPatient=""
    
# Definieren Sie eine Funktion, die aufgerufen wird, wenn sich die Auswahl ändert
def on_patient_change():
    # Diese Funktion könnte zum Beispiel das Gespräch zurücksetzen oder andere Aktionen ausführen
    st.session_state.clear()

#https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
st.session_state.selectedPatient=st.selectbox("Wähle einen Patienten. Achtung: Das bisherige Gespräch wird zurückgesetzt und ein neues beginnt",tuple(st.session_state.case_dict.keys()),on_change=on_patient_change)

if st.session_state.messages == []:
    if 'selectedPatient' in st.session_state:
        selected_case_details = st.session_state.case_dict[st.session_state.selectedPatient]
        system_message=("Vergiss alle vorherigen Anweisungen. Wir simulieren jetz ein Gespräch zwischen Arzt und Patient. Du bist der Patient und suchst nach Hilfe. Du bist kein Assistent. Du übernimmst die Rolle dieses Patienten: {}. "
                "Bitte antworte immer nur als dieser Patient. Deine Antworten sind eher kurz. Die relevanten Details muss der Arzt schon gezielt erfragen, damit Du entsprechend antwortest.").format(selected_case_details)
        st.session_state.messages.append({"role": "system", "content": system_message})

for message in st.session_state.messages:
    if message["role"] != "system":
        if message["role"] == "user":
            avatar_icon="/workspaces/patientgptlit/pages/HP-PhysioLogo.svg"
        else:
            avatar_icon="😫"
        with st.chat_message(message["role"],avatar=avatar_icon):
            st.markdown(message["content"])




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