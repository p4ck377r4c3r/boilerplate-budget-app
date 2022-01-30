class Category:
  def __init__(self, name):
    self.name = name
    self.balance = 0.0
    self.ledger = []

  def __repr__(self):
    l = f"{self.name:*^30}\n"
    acc = 0

    for item in self.ledger:
      l += f"{item['description']}{item['amount']:>{30-len(item['description'])}}\n"
      acc += item['amount']


    l += f"Total: {acc}\n"
    return (l)
  
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
  pass
