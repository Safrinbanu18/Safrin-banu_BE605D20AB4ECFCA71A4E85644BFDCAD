def fact(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * fact(n - 1)


num = int(input("Enter Number:"))
if (num < 0):
  print("Factorial  doesn't exit negative value")
else:
  print(" Factorial is:", fact(num))
