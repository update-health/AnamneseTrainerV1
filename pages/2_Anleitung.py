import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="centered")
# Einbinden von benutzerdefinierten CSS-Stilen für die App
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.markdown("""
### Nutzung des Anamnesetrainers

Nutzer\*innen wählen aus einer Dropdownliste einen fiktiven Patienten aus, dessen Daten im System hinterlegt sind. Das Gespräch erfolgt über eine Chatbox. Jederzeit ermöglicht ein Button das Anamnesegespräch zu beenden und ein Feedbackgespräch mit einem virtuellen Tutor zu starten. Es sollte aber immer erst das Anamnesegespräch vollständig zuende geführt werden. Gespräche können als PDF gespeichert werden.

### Verhaltenshinweise

Nutzer\*innen sollten mit dem Chatbot möglichst wie mit echten Patient\*innen kommunizieren, um ihre Anamnesefähigkeiten zu verbessern. Absurdes oder unangemessenes Verhalten sollte vermieden werden, um ein realistisches Trainingsszenario zu ermöglichen.

### Anzahl der Patientengespräche

Es sollten mindestens 2 ausführliche Anamnesegespräche mit anschließender Auswertung mit dem KI-Tutor durchgeführt werden.  
Es gibt kein Maximum an Gesprächen im Rahmen dieser Studienteilnahme.  

### Speichern der Gespräche
Sobald Sie im Anamnesetrainer einen neuen Patienten wählen oder zwischen dem Modus KI-Patient und KI-Tutor wechseln, ist der Gesprächsverlauf gelöscht. Sie haben jederzeit die Möglichkeit das aktuelle Gespräch als PDF zu speichern. Bitte machen Sie davon Gebrauch, um später in der Auswertung exakter auf bestimmte Aspekte der Interaktion eingehen zu können. Ebenso wäre es für die Studie wertvoll, Interaktionen exakt zitieren zu können. Daher bitte ich Sie, Ihre gespeicherten Gesprächsverläufe als PDF auf der letzen Seite "Dateiupload" mit hochzuladen. Alternativ können Sie auch Screenshots des Chatverlaufs als Bilder speichern. 

### Kontakt bei Fragen

Bei Fragen oder Unklarheiten steht Arne Brödel unter brodela@cardiff.ac.uk zur Verfügung.  
            
### Nächster Schritt               
            
Wechseln Sie zur Seite "Anamnesetrainer".
    """)
if st.button("Anamnesetrainer", use_container_width=True):
        switch_page("Anamnesetrainer")