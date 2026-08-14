import requests
import re
import json

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=n5UMBa"
session = requests.Session()
res = session.get(share_url)

match = re.search(r'g_listData\s*=\s*(\{.*?\});', res.text)
if match:
    data = json.loads(match.group(1))
    print("Folder URL:", data.get('ListUrlDir'))
    print("RootFolder:", data.get('RootFolder'))

match2 = re.search(r'"RootFolder"\s*:\s*"(.*?)"', res.text)
if match2:
    print("RootFolder 2:", match2.group(1))
    
match3 = re.search(r'"folderUrl"\s*:\s*"(.*?)"', res.text)
if match3:
    print("Folder URL 3:", match3.group(1))

