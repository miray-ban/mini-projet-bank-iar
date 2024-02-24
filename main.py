
from client import Client
from Account import Account
from bank import Bank
def create():
    username = input("Enter your username: ")
    cin = input("Enter your CIN: ")
    password = input("Enter your password: ")
    client1 = Client(username, cin, password)
    bank.add_client(client1)
    bank.create_account(cin)



def bank_menu(user):
    while True:
        print("\n Bank Application Menu:")
        print("1. view balance")
        print("2. transfer")
        print("3. show the transaction history")
        print("4. View  information")
        print("5. view bank information")
        print("6. log out")

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

def afficher_solde(user):
    print("solde")
    pass

def faire_transfert(user):
    print("trens")
    pass

def afficher_historique(user):
    print("his")
    pass

def afficher_info_client(user):
    print("his")
    pass

def afficher_info_banque():
    print("info")
    pass

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

bank = Bank("IAV", 0.15)

while True:
    print("Welcome to BANK IAV! ;)")
    print("\n\t1. Create an account\n\t2. Login\n\t3. Exit")
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



