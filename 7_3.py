fname = input("Enter a file name: ")
if fname == "na na boo boo":
  print("NA NA BOO BOO TO YOU - You have been punk'd!")
  quit()
try:
  fhand = open(fname)
except:
  print("Can't open file", fname)
  quit()
count = 0
for line in fhand:
  count = count + 1
print(f"There were {count} lines in {fname}")