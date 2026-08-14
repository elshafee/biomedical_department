import os
import sys

# load env
from dotenv import load_dotenv
load_dotenv('.env.local')
os.environ["ONEDRIVE_SHARE_URL"] = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=n5UMBa"

import services.onedrive
# Monkeypatch the config temporarily
old_config = services.onedrive.get_sharepoint_config
def new_config():
    share_url, base_url, site_url, _ = old_config()
    # USE THE ROOT FOLDER!
    return share_url, base_url, site_url, "/personal/aelshafee_horus_edu_eg/Documents"
services.onedrive.get_sharepoint_config = new_config

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.onedrive import upload_file_to_share

with open("dummy_test.txt", "w") as f:
    f.write("test")

res = upload_file_to_share("dummy_test.txt", "dummy_test.txt")
print("Upload result:", res)
