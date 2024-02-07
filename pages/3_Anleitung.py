import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.markdown("""
### Einsatzzweck des Anamnesetrainers

Der Anamnesetrainer soll das Erlernen strukturierter Anamnese und Kommunikationsfähigkeiten für Therapeuten und Mediziner unterstützen. Chatbots, basierend auf Large Language Models, bieten eine alternative oder ergänzende Methode zu traditionellen Rollenspielen, um Anamnesegespräche zu trainieren.

### Studienziele

Die Studie evaluiert die Eignung und Nützlichkeit von KI-Chatbots im Anamnesetraining, insbesondere die Anwendungsfreundlichkeit, den Realitätsgrad der Konversationen und den potentiellen Einsatz in der Ausbildung. Der Fokus liegt auf der Nutzerwahrnehmung des Chatbots als Patient.

### Nutzung des Anamnesetrainers

Nutzer wählen aus einer Dropdownliste einen Patienten aus, dessen Daten im System hinterlegt sind. Das Gespräch erfolgt über eine Chatbox. Nach den ersten vier Antworten ermöglicht ein Button das Gespräch zu beenden und ein Feedbackgespräch mit einem virtuellen Tutor zu starten. Gespräche können gespeichert werden, um in Reflektionen und Fokusgruppen genutzt zu werden.

### Verhaltenshinweise

Nutzer sollen den Chatbot realistisch als Patienten nutzen, um ihre Anamnesefähigkeiten zu verbessern. Absurdes oder unangemessenes Verhalten sollte vermieden werden, um ein realistisches Trainingsszenario zu gewährleisten.

### Anzahl der Patientengespräche

Es gibt kein Maximum an Gesprächen. Nutzer sollten den Fokus auf die Qualität und Realitätsnähe der Gespräche legen, mit einem Minimum von zwei umfassenden Patientengesprächen.

### Kontakt bei Fragen

Bei Fragen oder Unklarheiten steht Arne Brödel unter brodela@cardiff.ac.uk zur Verfügung. Um zu starten, ist zunächst ein Passwort auf der entsprechenden Seite einzugeben.

  
    """)
if st.button("Passwort"):
        switch_page("Passwort")