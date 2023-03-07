import json

import requests as httpclient

from utils.Logger import Logger
from values.CONSTANT import EchoMe_CONSTANT
from values.EndPoint import EndPoint


from requests_toolbelt import MultipartEncoder

from pprint import pprint

class EchoMeAPI:
    SESSION = httpclient.Session()
    PROTOCOL = EchoMe_CONSTANT.PROTOCOL
    IP = EchoMe_CONSTANT.IP
    PORT = EchoMe_CONSTANT.PORT
    SYSTEM = EchoMe_CONSTANT.SYSTEM

    @staticmethod
    def getSystemURL():
        if EchoMeAPI.PROTOCOL and EchoMeAPI.IP and EchoMeAPI.PORT and EchoMeAPI.SYSTEM:
            return "{}://{}:{}/{}".format(EchoMeAPI.PROTOCOL, EchoMeAPI.IP, EchoMeAPI.PORT, EchoMeAPI.SYSTEM)\

class KeyClockAPI:
    SESSION = httpclient.Session()
    PROTOCOL = EchoMe_CONSTANT.PROTOCOL
    IP = EchoMe_CONSTANT.IP
    PORT = EchoMe_CONSTANT.PORT
    SYSTEM = EchoMe_CONSTANT.SYSTEM

    @staticmethod
    def getSystemURL():
        if EchoMeAPI.PROTOCOL and EchoMeAPI.IP and EchoMeAPI.PORT and EchoMeAPI.SYSTEM:
            return "{}://{}:{}/{}".format(EchoMeAPI.PROTOCOL, EchoMeAPI.IP, EchoMeAPI.PORT, EchoMeAPI.SYSTEM)

class Service_Interface():
    def __init__(self):
        self.serviceLocation = ""
        self.params = {}

    def getServiceLocation(self):
        return self.serviceLocation

    def getDestination(self):
        return EchoMeAPI.getSystemURL() + self.getServiceLocation()

    def sendJSON(self, serviceMethod, query, headers = {}, log=True):
        try:
            url = EchoMeAPI.getSystemURL() + serviceMethod
            print(url)
            print(query)
            response = EchoMeAPI.SESSION.get(url=url, params=query, headers=headers)
            print(response.cookies.get_dict())
            if log:
                Logger.dwriteprint(response.url)
                Logger.dwriteprint(response.text)

            resultData = json.loads(response.text)
            return resultData
        except Exception as e:
            print(e)
            return None

    def sendPostJson(self, serviceMethod, query, data, headers= {}, log= True):
        try:
            url = EchoMeAPI.getSystemURL() + serviceMethod
            print(url)
            print(query)
            # EchoMeAPI.SESSION.headers.update(headers)
            response = EchoMeAPI.SESSION.post(url=url, params=query, data= data, timeout=30, headers=headers)
            pprint(response.url)
            pprint(response.headers)
            # print(response.cookies.get_dict())
            if log:
                Logger.dwriteprint(response.url)
                Logger.dwriteprint(response.text)

            resultData = json.loads(response.text)
            return resultData
        except Exception as e:
            print(e)
            return None


class SiteAPI(Service_Interface):

    siteDict = {}
    selectedSite = {}

    def getMainPage(self):
        serviceMethod = ""
        query = {}
        return self.sendJSON(serviceMethod, query)

    def listSite(self):
        serviceMethod = EndPoint.listLocSiteMethod
        query = {}
        resultList = self.sendJSON(serviceMethod, query)
        self.siteDict = {siteInfo["siteCode"]: siteInfo for siteInfo in resultList}
        return resultList

    def setSite(self, siteCode):
        serviceMethod = EndPoint.setSiteCodeMethod
        query = {"siteCode": siteCode}
        # headers = {"Cookie": "JSESSIONID=A6AFDE82C0E90ED1D6B0A8567F4FE05F"}
        result = self.sendJSON(serviceMethod, query, log=True)
        self.selectedSite = siteCode
        return result

    def getCurrentSiteInfo(self):
        return self.siteDict[self.selectedSite]

