import requests
import re
import json

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=fLXdAR"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
})
res = session.get(share_url)

match = re.search(r'g_listData\s*=\s*(\{.*?\});', res.text)
if match:
    data = json.loads(match.group(1))
    perms = data.get('ListPermsMask', {})
    print("Permissions:", perms)
    
match2 = re.search(r'"listPermsMask"\s*:\s*(\{.*?\})', res.text)
if match2:
    print("Permissions 2:", match2.group(1))

