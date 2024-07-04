def calculate():
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  op = input("Choose operation(+, -, *, /): ")

  if op== "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
  elif op== "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
  elif op== "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
  elif op == "/":
      result = num1 / num2
      print(f"{num1} / {num2} = {result}")
  else:
    print("Invalid operation")

calculate()