import streamlit as st
import hmac
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page

def check_password():
    """Check the user's password and control page access."""
    def password_entered():
        """Verify the entered password."""
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
            st.error("😕 Password incorrect")
        return False
    return True
check_password()

def display_content():
    st.markdown("Wenn Sie alle vorherigen Schritte abgeschlossen und alle Dokumente gelesen haben, können Sie nun mit dem Anamnesetrainer arbeiten.")
    if st.button("Anamnesetrainer"):
        switch_page("Anamnesetrainer")

if "password_correct" in st.session_state and st.session_state.get("password_correct", True):
    display_content()
