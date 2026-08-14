import os
import sys

# load env
from dotenv import load_dotenv
load_dotenv('.env.local')
os.environ["ONEDRIVE_SHARE_URL"] = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=n5UMBa"

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.onedrive import upload_file_to_share

with open("dummy_test.txt", "w") as f:
    f.write("test")

res = upload_file_to_share("dummy_test.txt", "dummy_test.txt")
print("Upload result:", res)
