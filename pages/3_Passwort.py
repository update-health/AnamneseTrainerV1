import streamlit as st
import hmac
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="centered")
# Einbinden von benutzerdefinierten CSS-Stilen für die App
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def check_password():
    #Check the user's password and control page access.
    def password_entered():
        #Verify the entered password.
        if hmac.compare_digest(st.session_state["password"], st.secrets["PASSWORD"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state or not st.session_state.get("password_correct", False):
        # Show input for password.
        st.markdown("Bitte geben Sie Ihr Passwort ein. Dieses wurde oder wird Ihnen nach Zusenden der Einverständniserklärung per Email zugesendet.")
        st.text_input("Passwort", type="password", on_change=password_entered, key="password")
        if "password_correct" in st.session_state:
            st.error("😕 Passwort fehlerhaft. Probieren Sie es erneut. Wenden Sie sich ansonsten an brodela@cardiff.ac.uk")
        return False
    return True
check_password()

def display_content():
    st.markdown("Wenn Sie die Einverständniserklärung unterschrieben, die Anleitung gelesen und keine weiteren Fragen haben, können Sie nun mit dem Anamnesetrainer arbeiten.")
    if st.button("Anamnesetrainer", use_container_width=True):
        switch_page("Anamnesetrainer")
    
    st.markdown('Falls Sie den Anamnesetrainer bereits verwendent haben und von der Seite "Fragebogen" oder "Dateiupload" hierhin umgeleitet wurden, können Sie nun über die beiden Buttons dorthin zurückkehren:')
    if st.button("Fragebogen", use_container_width=True):
        switch_page("Fragebogen")
    if st.button("Dateiupload", use_container_width=True):
        switch_page("Dateiupload")

if "password_correct" in st.session_state and st.session_state.get("password_correct", True):
    display_content()
