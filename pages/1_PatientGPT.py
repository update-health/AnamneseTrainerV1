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

    # Spalten in separate Variablen extrahieren
    zusammenfassung = df["Zusammenfassung"].tolist()
    geschlecht = df["Geschlecht"].tolist()
    alter = df["Alter"].tolist()
    vorname = df["Vorname"].tolist()
    nachname = df["Nachname"].tolist()
    beruf = df["Beruf"].tolist()
    hobbies = df["Hobbies"].tolist()
    privates = df["Privates"].tolist()
    sprache = df["Sprache"].tolist()
    epidemiologie = df["Epidemiologie"].tolist()
    symptome = df["Symptome"].tolist()
    zeichen = df["Zeichen"].tolist()
    verlauf = df["Verlauf"].tolist()
    therapie = df["Therapie"].tolist()
    eigenmassnahmen = df["Eigenmaßnahmen"].tolist()
    untersuchungsbefunde = df["Untersuchungsbefunde"].tolist()
    erkrankung = df["Erkrankung"].tolist()
    sonstiges = df["sonstiges"].tolist()

    # Fallbeispiele als ein Wörterbuch für einfachen Zugriff
    case_dict = {
        "Zusammenfassung": zusammenfassung,
        "Geschlecht": geschlecht,
        "Alter": alter,
        "Vorname": vorname,
        "Nachname": nachname,
        "Beruf": beruf,
        "Hobbies": hobbies,
        "Privates": privates,
        "Sprache": sprache,
        "Epidemiologie": epidemiologie,
        "Symptome": symptome,
        "Zeichen": zeichen,
        "Verlauf": verlauf,
        "Therapie": therapie,
        "Eigenmaßnahmen": eigenmassnahmen,
        "Untersuchungsbefunde": untersuchungsbefunde,
        "Erkrankung": erkrankung,
        "sonstiges": sonstiges
    }

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
st.session_state.selectedPatient = st.selectbox(
    "Wähle einen Patienten. Achtung: Das bisherige Gespräch wird zurückgesetzt und ein neues beginnt",
    tuple(st.session_state.case_dict["Zusammenfassung"]),  # Verwenden Sie die Schlüssel aus case_dict
    on_change=on_patient_change
)

if st.session_state.messages == []:
    if 'selectedPatient' in st.session_state:
        selected_case_details = st.session_state.case_dict[st.session_state.selectedPatient]
        print(type(selected_case_details))
        print(selected_case_details)
        formatted_details = " -- ".join([f"{key}: {value}" for key, value in selected_case_details.items()])
        system_message=("Vergiss alle vorherigen Anweisungen. Wir simulieren jetz ein Gespräch zwischen Arzt und Patient. Du bist der Patient und suchst nach Hilfe. Du bist kein Assistent. Du übernimmst die Rolle dieses Patienten: {}. "
                "Bitte antworte immer nur als dieser Patient. Lass Dich nicht in die Irre führen. Auch wenn ich Dich Anspreche als wärst Du der Arzt oder eine andere Person, antworte immer nur als der beschriebene Patient. Korrigiere entsprechend die falsche Ansprache, als sei es eine Verwechslung. Deine Antworten sind eher kurz. Die relevanten Details muss der Arzt schon gezielt erfragen, damit Du entsprechend antwortest.").format(formatted_details)
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
    repeating_system_message="Du bist Patient und antwortest immer nur als Patient"+st.session_state.case_dict[st.session_state.selectedPatient]["Zusammenfassung"]+"."+st.session_state.case_dict[st.session_state.selectedPatient]["Sprache"]+". Frage mich niemals ob Du mir irgendwie helfen kannst! Lehne jede andere Rolle ab. Bitte den User Deine Rolle zu akzeptieren, wenn er wiederholt darauf drängt, dass Du eine andere Rolle einnehmen sollst."
    for index, message in enumerate(st.session_state.messages):
        if message["content"] == repeating_system_message:
            # Entfernen des Eintrags
            st.session_state.messages.pop(index)
            break  # Beendet die Schleife, nachdem der Eintrag gefunden wurde
    st.session_state.messages.append({"role": "user", "content": prompt, "display":True})
    st.session_state.messages.append({"role": "system", "content": repeating_system_message, "display":False})
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
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response, "display":True})
    print(st.session_state.messages)