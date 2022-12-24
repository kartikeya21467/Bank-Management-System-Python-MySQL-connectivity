
import datetime
import mysql.connector
from random import randint

print("***********************************************")
print("BANK MANAGEMENT SYSTEM")
print("***********************************************")

print("===============================")
print(" ----Welcome to National Bank----       ")
print("***********************************************")
print("=<< 1. Open a new account                >>=")
print("=<< 2. Withdraw Money                       >>=")
print("=<< 3. Deposit Money                         >>=")
print("=<< 4. Balance Enquiry                       >>=")
print("=<< 5. Modify Account                         >>=")
print("=<< 6. Close Account                          >>=")
print("=<< 7. Exit/Quit                                     >>=")
print("***********************************************")
    
#Creating Table
mydb= mysql.connector.connect(host="localhost",user="root",password="Keshu_2003",\
                                                          database="Bank_Database")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE Account_Details(Account_Number  int(6) , Name varchar(15),\
                                     DOB date,City char(8), Phone_Number int(11),Balance int(10) )")

def Create_Account():
    username=input("Enter the Account holder name: ")
    yob=int(input("Enter year of birth: "))
    mob=int(input("Enter month of birth: "))
    d_ob=int(input("Enter date of birth: "))
    DOB=datetime.datetime(yob,mob,d_ob)
    city=input("Enter your City: ")
    ph_no=int(input("Enter Phone Number: "))
    balance=0
    acc_no=randint(10**5,(10**6)-1)
    mycursor.execute("INSERT INTO Account_Details VALUES\
                     (%s,%s,%s,%s,%s,%s)",(acc_no, username,DOB, city, ph_no,balance))
    mydb.commit()
    print("----New account created successfully !----")
    print("Your Account Number: ",acc_no)
    print("Your Account Balance: ",balance)
    





def Withdraw_Money():
    acc_no=int(input("Enter your Account Number: "))
    mon=int(input("Enter the Amount you want to withdraw: "))
    mycursor.execute("select * from Account_Details where Account_Number=%s",(acc_no,))
    myrecords=mycursor.fetchall()
    for row in myrecords:
        balance=row[5]
        
    if mon>balance:
        print ("Not enough Balance")
    else:
        balance-=mon
        print("Amount Withdrawn: ",mon)
        print("Your Account Balance: ",balance)
    mycursor.execute("Update Account_Details set Balance=%s where\
                                    Account_Number=%s",(balance,acc_no))
    mydb.commit()




def Deposit_Money():
    acc_no=int(input("Enter Your Account Number: "))
    mon=int(input("Enter Amount of money you want to Deposit: "))
    mycursor.execute("select * from Account_Details where Account_Number=%s",(acc_no,))
    myrecords=mycursor.fetchall()
    for row in myrecords:
        balance=row[5]
    
    mycursor.execute("Update Account_Details set Balance=Balance+%s where\
                                     Account_Number=%s",(mon,acc_no))
    mydb.commit()
    balance=balance+mon
    print("Amount deposited: ",mon)
    print("Your Account Balance: ",balance)


def Balance_Enquiry():
    acc_number=int(input('enter your account number'))
    mycursor.execute('select Account_Number,Balance from Account_Details where\
                                    Account_Number=%s',(acc_number,))
    record=mycursor.fetchall()
    for row in record:
        print('account number : ',row[0])
        print('current balance: ',row[1])

def Close_Account():
     acc_number=int(input('enter your account number'))
     mycursor.execute('DELETE from Account_Details where Account_Number=%s',(acc_number,))
     mydb.commit()
     print('account closed')
     
def Modify_Account():
    acc_number=int(input('enter your account number'))
    print('''1) modifiy yor name
             2) modify your date of birth
             3) modify your city of residence
             4) modify your phone number''')
    x=int(input('enter your choice'))
    if x==1:
         newname=input("Enter the correct Account holder name: ")
         mycursor.execute('update Account_Details set Name=%s where\
                                         Account_Number=%s',(newname,acc_number))
         mydb.commit()
    if x==2:
         yob=int(input("Enter year of birth: "))
         mob=int(input("Enter month of birth: "))
         d_ob=int(input("Enter date of birth: "))
         DOB1=datetime.datetime(yob,mob,d_ob)
         mycursor.execute('update Account_Details set DOB=%s where\
                                          Account_Number=%s',(DOB1,acc_number))
         mydb.commit()
    if x==3:
         city=input("Enter your City: ")
         mycursor.execute('update Account_Details set City=%s where\
                                         Account_Number=%s',(city,acc_number))
         mydb.commit()
    if x==4:
         ph_no=int(input("Enter Phone Number: "))
         mycursor.execute('update Account_Details set Phone_Number=%s where\
                                        Account_Number=%s',(ph_no,acc_number))
         mydb.commit()
    print('account modified')
    
ch="y"
while ch=="y":
    choicenumber = input("Select your choice number from the above menu : ")
    if choicenumber == "1":
        print("Choice number 1 is selected by the customer")
        Create_Account()
        
    elif choicenumber =="2":
        print("Choice number 2 is selected by the customer")
        Withdraw_Money()

    elif choicenumber== "3":
        print("Choice number 3 is selected by the customer")
        Deposit_Money()

    elif choicenumber== "4":
        print("Choice number 4 is selected by the customer")
        Balance_Enquiry()

    elif choicenumber== "5":
        print("Choice number 5 is selected by the customer")
        Modify_Account()

    elif choicenumber== "6":
        print("Choice number 6 is selected by the customer")
        Close_Account()

    elif choiceNumber == "7":
        print("Choice number 7 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        
    else:
        print("Invalid option selected by the customer")
        print("Please Try again!")
    
    ch=input("Do you want to continue or not?(y for yes, n for no)  :")    
    
    

    
    
