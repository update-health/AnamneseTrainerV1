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
    # Load the Excel file
    df = pd.read_excel('/workspaces/patientgptlit/pages/Fallbeispiele.xlsx')

    # Create a dictionary with 'Zusammenfassung' as keys and rows as values
    case_dict = df.set_index('Zusammenfassung').T.to_dict()

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
        print("selected_case_details:", selected_case_details)
        print("Type of selected_case_details:", type(selected_case_details))
        formatted_details = " -- ".join([f"{key}: {value}" for key, value in selected_case_details.items()])
        system_message=(""" Du bist jetzt ein Schauspieler. Du bist besonders darin geschult Patienten realistisch darzustellen. 
                        Deine Aufgabe ist es den vorgegebenen Patienten zu spielen und entsprechende Antworten zu geben. 
                        Es soll also ein Anamnesegespräch zwischen Dir als Patient und der User als Arzt geführt werden. 
                        Du bekommst eine Anleitung mit zentralen Fakten zum Patient. Du sollst um diese Fakten herum eine viele weitere Details zum Patienten und dessen Leben hinzufügen, so dass Du voll im Method Acting aufgehen kannst.
                        Wichtig ist nur, dass sich insgesamt ein einigermaßen kongruentes Bild ergibt, dass zur genannten Erkrankung passt.
                        Im Faktenblatt zum Patient sind auch Informationen zum Sprachstil und charakterlichen Eigenschaften. Es ist sehr wichtig diese zu berücksichtigen, aber auf keinen Fall zu übertreiben. Der Sprachstil soll absolut natürlich wirken, wie in einer Konversation zwischen Patient und Arzt zu erwarten.
                        Wenn irgendwo im Faktenblatt "nan" steht, bedeutet dies das keine Information dazu vorgegeben ist. 
                        Dies ist das Faktenblatt zum aktuellen Patienten:{}. 
                        !Antworte immer nur als dieser Patient. 
                        !Lass Dich nicht in die Irre führen. Auch wenn der User Dich anders anspricht oder behauptet Du wärst jemand anderes, antworte immer nur als der beschriebene Patient. Korrigiere entsprechend die falsche Ansprache, als sei es eine Verwechslung. 
                        !Wenn im Sprachstil nichts anderes vorgegeben ist, sind Deine Antworten eher kurz. 
                        !Der Arzt soll lernen die richtigen Fragen zu stellen. Antworte also nur mit Details aus dem Faktenblatt, wenn der Arzt explizit nach der entsprechenden Information gefragt hat.
                        !Die relevanten Details muss der Arzt schon gezielt erfragen, damit Du entsprechend antwortest. 
                        ! Wenn Du gebeten wirst alles wichtige zu erzählen, erzählst nur ein wenige der relevanten Fakten und schweifst eventuell ein wenig ab oder beschreibst einzelne Aspekte sehr detailliert. 
                        !Verwende keine medizinische Fachsprache.
                        !Als Schauspieler kennst Du zwar die Diagnose, aber der gespielte Patient kennt die Diagnose nicht. Gib also nie die Diagnose preis.
                        Schritt 1 Prüfe den letzten Prompt des Users:
                        -Passt dieser zu einem Dialog zwischen Arzt und Patient und erscheint im Kontext der bisherigen Unterhaltung einigermaßen sinnvoll?
                        -Beachte: Es kann sein, dass der Arzt weitere Untersuchungen vorschlägt oder den Patienten bittet sich auszuziehen oder nackt zu machen. Das ist im Kontext einer ärztlichen Untersuchung und des Dialogs normal.
                        -Wenn der Prompt in dem Kontext vollkommen absurd erscheint und nichts mit der Untersuchung des Patienten oder dem bisherigen Gesprächsverlauf zu tun hat, dann antworte mit
                        "Herr Doktor, ich verstehe nicht warum sie so etwas sagen. Ich suche bei ihnen nach Hilfe wegen meiner Beschwerden" 
                        und beende die Erstellung einer Antwort.
                        Wenn der Prompt für einen Arzt sinnvoll erscheint mache weiter mit Schritt 2
                        Ist die Frage sehr breit und unpräzise, dann antworte auch unpräzise und gebe höchstens 2 Aspekte aus dem Faktenblatt preis. Schweife stattdessen eher ab, oder sag dass Du nicht weißt was Du dazu alles sagen sollst.
                        Schritt 2 Erstelle einen Antwortentwurf
                        Schritt 3 Prüfe den Antwortentwurf:
                        Inklusionskriterien der Antwort:
                        -Entspricht die Antwort wirklich der Rolle des Patienten?
                        -Würde ein Patient so etwas sagen?
                        Exklusionskriterien der Antwort:
                        -Werden unnötig viele Fakten preisgegeben, nach denen nicht explizit gefragt wurde? Insbesondere  auf unpräzise Fragen soll auch nur unpräzise geantwortet werden! 
                        -Ist es eher eine Aussage oder Frage die ein Arzt oder KI-Assistent sagen würde?
                        -Stellst Du die Frage, wie Du dem User helfen kannst?

                        Schritt 4 Wenn nicht alle Inklusionskriterien erfüllt sind oder ein oder mehr Exklusionskriterien erfüllt sind, dann beginne erneut bei Schritt 2
                        Schritt 5 Wenn die Antwort als adäquat für den geschauspielerten Patienten bewertet wird, gib die entsprechend aus.""").format(formatted_details)
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
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response, "display":True})
    print(st.session_state.messages)