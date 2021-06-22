import mysql.connector
import re
import random

con = mysql.connector.connect(host = "localhost",user="root",password="",database="task2_db")
mycursor = con.cursor()

def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return(True)
    else:
        return(False)

class password(object):
    def __init__(self, username = ''):
        self.username = username

    def __lower(self):
        lower = any(passwd.islower() for passwd in self.username)
        return lower

    def __upper(self):
        upper = any(passwd.isupper() for passwd in self.username)
        return upper

    def __digit(self):
        digit = any(passwd.isdigit() for passwd in  self.username)
        return digit
    def getPassword(self):
        return(self.username)
    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()

        length = len(self.username)
        report =  lower and upper and digit and length >= 5 and length <= 16

        if report:
            return True
        else:
            return False

def register(Username,passwd): 
    if check(Username):
        if passwd.validate():
            sql = "INSERT INTO user_details (Username,Password) VALUES (%s,%s)"
            val = (Username,passwd.getPassword())   
            mycursor.execute(sql,val)
            con.commit()
            print(".....User Created Successfully.....")
        else:
            print("Password does't match the criteria please retry...")
    else:
        print("Please Enter a valid mail ID and continue...")
        print(".........Welcome to My web.........")

def login(Username,passwd):
    sql = "Select * from  user_details where Username = '"+ Username +"'"
    try:
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result[2]==passwd:
            return True
        else:
            return False
    except:
        return False
def forgotpwd(Username):
    sql = "Select * from  user_details where Username =  '"+ Username+"'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    return result[2]
print(".........Welcome to My web.........")


while True:
    print("CHOICES")
    print("1.Register")
    print("2.Login")
    print("3.Exit")
    choice=int(input("Enter Your Choice: "))

    if choice == 1:
        print("............Please Register your details Here!..............")
        Username=input("Enter Username: ")
        passwd = password(input("Enter Password : "))   
        register(Username,passwd)  
    elif choice == 2:
        print("................Please Login Here!.................")
        Username=input("Enter Username: ")
        passwd=input("Enter Password: ")
        if login(Username,passwd):
            print(" Logged in Sucessfully! ")
        else:
            print("Please Enter a valid user name or password: ")
            print("1.Login Again")
            print("2.Forgot Password")
            print("3.Register")
            print("4.Exit")
            relog=int(input("Please enter Your Choice: "))
            if relog==1:
                Username=input("Enter Username: ")
                passwd=input("Enter Password: ")
                if login(Username,passwd):
                    print("Logged in Sucessfully")
                else:
                    print("You have reached maximum attempts try to relogin")
                    continue
            elif relog==2:

                randint=random.randint(1000, 1999)
                print(randint)
                if int(input("Please type the above Number to continue: "))==randint:
                    print("Your Password is: "+forgotpwd(Username))
                else:
                    print(" Entered Number is Wrong :")
                    continue
            elif relog==3:
                if str(input("Register the same username and password (y/n): "))=="y":
                    register(Username,password(passwd))
                else:
                    Username=input("Enter Username: ")
                    passwd=password(input("Enter Password: "))
                    register(Username,passwd)
            elif relog==4:
                print("Thanks For Using the web ")
                break
            else:
                print("Wrong option selected going to main menu")

    elif choice == 3:
        print("Thanks For Using the web")
        break
    else:
        print("Please enter a correct option and continue")

