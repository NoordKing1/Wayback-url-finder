# By StrikeXD

import os
import requests


domain = input("[!] Enter Website Domain: ")

notable_startwith = ("http", "https")

if domain.startswith(tuple(notable_startwith)):
  print("[!] Please Type Domain Without http/s .")
  exit()

print("\n[*] Please Wait...")

url = f"http://web.archive.org/cdx/search/cdx?url={domain}%2F*&output=text&fl=original&collapse=urlkey&filter=statuscode%3A200"

r = requests.get(url)


with open("links.txt", "w+") as f:
  f.write(r.text)

path = os.getcwd()

print(f"\n[*] waybackurls saved in: {path}")
