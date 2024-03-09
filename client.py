import json
from Account import Account
from Transaction import Transaction
class Client:
    def __init__(self, username, cin, password):
        self.username = username
        self.cin = cin
        self.password = password
        self.accounts = []
        self.account_counter = 0

    def add_account(self, account_num):
        self.accounts.append(account_num)

    def remove_account(self, account_num):
        if account_num in self.accounts:
            self.accounts.remove(account_num)
            print(f"Account {account_num} removed successfully")
        else:
            print("Account not found in user's accounts")
    def aff_client(self):
        print(f"username:{self.username} cin : {self.cin} account{self.accounts}")

    def transfert(self, recipient_rib, amount):
        sender_account = None
        recipient_account = None

        with open("userdata.txt", "r") as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) >= 6 and data[1] == self.username and data[2] == self.cin:
                    sender_account = Account(data[4], float(data[5]))
                elif len(data) >= 6 and data[4] == recipient_rib:
                    recipient_account = Account(data[4], float(data[5]))

        if sender_account is None or recipient_account is None:
            print("Error: Sender or recipient account not found.")
            return

        if sender_account.solde < amount:
            print("Error: Insufficient balance for transfer.")
            return

        sender_account.solde -= amount
        recipient_account.solde += amount

        with open("userdata.txt", "r") as file:
            lines = file.readlines()
        with open("userdata.txt", "w") as file:
            for line in lines:
                data = line.strip().split(',')
                if len(data) >= 6 and data[1] == self.username and data[2] == self.cin:
                    line = f"{data[0]},{data[1]},{data[2]},{data[3]},{sender_account.rib},{sender_account.solde}\n"
                elif len(data) >= 6 and data[4] == recipient_rib:
                    line = f"{data[0]},{data[1]},{data[2]},{data[3]},{recipient_account.rib},{recipient_account.solde}\n"
                file.write(line)
        with open("transactiondata.txt", "a") as file:
            file.write(f"{self.account_counter},{self.username},{self.cin},{recipient_account.rib},{amount}\n")
        print(f"Transferred {amount} units from account {sender_account.rib} to RIB: {recipient_account.rib}")



