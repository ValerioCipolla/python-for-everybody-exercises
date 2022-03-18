fname = input("Enter a file name: ")
try:
  fhand = open(fname)
except: 
  print("Couldn't open file", fname)
  exit()
count = dict()
for line in fhand:
  if line.startswith("From "):
    words = line.split()
    email = words[1]
    count[email] = count.get(email, 0) + 1
max_address = None
max_count = None
for address, count in count.items():
  if max_count is None or max_count < count:
    max_address = address
    max_count = count
print(max_address, max_count)