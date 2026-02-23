class OldSystem:
    def old_method(self):
        return "Старый метод"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        return self.old_system.old_method()

old = OldSystem()
adapter = Adapter(old)

print(adapter.new_method())
