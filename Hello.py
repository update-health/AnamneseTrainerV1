import streamlit as st
import hmac
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page


LOGGER = get_logger(__name__)

def display_homepage():
    """Display the content of the homepage."""
    st.markdown("### Um zu starten, wechsel jetzt auf die Seite")
    if st.button("PatientGPT"):
        switch_page("PatientGPT")


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
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        if "password_correct" in st.session_state:
            st.error("😕 Password incorrect")
        return False
    return True

def run():
    st.set_page_config(page_title="PatientGPT", page_icon="👩‍⚕️")
    st.write("# Herzlich Willkommen zum Anamnesetrainer")

    # Check password before showing pages or homepage content
    if check_password():
        display_homepage()


if __name__ == "__main__":
    run()
