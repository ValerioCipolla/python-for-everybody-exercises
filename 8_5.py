fname = input("Enter file name: ")
try:
  fhand = open(fname)
except: 
  print("Couldn't open file", fname)
  quit()
count = 0
for line in fhand:
  if line.startswith("From "):
    count = count + 1
    words = line.split()
    sender = words[1]
    print(sender)
print (f"There were {count} lines with From as the first word")