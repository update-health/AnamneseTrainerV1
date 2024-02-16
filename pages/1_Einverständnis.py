import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# embed streamlit docs in a streamlit app
st.set_page_config(layout="wide")
st.markdown("""Auf dieser Seite finden Sie umfassende Informationen über die Studie, die Voraussetzungen zur Teilnahme, Ihre Rechte und Pflichten als Teilnehmende*r, Rechte und Pflichten von mir als verantwortlichem Forschenden und der Hochschule.  
            Bitte lesen Sie die Informationen bis Ihnen alle Aspekte ausreichend klar geworden sind um an der Studie teilzunehmen.  
            Insofern Sie sich weiterhin für die Teilnahme entscheiden, müssen Sie das Einverständnisformular ausfüllrn und digital unterschreiben.  
            ***Nach dem Signieren müssen Sie Ihre E-Mail-Adresse angeben. Sie erhalten dann eine E-Mail in der Sie einen Link zur Bestätigung klicken müssen. Erst dann ist die Einverständniserklärung vollständig.***  
            Sollte das Formular hier nicht richtig angezeigt werden, können Sie es über folgenden Link in einem neuen Tab öffnen:  
### <a href="https://na1.documents.adobe.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhCiEMN_Q4dJxTHT6usSMWYoT649Heg4qy33KAm_h_p7TgA7Ks3GCHjmhdfTiy7TSfY*" target="_blank">Einverständnisformular</a>  
<iframe src="https://na1.documents.adobe.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhCAGq8oqJb6o6-j3DH4OU5DHjivejCGQnalw8fjfY335sKphPllxVwRNpl-AvoIdg4*&hosted=false" width="100%" frameborder="0" style="border: 0; overflow: hidden; height: 1400px; max-height: 94vh; min-height: 500px; min-width: 600px;"></iframe>
            """, unsafe_allow_html=True)
st.markdown("Wenn das Dokument ausgefüllt und signiert ist, und auch die Unterschrift per E-Mail bestätigt wurde, wechseln Sie zur Anleitung.")
if st.button("Anleitung"):
    switch_page("Anleitung")
