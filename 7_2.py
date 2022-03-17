fname = input("Enter a file name: ")
try:
  fhand = open(fname)
except:
  print("Can't open file", fname)
  quit()

count = 0
total = 0
for line in fhand:
  if line.startswith("X-DSPAM-Confidence:"):
    zeroChar = line.find("0")
    try:
     spam_confidence = float(line[zeroChar:])
    except:
      print("Error")
      quit()
    total = total + spam_confidence
    count = count + 1
average_spam_confidence = total / count
print ("Average spam confidence:", round(average_spam_confidence, 12))
  
