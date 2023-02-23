class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def __str__(self) -> str:
        return ("I am vijay")
    # def get_name(self):
    #     self.name = "Mr." + self.name
    #     return(self.name)


vijay = BankAccount("vijay", 45000)
# print(vijay.get_name())
# print(vijay.name)
# print(vijay.name, vijay.balance)
print(vijay)
