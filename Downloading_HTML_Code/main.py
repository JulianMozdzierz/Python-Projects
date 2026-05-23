import os, sys
import urllib.parse
import validators
import requests
from datetime import datetime

print("Number of arguments: ", len(sys.argv))
print("Arguments list: ", sys.argv)


url = "https://google.com"
if len(sys.argv) > 1:
    url = sys.argv[1]

print("Webside to dowlnoad: ", url)

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
print("Current working dir: ", os.getcwd())

if not os.path.exists("./websides"):
    os.mkdir("websides")

parsedUrl=urllib.parse.urlparse(url)
print(parsedUrl)

validFlag = validators.url(url)
if validFlag:
    print("Url: ", url, " is valid" )
else:
    print("Url: ", url, " is invalid" )
    raise Exception("Bad url!")

response = requests.get(url, allow_redirects=True)
if response.ok == True:
    print("Response ok from server URL: ", url)
    now = datetime.now()
    dateStr = now.strftime("%d.%m.%Y %H.%M.%S")
    print(dateStr)
    fileName = "./websides/" + parsedUrl.netloc + " " + dateStr + ".html"
    print(fileName)

    fh = open(fileName, "wb")
    fh.write(response.content)
    fh.close()
