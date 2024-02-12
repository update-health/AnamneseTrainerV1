import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page

# embed streamlit docs in a streamlit app
st.set_page_config(layout="wide")
st.markdown("""Auf dieser Seite finden Sie umfassende Informationen über die Studie, die Voraussetzungen zur Teilnahme, Ihre Rechte und Pflichten als Teilnehmende*r, Rechte und Pflichten von mir als verantwortlichem Forschenden und der Hochschule.  
            Bitte lesen Sie die Informationen bis Ihnen alle Aspekte ausreichend klar geworden sind um an der Studie teilzunehmen.  
            Insofern Sie sich weiterhin für die Teilnahme entscheiden, müssen Sie das Einverständnisformular ausfüllrn und digital unterschreiben.  
            Nach dem Signieren müssen Sie Ihre E-Mail-Adresse angeben. Sie erhalten dann eine E-Mail in der Sie einen Link zur Bestätigung klicken müssen. Erst dann ist die Einverständniserklärung vollständig.  
            Sollte das Formular hier nicht richtig angezeigt werden, können Sie es über folgenden Link in einem neuen Tab öffnen:  
### <a href="https://na1.documents.adobe.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhCiEMN_Q4dJxTHT6usSMWYoT649Heg4qy33KAm_h_p7TgA7Ks3GCHjmhdfTiy7TSfY*" target="_blank">Einverständnisformular</a>
            """, unsafe_allow_html=True)
components.iframe("https://na1.documents.adobe.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhDW3E9SeyheYNuY6fKETpYtG2LRIgyEN0KyO8hhL8-BZafEpMUHjdIkrpcvoIlZKYQ*&hosted=false",None,800,True)
st.markdown("Wenn das Dokument ausgefüllt und signiert ist, und auch die Unterschrift per E-Mail bestätigt wurde, wechseln Sie zur Anleitung.")
if st.button("Anleitung"):
    switch_page("Anleitung")
