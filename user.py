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

    def load_from_file(userdata):
        users = []
        with open(userdata, 'r') as file:
            lines = file.readlines()
            username = None
            cin = None
            password = None
            accounts = []
            for line in lines:
                if line.startswith("Username:"):
                    username = line.split(":")[1].strip()
                elif line.startswith("CIN:"):
                    cin = line.split(":")[1].strip()
                elif line.startswith("Password:"):
                    password = line.split(":")[1].strip()
                elif line.startswith("-"):
                    accounts.append(line.strip())
                elif line == "\n":
                    user = User(username, cin, password)
                    user.accounts = accounts
                    users.append(user)
                    username = None
                    cin = None
                    password = None
                    accounts = []
        return users


# Create a new user
user1 = User("huda", "123456789", "password123")
user1.add_account("1234567890")
user1.add_account("0987654321")

# Save the user to file
user1.save_to_file("userdata.txt")

# Load users from file
users = User.load_from_file("userdata.txt")
for user in users:
    print(user.username, user.cin, user.password, user.accounts)

