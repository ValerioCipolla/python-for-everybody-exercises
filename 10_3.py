import string

alphabet = list(string.ascii_lowercase)
counts = dict()
tuples_list = list()

fname = input("Enter file name: ")
try:
  fhand = open(fname)
except: 
  print("Could not open file", fname)
  exit()
for line in fhand:
  line = line.split()
  for word in line:
    letters = list(word)
    for letter in letters:
      if letter.lower() in alphabet:
        counts[letter.lower()] = counts.get(letter.lower(), 0) + 1
for k, v in counts.items():
  newtup = (v, k)
  tuples_list.append(newtup)
sorted_list = sorted(tuples_list, reverse=True)
for tuple in sorted_list:
  print(f"{tuple[1]}: {tuple[0]}")

