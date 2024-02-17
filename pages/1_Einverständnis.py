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
            """, unsafe_allow_html=True)
st.markdown("Wenn das Dokument ausgefüllt und signiert ist, und auch die Unterschrift per E-Mail bestätigt wurde, wechseln Sie zur Anleitung.")
if st.button("Anleitung", use_container_width=True):
    switch_page("Anleitung")
#pdf_viewer("docs/Pilot_Studie_Dokumente_Read_Aloud.pdf")
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" type="application/pdf" width="100%" frameborder="0" style="border: 0; overflow: hidden; height: 1400px; max-height: 94vh; min-height: 500px; min-width: 600px;"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
displayPDF("docs/Pilot_Studie_Dokumente_Read_Aloud.pdf")