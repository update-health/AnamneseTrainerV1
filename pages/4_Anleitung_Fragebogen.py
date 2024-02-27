import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="centered")
# Einbinden von benutzerdefinierten CSS-Stilen für die App
with open("styles/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.header("Fragebogen und Laut-Denken")

st.markdown("""

Wenn Sie mindestens zwei Durchgänge mit dem Anamnesetrainer absolviert haben, kommt nun der nächste entscheidende Schritt im Rahmen dieser Studie: Die Datensammlung über Ihre gesammelten Erfahrungen und Eindrücke mit dem KI-Anamnesetrainer.  
Dazu kommen zwei Verfahren parallel zum Einsatz.  
Das erste Verfahren der Datensammlung ist das Ausfüllen eines Fragebogens.  
Bei den meisten Fragen muss eine Antwortoption oder ein Grad der Zustimmung auf einer Skala gewählt werden.  
Hinzu kommen einige Fragen, die mit kurzen freiformulierten Sätzen oder Stichwörtern zu beantworten sind.  
 
Das zweite Verfahren der Datensammlung, ist die sogenannte "Think-Aloud", oder auf Deutsch "Laut-Denken" Methode.  
Dabei sollen Sie versuchen alle Gedanken laut auszusprechen und diese dabei über ein Mikrofon aufzuzeichnen.  
Zum Einsatz kommt die Methode parallel zum Ausfüllen des Fragebogens. Es geht dabei darum, umfassend Ihre Interpretation der Fragen und Antwortoptionen, sowie Ihre Abwägungen und Gründe zu erfassen, welche zu Ihren Antworten führen.  
Sprechen und Schreiben gleichzeitig ist jedoch nicht ganz einfach. Sie sollten daher bei jeder Frage zunächst Ihre Gedanken äußern und dann anschließend Ihre Wahl treffen bzw. kurze Stichworte dazu aufschreiben.  Anschließend können Sie ergänzende Gedanken aussprechen.  
***Also bei jeder Frage "Laut-Denken" -> dann Schreiben -> dann evtl. nochmal "Laut-Denken".***  
Ich erhoffe mir wertvolle zusätzliche Informationen durch die Tonaufnahme. Sollte dies jedoch für Sie nicht möglich sein, oder Sie sich mit der Think-Aloud-Methode unwohl fühlen, ist es in Ordnung auch nur den Fragebogen schriftlich auszufüllen.  
Um die Aufnahme durchzuführen gibt es verschiedene Optionen, die ich hier kurz darstellen möchte und vom verwendeten Geräte abhängen.  
Wenn die Möglichkeit besteht, dann nutzen Sie bitte einen PC oder Laptop mit den Browsern Chrome, Edge oder Firefox.  
                    
<iframe width="820" height="460" style="max-width: 100%" src="https://www.youtube.com/embed/1U6t-lPX6eY?si=5yG3smk2cSj4FXCr&amp;" title="Video Teilnahmeanleitung Teil2" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>  
        """, unsafe_allow_html=True)
st.markdown(
        """
<style>
[data-testid="stExpander"] summary p{
font-weight: bold;
font-size: 1.6rem !important;
}
[data-testid="stExpander"] .st-emotion-cache-1dtefog{
flex-grow: 1;
}
[data-testid="stExpander"] .st-emotion-cache-1pbsqtx{
height: 2.6rem;
width: 2.6rem;


}
</style>
""", unsafe_allow_html=True)
with st.expander("PC oder Laptop"):
        st.markdown("""Nutzen Sie bevorzugt die Browser Chrome, Edge oder Firefox.  
                Diese erlauben die Verwendung des integrierten Screenrecorders. Diesen können Sie oben rechts im 3Punkte Menü starten und stoppen.  
                Die Verwendung wurde bereits im oberen Virdeo gezeigt. Wenn Sie es nochmal dargestellt sehen wollen ist die exakte Verwendung in diesem Video dargestellt:  
        <iframe width="560" height="315" style="max-width: 100%" src="https://www.youtube-nocookie.com/embed/kqY-hptEYDo?si=R0rOLYrKVy2lybKq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                """,unsafe_allow_html=True)
with st.expander("iPad oder iPhone"):
        st.markdown("""Auch auf iOS Geräten gibt es eine vorinstallierte Screenrekorder-Funktion. Wichtig ist dabei darauf zu achten das die Tonaufnahme aktiviert ist. Sonst wird nur der Bildschirm aufgezeichnet.  
                Anleitung dazu im Video:  
                <iframe width="315" height="560" style="max-width: 100%" src="https://www.youtube-nocookie.com/embed/acKuOw84C98?si=Bo5V6xu-skeGKG3b" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                """,unsafe_allow_html=True)
with st.expander("Android"):
        st.markdown("""Androidgeräte sind sehr unterschiedlich, die meisten haben jedoch eine eingebaute Screenrekorder-Funktion. Wichtig ist dabei darauf zu achten das die Tonaufnahme aktiviert ist. Sonst wird nur der Bildschirm aufgezeichnet.  
                Anleitung dazu im Video:  
                <iframe width="315" height="560" style="max-width: 100%" src="https://www.youtube.com/embed/Gju89EXCb58" title="AnleitungScreenRecAndroidVertical" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                """,unsafe_allow_html=True)
with st.expander("Alternative: Nur Ton aufzeichnen"):
        st.markdown("""Bevorzugt wird die Aufzeichnung von Bildschirmaktivität und Ton gemeinsam, da diese die Auswertung erleichtert.  
        Sollte keine der oben genannten Varianten der Aufzeichnung möglich sein oder Sie nicht zu einer Aufzeichnung Ihres Bildschirmes bereit sein, können Sie alternativ auch nur Ton über eine entsprechende Anwendung aufnehmen. Eine App mit der Funktion der Sprachaufnahme ist auf nahezu jedem Gerät vorinstalliert. Diese haben meist Bezeichnungen wie "Diktiergerät" oder "Sprachrekorder".     
""")
st.markdown("""Um eine anonyme Datenübermittlung zu ermöglichen und dennoch die Aufnahmen der Laut-Denken-Methode mit dem Fragebogen eindeutig verknüpfen zu können, erhalten Sie auf der kommenden Seite einen Zifferncode.  
""")
if st.button("Fragebogen"):
        switch_page("Fragebogen")