import json

class User:
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

    # Other methods like aff_clients, transfert, historique, etc.

    def save_to_file(self, userdata):
        with open(userdata, 'a') as file:
            file.write(f"Username: {self.username}\n")
            file.write(f"CIN: {self.cin}\n")
            file.write(f"Password: {self.password}\n")
            file.write("Accounts:\n")
            for account in self.accounts:
                file.write(f"- {account}\n")
            file.write("\n")
        print(f"User {self.username} saved to {userdata}")


if __name__ == "__main__":

 user1 = User("kaoutar", "z643206", "password123")
 user1.add_account("1234567890")
 user1.add_account("0987654321")

# Save the user to file
 user1.save_to_file("userdata.txt")
