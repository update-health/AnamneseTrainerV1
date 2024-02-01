import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
st.set_page_config(layout="wide")
st.markdown("""Sollte das Formular hier nicht richtig angezeigt werden, kannst Du es über folgenden Link in einem neuen Tab öffnen:  
### <a href="https://forms.office.com/e/nU5ruAxtxM" target="_blank">Fragebogen</a>
            """,unsafe_allow_html=True)
components.iframe("https://forms.office.com/Pages/ResponsePage.aspx?id=MEu3vWiVVki9vwZ1l3j8vIm_B-OUVLdPhs3ozbSACf9UNEpDNUxBQU9OUjBIUU1aSUZCR1FDU0dVQi4u&embed=true",None,800,True)
