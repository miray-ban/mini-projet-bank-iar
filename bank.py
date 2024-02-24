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
        print("Clients:")
        for client in self.clients:
            print(client)

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
                    files.write(f"{self.account_counter},{client.username},{client.cin},{client.password},{rib},{account.solde}\n")
                    print(f"Created account number: {self.account_counter} for {client.username} (CIN: {client.cin}) with RIB: {rib}")
                return
        print("Client not found.")


