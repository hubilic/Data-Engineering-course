class PaymentError(Exception):
    pass

class CardDeclined(PaymentError):
    pass

class InsufficientFunds(CardDeclined):
    pass

class FraudSuspected(CardDeclined):
    pass

class NetworkError(PaymentError):
    pass

try:
    raise InsufficientFunds("Not enough money")
except CardDeclined as e:
    print(f"Card declined: {e}")

try:
    raise NetworkError("Network is down")
except PaymentError as e:
    print(f"Payment error: {e}")
