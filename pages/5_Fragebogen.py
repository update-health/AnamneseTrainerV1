import streamlit as st
import scripts.random_ident_string as ris
import scripts.check_password as check_password
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="centered")
# Einbinden von benutzerdefinierten CSS-Stilen für die App
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Überprüfung, ob das Passwort korrekt ist; wenn nicht, wird zur Passworteingabe-Seite gewechselt
if 'password_correct' not in st.session_state or st.session_state["password_correct"] == False:
    check_password.check_password()
    st.stop()
        
if "random_id_string" not in st.session_state:
    st.session_state.random_id_string=ris.generate_random_string()

st.header("Fragebogen und Laut-Denken")
st.markdown("""
Bitte nehmen Sie sich die Zeit, alle Fragen so umfassend wie möglich zu beantworten. Wenn Sie bestimmte Fragen nicht beantworten können oder möchten, haben Sie die Möglichkeit, "möchte ich nicht angeben" auszuwählen oder die Frage zu überspringen.  
Bitte beachten Sie, dass Sie im Rahmen dieser Studie Sprachaufzeichnungen machen sollen, während Sie den Fragebogen ausfüllen. Testen Sie daher zunächst, ob Ihre gewählte Methode zur Sprachaufzeichnung funktioniert und ob der Ton in der Aufnahme gut hörbar ist. Stellen Sie sicher, dass die Aufnahme läuft, bevor Sie mit dem Ausfüllen des Fragebogens beginnen. Überprüfen Sie zwischendurch, ob die Aufnahme noch läuft und nicht unterbrochen wurde.  
Falls Sie während des Ausfüllens des Fragebogens feststellen, dass Sie zeitweise nicht aufgenommen haben oder vergessen haben zu sprechen, ist das kein Problem. Setzen Sie dann die Aufnahme fort und gehen Sie kurz auf die vorherigen Fragen ein. Sollte keine vollständige Aufnahme gelingen, ist auch das Ausfüllen des Fragebogens ohne Sprachaufnahme für die Studie wertvoll.""")

st.write("Dies ist Ihre persönliche Ziffernfolge um den Fragebogen mit den später hochzuladenden Dateien zu verknüpfen:")
st.write("### "+st.session_state.random_id_string[0]+" - "+st.session_state.random_id_string[1])
st.write("Der Code wird neu generiert wenn diese Seite geschlossen und neu geladen wird. Es ist aber wichtig, dass Sie beim Upload der Dateien den gleichen Code nutzen wie im Fragebogen.")

st.markdown("""
Sollte das Formular hier nicht richtig angezeigt werden, können Sie es über folgenden Link in einem neuen Tab öffnen:  
<a href="https://forms.office.com/e/rCDsFBkN8N" target="_blank">Fragebogen in neuem Tab öffnen</a>
<iframe height="1200px" src="https://forms.office.com/Pages/ResponsePage.aspx?id=MEu3vWiVVki9vwZ1l3j8vIm_B-OUVLdPhs3ozbSACf9UN0E4TDVNSFRGNEtZSlpPSzg4UUNYU1ZVNi4u&embed=true" frameborder="0" marginwidth="0" marginheight="0" style="border: none; width:100%; max-height:94vh" allowfullscreen webkitallowfullscreen mozallowfullscreen msallowfullscreen> </iframe>
        """,unsafe_allow_html=True)
st.markdown("""Vielen Dank für Ihre Teilnahme.  
            Fehlt nur noch der letzte Schritt: Laden Sie auf der folgenden Seite alle Audio- bzw. Bildschirmaufzeichnungen und weitere Dateien wie Gesprächsprotokolle zur Auswertung hoch.
            """)
if st.button("Dateiupload"):
        switch_page("Dateiupload")