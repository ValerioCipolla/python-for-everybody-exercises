numbers = list()
while True:
  user_input = input("Enter a number: ")
  if user_input == "done":
    break
  try: 
    int(user_input)
  except:
    print("Invalid input, try again")
    continue
  numbers.append(user_input)
max = max(numbers)
min = min(numbers)
print(f"Maximum: {max}\nMinimum: {min}")