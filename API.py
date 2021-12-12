
citi_jan = pd.read_csv('CitibikeJanuary2021.csv')


import bigdatacloudapi
import requests


a_lat = [i for i in citi_jan['start station latitude']]
a_long = [i for i in citi_jan['start station longitude']]
              
          

apiKey = "69136c65e9e44449aad09e93c691d334"
client = bigdatacloudapi.Client(apiKey)
resultObject,httpResponseCode = client.getIpGeolocationFull({"ip":"8.8.8.8"})

          
base_url = "https://api.bigdatacloud.net/data/reverse-geocode?latitude="
key = "69136c65e9e44449aad09e93c691d334"

zipcode = []
for i in range(len(citi_jan)):
    address = f"{a_lat[i]}&longitude={a_long[i]}&localityLanguage=en&key="
    zipcode.append(requests.get(f"{base_url}{address}{key}").json()['postcode'])
    print(requests.get(f"{base_url}{address}{key}").json()['postcode'])