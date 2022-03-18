import urllib.request, urllib.parse, urllib.error
import json

#needs API key to work

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

address = input("Enter location: ")

url = serviceurl + urllib.parse.urlencode({"address": address})

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

try:
  js = json.loads(data)
except:
  js = None
if not js or "status" not in js or js["status"] != "OK":
  print("Error")
print(js)