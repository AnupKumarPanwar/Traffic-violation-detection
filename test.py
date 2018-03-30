import requests
import json
import xmltodict

from flask import Flask
app = Flask(__name__)

@app.route('/owner/<path:url>')
def owner(url):

   # print ("https://api.openalpr.com/v2/recognize_url?image_url="+url+"&secret_key=sk_56f3f58c95876e8142b0d23b&recognize_vehicle=0&country=in&return_image=0&topn=10")

   headers={'Content-Type': 'application/json', 'Accept': 'application/json'}

   # r=requests.post("https://api.openalpr.com/v2/recognize_url?image_url="+url+"&secret_key=sk_56f3f58c95876e8142b0d23b&recognize_vehicle=0&country=in&return_image=0&topn=10", headers=headers)

   
   r=requests.post("https://api.openalpr.com/v2/recognize_url?image_url="+url+"&secret_key=sk_DEMODEMODEMODEMODEMODEMO&recognize_vehicle=0&country=in&return_image=0&topn=10", headers=headers, timeout=100)

   # print (json.dumps(r.text))
   # sk_DEMODEMODEMODEMODEMODEMO

   print (r.text)

   plateNumber=json.loads(r.text)['results'][0]['plate']

   parivahan = "https://parivahan.gov.in/rcdlstatus/vahsar/vahsarStatus/rcStatus"

   querystring = {"reg1":plateNumber[:-4],"reg2":plateNumber[-4:]}

   headers = {
    'cache-control': "no-cache",
    'postman-token': "01230a2a-bd07-e46f-cd93-45d76837c956"
    }

   ownerInfo = requests.request("GET", parivahan, params=querystring, headers=headers)

   print (ownerInfo.text)

   data=xmltodict.parse(ownerInfo.text)

   return (json.dumps(data))

if __name__ == '__main__':
   app.run()