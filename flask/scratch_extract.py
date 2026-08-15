import zipfile
import os

docx_path = "template_essic.docx"
out_dir = "public/assets"
os.makedirs(out_dir, exist_ok=True)

with zipfile.ZipFile(docx_path, 'r') as docx_zip:
    for item in docx_zip.namelist():
        if item.startswith("word/media/"):
            filename = os.path.basename(item)
            out_path = os.path.join(out_dir, filename)
            with open(out_path, 'wb') as f:
                f.write(docx_zip.read(item))
            print(f"Extracted: {filename}")

