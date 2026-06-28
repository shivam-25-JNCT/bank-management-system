from bank import Bank
b1 = Bank()

while True:

    a = int(input('''
==== BANKING MANAGEMENT SYSTEM ====

1 Create Account
2 Login
3 Exit

'''))

    if a == 1:
        b1.createAccount()

    elif a == 2:

        data = b1.login()

        if data:
            print("Welcome", data[1])   # agar data[1] name hai

            b1.Menu()

        else:
            print("Invalid Credentials, Try Again")
            
    elif a == 3:
        break

    else:
        print("Invalid Number Please Enter Valid Number")