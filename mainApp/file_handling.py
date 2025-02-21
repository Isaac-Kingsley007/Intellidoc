import os
import fitz  # PyMuPDF for PDF extraction
from app import app

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text(filepath):
    """Extracts text from PDF or Word document."""
    ext = filepath.rsplit(".", 1)[1].lower()

    if ext == "pdf":
        with fitz.open(filepath) as doc:
            text = "\n".join([page.get_text() for page in doc])
    # elif ext in ["doc", "docx"]:
    #     doc = docx.Document(filepath)
    #     text = "\n".join([para.text for para in doc.paragraphs])
    else:
        text = ""

    return text


if __name__ == '__main__':
    print(extract_text("uploads/Assignment - II Isaac Kingsley D.pdf"))
