import gradio as gr
from rembg import remove
from PIL import Image
import uuid
import os

# Cartella output
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Funzione per la rimozione dello sfondo
def remove_background(image: Image.Image):
    if image is None:
        return None, None
    output = remove(image)
    file_id = str(uuid.uuid4())
    output_path = os.path.join(OUTPUT_DIR, f"{file_id}.png")
    output.save(output_path)
    return output, output_path

# Carica le immagini dalla cartella gallery
GALLERY_DIR = "gallery"
gallery_files = sorted([
    os.path.join(GALLERY_DIR, f)
    for f in os.listdir(GALLERY_DIR)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
])

# Seleziona un'immagine dalla galleria
def load_gallery_image(evt: gr.SelectData):
    if evt.index < len(gallery_files):
        image_path = gallery_files[evt.index]
        return Image.open(image_path)
    return None

# Interfaccia di gradio con i css per il bottone
with gr.Blocks(title="Rimozione Sfondo") as demo:
    demo.css = """
    #orange-button {
        background-color: orange !important;
        color: white !important;
    }
    """

    gr.Markdown("# Rimuovi lo sfondo dalla tua immagine")
    gr.Markdown("Carica un'immagine personale, cattura un'immagine dalla tua webcam o scegline una dalla galleria.")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="Carica un'immagine", type="pil", sources=["upload", "webcam"])
            btn = gr.Button("Rimuovi lo Sfondo", elem_id="orange-button")
        
        gallery = gr.Gallery(label="Galleria immagini", value=gallery_files, columns=5, rows=1, height="auto")

    output_image = gr.Image(type="pil", label="Risultato")
    output_file = gr.File(label="Scarica il file")

    gallery.select(fn=load_gallery_image, outputs=image_input)
    btn.click(fn=remove_background, inputs=image_input, outputs=[output_image, output_file])

if __name__ == "__main__":
    demo.launch()