import os
import sys
import requests

# load env
from dotenv import load_dotenv
load_dotenv('.env.local')

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.onedrive import upload_file_to_share

with open("dummy_test_new.txt", "w") as f:
    f.write("test new upload")

res = upload_file_to_share("dummy_test_new.txt", "dummy_test_new.txt", is_preview=True)
print("Upload result (New Link):", res)
