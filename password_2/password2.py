import random

def checkPassword(password):
    if(len(password) != 47):
      return False
    newPass = list(password)
    for i in range(0,9):
      newPass[i] = password[i]
      print(newPass)
    for i in range(9,24):
      newPass[i] = password[32-i]
      print(newPass)
    for i in range(24,47,2):
      newPass[i] = password[70-i]
      print(newPass)
    for i in range(45,25,-2):
      newPass[i] = password[i]
      print(newPass)
    password = "".join(newPass);
    print(password)
    return password == "CYCTF{ju$@rcs_3l771l_@_t}bd3cfdr0y_u0t__03_0l3m"

password = input("Enter password: ")
if(checkPassword(password)):
  print("PASSWORD ACCEPTED\n")
else:
  print("PASSWORD DENIED\n")


