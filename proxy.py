class RealService:
    def request(self):
        print("Настоящий сервис работает")

class Proxy:
    def __init__(self):
        self.real_service = RealService()

    def request(self):
        print("Проверка доступа...")
        self.real_service.request()

proxy = Proxy()
proxy.request()
