import streamlit as st
import hmac

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

