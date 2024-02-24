from client import Client
from Account import Account
from bank import Bank
from Transaction import Transaction


def create():
    username = input("Enter your username: ")
    cin = input("Enter your CIN: ")
    password = input("Enter your password: ")
    client1 = Client(username, cin, password)
    bank.add_client(client1)
    rib = bank.create_account(cin)
    bank.choose_account_type(client1, rib)
    print("login : enter your name and password")
    login()


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("userdata.txt","r") as f2:
        for lines in f2:
            data = lines.strip().split(',')
            if len(data) == 6 and data[1] == username and data[3] == password:
                print("Login successful!")
                user = Client(data[1], data[2], data[3])
                bank_menu(user)
                return
        print("Invalid username or password.")
def exit_program():
    print("Thanks! See you later.")

def afficher_solde(user):
    with open("userdata.txt", "r") as f3:
        for line in f3:
            data = line.strip().split(',')
            if len(data) >= 4 and data[1] == user.username and data[2] == user.cin:
                print(f"Your balance is: {data[5]}")
                break
        else:
            print("User not found or data format incorrect.")


def faire_transfert(user):
    rib = input("Enter recipient's RIB: ")
    amount = float(input("Enter amount to transfer: "))
    user.transfert(rib, amount)

def afficher_historique(user):
    print("Transaction History:")
    try:
        with open("transactiondata.txt", "r") as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 5 and data[1] == user.username and data[2] == user.cin:
                    transaction = Transaction(data[0], data[1], data[3], float(data[4]))
                    transaction.aff_transaction()
    except FileNotFoundError:
        print("Transaction data file not found.")
    except Exception as e:
        print(f"An error occurred while reading transaction data: {e}")




def afficher_info_client(user):
    print(f"Client Information:")
    print(f"Username: {user.username}")
    print(f"CIN: {user.cin}")
    print("Accounts:")
    with open("accountdata.txt","r") as file:
        for line in file:
            data=line.strip().split(",")
            if user.cin==data[1]:
              print(f"your account :{data[2]}")



def afficher_info_banque():
    print(" infoermation bank \n")
    bank.aff_bank()



def bank_menu(user):
    while True:
        print("\n Bank Application Menu:")
        print("┌─────────────────────────────┐")
        print("│ 1. View balance             │")
        print("│ 2. Transfer                 │")
        print("│ 3. Show transaction history │")
        print("│ 4. View client information  │")
        print("│ 5. View bank information    │")
        print("│ 6. Log out                  │")
        print("└─────────────────────────────┘")
        choice = input("Enter your choice: ")

        if choice == '1':
            afficher_solde(user)
        elif choice == '2':
            faire_transfert(user)
        elif choice == '3':
            afficher_historique(user)
        elif choice == '4':
            afficher_info_client(user)
        elif choice == '5':
            afficher_info_banque()
        elif choice == '6':
            print("good by...")
            break
        else:
            print("Invalid choice. Please try again.")

bank = Bank("IAV", 0.15)

while True:
    print("\t\t\t\t\t************************")
    print("\t\t\t\t\t| Welcome to BANK IAV! ;)")
    print("\t\t\t\t\t************************")
    print("\t\t\t\t\t┌──────────────────────────────────┐")
    print("\t\t\t\t\t\t1. Create an account\n\t\t\t\t\t\t2. Login\n\t\t\t\t\t\t3. Exit")
    print("\t\t\t\t\t└──────────────────────────────────┘")
    choice = input("Enter your choice: ")

    if choice == '1':
        create()

    elif choice == '2':
        login()

    elif choice == '3':
        exit_program()
        break

    else:
        print("Invalid choice, please try again.")