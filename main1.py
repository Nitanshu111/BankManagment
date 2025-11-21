from pathlib import Path
import random
import string
import json

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open (database) as fs:
                data = json.load(fs.read())

        else:
            print("we are facing some errors")

    except Exception as err:
        print(f"An error occure as {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))

    @staticmethod
    def __accountno():
        alpha =random.choices(string.ascii_letters,k=5)
        digit = random.choices(string.digits,k=4)
        id = alpha+digit
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        d = {
            "name": input("tell your name: "),
            "email": input("tell your email: "),
            "phone no.": int(input("tell your phone no.: ")),
            "Account No.": Bank.__accountno(),
            "pin": int(input("tell your pin: ")),
            "balance": 0
        }
        print(f"please note down your account no. {d['Account No.']}")
        if len(str(d['phone no.'])) != 10:
            print("please review your number")

        elif len(str(d['pin'])) != 4:
            print("please review your pin")
            
        else:
            Bank.data.append(d)
            Bank.__update()

    def depositemoney(self):
        accNo = input("please tell your account number: ")
        pin = int(input("please tell your pin: "))
        user_data = [i for i in Bank.data if i['Account No.']==accNo and i['pin']==pin]
        print(user_data)
        if not user_data:
            print("user not found")
        else:
            amount = int(input("enter amount to be deposited: "))
            if amount <=0:
                print("Insufficient balance")
            elif amount > 10000:
                print("greater than 10000")
            else:
                user_data[0]['balance'] += amount
                Bank.__update()
                print("amount deposited")
                
    def withdrawmoney(self):
        accNo = input("enter your account number: ")
        pin = int(input("enter your pin: "))
        user_data = [i for i in Bank.data if i['Account No.']==accNo and i['pin']==pin]

        if not user_data:
            print("user not found")
        else:
            amount = int(input("enter amount to be credited: "))
            if amount <= 0:
                print("invalid amount")
            elif amount > 10000:
                print("Greater than 10000")
            else:
                if user_data[0]['balance'] < amount:
                    print("Insufficient amount")
                else:
                    user_data[0]['balance'] -= amount
        Bank.__update()


        print("amount credited")


    def viewdetail(self):
        accNo = input("Enter your account number: ")
        pin = int(input("enter your pin: "))
        user_data = [i for i in Bank.data if i['AccountNo']==accNo and i['pin']==pin]

        if not user_data:
            print("user not found")
        else:
            for keys,values in user_data[0].item():
                print(f"{keys}:{values}")

    def updatedetail(self):
        accNo = input("enter your account number: ")
        pin = int(input("enter your pin: "))
        user_data = [i for i in Bank.data if i['AccountNo.']==accNo and i['pin']==pin]
        
        if not user_data:
            print("user not found")
        else:
            print("you cannot changed account number and balance")
            print("now update your detail and skip it if you dont want to update")
            new_data = {
                "name" : input("enter your name: "),
                "email" : input("enter new email: "),
                "phone no" : input("enter your phone number: "), 
                "pin" : input("enter your pin: ")
            }
            
            #handle skip values
            for i in new_data:
                if new_data[i] == "":
                    new_data[i] == user_data[0][i]

            new_data['Account No.'] = user_data[0]['acc']
            new_data['pin'] = user_data[0]['pin']

            for i in user_data:
                if user_data[0][i] == new_data[i]:
                    continue
                else:
                    if new_data[i].isnumeric():
                        user_data[0][i] = int(new_data[i])
                    else:
                        user_data[0][i] = new_data[i]
            Bank.__update()
            print("detail updated")
            print(user_data)
           


user = Bank()
print("press 1 for creating account")
print("press 2 for depositing money")
print("press 3 for withdraw money")
print("pree 4 for details")
print("press 5 for update details")
print("pres 6 for delete account")

check = int(input("tell your choice: "))

if check==1:
    user.createaccount()

if check==2:
    user.depositemoney()

if check==3:
    user.withdrawmoney()

if check==4:
    user.viewdetail()

if check==5:
    user.updatedetail()