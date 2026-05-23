from websites import *
import os, sys, threading, time, requests
import validators

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites("websites.txt")

# websites.putwebsiteData({"index": 0, "website" : "duckduckgo.com" , "status code": 200})
# websites.saveReport()

dataLock = threading.Lock()


class Client(threading.Thread):
    def __init__(self, threadName, websites, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.websites = websites
        self.sleepTime = sleepTime

    def run(self):
        while True:
            dataLock.acquire()
            webisteToCheck = self.websites.getNextWebsiteToCheck()
            dataLock.release()
            if not webisteToCheck:
                break
            
            print(webisteToCheck)
            self.checkUrl(webisteToCheck)
            time.sleep(self.sleepTime)

        print(self.threadName, "ended")

    def checkUrl(self, data):
        try:
            validUrlFlag = validators.url(data["website"])
            if validUrlFlag:
                data["validUrlFlag"] = True
                response = requests.get(data["website"], allow_redirects=True)
                data["status code"] = response.status_code

            else:
                data["validUrlFlag"] = True
        except:
            data["exception"] = sys.exc_info()[0]

        dataLock.acquire()
        self.websites.putwebsiteData(data)
        dataLock.release()
        

numThreads = 10
threadsList = []
num = 0 
while num < numThreads:
    t = Client("T" + str(num), websites, 0.1)
    threadsList.append(t)
    t.start()
    num += 1

for t in threadsList:
    t.join()

websites.saveReport()
print("Job done")