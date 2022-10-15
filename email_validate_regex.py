import re
e =input("Enter the email:")
condition = "^[a-zA-Z]+[\._]?[a-zA-Z0-9]+[@]\w+[a-z]+[.]\w+[a-z]{2,3}$"
if re.search(condition,e):
    print("Right Email")
else:print("Wrong Email")