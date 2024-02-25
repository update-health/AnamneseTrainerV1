# Importieren benötigter Module
from openai import OpenAI
import streamlit as st
import yaml
import io
import scripts.check_password as check_password
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from streamlit_extras.switch_page_button import switch_page
# Streamlit set_page_config-Methode hat ein 'initial_sidebar_state'-Argument, das den Zustand der Seitenleiste steuert.

st.set_page_config(layout="centered")

# Einbinden von benutzerdefinierten CSS-Stilen für die App
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.markdown(
        """
<style>
[data-testid="stExpander"] summary p{
    color: red;
}
""",unsafe_allow_html=True)

if 'password_correct' not in st.session_state or st.session_state["password_correct"] == False:
    check_password.check_password()
    st.stop()

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-0125-preview"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_mode" not in st.session_state:
    st.session_state.chat_mode = "KI-Patient"

if "selected_patient" not in st.session_state:
    st.session_state.selected_patient = ""

# Initialisierung der OpenAI-Clientinstanz
if "ai_client" not in st.session_state:    
    st.session_state.ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "case_dict" not in st.session_state:
    Fallbeispiele_yaml = 'data/Fallbeispiele.yaml'
    # Lesen der YAML-Datei
    with open(Fallbeispiele_yaml, 'r', encoding='utf-8') as file:
        case_list = yaml.safe_load(file)
    # Umwandlung der Liste von Fällen in ein Wörterbuch mit 'Kurzform' als Schlüssel und Zeilen als Werte
    case_dict = {case['Kurzform']: case for case in case_list}
    st.session_state.case_dict = case_dict


# Festlegen von Avatar-Icons und Eingabeplatzhalter basierend auf dem aktuellen Chat-Modus
if st.session_state.chat_mode == "KI-Patient":
    st.session_state.avatar_user = "👩‍⚕️"
    st.session_state.avatar_assistant = "😫"
    st.session_state.chat_input_placeholder = "Sprechen Sie mit Ihrem Patienten"
else:
    st.session_state.avatar_user = "👩‍⚕️"
    st.session_state.avatar_assistant = "👨‍🏫"
    st.session_state.chat_input_placeholder = "Sprechen Sie mit Ihrem Anamnese-Tutor"



# Funktion zum Erstellen eines PDF im Speicher
def create_pdf_in_memory():
    buffer = io.BytesIO()  # Puffer für das PDF erstellen
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    flowables = []

    # Flag zum Verfolgen, ob eine Nachricht den Anzeigekriterien entspricht
    message_displayed = False

    for message in st.session_state.messages:
        if message.get("display", False):  # Überprüfen, ob die Anzeige-Eigenschaft True ist
            message_displayed = True
            text = f"{message['role']}: {message['content']}"
            flowables.append(Paragraph(text, styles['Normal']))
            flowables.append(Spacer(1, 12))

    # Wenn keine Nachrichten hinzugefügt wurden, eine Standardnachricht hinzufügen
    if not message_displayed:
        text = "Im aktuellen Anamnesegespräch gab es keine Nachrichten."
        flowables.append(Paragraph(text, styles['Normal']))

    doc.build(flowables)
    buffer.seek(0)  # Pufferposition auf den Anfang zurücksetzen
    return buffer.getvalue()


def start_feedback():
    client=st.session_state.ai_client
    st.session_state.chat_mode = "KI-Tutor"
    st.session_state.message_history = st.session_state.messages
    st.session_state.messages = []
    # Entfernen von Einträgen aus st.session_state.messages, bei denen display == False ist
    st.session_state.message_history = [message for message in st.session_state.message_history if
                                        message['display'] == True]
    st.session_state.chat_input_placeholder = "Sprechen Sie mit Ihrem Anamnese-Tutor"
    # Weiter im Button-Event-Block
    with open('data/Tutor_instructions.yaml', 'r', encoding='utf-8') as file:
        tutor_instructions = yaml.safe_load(file)
    for message in tutor_instructions['messages']:
        if "{MessageHistory}" in message['content']:
            formatted_history = ""
            for msg in st.session_state.message_history:
                role = "Student: " if msg["role"] == "user" else "Patient: "
                formatted_history += role + msg["content"] + "\n"
            message['content'] = message['content'].replace("{MessageHistory}", formatted_history)
        if "{NamePatient}" in message['content']:
            selected_patient_key = st.session_state.selected_patient
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
        st.session_state.messages.append(
            {"role": message["role"], "content": message["content"], "display": message["display"]})
    st.rerun()



# Funktion, die aufgerufen wird, wenn sich die Auswahl ändert
def on_patient_change():
    # Diese Funktion könnte zum Beispiel das Gespräch zurücksetzen oder andere Aktionen ausführen
    del st.session_state.messages
    del st.session_state.selected_patient
    st.session_state.chat_mode = "KI-Patient"


def print_button(key):
    btn = st.download_button(
                key=key,
                label="Gespräch als PDF speichern",
                data=create_pdf_in_memory(),
                file_name="chat_history.pdf",
                mime="application/octet-stream",
                use_container_width=True
            )
    return btn

def patient_selectbox():
    pt_sbx=st.selectbox(
            "Wählen Sie nach Wunsch einen neuen Patienten",
            tuple(st.session_state.case_dict.keys()),  # Jetzt sind die Schlüssel 'Zusammenfassung'
            on_change=on_patient_change
        )
    return pt_sbx




