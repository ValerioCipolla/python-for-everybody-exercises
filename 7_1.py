fname = input("Enter a file name: ")
try:
  fhand = open(fname)
except:
  print("Can't open file", fname)
  quit()
for line in fhand:
  print(line.upper())