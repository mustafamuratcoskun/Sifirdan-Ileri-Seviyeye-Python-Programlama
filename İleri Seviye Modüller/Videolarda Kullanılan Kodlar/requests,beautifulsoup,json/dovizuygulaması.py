import requests

import sys
url = "http://api.fixer.io/latest?base="

birinci_doviz = input("Birinci Döviz:")
ikinci_döviz = input("İkinci Döviz:")
miktar = float(input("Miktar:"))


response = requests.get(url + birinci_doviz)

json_verisi = response.json()
try:
    print(json_verisi["rates"][ikinci_döviz] * miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru girin")
    sys.stderr.flush()








