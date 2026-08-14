import copy
from docx import Document

def fix_template():
    doc = Document("template_essic.docx")
    for p in doc.paragraphs:
        if 'SENDER' in p.text:
            text = "".join(r.text for r in p.runs)
            if '{{SENDER_TOP}} / {{SENDER_POSITION}}' in text:
                text = text.replace('{{SENDER_TOP}} / {{SENDER_POSITION}}', '{{SENDER_TOP}}')
                p.runs[0].text = text
                for r in p.runs[1:]:
                    r.text = ""
    doc.save("template_essic.docx")
    print("Template fixed.")

if __name__ == "__main__":
    fix_template()