class AssetRegistrationAPI(Service_Interface):

    def getOrderHeader(self, regNum = ""):
        serviceMethod = EndPoint.assetRegistrationMethod
        sortInfo = {
            "id": 1,
            "name": "modifiedDate",
            "type": "",
            "dir": -1
        };

        filter = {}
        if regNum:
            filter.update({
                "value": regNum,
                "name": "regNum",
                "operator": "contains",
                "type": "string"
            });

        query = {
            "filterBy": json.dumps([filter]),
            "sortInfo": json.dumps(sortInfo)
        };
        return self.sendJSON(serviceMethod, query)

    def getOrderLine(self, regNum = ""):
        serviceMethod = EndPoint.assetRegistrationLineMethod
        sortInfo = {
            "id": 1,
            "name": "modifiedDate",
            "type": "",
            "dir": -1
        };

        filter = {}
        if regNum:
            filter.update({
                "value": regNum,
                "name": "regNum",
                "operator": "contains",
                "type": "string"
            });

        query = {
            "filterBy": filter,
            "sortInfo": sortInfo
        }

        query = {
            "filterBy": json.dumps([filter]),
            "sortInfo": json.dumps(sortInfo)
        }
        return self.sendJSON(serviceMethod, query)

    def listAllPrefixSequence(self):
        serviceMethod = EndPoint.listAllPrefixSequence
        query = {}
        return self.sendJSON(serviceMethod, query)

    def setContainerPrefix(self, prefix):
        serviceMethod = EndPoint.genRfidItem
        query = {"prefix": prefix}
        return self.sendJSON(serviceMethod, query)

    def genRfidContainer(self, containerQty, rfidQty):
        serviceMethod = EndPoint.genRfidContainer
        query = {"containerQty": containerQty, "rfidQty": rfidQty}
        return self.sendJSON(serviceMethod, query)

    def setContainerPrefix(self, containerPrefix):
        serviceMethod = EndPoint.setContainerPrefix
        query = {"containerPrefix": containerPrefix}
        return self.sendJSON(serviceMethod, query)

    def genRfidItem(self, regNum):
        serviceMethod = EndPoint.genRfidItem
        query = {"regNum": regNum}
        return self.sendJSON(serviceMethod, query)

    def getOrderDetail(self, regNum, site):
        serviceMethod = EndPoint.getOrderDetailARMethod
        query = {"regNum": regNum, "site": site}
        return self.sendJSON(serviceMethod, query)

    def checkInContainer(self, regNum, rfids):
        serviceMethod = EndPoint.registerContainerMethod
        query = {"regNum": regNum, "rfids": rfids}
        return self.sendJSON(serviceMethod, query)

    def checkInItem(self, regNum, containerAssetCode, rfids):
        serviceMethod = EndPoint.registerItemsMethod
        query = {"regNum": regNum, "containerAssetCode": containerAssetCode, "rfids": rfids}
        return self.sendJSON(serviceMethod, query)

    def completeOrder(self, regNum):
        serviceMethod = EndPoint.registerCompleteMethod
        query = {"regNum": regNum}
        return self.sendJSON(serviceMethod, query)

    def uploadARFile(self, fileLocation):
        serviceMethod = EndPoint.assetRegistrationUploadMethod
        headers = {
            'accept': '*/*',
            'content-type': 'multipart/form-data',
        }
        query = {"userName": 2}
        data = {"file": (fileLocation ,open(fileLocation, "rb"))}

        data = MultipartEncoder(fields={"file": (fileLocation, open(fileLocation, "rb"), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")})
        headers = {'Content-type': data.content_type}
        # data = {fileLocation :open(fileLocation, "rb")}
        # data = {"file": open(fileLocation, "rb")}
        return self.sendPostJson(serviceMethod, query, data, headers=headers)


