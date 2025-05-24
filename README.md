# Remove Background App

![Anteprima dell'app](./img/appview.png)

Un'applicazione interattiva realizzata con Gradio per rimuovere lo sfondo dalle immagini, pronta per essere hostata su Hugging Face.

## 🌐 Demo online

Prova il progetto online su Hugging Face:

🔗 Rimozione Sfondo – Hugging Face Space: https://huggingface.co/spaces/Danzer93/RemoveBackground

## ✨ Funzionalità

- ✅ Carica un'immagine dal tuo dispositivo o scatta una foto con la webcam
- ✅ Seleziona un'immagine pre-caricata dalla galleria
- ✅ Visualizza l'immagine con lo sfondo rimosso
- ✅ Scarica l'immagine risultante in formato .png con sfondo trasparente
- ✅ CSS personalizzati e interfacce localizzate in italiano

## 🛠️ Tecnologie utilizzate

- Gradio — per creare l'interfaccia utente web
- Rembg — per rimuovere lo sfondo dalle immagini
- Pillow (PIL) — per la manipolazione delle immagini
- Python 3.10+

## 🧪 Esegui in locale

### 1. Clona la repository

git clone https://github.com/tuo-username/rimozione-sfondo.git
cd rimozione-sfondo

### 2. Installa le dipendenze

Ti consigliamo di usare un ambiente virtuale:

python -m venv venv
source venv/bin/activate  # su Linux/Mac
venv\Scripts\activate     # su Windows

pip install -r requirements.txt

Oppure installale manualmente:

pip install gradio rembg pillow

### 3. Avvia l'app

python app.py

Apri il browser su http://localhost:7860

## 🚀 Host su Hugging Face Spaces

1. Crea uno Space su Hugging Face Spaces (https://huggingface.co/spaces)
2. Scegli il tipo Gradio
3. Carica tutti i file della repo (inclusi app.py, gallery/, outputs/, ecc.)
4. Crea un file requirements.txt con:

gradio
rembg
pillow

5. Lo Space si avvierà automaticamente (ci vorrà qualche minuto)

## 📁 Struttura della cartella

├── app.py               # codice principale dell'app
├── gallery/             # immagini mostrate nella galleria
├── outputs/             # immagini elaborate generate
├── requirements.txt     # dipendenze Python
└── README.md            # questo file


## 📄 Licenza

Distribuito sotto licenza MIT. Vedi LICENSE per maggiori dettagli.
