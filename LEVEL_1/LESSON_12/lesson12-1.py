#1. Описать класс "Банковский счет", атрибуты у которого:
#   имя аккаунта - str
#   уникальный id (uuid)
#   баланс float
#   транзакции (список)
#   Методы
#    депозит средств
#    вывод средств
#    получить баланс

#   При изменении баланса записывать в транзакции (сумма, тип операции, текущая_дата)
#   * доп. добавить и учитывать банковские комиссии (1%)

class Bank_account():
    """Банковский счет."""
    def __init__(self, str, uuid, float, list):
        """Инициализирует атрибуты str, uuid, float, list."""
        self.str = str
        self.uuid = uuid
        self.float = float
        self.list = list
    def deposit_of_funds(self):
        """Депозит средств."""
        print(f"{self.str} is now deposit_of_funds.")
    def withdrawal_of_funds(self):
        """Вывод средств."""
        print(f"{self.list} is now withdrawal_of_funds")
    def get_balance(self):
        """Получить баланс."""
        print(f"{self.float} is now balance")