class PayByCard:
    def pay(self, amount):
        print(f"Оплата {amount} картой")

class PayByCash:
    def pay(self, amount):
        print(f"Оплата {amount} наличными")

class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def checkout(self, amount):
        self.strategy.pay(amount)

# Использование
payment = Payment(PayByCard())
payment.checkout(100)

payment = Payment(PayByCash())
payment.checkout(200)
