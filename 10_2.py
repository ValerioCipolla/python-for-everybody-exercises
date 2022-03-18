fname = input("Please enter a file name: ")
try: 
  fhand = open(fname)
except: 
  print("Could not open file", fname)
  quit()
counts = dict()
for line in fhand:
  if line.startswith("From "):
    time = line.split()[5]
    hour = time.split(":")[0]
    counts[hour] = counts.get(hour, 0) + 1
list = list()
for k, v in counts.items():
  newtup = (k, v)
  list.append(newtup)
sorted_list = sorted(list)
for tup in sorted_list:
  print(tup[0], tup[1])

    