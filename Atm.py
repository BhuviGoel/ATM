class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 50000 rupees.")

    def withdrawl(self,amount):
        left_amount = 50000 - amount
        print("You have withdrawn amount "+str(amount) +" rupees. Your remaining balance is "+ str(left_amount) + " rupees.")

    def deposit(self,amount):
        add_amount = 50000 + amount
        print("You have deposited amount "+str(amount) +" rupees. Your new balance is "+ str(add_amount) + " rupees.")    
    
    def bills(self,amount,commodity):
        left_amount = 50000 - amount
        self.commodity = commodity
        print("You have payed amount "+str(amount) +" rupees to " + self.commodity + " company. Your remaining balance is "+ str(left_amount) + " rupees.")    


def main():
    print("Welcome to the ATM!")
    Card_number = input("Please enter your card number: ")
    pin_number  = input("Please enter your pin number: ")

    user =  Atm(Card_number ,pin_number)

    print("Choose your activity")
    print("1.Balance Enquriy     2.Money Withdrawl     3.Deposit Money     4.Pay Bills")
    activity = int(input("Enter activity number: "))

    if (activity == 1):
        user.check_balance()
    elif (activity == 2):
        amount = int(input("Enter the amount you would like to withdraw: "))
        user.withdrawl(amount)
    elif (activity == 3):
        amount = int(input("Enter the amount you would like to deposit: "))
        user.deposit(amount)
    elif (activity == 4):
        commodity = input("Which bill would you like to pay for (Ex: Electricity, Water, etc.): ")
        amount = int(input("Enter the amount you need to pay: "))
        user.bills(amount,commodity)
    else:
        print("Please enter a valid activity number")

main()