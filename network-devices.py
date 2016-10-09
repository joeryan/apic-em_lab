import requests
import json

controller = "devnetapi.cisco.com/sandbox/apic_em"

def getTicket():
    url = "https://" + controller + "/api/v1/ticket"
    payload = {"username":"devnetuser","password":"Cisco123!"}
    header = {"content-type":"application/json"}

    response = requests.post(url,data=json.dumps(payload),headers=header, verify=False)

    r_json = response.json()
    ticket = r_json["response"]["serviceTicket"]
    return ticket

def getNetworkDevices(ticket):
    url = "https://" + controller + "/api/v1/network-device"
    header = {"content-type":"application/json", "X-Auth-Token":ticket}
    response = requests.get(url, headers=header, verify=False)

    print("Network Devices: ")
    print(json.dumps(response.json(), indent=4, separators=(',', ': ')))

    r_json = response.json()

    for dev in r_json["response"]:
        print(dev["id"] + ":  " + dev["series"])

theTicket = getTicket()
getNetworkDevices(theTicket)
