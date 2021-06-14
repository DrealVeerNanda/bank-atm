class Atm(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    def CashWithdrawal(self):
        print("withdrawing cash")

    def BalanceCheck(self):
        print("your balance is 2000$")

    

Atm = Atm( "1234", "4321")
print(Atm.card_number)