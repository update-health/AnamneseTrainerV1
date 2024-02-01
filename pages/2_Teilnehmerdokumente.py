import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_extras.switch_page_button import switch_page

# embed streamlit docs in a streamlit app
st.set_page_config(layout="wide")
st.markdown("""Unten auf der Seite findest Du Dokumente, welche die späteren Teilnehmenden der Studie lesen und unterzeichnen müssen.  
Die weitere Einverständniserklärung am Ende musst Du nicht unterzeichnen, aber bitte durchlesen und auf Verständlichkeit prüfen.  
Ich erinnere an die bereits zuvor dargestellten Methoden "read-aloud" und "think-aloud".  
Nahezu jedes Smartphone, jedes Tablet oder Laptop hat ein Mikrofon und einen Sprachrekorder.  
Diese heißen oft auf „Sprachrekorder“, „Diktiergerät“ oder ähnlich.  
Aufgezeichnet werden sollen:  
- Das Lesen der folgenden Dokumente:
    - Einladungsbrief für potenzielle Teilnehmende
    - Informationsblatt für Teilnehmende
    - Einverständniserklärung
- Das Ausfüllen des Fragebogens (später nach Verwendung des Chatbots)  
Das kann auch in mehreren Abschnitten erfolgen. Das größte Augenmerk ist dabei auf den Fragebogen zu richten. Dieser ist allerdings erst nach der Interaktion mit dem KI-Chatbot auszufüllen.  
Anschließend lade die Audiodatei(en) bitte in folgenden Cloudordner:  
### <a href="https://cf-my.sharepoint.com/:f:/g/personal/brodela_cardiff_ac_uk/EtexNRViovRPtM1d8eXJHp8BGAnWNJfnHF_idSz1xjqDyA" target="_blank">Audio recording Pilot</a>
Du kannst die Anzeige der Dokumente unten hereinzoomen. Falls diese dennoch nicht gut angezeigt werden folge diesem  
### <a href="https://cf-my.sharepoint.com/:b:/g/personal/brodela_cardiff_ac_uk/EbNNZBO6k91FidHrGyrC5jsBtgZcpMtMaJHcMYkBUIRM7g" target="_blank">Link zu den Teilnehmerdokumenten</a>
            """, unsafe_allow_html=True)
# def get_pdf_base64(file_path):
#     with open(file_path, "rb") as f:
#         pdf_file = f.read()
#     pdf_base64 = base64.b64encode(pdf_file).decode('utf-8')
#     return pdf_base64

# def display_pdf(file_path):
#     pdf_base64 = get_pdf_base64(file_path)
    
#     # Create the HTML to embed the PDF
#     pdf_display = f'''
#     <iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000" type="application/pdf">
#     '''
    
#     st.markdown(pdf_display, unsafe_allow_html=True)

# # Path to your local PDF file
# pdf_file_path = "docs/Pilot_Studie_Dokumente_Read_Aloud.pdf"

# display_pdf(pdf_file_path)
#components.iframe("https://cf-my.sharepoint.com/personal/brodela_cardiff_ac_uk/_layouts/15/embed.aspx?id=%2Fpersonal%2Fbrodela%5Fcardiff%5Fac%5Fuk%2FDocuments%2FMedical%20Education%2FYear3%20Dissertation%2FChatBot%2FPilotstudie%2FPilot%20Studie%20Dokumente%20Read%20Aloud%2Epdf&parent=%2Fpersonal%2Fbrodela%5Fcardiff%5Fac%5Fuk%2FDocuments%2FMedical%20Education%2FYear3%20Dissertation%2FChatBot%2FPilotstudie&ga=1")
st.markdown("""
            <iframe src="https://cf-my.sharepoint.com/personal/brodela_cardiff_ac_uk/_layouts/15/embed.aspx?id=%2Fpersonal%2Fbrodela%5Fcardiff%5Fac%5Fuk%2FDocuments%2FMedical%20Education%2FYear3%20Dissertation%2FChatBot%2FPilotstudie%2FPilot%20Studie%20Dokumente%20Read%20Aloud%2Epdf&parent=%2Fpersonal%2Fbrodela%5Fcardiff%5Fac%5Fuk%2FDocuments%2FMedical%20Education%2FYear3%20Dissertation%2FChatBot%2FPilotstudie&ga=1" width="100%" height="800"/>
            Wenn das erledigt ist kommt der nächste Schritt, die Arbeit mit dem KI-Chatbot. Gehe dabei vor wie im vorherigen Dokument unter "4. Was beinhaltet die Teilnahme am Projekt?" beschrieben.
Die detaillierte Anleitung findest Du über folgenden Button""",True)
if st.button("Anleitung"):
    switch_page("Anleitung")
st.markdown("""Dort geht es dann auch zum KI-Chatbot.   
            """)
st.markdown("""Das Passwort hast Du nach dem Ausfüllen der Einverständniserklärung per Email an die dort angegebene Adresse erhalten.  
            Ansonsten frag bei Arne über brodela@cardiff.ac.uk nach""")

