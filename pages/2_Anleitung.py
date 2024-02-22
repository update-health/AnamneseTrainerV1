import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="centered")
# Einbinden von benutzerdefinierten CSS-Stilen für die App
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.markdown("""
### Nutzung des Anamnesetrainers

Nutzer*innen wählen aus einer Dropdownliste einen Patienten aus, dessen Daten im System hinterlegt sind. Das Gespräch erfolgt über eine Chatbox. Jederzeit ermöglicht ein Button das Anamnesegespräch zu beenden und ein Feedbackgespräch mit einem virtuellen Tutor zu starten. Es sollte aber immer erst das Anamnesegespräch vollständig zuende geführt werden. Gespräche können als PDF gespeichert werden, um in Reflektionen und Fokusgruppen genutzt zu werden.

### Verhaltenshinweise

Nutzer*innen sollten mit dem Chatbot möglichst wie echten Patient*innen umgehen, um ihre Anamnesefähigkeiten zu verbessern. Absurdes oder unangemessenes Verhalten sollte vermieden werden, um ein realistisches Trainingsszenario zu ermöglichen.

### Anzahl der Patientengespräche

Es sollten mindestens 2 ausführliche Anamnesegespräche und anschließende Auswertung mit dem KI-Tutor durchgeführt werden.  
Es gibt kein Maximum an Gesprächen im Rahmen dieser Studienteilnahme.  
Nutzer sollten den Fokus auf die Qualität und Realitätsnähe der Gespräche legen.

### Speichern der Gespräche
Sobald Sie im Anamnesetrainer einen neuen Patienten wählen oder zwischen dem Modus KI-Patient und KI-Tutor wechseln, ist der Gesprächsverlauf gelöscht. Sie haben jederzeit die Möglichkeit das aktuelle Gespräch als PDF zu speichern. Bitte machen Sie davon Gebrauch, um später in der Auswertung exakter auf bestimmte Aspekte der Interaktion eingehen zu können. Ebenso wäre es für die Studie wertvoll, Interaktionen exakt zitieren zu können. Daher wäre es hilfreich, wenn Sie Ihre gespeicherten Gesprächsverläufe als PDF auf der letzen Seite "Dateiupload" mit hochladen. Es ist auch möglich nur Auszüge der Gespräch hochzuladen, in dem Sie das gespeicherte PDF bearbeiten, Text daraus in eine neue Datei kopieren oder einfach Screenshots des Chatverlaufs als Bilder speichern. 

### Kontakt bei Fragen

Bei Fragen oder Unklarheiten steht Arne Brödel unter brodela@cardiff.ac.uk zur Verfügung.  
            
### Nächster Schritt               
            
Um zu starten, ist zunächst ein Passwort auf der entsprechenden Seite einzugeben. Dieses Passwort sollte spätestens 24 Stunden nach Zusendung der Einverständniserklärung an die angebene E-Amil-Adresse gesendet worden sein. Falls Sie kein Passwort erhalten haben, schreiben Sie bitte an brodela@cardiff.ac.uk  
Um das Passwort einzugeben, wechseln Sie bitte jetzt auf die Seite Passwort
 
    """)
if st.button("Passwort", use_container_width=True):
        switch_page("Passwort")