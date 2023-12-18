from openai import OpenAI
import streamlit as st
import pandas as pd
import yaml
from streamlit_extras.switch_page_button import switch_page

# Initialize a session state variable that tracks the sidebar state (either 'expanded' or 'collapsed').
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

# Streamlit set_page_config method has a 'initial_sidebar_state' argument that controls sidebar state.
st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)
if 'password_correct' not in st.session_state or st.session_state["password_correct"]==False:
    switch_page("hello")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-1106-preview"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "case_dict" not in st.session_state:
    yaml_file_path = 'data/Fallbeispiele.yaml'

    # Read the YAML file
    with open(yaml_file_path, 'r', encoding='utf-8') as file:
        case_list = yaml.safe_load(file)

    # Convert the list of cases to a dictionary with 'Kurzform' as keys and rows as values
    case_dict = {case['Kurzform']: case for case in case_list}

    st.session_state.case_dict = case_dict

if "selectedPatient" not in st.session_state:
    st.session_state.selectedPatient=""

avatar_user="👩‍⚕️"
avatar_assistant="😫"

# Definieren Sie eine Funktion, die aufgerufen wird, wenn sich die Auswahl ändert
def on_patient_change():
    # Diese Funktion könnte zum Beispiel das Gespräch zurücksetzen oder andere Aktionen ausführen
    del st.session_state.messages
    del st.session_state.selectedPatient

#https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
# SelectBox for choosing a patient
st.markdown("##### Wähle einen Patienten") 
st.session_state.selectedPatient = st.selectbox(
    "Achtung: Das bisherige Gespräch wird zurückgesetzt und ein neues beginnt",
    tuple(st.session_state.case_dict.keys()),  # Now the keys are 'Zusammenfassung'
    on_change=on_patient_change
)

if st.session_state.messages == []:
    if 'selectedPatient' in st.session_state:
        selected_case_details = st.session_state.case_dict[st.session_state.selectedPatient]

        # Read the YAML file for instruction messages
        with open('data/instruction_messages.yaml', 'r', encoding='utf-8') as file:
            instruction_content = file.read()

        # Prepare the data to replace placeholders
        patient_details_str = ", ".join([f"{key}: {value}" for key, value in selected_case_details.items()])
        replacements = {
            "Vorname": selected_case_details["Basisdaten"]["Vorname"],
            "Nachname": selected_case_details["Basisdaten"]["Nachname"],
            "Charakter": selected_case_details["Person"]["Charakter"],
            "Sprache": selected_case_details["Person"]["Sprache und Kommunikationstil"],
            "Gruss": selected_case_details["Person"]["Gruss"],
            "PatientenDetails": patient_details_str
        }

        # Replace placeholders in the entire YAML content
        formatted_content = instruction_content.format(**replacements)

        # Convert the formatted content back to YAML structure
        instruction_messages = yaml.safe_load(formatted_content)

        # Append messages to st.session_state.messages
        for message in instruction_messages['messages']:
            st.session_state.messages.append({
                "role": message['role'],
                "content": message['content'],
                "display": False
            })         

for message in st.session_state.messages:
    if message["display"]:
        if message["role"] == "user":
            avatar_icon=avatar_user
        else:
            avatar_icon=avatar_assistant
        with st.chat_message(message["role"],avatar=avatar_icon):
            st.markdown(message["content"])

if prompt := st.chat_input("Begrüße den Patienten und führe ein Anamnesegespräch"):
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



