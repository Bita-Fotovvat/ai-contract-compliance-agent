from pypdf import PdfReader

def extract_text(uploaded_file) -> str:
    reader = PdfReader(uploaded_file)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())