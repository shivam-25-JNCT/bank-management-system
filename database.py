import sqlite3
conn = sqlite3.connect("bank.db")

# conn.execute("""
# CREATE TABLE User(
             
#     id INTEGER PRIMARY KEY AUTOINCREMENT ,
#     name TEXT,
#     email TEXT,
#     password TEXT,
#     AccountNum INTEGER UNIQUE,
#     balance INTEGER
# )
# """)

def insert_data_in_userTable(name, email, password, accNum, balance):
    conn.execute(
        "INSERT INTO User (name,email,password,accountNum,balance) VALUES (?,?,?,?,?)",
        (name, email, password, accNum, balance)
    )
    conn.commit()

def insert_data_in_transection(senderAcc,recAcc,Amount,date):
    conn.execute("INSERT INTO Transections (sender_acc,receiver_acc,amount,date) VAlUES (?,?,?,?) ",(senderAcc,recAcc,Amount,date)) 
    conn.commit()
    

def delete(self , name,accountNo ):
    conn.execute("DELETE FROM User where name=? and accoundNo=? ",(self.name,self.accountNo))

def fetchData(self,name):
    conn.execute("SELECT name,accoundNo,balence FROM User where name =?",(self.name))

def login(email,password):
    val =conn.execute("SELECT * FROM User where email=? AND password=?",(email,password))
    user=val.fetchone()
    return user
#  deposit data

def deposit(accNum, amount):

    cursor = conn.execute(
        "UPDATE User SET balance = balance + ? WHERE AccountNum=?",
        (amount, accNum)
    )

    if cursor.rowcount == 0:
        return False

    conn.commit()
    return True

    # withdraw
def withdraw(accNum, amount):
    val = conn.execute(
        "SELECT balance FROM User WHERE AccountNum=?",
        (accNum,)
    )
    result = val.fetchone()

    if result is None:
        return False
        
    balance = result[0]

    if amount <= balance:
        conn.execute(
            "UPDATE User SET balance = balance - ? WHERE AccountNum=?",
            (amount, accNum)
        )
        conn.commit()
        return True

    else:

        return False
   
def checkBalance (accNumber):
    cursor= conn.execute("SELECT name , balance FROM User WHERE AccountNum= ?",(accNumber,))
    return cursor.fetchone()

def updatePassword(accNum,newpass):
    conn.execute("UPDATE User SET password = ? where AccountNum = ?",(newpass,accNum))
    conn.commit()

    # ========================================
def updateProfile(accNum,newName,newEmail):
    conn.execute("UPDATE User SET name = ? , email=?  where AccountNum = ?",(newName,newEmail,accNum))
    conn.commit()

    # ======================================
# ===================================================
def transfer_money(senderAcc,receiverAcc,balance):
    if balance <=0:
        return False
    
    if senderAcc ==receiverAcc :
        return False
    
    senderData=conn.execute("SELECT balance FROM User WHERE AccountNum=? ",(senderAcc,))
    receiverData=conn.execute("SELECT balance FROM User WHERE AccountNum=? ",(receiverAcc,))

    result1=senderData.fetchone()
    result2 = receiverData.fetchone()
    
    if result1 is None or result2 is None:
       return False
    userBalance=result1[0]
   
    if balance <= userBalance:
            conn.execute("UPDATE User SET balance = balance - ? WHERE  AccountNum = ? ",(balance,senderAcc))
    
            conn.execute("UPDATE User SET balance = balance + ? WHERE  AccountNum = ? ",(balance,receiverAcc))

            conn.commit()
            return True
    else:
       return False
    
def check_accont(accNum):
    val=conn.execute("SELECT * FROM User WHERE AccountNum=?",(accNum,))
    return val.fetchone()

def transection_history():
    cursor=conn.execute("SELECT * FROM Transections ORDER BY id DESC LIMIT 5 ")
    return cursor.fetchall()

