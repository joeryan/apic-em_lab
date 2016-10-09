import requests
import json

controller = "devnetapi.cisco.com/sandbox/apic_em"
url = "https://" + controller + "/api/v1/ticket"
payload = {"username":"devnetuser","password":"Cisco123!"}
header = {"content-type":"application/json"}

response = requests.post(url,data=json.dumps(payload),headers=header, verify=False)

r_json = response.json()
ticket = r_json["response"]["serviceTicket"]

url = "https://" + controller + "/api/v1/host"
header = {"content-type":"application/json", "X-Auth-Token":ticket}
response = requests.get(url, headers=header, verify=False)

print("Hosts: ")
print(json.dumps(response.json(), indent=4, separators=(',', ': ')))
