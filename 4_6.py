def computepay(hours, rate):
  try:
    hours = float(hours)
    rate = float(rate)
  except:
    return("Please enter numeric input")
  overtime_hours = hours - 40
  overtime_rate = rate * 1.5
  if overtime_hours > 0:
    hours = hours - overtime_hours
    pay = (hours * rate) + (overtime_hours * overtime_rate)
  else:
    pay = hours * rate
  return pay

hours = input("Enter hours")
rate = input("Enter rate")
print(computepay(hours, rate))
