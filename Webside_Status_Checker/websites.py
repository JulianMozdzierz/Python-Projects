
class Websites:
    def __init__(self, fileName):
        self.fileName = fileName
        self.fileList = []
        self.reportList = []
        self.index = 0
        self.loadFile(fileName)

    def loadFile(self, fileName):
        fh = open(fileName, "r")
        dataList = fh.readlines()

        for v in dataList:
            v = "https://" + v.strip()
            data = {"website" : v , "status code" : -1}
            self.fileList.append(data)
            data["index"] = len(self.fileList) - 1
            #print(data)


    def getNextWebsiteToCheck(self):
        if self.index >= len(self.fileList):
            return None
        
        data = self.fileList[self.index]
        self.index +=1
        return data

    def putwebsiteData(self, data):
        if "index" in data and "website" in data and "status code" in data:
            self.reportList.append(data)
        else:
            print("Bad keys in report: " + str(data))


    def saveReport(self):
        fh = open("report.txt", "w")

        for el in self.reportList:
            print(el)
            fh.write(str(el["website"]) + "-" + str(el) + "\n")

        fh.close()
        print("Raport saved!")