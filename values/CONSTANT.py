import os

APPLICATION_NAME = "autoReg"
FULLPATH_ENDINDEX = os.getcwd().index(APPLICATION_NAME) + APPLICATION_NAME.__len__()
APPLICATION_NAME_FULL_PATH = os.getcwd()[0:FULLPATH_ENDINDEX]

class EchoMe_CONSTANT():
    PROTOCOL = "http"
    IP = "qa-echome.ddns.net"
    PORT = "80"
    SUPPORT_PORT = "8994"
    SYSTEM = "echoMe"

    domainMap = {"DFS": "http://echome.dfs.com",
                 "AWS": "http://qa-echome.ddns.net",
                 "AWS_IP": "http://16.162.105.236",
                 "new_AWS_IP": "http://18.162.168.95"
                 }


class KeyCloak_CONSTANT():
    PROTOCOL = "https"
    IP = "qa-proteksso.ddns.net"
    PORT = "443"
    SUPPORT_PORT = "8994"
    SYSTEM = "auth/realms/MEGA-WMS/protocol/openid-connect"

    keyClockDomainMap = {"AWS": "https://qa-proteksso.ddns.net",
                         "DFS": "https://atlrfid.dfs.com",
                         "AWS_IP": "http://16.162.105.236",
                         "new_AWS_IP": "http://18.162.168.95"}