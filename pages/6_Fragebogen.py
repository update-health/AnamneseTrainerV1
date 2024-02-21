import streamlit as st
import scripts.random_ident_string as ris
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="centered")
# Überprüfung, ob das Passwort korrekt ist; wenn nicht, wird zur Passworteingabe-Seite gewechselt
if 'password_correct' not in st.session_state or st.session_state["password_correct"] == False:
        switch_page("Passwort")
        st.stop()
        
if "random_id_string" not in st.session_state:
    st.session_state.random_id_string=ris.generate_random_string()

st.header("Fragebogen und Laut-Denken")

st.write("Dies ist Ihre persönliche Ziffernfolge um den Fragebogen mit den später hochzuladenden Dateien zu verknüpfen:")
st.write("### "+st.session_state.random_id_string[0]+" - "+st.session_state.random_id_string[1])
st.write("Es kann sinnvoll sein sich diese Ziffernfolge aufzuschreiben, insbesondere dann, wenn Sie möglicherweise zwischen Fragebogen ausfüllen und dem Upload Ihrer Daten den Browser verlassen. Der Code würde beim erneuten Öffnen der Seite neu generiert. Es ist aber wichtig, dass Sie beim Upload der Dateien den gleichen Code nutzen wie im Fragebogen.")

st.markdown("""Wenn Sie mindestens zwei Durchgänge mit dem Anamnesetrainer absolivert haben, füllen Sie bitte nun den Fragebogen aus.  
        Sollte das Formular hier nicht richtig angezeigt werden, können Sie es über folgenden Link in einem neuen Tab öffnen:  
### <a href="https://forms.office.com/e/rCDsFBkN8N" target="_blank">Fragebogen</a>
<iframe height="1200px" src="https://forms.office.com/Pages/ResponsePage.aspx?id=MEu3vWiVVki9vwZ1l3j8vIm_B-OUVLdPhs3ozbSACf9UN0E4TDVNSFRGNEtZSlpPSzg4UUNYU1ZVNi4u&embed=true" frameborder="0" marginwidth="0" marginheight="0" style="border: none; width:100%; max-height:94vh" allowfullscreen webkitallowfullscreen mozallowfullscreen msallowfullscreen> </iframe>
        """,unsafe_allow_html=True)
st.markdown("""Vielen Dank für Ihre Teilnahme.  
            Fehlt nur noch der letzte Schritt: Laden Sie auf der folgenden Seite alle Audio- bzw. Bildschirmaufzeichnungen und weitere Dateien wie Gesprächsprotokolle zur Auswertung hoch.
            """)
if st.button("Dateiupload"):
        switch_page("Dateiupload")