import os
import sys

# load env
from dotenv import load_dotenv
load_dotenv('.env.local')

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.onedrive import upload_file_to_share

with open("dummy_test_old.txt", "w") as f:
    f.write("test old upload")

res = upload_file_to_share("dummy_test_old.txt", "dummy_test_old.txt", is_preview=False)
print("Upload result (Old Link):", res)
