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

```bash
git clone https://github.com/Danzer-bit/RimuoviSfondoApp.git
cd rimozione-sfondo
 ```

### 2. Installa le dipendenze

Ti consigliamo di usare un ambiente virtuale:
```bash
python -m venv venv
source venv/bin/activate  # su Linux/Mac
venv\Scripts\activate     # su Windows

pip install -r requirements.txt
 ```

### 3. Avvia l'app
```bash
python app.py
```
Apri il browser su http://localhost:7860

## 🚀 Host su Hugging Face Spaces

1. Crea uno Space su Hugging Face Spaces (https://huggingface.co/spaces)
2. Scegli il tipo Gradio
3. Carica tutti i file della repo (inclusi app.py, gallery/, outputs/, ecc.)


5. Lo Space si avvierà automaticamente (ci vorrà qualche minuto)

## 📁 Struttura della cartella

```text
├── gallery/             # immagini mostrate nella galleria, modificabili a piacere
├── outputs/             # immagini elaborate generate
├── .gitattributes       # configurazione EOL e linguist (opzionale)
├── app.py               # codice principale dell'app
├── requirements.txt     # dipendenze Python
└── README.md            # questo file, da sostituire con file per Hugging Face
```

Non hai bisogno della cartella img di questa repo, usata solo per la preview di questa guida

## 🧑‍💻 Crediti

Fox photo by <a href="https://unsplash.com/@rayhennessy?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Ray Hennessy</a> on <a href="https://unsplash.com/photos/brown-fox-on-snow-field-xUUZcpQlqpM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      

Yellow Bird photo by <a href="https://unsplash.com/@hynesight?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Jeremy Hynes</a> on <a href="https://unsplash.com/photos/a-yellow-bird-sitting-on-a-branch-of-a-tree-3Okh7LBdgvc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      

Gold Statue photo by <a href="https://unsplash.com/@etiennegirardet?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Etienne Girardet</a> on <a href="https://unsplash.com/photos/gold-statue-under-gray-sky-Nqi444i_6Z0?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      

Statue of Liberty photo by <a href="https://unsplash.com/@gautamkrishnan?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Gautam Krishnan</a> on <a href="https://unsplash.com/photos/low-angle-photography-of-statue-of-liberty-piTwIwK7O98?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      

Fox Puppy photo by <a href="https://unsplash.com/@sunyu?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Sunguk Kim</a> on <a href="https://unsplash.com/photos/selective-focus-photography-of-orange-fox-tIfrzHxhPYQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>


## 📄 Licenza

Distribuito sotto licenza MIT. Vedi LICENSE per maggiori dettagli.
