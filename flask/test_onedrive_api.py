import requests
import json
import urllib.parse

share_url = "https://horusuni-my.sharepoint.com/:f:/g/personal/aelshafee_horus_edu_eg/IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8?e=n5UMBa"
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
})
res = session.get(share_url)

site_url = "https://horusuni-my.sharepoint.com/personal/aelshafee_horus_edu_eg"
ctx_response = session.post(f"{site_url}/_api/contextinfo", headers={'Accept': 'application/json;odata=verbose'})
digest = ctx_response.json()['d']['GetContextWebInformation']['FormDigestValue']

# Get the list of folders the guest has access to?
# Actually, let's see if we can get the item from the sharing link
# The sharing link token is the part after /g/personal/aelshafee_horus_edu_eg/
token = "IgB8bbTxDL1DSbc_8o2geGwTAY4tuq4OTEUwSWSPHfhL8b8"
encoded_url = urllib.parse.quote(share_url, safe='')

# There's an endpoint: _api/SP.RemoteWeb(@a1)/Web/GetFileByGuestUrl(@a1) or similar.
# Let's try _api/web/GetList(@a1) or something? 
# Let's just try to get all folders in the root Documents
folders_res = session.get(f"{site_url}/_api/web/GetFolderByServerRelativePath(DecodedUrl='/personal/aelshafee_horus_edu_eg/Documents')/Folders", headers={'Accept': 'application/json;odata=verbose'})
print(folders_res.status_code)
if folders_res.status_code == 200:
    for folder in folders_res.json()['d']['results']:
        print("Folder:", folder['ServerRelativeUrl'])
