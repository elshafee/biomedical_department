import requests
import re
import urllib.parse
import json

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=n5UMBa"
session = requests.Session()
res = session.get(share_url)

paths = set(re.findall(r'/personal/aelshafee_horus_edu_eg/[^\"]*', res.text))
print("Found paths:", paths)

