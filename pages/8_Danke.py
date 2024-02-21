import streamlit as st

# embed streamlit docs in a streamlit app
st.set_page_config(layout="centered")
# Einbinden von benutzerdefinierten CSS-Stilen für die App
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.header("Abschließende Information für Teilnehmende")
st.markdown(""" 
            <iframe src="https://drive.google.com/file/d/15yijN2-iZ2TPGFdiCgNtKyTiqSVdAsa-/preview" style="width: 100%; height: 1000px; max-height: 94vh" allow="autoplay"></iframe>  
              
            Wenn Sie Fragen und Anregungen haben, oder einen Austausch zur Teilnahme an der Studie und der dargestellten Thematik wünschen, schreiben Sie mir gerne unter brodela@cardiff.ac.uk  
            Vielen Dank für Ihre Zeit und das Engagement, welches ich sehr zu schätzen weiß.  
            Arne Brödel
            """,unsafe_allow_html=True)

