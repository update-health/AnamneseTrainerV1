import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64

# embed streamlit docs in a streamlit app
st.set_page_config(layout="centered")
# Einbinden von benutzerdefinierten CSS-Stilen für die App
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.header("Teilnehmenden-Information und Einverständnis")
st.markdown("""Auf dieser Seite finden Sie umfassende Informationen über die Studie, die Voraussetzungen zur Teilnahme, Ihre Rechte und Pflichten als Teilnehmende*r, Rechte und Pflichten von mir als verantwortlichem Forschenden und der Hochschule.  
            Bitte lesen Sie die Informationen bis Ihnen alle Aspekte ausreichend klar geworden sind um an der Studie teilzunehmen.  
            Insofern Sie sich weiterhin für die Teilnahme entscheiden, müssen Sie das Einverständnisformular unten auf dieser Seite ausfüllen. Sie erhalten dann erneut eine E-Mail in der Sie Ihre Identität bestätigen müssen.  
            Dann ist Ihre Einverständniserkärung vollständig und Sie bekommen das Passwort für den Anamnesetrainer.  
            Sollte das Formular hier nicht richtig angezeigt werden, können Sie es über folgenden Link in einem neuen Tab öffnen:  
            <a href="https://drive.google.com/file/d/1TzYIduwwkN61J8eE_Qm2XFp2VtUdymhp/view">Link zu den Teilnehmenden Informationen</a>
            <iframe src="https://drive.google.com/file/d/1TzYIduwwkN61J8eE_Qm2XFp2VtUdymhp/preview" style="width: 100%; height: 1000px; max-height: 94vh" allow="autoplay"></iframe>
            <iframe style="width: 100%; height: 1000px; max-height: 94vh" src="https://forms.office.com/Pages/ResponsePage.aspx?id=MEu3vWiVVki9vwZ1l3j8vIm_B-OUVLdPhs3ozbSACf9UNTU4WU5IOFhQMzVXSlI1VlkxQlhMWlBRQS4u&embed=true" frameborder="0" marginwidth="0" marginheight="0" style="border: none; max-width:100%; max-height:100vh" allowfullscreen webkitallowfullscreen mozallowfullscreen msallowfullscreen> </iframe>
            """, unsafe_allow_html=True)
st.markdown("Wenn das Dokument ausgefüllt und signiert ist, und auch die Unterschrift per E-Mail bestätigt wurde, wechseln Sie zur Anleitung.")
if st.button("Anleitung", use_container_width=True):
    switch_page("Anleitung")
