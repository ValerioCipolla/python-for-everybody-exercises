score = input("Please enter score between 0.0 and 1.0")
try:
  score = float(score)
except:
  print("Please enter a valid score")
  exit()
if score < 0:
  print("Please enter a valid score")
  exit()
elif score > 1:
  print("Please enter a valid score")
  exit()
if score >= 0.9:
  print("A")
elif score > 0.8:
  print("B")
elif score > 0.7:
  print("C")
elif score > 0.6:
  print("D")
elif score <= 0.6:
  print("F")
