class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self.currency = currency
    
    def convert_to_usd(self):
        return self._amount / 3.4
    
    def __repr__(self):
        return f"Money({self._amount}, {self.currency})"
    
    @classmethod
    def from_usd(cls, money):
        return Money(money._amount * 3.4, "pln")
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        print ("Nie wolno")


        


money_pln = Money(3, "PLN")
money_pln.amount = 50


money_will_be = Money(2, "USD")

print(money_pln)
print(money_pln.convert_to_usd())
print(Money.from_usd(money_will_be))
