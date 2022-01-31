class Category:
  def __init__(self, name):
    self.name = name
    self.balance = 0.0
    self.ledger = []

  def __str__(self):
    ledger = f"{self.name:*^30}\n"
    items = ""
    total = 0

    for item in self.ledger:
      amount = f"{item['amount']:.2f}"
      description = f"{item['description'][:29-len(str(amount))]}"
      items += f"{description}{amount:>{30-len(description)}}\n"
      total += item['amount']

    output = ledger + items +"Total: "+str(total)

    return (output)
  
  def deposit(self, amount, *args):
    self.balance += amount

    description = args[0] if args else ""

    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, *args):
    can_withdraw = self.check_funds(amount)
    
    description = args[0] if args else ""

    if can_withdraw:
      self.balance -= amount
      self.ledger.append({"amount": -amount, "description": description})

    return can_withdraw

  def get_balance(self):
    return self.balance

  def transfer(self, amount, account):
    can_transfer = self.check_funds(amount)
    
    if can_transfer:
      self.withdraw(amount, f"Transfer to {account.name}")
      account.deposit(amount, f"Transfer from {self.name}")
    
    return can_transfer

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    return True

def create_spend_chart(categories):
  output = "Percentage spent by category\n"
  total = 0
  percents = []
  accounts = []

  for category in categories:
    total = total + category.get_balance()
  
  for category in categories:
    percents.append(category.get_balance() * 100 / total)

  for n in range(100, -1, -10):
    output += f"{n:>3}|"
    for percent in percents:
      if percent >= n:
        output += " o "
      else:
        output += "   "
    output += "\n"

  output += f"    -{(len(percents) * 3) * '-'}\n"
  
  for category in categories:
    accounts.append(list(category.name))
  
  account_copy = accounts.copy()

  while len(account_copy) > 0:
    vertical_name = ""

    for account in accounts:
      vertical_name = vertical_name + " " + account[0] + " "
      if len(account) >= 1 and account[0] != " ":
        account.remove(account[0])
        if len(account) == 0:
          account.append(" ")
          account_copy.remove(account_copy[0])

    if(len(account_copy) > 0):
      vertical_name = vertical_name + "\n"
    
    output = output + "    " + vertical_name
  
  return output
