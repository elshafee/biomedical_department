import copy
from docx import Document

def run_test():
    doc = Document("template_essic.docx")
    
    replacements = {
        "{{CODE_NUMBER}}": "0001 AIE 08-2026",
        "{{SEND_TO}}": " ",
        "{{SUBJECT}}": " ",
        "{{STACK_HOLDER}}": "\u202Bا.د حاتم خاطر\u202C",
        "{{POSITION}}": "\u202Bعميد كلية الهندسة\u202C",
        "{{BODY_TEXT}}": " ",
        "{{SENDER}}": "",
        "{{SENDER_TOP}}": "\u202Aأ.م.د/ محمد كمال عبد السلام\u202C",
        "{{SENDER_POSITION}}": " ",
        "{{AIE}}": ""
    }

    for paragraph in doc.paragraphs:
        full_text = "".join(run.text for run in paragraph.runs)
        modified = False
        
        for k, v in replacements.items():
            if k in full_text:
                full_text = full_text.replace(k, v)
                modified = True
                
        if modified:
            if not full_text.strip():
                pass
            elif paragraph.runs:
                paragraph.runs[0].text = full_text
                for run in paragraph.runs[1:]:
                    run.text = ""

    doc.save("test_output.docx")
    print("Done")

if __name__ == "__main__":
    run_test()
