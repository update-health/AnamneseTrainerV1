import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.markdown("""
### Welchen potentiellen Einsatzzweck hat der Anamnesetrainer?

Die Ausbildung von Therapeuten und Medizinern legt einen Schwerpunkt auf das Erlernen strukturierter Anamnese und effektiver Kommunikationsfähigkeiten. Praktische Übungen, oft als Rollenspiel unter Kolleg*innen und mit Schauspieler*innen, sind essentiell um diese Fähigkeiten zu verbessern. Die Effektivität dieser Übungen hängt jedoch von den schauspielerischen Fähigkeiten der Teilnehmenden ab. Chatbots, basierend auf Large Language Models, könnten eine alternative oder ergänzende Methode bieten, um Anamnesegespräche zu trainieren.

### Was soll im Rahmen der Studie evaluiert werden?

Viele Faktoren können für die Eignung und Nützlichkeit von KI-Chatbots zum Anamnesetraining entscheidend beitragen. Wird die Anwendung als zu kompliziert oder herausfordernd empfunden? Wie wird der Realitätsgrad der Konversation mit dem Chatbot bewertet? Welche Faktoren tragen besonders dazu bei? Welchen Einsatzzweck sehen die Teilnehmenden in der zukünftigen Ausbildung von Physiotherapeuten?

Der Fokus der Untersuchung liegt dabei auf der Wahrnehmung der Nutzer*innen vom Chatbot in der Rolle eines Patienten.

### Wie funktioniert die Verwendung des Anamnesetrainers?

Auf der Seite "Anamnesetrainer" kann der Nutzer aus einer Dropdownliste oben auf der Seite einen Patienten auswählen. Deren relevanten Daten sind als eine Art Skript, im Sinne eines standardisierten Patienten, im System hinterlegt. Es kann jederzeit ein anderer Patient aus der Liste gewählt werden. Dann wird sofort die bisherige Unterhaltung gelöscht und ein neues Gespräch startet. Das Gespräch wird über eine einfache Chatbox geführt, sowie viele es von Messengerdiensten (wie z.B. WhatsApp) oder anderen Chatbots (wie z.B. ChatGPT) kennen. Unten ist die Eingabezeile zu sehen. In diese kann per Tastatur, aber auch per Spracheingabe (abhängig vom jeweiligen System) Text eingegeben werden. Nach den ersten 4 Antworten im Chatfenster, erscheint unterhalb des Textes ein Button, der es dem Nutzer ermöglicht das Patientengespräch zu beenden und eine Evaluation mit dem virtuellen Tutor zu starten. Dieser analysiert das Anamnesegespräch und leitet ein Feedbackgespräch dazu an. Das Gespräch mit dem Patienten kann dann nicht weitergeführt, sondern nur neu gestartet werden. Jederzeit kann ganz nach oben gescrollt werden, um einen neuen Patienten zu wählen und ein neues Patientengespräch zu starten. Auf der linken Seite in der Seitenleiste ist ein Button "Gespräch als PDF speichern" der genau das tut. Das aktuelle Gespräch wird heruntergeladen und auf Ihrem Gerät gespeichert. Machen Sie davon gerne Gebrauch um später in der Reflektion und Fokusgruppen auf konkrete Beispiele eingehen zu können. 

### Wie soll ich mich verhalten?

Um ein insgesamt realistisches Szenario zu ermöglichen, muss nicht nur der Chatbot möglichst realistisch antworten, sondern auch der Nutzer. Es kann verlockend sein den Chatbot, durch absurde oder unangemessene Sprache oder Aufforderungen an die Grenzen zu bringen. Das wäre vergleichbar mit dem Rollenspiel unter Mitstudierenden, in denen mindestens ein Student in seiner Rolle bewusst unsinnig agiert. Wir gehen davon aus, dass der Nutzer ein Interesse an der Verbesserung der eigenen Anamnesefähigkeiten hat und das Tool nutzt, um ein Patientengespräch realitätsnah zu simulieren. Versuchen Sie daher möglichst so zu fragen oder zu antworten, wie Sie es bei einem echten Patienten auch tun würden. Das gleiche gilt für das anschließende Feedbackgespräch mit dem virtuellen Tutor.

### Wie viele Patientengespräche soll und darf ich führen?

Es gibt kein vorgeschriebenes Maximum an Versuchen. Legen Sie als Teilnehmer*in der Studie jedoch zunächst Fokus auf Qualität und weniger auf Quantität der Gespräche. Bitte nehmen Sie sich daher ausreichend Zeit, bevor Sie ein Gespräch starten. Mindestens zwei Patientengespräche sollten umfassend und, von Ihrer Seite aus, möglichst realitätsnah geführt werden. Gerne auch mehr. Der Fokus der Studie liegt auf dem Chatbot in der Rolle als Patient.   

### Wohin wende ich mich bei Fragen?

Wenn Sie Fragen zur Studie oder Unklarheiten bei der Verwendung des Tools haben, wenden Sie sich per E-Mail an Arne Brödel unter brodela@cardiff.ac.uk.

Um zu starten, klicken Sie den Button. Sie wechseln dann zur Seite "Passwort", wo Sie zunächst das Passwort eingeben müssen, bevor Sie zum Anamnesetrainer wechslen können.
  
    """)
if st.button("Passwort"):
        switch_page("Passwort")