from docx import Document
doc = Document('BONAFIDE.docx')
text = ''
for para in doc.paragraphs:
    text += para.text + '\n'
print(text)
