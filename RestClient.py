import requests

#Specify URL
url ="http://moviecatalogservice-101.cfapps.io/catalog/ss"

#Call REST API
response = requests.get(url)

#Print response
print (response.text)