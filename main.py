# import requests
# import json

# url = "https://cryptoprices.com/wp-content/plugins/coinpress/assets/public"



# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# }
# result = requests.get(url, headers=headers)
# for coin in result["data"]:
#     print(f"{coin}")

import fitz # install using: pip install PyMuPDF

with fitz.open("example.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

print(text)