import xmltodict, json
import requests

url = "https://parivahan.gov.in/rcdlstatus/vahsar/vahsarStatus/rcStatus"

querystring = {"reg1":"MH12DE","reg2":"1433"}

response = requests.request("GET", url, params=querystring)

data=xmltodict.parse(response.text)

print(json.dumps(data))