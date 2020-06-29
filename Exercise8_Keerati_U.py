usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "john" and passwordInput == "qwerty":
  print("Login")
  print("----- Product List -----")
  print("1. TypeA  100 THB")
  print("2. TypeB  200 THB")
  print("3. TypeC  300 THB")
  print("4. TypeR  499 THB")
  print("5. TypeS  599 THB")
  item = input("Choose product Number : ")
  if item == "1":
    qty = int(input("quantity : "))
    print("Total price =",100 * qty)
  elif item == "2":
    qty = int(input("quantity : "))
    print("Total price =",200 * qty)
  elif item == "3":
    qty = int(input("quantity : "))
    print("Total price =",300 * qty)
  elif item == "4":
    qty = int(input("quantity : "))
    print("Total price =",499 * qty)
  elif item == "5":
    qty = int(input("quantity : "))
    print("Total price =",599 * qty)
  else:
    print("error")
else:
  print("Incorrect Username or Password")
