fhand = open("words.txt")
dict = dict()
for line in fhand:
  words = line.split()
  for word in words:
    if word not in dict:
      dict[word] = "present"
print(dict)