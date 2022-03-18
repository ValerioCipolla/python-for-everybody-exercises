import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "https://cat-fact.herokuapp.com/facts"

print("Retrieving", serviceurl)
uh = urllib.request.urlopen(serviceurl)
data = uh.read().decode()
js = json.loads(data)
count = 1
for fact in js:
  print(f"Fact #{count}: {fact['text']}")
  count = count + 1