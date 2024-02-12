from openai import OpenAI
import streamlit as st
import yaml
import io
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from streamlit_extras.switch_page_button import switch_page

# Initialize a session state variable that tracks the sidebar state (either 'expanded' or 'collapsed').
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'expanded'
# Streamlit set_page_config method has a 'initial_sidebar_state' argument that controls sidebar state.
st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
if 'password_correct' not in st.session_state or st.session_state["password_correct"]==False:
    switch_page("Passwort")
    st.stop()
def language_changed():
    st.session_state['language_changed'] = True
    on_patient_change()
#language = st.sidebar.selectbox('Choose your language:', 
                                #('Deutsch', 'English'), 
                                #on_change=language_changed)
    
st.session_state['language'] = 'Deutsch'
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-1106-preview"
if "messages" not in st.session_state:
    st.session_state.messages = []
if "case_dict" not in st.session_state or 'language_changed' in st.session_state:
    if st.session_state['language'] == 'Deutsch':
        Fallbeispiele_yaml = 'data/Fallbeispiele.yaml'
    else:
        Fallbeispiele_yaml = 'data/Fallbeispiele_English.yaml'
    # Read the YAML file
    with open(Fallbeispiele_yaml, 'r', encoding='utf-8') as file:
        case_list = yaml.safe_load(file)
    # Convert the list of cases to a dictionary with 'Kurzform' as keys and rows as values
    case_dict = {case['Kurzform']: case for case in case_list}
    st.session_state.case_dict = case_dict
    st.session_state.pop('language_changed', None)  # Clear the flag
if "selectedPatient" not in st.session_state:
    st.session_state.selectedPatient=""

if "chatMode" not in st.session_state:
    st.session_state.chatMode="patient"
        
if st.session_state.chatMode=="patient":
    st.session_state.avatar_user="👩‍⚕️"
    st.session_state.avatar_assistant="😫"
    st.session_state.chatinputPlaceholder="Sprechen Sie mit Ihrem Patienten"
else:
    st.session_state.avatar_user="👩‍⚕️"
    st.session_state.avatar_assistant="👨‍🏫"
    st.session_state.chatinputPlaceholder="Sprechen Sie mit Ihren Anamnese-Tutor"




def create_pdf_in_memory(messages):
    buffer = io.BytesIO()  # Create a buffer for the PDF
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    flowables = []

    # Flag to track if any message meets the display criteria
    message_displayed = False

    for message in messages:
        if message.get("display", False):  # Check if display property is True
            message_displayed = True
            text = f"{message['role']}: {message['content']}"
            flowables.append(Paragraph(text, styles['Normal']))
            flowables.append(Spacer(1, 12))

    # If no messages were added, add a default message
    if not message_displayed:
        text = "Im aktuellen Anamnesegespräch gab es keine Nachrichten."
        flowables.append(Paragraph(text, styles['Normal']))

    doc.build(flowables)
    buffer.seek(0)  # Reset buffer position to the start
    return buffer.getvalue()

def startFeedback():
    st.session_state.chatMode="feedback"
    st.session_state.messageHistory = st.session_state.messages
    st.session_state.messages = []
    # Entfernen aller Einträge aus st.session_state.messages, bei denen display == False ist
    st.session_state.messageHistory = [message for message in st.session_state.messageHistory if message['display'] == True]
    st.session_state.chatinputPlaceholder="Sprechen Sie mit Ihrem Anamnese-Tutor"
    # Weiter im Button-Event-Block
    with open('data/Tutor_instructions.yaml', 'r', encoding='utf-8') as file:
        tutor_instructions = yaml.safe_load(file)

    for message in tutor_instructions['messages']:
        if "{MessageHistory}" in message['content']:
            formatted_history = ""
            for msg in st.session_state.messageHistory:
                role = "Student: " if msg["role"] == "user" else "Patient: "
                formatted_history += role + msg["content"] + "\n"
            message['content'] = message['content'].replace("{MessageHistory}", formatted_history)
        if "{NamePatient}" in message['content']:
            selected_patient_key = st.session_state.selectedPatient
            selected_patient_details = st.session_state.case_dict[selected_patient_key]
            vorname = selected_patient_details["Basisdaten"]["Vorname"]
            nachname = selected_patient_details["Basisdaten"]["Nachname"]
            message['content'] = message['content'].replace("{NamePatient}", f"{vorname} {nachname}")
        if "{Generated}" in message['content']:
            # Senden der bisherigen Messages an die OpenAI API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            )
            generated_response = response.choices[0].message.content.strip()
            # Löschen des {Generated} Markers
            message['content'] = message['content'].replace("{Generated}", generated_response)
        st.session_state.messages.append({"role": message["role"], "content": message["content"], "display": message["display"]})
    st.rerun()

#https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
# SelectBox for choosing a patient

# Definieren Sie eine Funktion, die aufgerufen wird, wenn sich die Auswahl ändert
def on_patient_change():
    # Diese Funktion könnte zum Beispiel das Gespräch zurücksetzen oder andere Aktionen ausführen
    del st.session_state.messages
    del st.session_state.selectedPatient
    st.session_state.chatMode="patient"

