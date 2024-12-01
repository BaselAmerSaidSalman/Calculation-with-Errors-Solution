import time
print("Welcome to Calculation")
while True:
  try:
    number = int(input("Please enter a number: "))
    for i in range(1, 11):
      print(f"{number} x {i} = {number * i}")
    break

  except ValueError:
    print("You can only enter a number")

print(f"Multiplication table of {number} is printed")
time.sleep(2)   
