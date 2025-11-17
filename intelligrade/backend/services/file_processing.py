# services/file_processing.py
import fitz  # PyMuPDF for PDF text extraction
from docx import Document
from io import BytesIO

def extract_text_from_pdf(file_content: bytes) -> str:
    """Extract text from PDF file."""
    try:
        # Convert bytes to BytesIO
        pdf_stream = BytesIO(file_content)
        doc = fitz.open(stream=pdf_stream, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {e}")

def extract_text_from_docx(file_content: bytes) -> str:
    """Extract text from DOCX file."""
    try:
        # Convert bytes to BytesIO
        docx_stream = BytesIO(file_content)
        doc = Document(docx_stream)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"Error extracting text from DOCX: {e}")

def extract_text_from_txt(file_content: bytes) -> str:
    """Extract text from TXT file."""
    try:
        return file_content.decode("utf-8", errors="ignore").strip()
    except Exception as e:
        raise Exception(f"Error extracting text from TXT: {e}")