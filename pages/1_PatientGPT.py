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
    json_file_path = '/workspaces/patientgptlit/pages/Fallbeispiele.json'

    # Read the JSON file
    df = pd.read_json(json_file_path)

    # Create a dictionary with 'Zusammenfassung' as keys and rows as values
    case_dict = df.set_index('Kurzform').T.to_dict()

    st.session_state.case_dict = case_dict

if "selectedPatient" not in st.session_state:
    st.session_state.selectedPatient=""

avatar_user="👩‍⚕️"
avatar_assistant="😫"

# Definieren Sie eine Funktion, die aufgerufen wird, wenn sich die Auswahl ändert
def on_patient_change():
    # Diese Funktion könnte zum Beispiel das Gespräch zurücksetzen oder andere Aktionen ausführen
    st.session_state.clear()

#https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
# SelectBox for choosing a patient
st.session_state.selectedPatient = st.selectbox(
    "Wähle einen Patienten. Achtung: Das bisherige Gespräch wird zurückgesetzt und ein neues beginnt",
    tuple(st.session_state.case_dict.keys()),  # Now the keys are 'Zusammenfassung'
    on_change=on_patient_change
)

if st.session_state.messages == []:
    if 'selectedPatient' in st.session_state:
        selected_case_details = st.session_state.case_dict[st.session_state.selectedPatient]
        print("selectedPatient:", st.session_state.selectedPatient)
        print("Type of selected_case_details:", type(selected_case_details))
        with open('/workspaces/patientgptlit/pages/system_message_template.txt', 'r', encoding='utf-8') as file:
            system_message_template = file.read()
            selected_case_details_string = ", ".join([f"{key}: {value}" for key, value in selected_case_details.items()])
            system_message = system_message_template.format(Patientendetails=selected_case_details_string,SpracheCharakter=selected_case_details["Person"]["Charakter"]+selected_case_details["Person"]["Sprache und Kommunikationstil"])
            print(system_message)
        st.session_state.messages.append({"role": "system", "content": system_message, "display":False})

for message in st.session_state.messages:
    if message["display"]:
        if message["role"] == "user":
            avatar_icon=avatar_user
        else:
            avatar_icon=avatar_assistant
        with st.chat_message(message["role"],avatar=avatar_icon):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    selected_patient_summary = st.session_state.selectedPatient
    st.session_state.messages.append({"role": "user", "content": prompt, "display":True})
    with st.chat_message("user",avatar=avatar_user):
        st.markdown(prompt)

    with st.chat_message("assistant",avatar=avatar_assistant):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True, frequency_penalty=0.2, presence_penalty=0.4, temperature=1.2
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response, "display":True})
    print(st.session_state.messages)