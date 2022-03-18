import urllib.request, urllib.parse, urllib.error
url = input("Enter url - ")
fhand = urllib.request.urlopen(url)
text = ""
count = 0
for line in fhand:
  line = line.decode()
  for char in line:
    text = text + char
    count = count + 1
text = text[:3000]
print(f"text: {text}\n count: {count}")
