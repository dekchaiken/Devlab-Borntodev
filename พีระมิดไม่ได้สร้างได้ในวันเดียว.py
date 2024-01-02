rows = int(input(""))

for i in range(1, rows+1):
  spaces = rows - i
  asterisks = 2 * i - 1
  print(" " * spaces + "*" * asterisks)