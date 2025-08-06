from pypdf import PdfReader

reader = PdfReader('/content/s11042-024-18826-4.pdf')
for page in reader.pages:
    text = page.extract_text()
    print(text)
