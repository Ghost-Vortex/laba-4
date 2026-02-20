class MyCollection:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)

if __name__ == "__main__":
    collection = MyCollection([1, 2, 3])
    for item in collection:
        print(item)
