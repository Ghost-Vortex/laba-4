class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using credit card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self, amount):
        return self.strategy.pay(amount)

if __name__ == "__main__":
    context = PaymentContext(CreditCardPayment())
    print(context.pay(100))

    context.strategy = PayPalPayment()
    print(context.pay(200))
