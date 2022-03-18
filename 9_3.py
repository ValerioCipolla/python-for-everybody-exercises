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
print(count)