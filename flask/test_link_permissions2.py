import requests
import re
import json

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgAF0pZx5Dl6RoJaYmkO42oZAS1tnBKrz2mgHw7OE0Wps4w?e=iQA0ZT"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
})
res = session.get(share_url)
match2 = re.search(r'"listPermsMask"\s*:\s*(\{.*?\})', res.text)
if match2:
    print("Old link Permissions:", match2.group(1))

