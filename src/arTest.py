import os.path

from lib.echoMeAPI import EchoMeAPI, AssetRegistrationAPI, SiteAPI
from utils.Logger import Logger
from values import CONSTANT

def simpleAr1():

    echoMeAPI = EchoMeAPI()
    print(echoMeAPI.getSystemURL())

    arAPI = AssetRegistrationAPI()
    # resultData = arAPI.getOrderDetail("AR_06/03/2023 02:49:55", 2)
    # arAPI.getOrderHeader()

    siteAPI = SiteAPI()
    siteAPI.getMainPage()
    siteAPI.listSite()
    siteAPI.setSite("HKG_ATL_3F")

    a = arAPI.getOrderHeader()
    # b = arAPI.uploadARFile(os.path.join(CONSTANT.APPLICATION_NAME_FULL_PATH, "files/testExcelFile/AssetRegistration_test1.xlsx"))
    b = arAPI.uploadARFile("AssetRegistration_test1.xlsx")
    c = arAPI.getOrderHeader()
    orderNum = c[0]["regNum"]
    d = arAPI.getOrderLine(orderNum)
    oddLineList = []
    evenLineList = []

    siteInfo = siteAPI.getCurrentSiteInfo()
    e = arAPI.getOrderDetail(orderNum, siteInfo["id"])

    f = arAPI.genRfidItem(orderNum)
    for i in range(len(f)):
        if i % 2:
            oddLineList.append(f[i]["rfid"])
        else:
            evenLineList.append(f[i]["rfid"])
    g = arAPI.getOrderDetail(orderNum, siteInfo["id"])

    h = arAPI.listAllPrefixSequence()
    prefix = h[0]["prefix"]
    i = arAPI.setContainerPrefix(prefix)

    j = arAPI.genRfidContainer(1,1)
    containerInfo = j[0]
    k = arAPI.checkInContainer(orderNum, containerInfo["rfid"])


    l = arAPI.checkInItem(orderNum, containerInfo["containerAssetCode"], ",".join(oddLineList))
    m = arAPI.getOrderLine(orderNum)
    n = arAPI.checkInItem(orderNum, containerInfo["containerAssetCode"], ",".join(evenLineList))
    o = arAPI.getOrderLine(orderNum)

    p = arAPI.completeOrder(orderNum)
    r = arAPI.getOrderHeader(orderNum)
    s = arAPI.getOrderLine(orderNum)

    print("")


if __name__ == "__main__":
    simpleAr1()

    print("")