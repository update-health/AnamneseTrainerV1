import streamlit as st

def display_homepage():
    # Einbinden von benutzerdefinierten CSS-Stilen für die App
    with open("styles/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    #Display the content of the homepage.
    st.markdown("""
### Herzlich Willkommen zur Studie zum KI-basierten Anamnesetraining
Vielen Dank für Ihre Teilnahme.  
Auf diesen Seiten wird die Durchührung auch schriftlich genau beschrieben. Das folgende Video kann aber sehr hilfreich sein, um einen guten Überblick über alle Schritte der Teilnahme zu bekommen.  
<iframe width="820" height="460" style="max-width: 100%" src="https://www.youtube.com/embed/DiWaal9TymY?si=IsNPRJpuEQ6ByDZc&amp;" title="Video Teilnahmeanleitung Teil1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>  
  
Die Teilnahme besteht aus den folgenden Schritten:  
1. Auf der Seite "Einverständnis" das Einverständnis-Formular ausfüllen und absenden. Sie müssen dabei Ihre E-Mail-Adresse angeben und bestätigen. Danach erhalten Sie eine E-Mail von mir mit dem Zugangspasswort für den Anamnesetrainer.   
2. Auf der Seite "Anleitung" die detaillierte Anleitung zur Nutzung des Anamnesetrainers lesen.  
3. Auf der Seite "Anamnesetrainer" entsprechend der Anleitung Anamnesegespräch mit mindestens zwei KI-Patienten führen und die Anamnesegespräche mit dem KI-Tutor evaluieren. Die Gesprächsverläufe können Sie als PDF speichern.  
4. Auf der Seite "Anleitung Fragebogen" die genaue Durchführung der Datenerfassung mit Fragebogen und Sprachrekorder kennenlernen.  
5. Auf der Seite "Fragebogen" den Fragebogen ausfüllen und dabei die eigenen Gedanken aussprechen und eine oder mehrere Sprachaufnahmen anfertigen.  
6. Auf der Seite "Dateiupload" den Link öffnen um dort Ihre Sprachaufnahmen und von Ihnen gespeicherte Gesprächsverläufe mit dem KI-Anamnesetrainer auf einen sicheren Cloud-Speicher der Cardiff University hochladen. 

Die Teilnahme an der Studie sollte an nahezu jedem PC, Laptop, Tablet oder Smartphone möglich sein. Bevorzugt sollte jedoch ein Laptop oder PC mit den Browsern Chrome, Edge oder Firefox verwendet werden.  
                                        
### Wohin wende ich mich bei Fragen?

Wenn Sie Fragen zur Studie oder Unklarheiten bei der Verwendung des Anamnesetrainers haben, wenden Sie sich bitte per E-Mail an Arne Brödel unter arne@update.health .

    """, unsafe_allow_html=True)
    st.markdown('Wechseln Sie jetzt zur Seite "Einverständnis"')
    if st.button("Einverständnis"):
        st.switch_page("pages/1_Einverständnis.py")
    



def run():
    st.set_page_config(page_title="Anamnesetrainer", page_icon="👩‍⚕️",layout="centered")
    display_homepage()
    



if __name__ == "__main__":
    run()