# Erstellung eines Header-Containers
st.subheader('Modus: ' + st.session_state.chat_mode,"top")
headercontainer = st.expander(label="weitere Informationen")
with headercontainer:
    if st.session_state.chat_mode == "KI-Patient":
        st.markdown("""
                    Ganz unten ist die Eingabezeile. Darüber kommunizieren Sie mit dem Patienten. Führen Sie immer ein Anamnesegespräch nach eigenem Ermessen zu Ende. Dann haben Sie die Wahl ein Feedbackgespräch mit einem Tutor zu führen oder ein neues Gespräch mit einem Patienten zu beginnen, in dem Sie einen neuen Patienten wählen. Das alte Gespräch wird dann gelöscht. Beim Feedback greift der Tutor immer nur auf das letzte Gespräch zurück.  
                    Speichern Sie das Gespräch mit dem Patienten zu einem beliebigen Zeitpunkt als PDF.""")
        
    elif st.session_state.chat_mode == "KI-Tutor":
        st.markdown("""
                    Ganz unten ist die Eingabezeile. Darüber kommunizieren Sie mit dem Tutor. Beim Feedback greift der Tutor immer nur auf das letzte Gespräch zurück.     
                    Wenn Sie ein neues Anamnesegespräch beginnen wollen, wählen Sie einfach einen neuen Patienten.  
                    Wenn Sie mindestens 2 Durchgänge mit dem Anamnesetrainer trainiert haben, wechseln Sie zur Anleitung des Fragebogens.""")
    print_button("print_btn")
    if st.session_state.chat_mode == "KI-Patient":
        with st.spinner('Warte bis der Anamnese-Tutor bereit ist...'):
                if st.button("Beende Anamnese, Starte Feedback/Tutor Modus", use_container_width=True):
                    start_feedback()
    st.session_state.selected_patient=patient_selectbox()
    
    if st.session_state.chat_mode == "KI-Tutor":
        st.write("Wenn Sie ausreichend Anamnesegespräche geführt haben, wechseln Sie zum Fragebogen")
        if st.button("Anleitung zum Fragebogen", use_container_width=True):
            switch_page("Anleitung_Fragebogen")

# Anzeige des aktuellen Patienten
st.write('**Aktueller Patient: ' +st.session_state.case_dict[st.session_state.selected_patient]['Kurzform']+'**')

# Überprüfung, ob Nachrichten vorhanden sind, und Anzeigen von Anweisungen, falls nicht
if st.session_state.messages == []:
    if 'selected_patient' in st.session_state:
        selected_case_details = st.session_state.case_dict[st.session_state.selected_patient]
        instructions_yaml = 'data/instruction_messages.yaml'
        # Lesen der YAML-Datei für Anweisungsnachrichten
        with open(instructions_yaml, 'r', encoding='utf-8') as file:
            instruction_content = file.read()
        # Vorbereitung der Daten zur Ersetzung von Platzhaltern
        patient_details_str = ", ".join(
            [f"{key}: {value}" for key, value in selected_case_details.items()])
        replacements = {
            "Vorname": selected_case_details["Basisdaten"]["Vorname"],
            "Nachname": selected_case_details["Basisdaten"]["Nachname"],
            "Charakter": selected_case_details["Person"]["Charakter"],
            "Sprache": selected_case_details["Person"]["Sprache und Kommunikationstil"],
            "Gruss": selected_case_details["Person"]["Gruss"],
            "PatientenDetails": patient_details_str
        }
        # Ersetzen von Platzhaltern im gesamten YAML-Inhalt
        formatted_content = instruction_content.format(**replacements)
        # Konvertieren des formatierten Inhalts zurück in die YAML-Struktur
        instruction_messages = yaml.safe_load(formatted_content)
        # Hinzufügen von Nachrichten zu st.session_state.messages
        for message in instruction_messages['messages']:
            st.session_state.messages.append({
                "role": message['role'],
                "content": message['content'],
                "display": False
            })


# Funktion zur Anzeige von Nachrichten
def display_messages():
    for message in st.session_state.messages:
        if message["display"]:
            if message["role"] == "user":
                avatar_icon = st.session_state.avatar_user
            else:
                avatar_icon = st.session_state.avatar_assistant
            with st.chat_message(message["role"], avatar=avatar_icon):
                st.markdown(message["content"])


display_messages()


# Überprüfung der Eingabe und Erstellung einer Antwort
if prompt := st.chat_input(st.session_state.chat_input_placeholder):
    client=st.session_state.ai_client
    selected_patient_summary = st.session_state.selected_patient
    st.session_state.messages.append({"role": "user", "content": prompt, "display": True})
    with st.chat_message("user", avatar=st.session_state.avatar_user):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar=st.session_state.avatar_assistant):
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
    st.session_state.messages.append({"role": "assistant", "content": full_response, "display": True})
    print(st.session_state.messages)
    #rerun dient nur dazu, dass die beiden letzten Messages auch im PDF enthalten sind wenn auf Drucken geklickt wird
    st.rerun()

st.markdown('[Zurück nach oben scrollen für weitere Optionen](#top)')




