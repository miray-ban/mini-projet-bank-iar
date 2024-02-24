import json

class Client:
    def __init__(self, username, cin, password):
        self.username = username
        self.cin = cin
        self.password = password
        self.accounts = []

    def add_account(self, account_num):
        self.accounts.append(account_num)

    def remove_account(self, account_num):
        if account_num in self.accounts:
            self.accounts.remove(account_num)
            print(f"Account {account_num} removed successfully")
        else:
            print("Account not found in user's accounts")
    def aff_client(self):
        print(f"username:{self.username} cin : {self.cin}")
    def transfert(self, rib, amount):
        for account in self.accounts:
            if account.rib == rib:
                if account.solde >= amount:
                    account.solde -= amount
                    print(f"Transferred {amount} units from account {account.rib} to RIB: {rib}")
                else:
                    print("Insufficient balance for transfer")
                return
        print("Recipient account not found")


