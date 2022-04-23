import requests
from .secrets import jwt

def file_upload(file):
    file = str(file).replace(" ", "_")
    url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'
    files = {'file': open("uploads/"+str(file), 'rb')}
    header = {'Authorization': 'Bearer {}'.format(jwt)}
    my_response = requests.post(url, headers=header, files=files)
    hash_value = my_response.text[13:59]
    upload_url = 'ipfs.io/ipfs/' + hash_value
    return upload_url
        