from pypdf import PdfReader

def get_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def classify_resume(pdf_path):
    text = get_pdf_text(pdf_path)
    return ["Software Engineer", "Data Scientist", "Business Analyst"]