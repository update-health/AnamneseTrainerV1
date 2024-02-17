import streamlit as st
import scripts.random_ident_string as ris
from streamlit_extras.switch_page_button import switch_page

# embed streamlit docs in a streamlit app
st.set_page_config(layout="centered")

# Überprüfung, ob das Passwort korrekt ist; wenn nicht, wird zur Passworteingabe-Seite gewechselt
if 'password_correct' not in st.session_state or st.session_state["password_correct"] == False:
        switch_page("Passwort")
        st.stop()


if "random_id_string" not in st.session_state:
    random_id_string=["12AB","34xy",True]
else:
     random_id_string=st.session_state.random_id_string 

st.header("Dateiupload")
st.write("Auf dieser Seite sollen Sie alle Aufnahmen und Gesprächsprotokolle von Ihnen hochladen.")
st.markdown("""Über den folgenden Link gelangen Sie zu einer Seite über die Sie die Bildschirm- bzw. Sprachaufzeichnungen, aber auch z.B. gespeicherte Gesprächsprotokolle, auf meinen Cloudspeicher bei der Cardiff University hochladen können.  
            Es handelt sich um einen Microsoft Dienst. Falls Sie in Ihrem Browser mit einem Microsoft Konto angemeldet sind, wird daraus Ihr Vorname und Nachname einfach übernommen.  
            Um dies zu verhindern, kopieren Sie den Link einfach in ein neues privates Browser Fenster. Je nach Browser heißen diese "Privat", "In-private", "Inkognito" oder ähnlich.""")    
st.image("assets/InkognitoFenster.jpg")
st.write('oder klicken auf den unten stehenden Link mit der rechten Maustaste und wählen dann dort "InPrivate-Fenster" öffnen, wie in diesem Bild zu sehen:')
st.image("assets/InkognitoFensterRechtsklick.jpg")
if random_id_string[2]==False:
      st.write("Zur Erinnerung: Dies ist Ihr Zifferncode um den ausgefüllten Fragenbogen den hochgeladenen Dateien zuordnen zu können:")
      st.write("#### "+random_id_string[0]+" - "+random_id_string[1])

st.markdown("""Das Uploadformular sieht vor, dass die Nutzer*innen einen Vornamen und Nachnamen eingeben. Dieser wird dann den Dateinamen angehangen.  
            Sie sollen nicht Ihren tatsächlichen Vornamen und Nachnamen eingeben, sondern stattdessen die beiden Hälften Ihres Zifferncodes eingeben.  
            """)
if random_id_string[2]==True:
      st.markdown(f"""***Nutzen Sie den unbedingt den gleichen Zifferncode, den Sie auch in den Fragebogen eingetragen haben. Dieser wird immer neu erstellt sobald die Seite verlassen wurde.  
                  Der folgende Code ist daher nur beispielhaft.***  
                  ***Wäre Ihr Code also {random_id_string[0]} - {random_id_string[1]},***""")
st.write("***"+"Dann nutzen Sie einfach:  First name: :red["+random_id_string[0]+"] Last name: :red["+random_id_string[1]+"]***")
st.markdown("""### <a href="https://cf-my.sharepoint.com/:f:/g/personal/brodela_cardiff_ac_uk/EtexNRViovRPtM1d8eXJHp8BGAnWNJfnHF_idSz1xjqDyA" target="_blank">Webseite zum Hochladen der Audiodateien</a>  
                        """,unsafe_allow_html=True)
st.markdown("""Sollte es irgendwelche Probleme beim Hochladen der Dateien geben, melden Sie sich bitte umgehend bei mir.  
            Wenn Sie den Upload abgeschlossen haben, sind alle Schritte Ihrer Teilnahme an der Studie abgeschlossen.  
            Herzlichen Dank.  
            Wenn Sie Erfahren wollen wie es weiter geht und wie Sie Einblick in die Ergebnisse erhalten können, lesen Sie auf der nächsten Seite weiter.
            """)
if st.button("Danke"):
        switch_page("Danke")