age = int (input("Enter Your Age : "))
if age >= 15:
    username = input("Enter Username : ")
    password = input("Enter Password : ")

    if username == 'abc' and password == '1234':
        print("Login Suceessfully")
    elif username == 'abc':
        print("Invalid Password")
    elif password == '1234':
        print("Invalid Username")
    else :
        print("Both Username & Password are Invalid")
else :
    print("Age Must be more than 18")