import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page

# embed streamlit docs in a streamlit app
st.set_page_config(layout="wide")
st.markdown("""Wenn Sie mindestens zwei Durchgänge mit dem Anamnesetrainer absolivert haben, füllen Sie bitte nun den Fragebogen aus.  
            Sollte das Formular hier nicht richtig angezeigt werden, können Sie es über folgenden Link in einem neuen Tab öffnen:  
### <a href="https://forms.office.com/e/nU5ruAxtxM" target="_blank">Fragebogen</a>
            """,unsafe_allow_html=True)
components.iframe("https://forms.office.com/Pages/ResponsePage.aspx?id=MEu3vWiVVki9vwZ1l3j8vIm_B-OUVLdPhs3ozbSACf9UNEpDNUxBQU9OUjBIUU1aSUZCR1FDU0dVQi4u&embed=true",None,800,True)
st.markdown("""Vielen Dank für Ihre Teilnahme.  
            Nach dem Ausfüllen des Fragebogens kommt als nächstes die "Think-aloud" Methode zum Einsatz um umfassende und tiefergehende Einschätzungen von Ihnen zu gewinnen.  
            Sie benötigen für den nächsten Schritt einen Sprachrekorder, dessen Aufnahmen Sie anschließend in einen zur Verfügung gestellten Cloud-Ordner hochladen.  
            Eine detailierte Anleitung finden Sie auf der nächsten Seite.
            """)
if st.button("Think-aloud"):
        switch_page("Think-aloud")