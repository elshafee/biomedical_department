import requests
import re
url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgAF0pZx5Dl6RoJaYmkO42oZAS1tnBKrz2mgHw7OE0Wps4w?e=iQA0ZT"
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})
res = session.get(url)
print("Status:", res.status_code)
# Search for serverRelativeUrl or similar in the response text
m = re.search(r'"serverRelativeUrl":"([^"]+)"', res.text)
if m:
    print("Folder Path:", m.group(1))
m2 = re.search(r'"ListUrl":"([^"]+)"', res.text)
if m2:
    print("List URL:", m2.group(1))
