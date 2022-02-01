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

    output = ledger + items +f"Total: {total:.2f}"

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
  percents = {}
  accounts = []

  for category in categories:
    percents[category.name] = 0
    for deduction in  category.ledger:
      if deduction['amount'] < 0:
        percents[category.name] += deduction['amount']
    
    percents[category.name] = -percents[category.name]
    total += percents[category.name]
  
  for percent in percents:
    percents[percent] = int(percents[percent] * 100 / total)

  for n in range(100, -1, -10):
    output += f"{n:>3}| "
    for percent in percents:
      if percents[percent] >= n:
        output += "o  "
      else:
        output += "   "
    output += "\n"

  output += " " * 4 + "-" * (len(percents) * 3 + 1) + '\n'
  
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
      vertical_name = vertical_name + " \n"
    else:
      vertical_name = vertical_name + " "
    
    output = output + "    " + vertical_name

  return output
