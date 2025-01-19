# Laertius-TTS - a one-liner text-to-speech v0.02

import os
from gtts import gTTS
import fitz  # PyMuPDF for PDF text extraction

# Input and output directories
INPUT_DIR = "./input_pdfs"
OUTPUT_DIR = "./output_audios"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

def convert_text_to_audio(text, output_path):
    """Converts text to audio using gTTS and saves it."""
    try:
        tts = gTTS(text=text, lang='pt-br')
        tts.save(output_path)
        print(f"Audio saved: {output_path}")
    except Exception as e:
        print(f"Error converting text to audio: {e}")

def process_pdfs(input_dir, output_dir):
    """Processes all PDFs in the input directory and saves audio in the output directory."""
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            audio_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".mp3")

            print(f"Processing: {filename}")
            text = extract_text_from_pdf(pdf_path)
            
            if text.strip():  # Ensure there is text to process
                convert_text_to_audio(text, audio_path)
            else:
                print(f"No text found in {filename}. Skipping.")

# Run the process
if __name__ == "__main__":
    process_pdfs(INPUT_DIR, OUTPUT_DIR)
