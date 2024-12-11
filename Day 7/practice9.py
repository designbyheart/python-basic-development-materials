class CurrencyConverter:
    @staticmethod
    def get_currency_amount(account, amount, currency):
        if currency == account.currency:
            return amount
        elif currency == "EUR" and account.currency == "RSD":
            return amount * 118
        
        elif currency == "RSD" and account.currency == "EUR":
            return amount // 118
        
        return 0

class BankAccount:

    def __init__(self, account_number, name, balance=0, currency="RSD"):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def __str__(self):
        return f"Account no. {self.account_number}, Name: {self.name}, Balance: {self.balance} {self.currency}"
    
    # define a method which will take amount, 
    # convert amount to proper value (according to currency)
    # deposit that amount into the account

	# 1. definisi funkciju koja se zove konvertuj valutu
	# 2. napravi uslov koju valutu ubacujemo
		# 2.a: ako je nalog dinarski i hocemo da ubacimo dinare
		# 2.b: ako je nalog dinarski i hocemo da ubacimo eure, konvertuj eure u dinare
		# 2.c: ako je nalog euro i hocemo da ubacimo dinare, konvertuj u eure
	# 3. promeni stanje sa novim iznosom
	
  

acct1 = BankAccount("1234", "John Doe", 500)
acct2 = BankAccount("2345", "Jane Doe")
acct3 = BankAccount("3456", "Pedja Jevtic", 10000000, "EUR")

newAmount = CurrencyConverter.get_currency_amount(acct3, 1000, "RSD")
acct3.deposit(newAmount)

print(newAmount)
print(acct3)
# "Account no. 3456, Name: Pedja Jevtic, Balance: 10000000"