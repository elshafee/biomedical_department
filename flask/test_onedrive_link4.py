import requests
import re
import urllib.parse
import json

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=n5UMBa"
session = requests.Session()
res = session.get(share_url)

match = re.search(r'\"ServerRelativeUrl\"\s*:\s*\"([^\"]+)\"', res.text)
if match:
    print("ServerRelativeUrl:", match.group(1))

# Search for any string starting with /personal/aelshafee_horus_edu_eg/Documents
paths = set(re.findall(r'/personal/aelshafee_horus_edu_eg/Documents/[^\"]*', res.text))
print("Found paths:", paths)

