list = []
while True:
  user_input = input("Enter a number: ")
  if user_input == "done":
    break
  try:
    number = int(user_input)
  except:
    print("Invalid input")
    continue
  list.append(number)
biggest = None
smallest = None
for number in list:
  if biggest is None:
    biggest = number
  elif biggest < number:
    biggest = number
  if smallest is None:
    smallest = number
  elif smallest > number:
    smallest = number
print("List: ", list)
print("Smallest: ", smallest)
print("Biggest: ", biggest)