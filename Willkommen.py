import streamlit as st
import hmac
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page
import scripts.random_ident_string as ris


LOGGER = get_logger(__name__)

def display_homepage():
    # Einbinden von benutzerdefinierten CSS-Stilen für die App
    with open("styles/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    #Display the content of the homepage.
    st.markdown("""
### Herzlich Willkommen zur Studie zum KI-basierten Anamnesetraining
Vielen Dank, für Ihre Teilnahme.  
Diese besteht aus den folgenden Schritten:  
1. Auf der Seite "Einverständnis" das Informationsschreiben lesen und das Einverständnis-Formular ausfüllen und absenden. Sie müssen dabei Ihre E-Mail-Adresse angeben und bestätigen. Danach erhalten Sie eine E-Mail von mir mit dem Zugangspasswort für den Anamnesetrainer.   
2. Auf der Seite "Anleitung" die detaillierte Anleitung zur Nutzung des Anamnesetrainers lesen.  
3. Auf der Seite "Passwort" das Passwort eingeben, welches Sie per Email von mir erhalten haben. Wenn Sie auch 24 Stunden nach Einsendung der Einverständniserklrärung keines erhalten hast, melden Sie sich bitte bei mir unter brodela@cardiff.ac.uk  
4. Auf der Seite "Anamnesetrainer" entsprechend der Anleitung Anamnesegespräch mit mindestens zwei KI-Patienten führen und die Anamnesegespräche mit dem KI-Tutor evaluieren.  Die Gesprächsverläüfe können Sie als PDF speichern.
5. Auf der Seite "Anleitung Fragebogen" die genaue Durchführung der Datenerfassung mit Fragebogen und Sprachrekorder kennenlernen.  
6. Auf der Seite "Fragebogen" den Fragebogen ausfüllen und dabei die eigenen Gedanken aussprechen und eine oder mehrere Sprachaufnahmen anfertigen.  
7. Auf der Seite "Dateiupload" den Link öffnen um dort Ihre Sprachaufnahmen und von Ihnen gespeicherte Gesprächsverläufe mit dem KI-Anamnesetrainer auf einen sicheren Cloud-Speicher der Cardiff University hochladen. 

Die Teilnahme an der Studie sollte an nahezu jedem PC, Laptop, Tablet oder Smartphone möglich sein. Bevorzugt sollte jedoch ein Laptop oder PC mit den Browsern Chrome, Edge oder Firefox verwendet werden.  
                                        
### Wohin wende ich mich bei Fragen?

Wenn Sie Fragen zur Studie oder Unklarheiten bei der Verwendung des Anamnesetrainers haben, wenden Sie sich bitte per E-Mail an Arne Brödel unter brodela@cardiff.ac.uk.

    """)
    st.markdown('Wechseln Sie jetzt zur Seite "Einverständnis"')
    if st.button("Einverständnis"):
        switch_page("Einverständnis")
    



def run():
    st.set_page_config(page_title="Anamnesetrainer", page_icon="👩‍⚕️",layout="centered")
    display_homepage()
    if "random_id_string" not in st.session_state:
        st.session_state.random_id_string=ris.generate_random_string()



if __name__ == "__main__":
    run()
