import re
import requests
from bs4 import BeautifulSoup

url = "https://www.nesoacademy.org/cs/03-operating-system/01-introduction-and-basics/01-introduction-to-operating-system"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Referer": "https://player.vdocipher.com/",
}

with requests.session() as s:
    soup = BeautifulSoup(s.get(url, headers=headers).content, "html.parser")
    url2 = soup.iframe["src"]
    html_doc = s.get(url2, headers=headers).text
    link = re.search(r'file:".*?(http[^",]+)', html_doc).group(1)
    print(link)

    with open("file.mp4", "wb") as f:
        f.write(s.get(link, headers=headers, verify=False).content)

    print("Done.")
