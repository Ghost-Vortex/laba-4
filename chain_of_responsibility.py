class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)

class NumberHandler(Handler):
    def handle(self, request):
        if request < 10:
            return f"Handled {request} by NumberHandler"
        else:
            return super().handle(request)

class LargeNumberHandler(Handler):
    def handle(self, request):
        return f"Handled {request} by LargeNumberHandler"

if __name__ == "__main__":
    handler_chain = NumberHandler(LargeNumberHandler())
    print(handler_chain.handle(5))
    print(handler_chain.handle(50))
