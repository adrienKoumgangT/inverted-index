import pdfplumber
from bs4 import BeautifulSoup
import docx
import pytesseract
from PIL import Image
import pdf2image


def extract_text_from_file(filepath):
    """Extract text from any supported file format"""
    text = ""
    try:
        if filepath.lower().endswith('.pdf'):
            # Try regular PDF extraction first
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    text += page.extract_text(x_tolerance=1, y_tolerance=1) + "\n"
            # Fallback to OCR if little text was extracted
            if len(text.strip()) < 50:
                images = pdf2image.convert_from_path(filepath)
                text = "\n".join(pytesseract.image_to_string(img) for img in images)

        elif filepath.lower().endswith(('.docx', '.doc')):
            doc = docx.Document(filepath)
            text = "\n".join(para.text for para in doc.paragraphs)

        elif filepath.lower().endswith('.html'):
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                text = soup.get_text(separator='\n', strip=True)

        elif filepath.lower().endswith(('.jpg', '.jpeg', '.png')):
            text = pytesseract.image_to_string(Image.open(filepath))

        else:  # Default .txt handling
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()

    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")
        return None

    return text.lower()


def safe_extract(filepath):
    try:
        return extract_text_from_file(filepath)
    except Exception as e:
        print(f"Skipping {filepath} due to error: {str(e)}")
        return None


