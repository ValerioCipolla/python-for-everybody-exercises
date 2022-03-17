unique_words = list()
fname = input("Enter file name: ")
try:
  fhand = open(fname)
except:
  print("Could not open file", fname)
  quit()
for line in fhand:
  words = line.split()
  for word in words:
    if word not in unique_words:
      unique_words.append(word)
unique_words.sort()
print(unique_words)