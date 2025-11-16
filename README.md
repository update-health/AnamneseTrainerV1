# AI-Anamnese-Trainer

Dieses Projekt wurde im Rahmen einer Masterarbeit an der Cardiff University entwickelt.

**Titel der Abschlussarbeit:** AI Chatbots in Anamnesis Training: Exploratory Mixed-Methods Study Based on the AIDUA Model on Acceptance, User Experience, and Educational Potential among Physiotherapists in Germany  
**Autor:** Arne Brödel  
**Abschluss:** M.Sc. Medical Education 2024  
**Universität:** Cardiff University

---

## Abstract

> This dissertation explores the integration of generative Artificial Intelligence (AI) chatbots based on Large Language Models (LLMs) in anamnesis training for physiotherapists, aiming to evaluate their effectiveness and suitability as simulated patients. This study leverages advanced AI technologies to enhance realism, flexibility, and accessibility in learning experiences. The research, grounded in the Extended Artificial Intelligence Device Use Acceptance (AIDUA) Model, explores key factors influencing acceptance, including social influence, hedonic motivation, and perceived humanness among German physiotherapists.
> The AI-Anamnesis-Trainer application, developed specifically for this study using Python, Streamlit, and the OpenAI Chat-API, was designed to offer realistic patient scenarios and immediate feedback through a virtual tutor tailored to professional physiotherapists' specific learning needs. A mixed-methods approach with a convergent design was adopted, combining quantitative data with qualitative insights from structured questionnaires and think-aloud recordings.
> Initial findings indicate promising potential for using an AI chatbot to complement traditional anamnesis training methods. Participants noted various benefits and identified areas for improvement, providing valuable insights for educators, policymakers, and developers. The study concludes with recommendations for integrating AI chatbots into physiotherapy curricula and potential directions for future research, emphasising the need for ongoing development and evaluation of AI-driven educational tools.

---

## Über dieses Projekt

Der `AI-Anamnese-Trainer` ist eine Webanwendung, die mit Python und Streamlit erstellt wurde. Sie ermöglicht es Physiotherapiestudierenden und Fachkräften, ihre Fähigkeiten in der Anamneseerhebung zu trainieren, indem sie mit einem KI-gesteuerten simulierten Patienten interagieren. Nach einer Anamnese-Sitzung können die Nutzer Feedback von einem KI-Tutor erhalten, um ihre Gesprächsführung zu verbessern.

## Aktueller Status

**Wichtiger Hinweis:** Dieses Repository spiegelt den Stand des Projekts wider, wie er während der wissenschaftlichen Studie für die oben genannte Masterarbeit verwendet wurde. Es wurde seit Abschluss der Studie nicht mehr aktualisiert oder verändert.

## Erste Schritte

Um das Projekt lokal auszuführen, folgen Sie bitte den nachstehenden Anweisungen.

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python package installer)

### Installation

1.  **Klonen Sie das Repository:**

    ```bash
    git clone https://github.com/update-health/AnamneseTrainerV1.git
    cd AnamneseTrainerV1
    ```

2.  **Installieren Sie die Abhängigkeiten:**
    Es wird empfohlen, eine virtuelle Umgebung zu verwenden.
    ```bash
    python -m venv venv
    source venv/bin/activate  # Auf Windows: venv\Scripts\activate
    ```
    Installieren Sie die erforderlichen Pakete mit der `requirements.txt`-Datei:
    ```bash
    pip install -r requirements.txt
    ```

## Konfiguration: Secrets Management

Die Anwendung benötigt zwei "Secrets" (geheime Schlüssel), um ordnungsgemäß zu funktionieren: `PASSWORT` und `OPENAI_API_KEY`.

- `OPENAI_API_KEY`: Ihr API-Schlüssel für den Zugriff auf die OpenAI-API.
- `PASSWORT`: Ein einfaches Passwort, um den Zugriff auf die App zu beschränken.

### Lokale Entwicklung

Für die lokale Ausführung erstellen Sie eine Datei unter `.streamlit/secrets.toml` im Hauptverzeichnis Ihres Projekts. Fügen Sie Ihre Schlüssel wie folgt hinzu:

```toml
# .streamlit/secrets.toml

OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PASSWORT = "IhrGeheimesPasswort"
```

### Bereitstellung in der Streamlit Cloud

Wenn Sie die Anwendung in der Streamlit Cloud bereitstellen, fügen Sie die Secrets in den App-Einstellungen hinzu:

1.  Gehen Sie zu Ihrem Streamlit Cloud Dashboard und wählen Sie die App aus.
2.  Klicken Sie auf "Settings".
3.  Gehen Sie zum Abschnitt "Secrets".
4.  Fügen Sie die beiden Schlüssel (`OPENAI_API_KEY` und `PASSWORT`) und deren Werte hinzu.

### ⚠️ Sicherheitswarnung

**Veröffentlichen Sie Ihre Secrets niemals auf GitHub oder in einem anderen öffentlichen Repository!**

Die `.gitignore`-Datei in diesem Projekt ist bereits so konfiguriert, dass der Ordner `.streamlit/` und die `secrets.toml`-Datei ignoriert werden, um ein versehentliches Hochladen zu verhindern. Stellen Sie sicher, dass Ihre geheimen Schlüssel sicher und privat bleiben.

## Verwendung

Um die Anwendung lokal zu starten, führen Sie den folgenden Befehl im Hauptverzeichnis des Projekts aus:

```bash
streamlit run Willkommen.py
```

Die Anwendung wird in Ihrem Standard-Webbrowser geöffnet.

## Projektstruktur

```
AnamneseTrainerV1/
├── .streamlit/
│   └── secrets.toml      # (Lokal) Speichert geheime Schlüssel
├── assets/               # Bilder und andere statische Dateien
├── data/                 # YAML-Dateien mit Fallbeispielen, Instruktionen etc.
├── pages/                # Die einzelnen Seiten der Streamlit-Anwendung
├── scripts/              # Hilfsskripte (z.B. Passwort-Check)
├── styles/               # CSS-Dateien für das Styling
├── Willkommen.py         # Haupt-Startseite der Anwendung
├── requirements.txt      # Python-Abhängigkeiten
└── README.md             # Diese Datei
```
