#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib"""

import urllib.request

url = "https://alu-intranet.hbtn.io/status"
headers = {"User-Agent": "Mozilla/5.0"}

request = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(request) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))

