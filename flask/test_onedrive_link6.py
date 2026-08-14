import requests
import re
import urllib.parse

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgAF0pZx5Dl6RoJaYmkO42oZAS1tnBKrz2mgHw7OE0Wps4w?e=iQA0ZT"
session = requests.Session()
res = session.get(share_url)

paths = set(re.findall(r'/personal/aelshafee_horus_edu_eg/[^\"]*', res.text))
print("Old link found paths:", paths)

