fname = input("Enter a file name: ")
try:
  fhand = open(fname)
except: 
  print("Could not open file", fname)
  exit()
count = dict()
for line in fhand:
  if line.startswith("From "):
    words = line.split()
    day_of_week = words[2]
    count[day_of_week] = count.get(day_of_week, 0) + 1
print(count)
    