# Check the current chat mode and set headerlabel accordingly
if st.session_state.chatMode == "patient":
    headerlabel = "Neuen Patient wählen, Feedback/Tutor Modus starten...hier klicken"
elif st.session_state.chatMode == "feedback":
    headerlabel = "Neue Anamnese starten, Training beenden...hier klicken"
else:
    # Optionally, set a default value for headerlabel if chatMode is not set or has an unexpected value
    headerlabel = "weitere Optionen"

headercontainer=st.container(border=True)  
with headercontainer:
    st.markdown('##### Verwendung')
    if st.session_state.chatMode=="patient":
        st.write("Ganz unten ist die Eingabezeile. Darüber kommunizieren Sie mit dem Patienten. Führen Sie immer ein Anamnesegespräch zu Ende. Dann haben Sie die Wahl ein Feedbackgespräch mit einem Tutor zu führen oder ein neues Gespräch mit einem Patienten zu beginnen, in dem Sie hier einen neuen Patienten wählen. Das alte Gespräch wird dann gelöscht. Beim Feedback greift der Tutor immer nur auf das letzte Gespräch zurück.") 
        st.session_state.selectedPatient = st.selectbox(
        "Wählen Sie nach Wunsch einen neuen Patienten",
        tuple(st.session_state.case_dict.keys()),  # Now the keys are 'Zusammenfassung'
        on_change=on_patient_change
        )
        with st.spinner('Warte bis der Anamnese-Tutor bereit ist...'):
            st.write("Speichern Sie das Gespräch mit dem Patienten zu einem beliebigen Zeitpunkt als PDF")
            btn = st.download_button(
                    label="Gespräch als PDF speichern",
                    data=create_pdf_in_memory(st.session_state.messages),
                    file_name="chat_history.pdf",
                    mime="application/octet-stream"
                )
            if st.button("Beende Anamnese, Starte Feedback/Tutor Modus"):
                startFeedback()
    elif st.session_state.chatMode=="feedback":
        st.write("Ganz unten ist die Eingabezeile. Darüber kommunizieren Sie mit dem Tutor. Beim Feedback greift der Tutor immer nur auf das letzte Gespräch zurück. Wenn Sie mit dem Gespräch fertig sind, können Sie einen neuen Patienten wählen, um ein neues Anamnesegespräch zu starten.") 
        st.write("Speichern Sie das Gespräch mit dem Tutor zu einem beliebigen Zeitpunkt als PDF")
        btn = st.download_button(
                label="Gespräch als PDF speichern",
                data=create_pdf_in_memory(st.session_state.messages),
                file_name="chat_history.pdf",
                mime="application/octet-stream"
            )    
        with st.expander("Wenn Sie ein neues Anamnesegespräch beginnen wollen, wählen Sie einfach einen neuen Patienten."):
            st.write("Achtung: Das vorherige Anamnesegespräch wird dann gelöscht. Weder Sie noch der Tutor kann dann darauf zurückgreifen.")
            st.session_state.selectedPatient = st.selectbox(
            "Wählen Sie nach Wunsch einen neuen Patienten",
            tuple(st.session_state.case_dict.keys()),  # Now the keys are 'Zusammenfassung'
            on_change=on_patient_change
            )  
        st.write("Wenn Sie ausreichend und mindestens 2 Durchgänge mit dem Anamnesetrainer trainiert haben, wechseln Sie zum Fragebogen um den nächsten Schritt der Studienteilnahme zu absolvieren.")
        if st.button("Fragebogen der Studie"):
            switch_page("Fragebogen")
    
st.write(f"Aktueller Patient: {st.session_state.case_dict[st.session_state.selectedPatient]['Kurzform']}")
if st.session_state.messages == []:
    if 'selectedPatient' in st.session_state:
        selected_case_details = st.session_state.case_dict[st.session_state.selectedPatient]
        if st.session_state['language'] == 'Deutsch':
            instructions_yaml = 'data/instruction_messages.yaml'
        else:
            instructions_yaml = 'data/instruction_messages_English.yaml'
        # Read the YAML file for instruction messages
        with open(instructions_yaml, 'r', encoding='utf-8') as file:
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

def display_messages():
    for message in st.session_state.messages:
        if message["display"]:
            if message["role"] == "user":
                avatar_icon=st.session_state.avatar_user
            else:
                avatar_icon=st.session_state.avatar_assistant
            with st.chat_message(message["role"],avatar=avatar_icon):
                st.markdown(message["content"])

display_messages()

if prompt := st.chat_input(st.session_state.chatinputPlaceholder):
    selected_patient_summary = st.session_state.selectedPatient
    st.session_state.messages.append({"role": "user", "content": prompt, "display":True})
    with st.chat_message("user",avatar=st.session_state.avatar_user):
        st.markdown(prompt)
    with st.chat_message("assistant",avatar=st.session_state.avatar_assistant):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True, frequency_penalty=0.2, presence_penalty=0.4, temperature=1.1
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response, "display":True})
    print(st.session_state.messages)
st.markdown('[Zurück nach oben scrollen für weitere Optionen](#verwendung)')
    



