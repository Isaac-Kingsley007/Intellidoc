import pypandoc
from PyPDF2 import PdfReader, PdfWriter
from docx import Document

ALLOWED_EXTENSIONS = {
    'pdf': 'PDF Document',
    'docx': 'Word Document',
    'doc': 'Word Document (Legacy)',
    'txt': 'Text File',
    'md': 'Markdown',
    'rtf': 'Rich Text Format',
    'odt': 'OpenDocument Text'
}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()

def convert_document(input_path, output_path, input_format, output_format):
    """Convert document using appropriate method based on input/output formats"""
    try:
        # Special handling for PDF to DOCX
        if input_format == 'pdf' and output_format == 'docx':
            return convert_pdf_to_docx(input_path, output_path)
       
        # Special handling for DOCX to PDF
        elif input_format == 'docx' and output_format == 'pdf':
            return convert_docx_to_pdf(input_path, output_path)
       
        # Use pandoc for other conversions
        else:
            pypandoc.convert_file(
                input_path,
                output_format,
                outputfile=output_path,
                format=input_format
            )
            return True
    except Exception as e:
        print(f"Conversion error: {str(e)}")
        return False

def convert_pdf_to_docx(pdf_path, docx_path):
    """Convert PDF to DOCX using PyPDF2 and python-docx"""
    try:
        reader = PdfReader(pdf_path)
        doc = Document()
       
        for page in reader.pages:
            text = page.extract_text()
            doc.add_paragraph(text)
       
        doc.save(docx_path)
        return True
    except Exception as e:
        print(f"PDF to DOCX conversion error: {str(e)}")
        return False

def convert_docx_to_pdf(docx_path, pdf_path):
    """Convert DOCX to PDF using pandoc"""
    try:
        pypandoc.convert_file(
            docx_path,
            'pdf',
            outputfile=pdf_path,
            format='docx'
        )
        return True
    except Exception as e:
        print(f"DOCX to PDF conversion error: {str(e)}")
        return False

if __name__ == '__main__':
    pf = "uploads\\Instructions.pdf"
    of = "uploads\\ok.docx"
    convert_document(pf, of, 'pdf', 'docx')