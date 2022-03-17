total = 0
count = 0
while True:
  user_input = input("Enter a number: ")
  if user_input == "done":
    break
  try:
    number = int(user_input)
  except:
    print("Invalid input")
    continue
  total = int(total + number)
  count = count + 1
  average = total / count
print(total, count, average)
