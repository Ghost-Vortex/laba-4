class MyCollection:
    def __init__(self):
        self.data = [1, 2, 3]

    def __iter__(self):
        return iter(self.data)

collection = MyCollection()

for item in collection:
    print(item)
