import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
st.set_page_config(layout="wide")
st.markdown("""Bitte die Informationen lesen und das Einverständnisformular ausfüllen.  
            Sollte das Formular hier nicht richtig angezeigt werden, kannst Du es über folgenden Link in einem neuen Tab öffnen:  
### <a href="https://na1.documents.adobe.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhCiEMN_Q4dJxTHT6usSMWYoT649Heg4qy33KAm_h_p7TgA7Ks3GCHjmhdfTiy7TSfY*" target="_blank">Einverständnisformular</a>
            """, unsafe_allow_html=True)
components.iframe("https://na1.documents.adobe.com/public/esignWidget?wid=CBFCIBAA3AAABLblqZhCiEMN_Q4dJxTHT6usSMWYoT649Heg4qy33KAm_h_p7TgA7Ks3GCHjmhdfTiy7TSfY*&hosted=false",None,800,True)
