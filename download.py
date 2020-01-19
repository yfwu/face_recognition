import requests
from bs4 import BeautifulSoup
import re
import shutil
import time

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://www.javbus.com/actresses/"

namelist = []
for page in range(1, 209):
    req = session.get(url+str(page), headers=headers)
    bsObj = BeautifulSoup(req.text)
    namelist.extend([{"title":i["title"], "src":i["src"]} for i in bsObj.findAll("img", {"src":re.compile(".*\.jpg")})])
    time.sleep(0.3)

for name in namelist:         
    response = requests.get(name["src"], stream=True, headers=headers)
    with open("database/"+name["title"]+'.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    time.sleep(0.3)
