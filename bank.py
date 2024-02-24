from Account import Account
import random
class Bank:
    def __init__(self, name, tauxin):
        self.name = name
        self.tauxin = tauxin
        self.clients = []
        self.account_counter = 0

    def add_client(self, client):

        for exist_client in self.clients:
            if exist_client.username == client.username or exist_client.cin == client.cin:
                print("exist :<")

        self.clients.append(client)
        with open("bankdata.txt","a") as file:
            file.writelines(f"{client.username}:{client.cin}\n")

    def aff_bank(self):
        print(f"Bank Name: {self.name}")
        print(f"Taux d'intérêt: {self.tauxin}")


    def getTi(self):
        return self.tauxin

    def create_account(self, cin):
        for client in self.clients:
            if client.cin == cin:
                rib = random.randint(1000000, 5000000)
                account = Account(rib)
                client.add_account(account)
                self.account_counter += 1
                with open("userdata.txt", "a") as files:
                    files.write(
                        f"{self.account_counter},{client.username},{client.cin},{client.password},{rib},{account.solde}\n")
                    print(
                        f"Created account number: {self.account_counter} for {client.username} (CIN: {client.cin}) with RIB: {rib}")

                account_type = self.choose_account_type(client, rib)
                with open("accountdata.txt", "a") as file:
                    file.write(f"{client.username},{client.cin},{account_type}\n")
                return
            print("Client not found.")
    def choose_account_type(self, client, rib):
        print(f"Choose an account type for account with RIB {rib}:")
        print("1. Savings")
        print("2. Checking")
        print("3. Investment")
        print("4. Credit")
        choice = input("Enter your choice: ")
        while choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
        account_type = None
        if choice == '1':
            account_type = "Savings"
        elif choice == '2':
            account_type = "Checking"
        elif choice == '3':
            account_type = "Investment"
        elif choice == '4':
            account_type = "Credit"
        return account_type


