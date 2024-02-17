import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_pdf_viewer import pdf_viewer
import base64

# embed streamlit docs in a streamlit app
st.set_page_config(layout="wide")
st.markdown("""Auf dieser Seite finden Sie umfassende Informationen über die Studie, die Voraussetzungen zur Teilnahme, Ihre Rechte und Pflichten als Teilnehmende*r, Rechte und Pflichten von mir als verantwortlichem Forschenden und der Hochschule.  
            Bitte lesen Sie die Informationen bis Ihnen alle Aspekte ausreichend klar geworden sind um an der Studie teilzunehmen.  
            Insofern Sie sich weiterhin für die Teilnahme entscheiden, müssen Sie das Einverständnisformular ausfüllrn und digital unterschreiben.  
            ***Nach dem Signieren müssen Sie Ihre E-Mail-Adresse angeben. Sie erhalten dann eine E-Mail in der Sie einen Link zur Bestätigung klicken müssen. Erst dann ist die Einverständniserklärung vollständig.***  
            Sollte das Formular hier nicht richtig angezeigt werden, können Sie es über folgenden Link in einem neuen Tab öffnen:  
            <iframe src="https://drive.google.com/file/d/0B8-azs9_jXsNbmFLQjJoZ0lwcW8/preview?resourcekey=0-z2c-id26IxhNKbr_SyLF3A" style="width: 100%; height: 1000px" allow="autoplay"></iframe>""", unsafe_allow_html=True)
st.markdown("Wenn das Dokument ausgefüllt und signiert ist, und auch die Unterschrift per E-Mail bestätigt wurde, wechseln Sie zur Anleitung.")
if st.button("Anleitung", use_container_width=True):
    switch_page("Anleitung")
st.markdown("""

            """, unsafe_allow_html=True)
