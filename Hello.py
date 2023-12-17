import streamlit as st
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page


LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="PatientGPT",
        page_icon="👩‍⚕️",
    )

    st.write("# Herzlich Willkommen zum Anamnesetrainer")


    st.markdown("### Um zu starten, wechsel jetzt auf die Seite")

    if st.button("PatientGPT"):
        switch_page("PatientGPT")


if __name__ == "__main__":
    run()
