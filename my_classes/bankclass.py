


class BankAccount:
    ac_nums=[]
    last_ac_num=999

    def __init__(self,name):

        BankAccount.last_ac_num+=1
        self.account_number=BankAccount.last_ac_num
        BankAccount.ac_nums.append((BankAccount.last_ac_num))
        self.name=name
        self.balance=0

    def display(self):

        print(f'{self.name} balance is: {self.balance}Toman ')

    def deposit(self):
        amount=float(input('Please enter the currency you want to add to your deposit:'))
        self.balance+=amount
        self.display()

    def withdarw(self):
        amount=float(input('Please enter the amount of deposit you want to get:'))
        if amount>self.balance:
            print(f'You short of money{self.balance-amount}')
        else:
            self.balance-=amount
        self.display()



def main():
    acc1=BankAccount('amiir salehi')
    acc1.display()
    print(f'Your acc num:{acc1.account_number}')
    while True:
        ch_=int(input('For deposit Enter 1 \nFor withdraw Enter 2 \nYour choice:'))
        if ch_ == 1:
            acc1.deposit()
        elif ch_ == 2:
            acc1.withdarw()
        break

if __name__ == '__main__':
    main()
acc2=BankAccount('ali')
print(f'Your acc num:{acc2.account_number}')
