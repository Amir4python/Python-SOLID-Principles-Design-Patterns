class BankAccount:
    def __init__(self,accountId,balance):
        self.accountId=accountId
        self._balance=balance

    def set_balance(self,balance):
        if balance<0:
            raise ValueError("Balance cannot be negative")
        self._balance=balance
    def get_balance(self):
        return self._balance


    def desposit(self,amount):
        if amount<0:
            raise ValueError("Amount cannot be negative")
        self._balance+=amount

    def withdraw(self,amount):
        if amount<0:
            raise ValueError("Amount cannot be negative")
        if amount>self._balance:
            raise ValueError("Insufficient balance")
        self._balance-=amount

if __name__=="__main__":
    AxisAccount=BankAccount('AXIS_001',10000)
   

    AxisAccount.set_balance(6000)
    print('initial',AxisAccount.get_balance())
    AxisAccount.desposit(5000)
    print('after 5000 deposit')
    print(AxisAccount.get_balance())

    AxisAccount.withdraw(10000)
    print('after 10000 withdraw')
    print(AxisAccount.get_balance())