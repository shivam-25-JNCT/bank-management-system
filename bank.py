import  database 
import user
from datetime import datetime
import random
# import database
class Bank:
        
    def createAccount(self):
        self.name = input("Enter Name : ")
        while True:
            self.email = input("Enter Email : ")
            if self.email.endswith("@gmail.com"):
                 break
            else:
                print("Invalid Email ")
        while True:
            self.password = input("Enter Password between (6-12) : ")
            if len(self.password) >=6 and len(self.password) <=12 :
                break
            else:
                print("Invalid Password")
        self.balance = int(input("Enter Initial Balance : "))

        while True:
            self.accNum=  random.randint(10000000000, 99999999999)
            if not database.check_accont(self.accNum):
                break

        database.insert_data_in_userTable(self.name,self.email,self.password,self.accNum,self.balance)
        print("\nAccount Created Successfully ")
        print("Your Account Number is : ",self.accNum)

        # Login ===============================
    def login(self):
        while True:
            self.email=input("enter email id : ")
            self.password=input("enter email password : ")
        
            user = database.login(self.email,self.password)
            return user
        
    
#   transfer data==================================
    def transfer_money(self):
            while True:
                senderAcc=int(input("Enter the Senders Account Number : "))
                reciverAcc=int(input("Enter the reciever Acoount Number : "))
                varify=int (input("please varify the reciever Acoount Number : "))
                amount=int(input("Enter the Amount : "))
            
                if reciverAcc == varify :
                    data=database.transfer_money(senderAcc,reciverAcc,amount)

                    database.insert_data_in_transection(senderAcc,reciverAcc,amount,datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
                    return data
                else:
                    print("Account Number doesn't match") 
                 
            

     
    def transaction_history(self):
        data=database.transection_history()
        for row in data:

          print("--------------------------")
          print("Sender :", row[1])
          print("Receiver :", row[2])
          print("Amount :", row[3])
          print("Date :", row[4])

    def Menu(self):
       while True:
        self.userInput= int(input('''
1. Deposit Amount
2. Withdraw Amount
3. Check Balance
4. Transfer Amount
5. Transaction History Last 5 
6. Change Password
7. Update Profile
8. Log Out..
''') )   
        match self.userInput:
            case 1:
                user.depositAmount()
            case 2:
                user.withdrawAmount()
            case 3:
                
                user.check_balance()
            case 4:
                if self.transfer_money():
                    print("Money successfully Transfer ")
            case 5:
                self.transaction_history()
            case 6:
                user.update_password()
            case 7:
                user.change_profile()
            case 8:
                break
