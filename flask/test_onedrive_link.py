import requests
import re
import urllib.parse

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=n5UMBa"
session = requests.Session()
res = session.get(share_url)
print("Status Code:", res.status_code)

match = re.search(r'\"ListUrl\"\s*:\s*\"([^\"]+)\"', res.text)
if match:
    print("ListUrl (decoded):", match.group(1))

# Check for ServerRelativeUrl
match2 = re.search(r'\"ServerRelativeUrl\"\s*:\s*\"([^\"]+)\"', res.text)
if match2:
    print("ServerRelativeUrl:", match2.group(1))

match3 = re.search(r'\"folderUrl\"\s*:\s*\"([^\"]+)\"', res.text)
if match3:
    print("folderUrl:", urllib.parse.unquote(match3.group(1).encode('utf-8').decode('unicode_escape')))
