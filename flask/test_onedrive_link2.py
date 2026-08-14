import requests
import re
import urllib.parse

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=n5UMBa"
session = requests.Session()
res = session.get(share_url)

match = re.search(r'\"(.*?/personal/aelshafee_horus_edu_eg/.*?)\"', res.text)
if match:
    print("Found path:", match.group(1))

lines = [line for line in res.text.split('\n') if '/personal/' in line]
for line in lines[:5]:
    print(line[:200])

