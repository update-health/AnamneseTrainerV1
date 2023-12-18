import streamlit as st
import hmac
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page
from st_pages import show_pages, Page, hide_pages


LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="PatientGPT",
        page_icon="👩‍⚕️",
    )

if __name__ == "__main__":
    run()

st.write("# Herzlich Willkommen zum Anamnesetrainer")


#password Check
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["PASSWORD"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

show_pages(
    [
        Page("Hello.py", "Home", icon="🏠"),
        Page("pages/1_PatientGPT.py", "PatientGPT", icon="👩‍⚕️")
    ]
)
#actual page
st.markdown("### Um zu starten, wechsel jetzt auf die Seite")

if st.button("PatientGPT"):
    switch_page("PatientGPT")



