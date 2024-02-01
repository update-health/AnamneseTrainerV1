import streamlit as st
import hmac
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page


LOGGER = get_logger(__name__)

def display_homepage():
    #Display the content of the homepage.
    st.markdown("""
### Herzlich Willkommen zur Pilotstudie zum KI-basierten Anamnesetrainer
Du musst wie folgt vorgehen:  
        1. Auf der Seite "Konsent" das entsprechende Formular ausfüllen und absenden. Du musst dabei Deine E-Mail-Adresse angeben und bestätigen. Danach erhälst Du eine E-Mail von mir mit dem Zugangspasswort für den Anamnesetrainer.  
        2. Auf der Seite "Teilnehmerdokumente" die Informationen für die Teilnehmenden der Studie durchlesen. Auf der Seite "Konsent" ist die "read-aloud, think-aloud" Methode vorgestellt, die Du hier anwenden sollst.  
        3. Auf der Seite "Anleitung" die detaillierte Anleitung zur Nutzung des Anamnesetrainers lesen.  
        4. Auf der Seite "Passwort" das Passwort eingeben welches Du per Email von mir bekommst. Wenn Du bis dahin keines erhalten hast, melde Dich bitte bei mir.
        5. Auf der Seite "Anamnesetrainer" entsprechend der Anleitung zwei Runden Anamnesegespräch mit Patienten führen.
        6. Auf der Seite "Fragebogen" den Fragenbogen für die Studie ausfüllen. Hierbei bitte auch wieder eine Sprachaufnahme mit der "read-aloud, think-aloud" Methode machen.   
                        
### Wohin wende ich mich bei Fragen?

Wenn Sie Fragen zur Studie oder Unklarheiten bei der Verwendung des Tools haben, wenden Sie sich per E-Mail an Arne Brödel unter brodela@cardiff.ac.uk.

Um zu starten, klicken Sie den Button. Sie wechseln dann zur Seite "Anamnesetrainer".
  
    """)
    
    if st.button("Anamnesetrainer"):
        switch_page("Anamnesetrainer")


def run():
    st.set_page_config(page_title="Anamnesetrainer", page_icon="👩‍⚕️")
    st.write("# Herzlich Willkommen zum Anamnesetrainer")

    display_homepage()


if __name__ == "__main__":
    run()
