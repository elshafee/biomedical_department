import os
import sys

# load env
from dotenv import load_dotenv
load_dotenv('.env.local')
# Let's force the PREVIEW link for the test
os.environ["ONEDRIVE_SHARE_URL"] = os.environ.get("ONEDRIVE_PREVIEW_SHARE_URL")

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.onedrive import upload_file_to_share

with open("dummy_test.txt", "w") as f:
    f.write("test preview upload")

res = upload_file_to_share("dummy_test.txt", "dummy_test.txt", is_preview=True)
print("Upload result:", res)
