import streamlit as st
import scripts.check_password as check_password
from streamlit_extras.switch_page_button import switch_page

# embed streamlit docs in a streamlit app
st.set_page_config(layout="centered")
# Einbinden von benutzerdefinierten CSS-Stilen für die App
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Überprüfung, ob das Passwort korrekt ist; wenn nicht, wird zur Passworteingabe-Seite gewechselt
if 'password_correct' not in st.session_state or st.session_state["password_correct"] == False:
    check_password.check_password()
    st.stop()


if "random_id_string" not in st.session_state:
    random_id_string=["1ab","xy2",True]
else:
     random_id_string=st.session_state.random_id_string 

st.header("Dateiupload")
st.write("Auf dieser Seite sollen Sie alle Aufnahmen und Gesprächsprotokolle von Ihnen hochladen.")
st.markdown("""Über den folgenden Link gelangen Sie zu einer Seite, auf der Sie Bildschirm- und Sprachaufzeichnungen sowie gespeicherte Gesprächsprotokolle in meinen Cloudspeicher bei der Cardiff University hochladen können.  
            Dieser Service wird von Microsoft bereitgestellt. Falls Sie in Ihrem Browser mit einem Microsoft-Konto angemeldet sind, werden automatisch Ihr Vorname und Nachname übernommen.  
            Um Ihre Anonymität zu wahren, bitte ich Sie, den Link in einem neuen privaten Browserfenster zu öffnen. Je nach Browser können diese Modi als “Privat”, “In-private” oder “Inkognito” bezeichnet sein.""")    
st.image("assets/InkognitoFenster.jpg")
st.write('oder klicken auf den unten stehenden Link mit der rechten Maustaste und wählen dann dort "InPrivate-Fenster" öffnen, wie in diesem Bild zu sehen:')
st.image("assets/InkognitoFensterRechtsklick.jpg")
st.markdown("""##### :red[Statt Ihrem Vornamen und Nachnamen, sollen Sie die beiden Hälften Ihres Zifferncodes eingeben.]  
            """)

if random_id_string[2]==False:
      st.markdown(f"""***Nutzen Sie unbedingt den gleichen Zifferncode, den Sie auch in den Fragebogen eingetragen haben. Dieser wird immer neu erstellt, sobald die Seite verlassen wurde.***  
                  Insofern Sie direkt nach dem Ausfüllen des Fragebogens zu dieser Seite gewechselt sind, ist Ihr Zifferncode:  
                  {random_id_string[0]} - {random_id_string[1]}.  
                  Nutzen Sie dann einfach:  First name: :red[{random_id_string[0]}] Last name: :red[{random_id_string[1]}]""",unsafe_allow_html=True)
      st.write("#### ")


if random_id_string[2]==True:
      st.markdown(f"""***Nutzen Sie den unbedingt den gleichen Zifferncode, den Sie auch in den Fragebogen eingetragen haben. Dieser wird immer neu erstellt, sobald die Seite verlassen wurde.  
                  Der folgende Code ist daher nur beispielhaft.***  
                  **Wäre Ihr Code {random_id_string[0]}-{random_id_string[1]}, dann wäre Ihre Eingabe:  First name: _{random_id_string[0]}_ und Last name: _{random_id_string[1]}_**""")
st.markdown("""### <a href="https://cf-my.sharepoint.com/:f:/g/personal/brodela_cardiff_ac_uk/EtexNRViovRPtM1d8eXJHp8BGAnWNJfnHF_idSz1xjqDyA" target="_blank">Webseite zum Hochladen der Audiodateien</a>  
                        """,unsafe_allow_html=True)
st.markdown("""Sollte es irgendwelche Probleme beim Hochladen der Dateien geben, melden Sie sich bitte umgehend bei mir.  
            Wenn Sie den Upload abgeschlossen haben, sind alle Schritte Ihrer Teilnahme an der Studie abgeschlossen.  
            Herzlichen Dank.  
            Wenn Sie Erfahren wollen wie es weiter geht und wie Sie Einblick in die Ergebnisse erhalten können, lesen Sie auf der nächsten Seite weiter.
            """)
if st.button("Danke"):
        switch_page("Danke")