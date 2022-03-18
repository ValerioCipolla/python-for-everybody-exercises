fname = input("Please enter a file name: ")
try:
  fhand = open(fname)
except: 
  print("Could not open file", fname)
  quit()
counts = dict()
for line in fhand:
  if line.startswith("From "):
    email = line.split()[1]
    counts[email] = counts.get(email, 0) + 1
list = list()
for k, v in counts.items():
  newtup = (v, k)
  list.append(newtup)
sorted_list = sorted(list, reverse=True)
most_commits = sorted_list[0]
print(most_commits[1], most_commits[0])