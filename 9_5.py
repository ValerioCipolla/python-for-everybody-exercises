fname = input("Please enter a file name: ")
try:
  fhand = open(fname)
except:
  print("Could not open file", fname)
  exit()
count = dict()
for line in fhand:
  if line.startswith("From "):
    words = line.split()
    email = words[1]
    domain = email.split("@")[1]
    count[domain] = count.get(domain, 0) + 1
print(count)
    