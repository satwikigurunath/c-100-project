class atm(object):
    def __init__(self,cardNumber,pin):
        
        self.cardNumber=cardNumber
        self.pin=pin                                  

    def chekBalance(self):
        print('Your balance is $1562')

    def withdrawal(self,amount):
        newAmount=1562-amount
        print("you have withdrawn "+str(amount))
        print("your remaining balance is "+str(newAmount))

def main():
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number:- ")

    new_user =  atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()
    