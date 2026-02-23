class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)

class Level1(Handler):
    def handle(self, request):
        if request == "simple":
            print("Решено на 1 уровне")
        else:
            super().handle(request)

class Level2(Handler):
    def handle(self, request):
        if request == "hard":
            print("Решено на 2 уровне")
        else:
            super().handle(request)

chain = Level1(Level2())
chain.handle("hard")
