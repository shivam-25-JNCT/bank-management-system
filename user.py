import database

def depositAmount():
    accNum=input("Enter the account Number :  ")
    amount=input ("Enter the amount ")
    if database.deposit(accNum, amount):
       print("Amount Deposited Successfully")
    else:
       print("Account Not Found")


# =================================================
def withdrawAmount():
    acountNumber=int(input("Enter the account Number :  "))
    amount=int(input ("Enter the amount "))
    if database.withdraw(acountNumber,amount):
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")  
#  ============================================ check balance
def check_balance():
    accNum=input("Enter the Nccount Number : ")
    val = database.checkBalance(accNum)

    if val:
        print(f"Hii {val[0]}")
        print(f"Your Total Account Balance is {val[1]}")
    else:
        print("Account Not Found")
# =====================================
def change_profile():
    accNum=input("Enter the Account Numebr : ")
    newName=input("Emter the new Name : ")
    while True:
        newEmail=input("Emter the new Email : ")
        if not newEmail.endswith("@gmail.com"):
           print("Invalid Email")
        else:
          database.updateProfile(accNum,newName,newEmail)
          break

    print("Profile Updated Successfully")
    #  [===============================================]
def update_password():
    accNum=input("Enter the Account Number : ")
    while True:

        print("Password must be 4-8 characters")

        newPass = input("Enter New Password: ")

        if 4 <= len(newPass) <= 8:

            database.updatePassword(accNum,newPass)

            print("Password Updated Successfully")

            break

        else:

            print("Invalid Password Length")