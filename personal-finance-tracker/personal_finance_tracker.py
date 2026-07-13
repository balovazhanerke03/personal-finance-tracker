import json


class Finance:
    def __init__(self):
        self.balance = 0
        self.history = []
        self.load_data()


    def save_data(self):
        try:
            with open('finance.json', 'w', encoding='utf-8') as file:
                json.dump({'balance': self.balance, 'history': self.history} , file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            pass

    def load_data(self):
        try:
            with open('finance.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            self.balance = data['balance']
            self.history = data['history']
        except FileNotFoundError:
            pass


    def add_income(self):
        try:
            amount = int(input("Введите доход: "))
            self.balance += amount
            self.history.append("+ {}".format(amount))


            self.save_data()
        except ValueError:
            print("Ошибка: введите число")

    def add_expense(self):
        try:
            amount = int(input("Введите расход: "))
            if amount > self.balance:
                print("Ошибка: недостаточно средств")
                return
            self.balance -= amount
            self.history.append("- {}".format(amount))


            self.save_data()
        except ValueError:
            print("Ошибка: введите число")

    def show_balance(self):
        print("Баланс: {}".format(self.balance))

    def show_history(self):
        if self.history:
            print("История операций:")
            for item in self.history:
                print(item)
        else:
            print("История пуста")


if __name__ == "__main__":
    app = Finance()

    while True:
        print("\n1 - Доход")
        print("2 - Расход")
        print("3 - Баланс")
        print("4 - История")
        print("0 - Выход")

        choice = input("Выбери действие: ")

        if choice == "1":
            app.add_income()
        elif choice == "2":
            app.add_expense()
        elif choice == "3":
            app.show_balance()
        elif choice == "4":
            app.show_history()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор")

