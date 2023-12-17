import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="PatientGPT",
        page_icon="👩‍⚕️",
    )

    st.write("# Herzlich Willkommen zum Anamnesetrainer")


    st.markdown(
        """
        ### Um zu starten, wechsel jetzt auf die Seite [PatientGPT](/PatientGPT)
    """
    )


if __name__ == "__main__":
    run()
