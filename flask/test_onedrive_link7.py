import requests
import re
import urllib.parse
import json

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=n5UMBa"
session = requests.Session()
res = session.get(share_url)

match = re.search(r'<title>(.*?)</title>', res.text, re.IGNORECASE)
if match:
    print("Title:", match.group(1))

# Try to find folder name from Next.js or React hydration data
match2 = re.search(r'"Title"\s*:\s*"(.*?)"', res.text)
if match2:
    print("Title 2:", match2.group(1))

