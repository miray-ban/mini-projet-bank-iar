import json
import random
from Account import Account
from Transaction import Transaction
from client import Client
from bank import Bank
from admin import Admin


def create():
    username = input("-- Enter your username: ")
    cin = input("-- Enter your CIN: ")
    password = input("-- Enter your password: ")
    client1 = Client(username, cin, password)
    bank.add_client(client1)
    rib = bank.create_account(cin)
    print("--- login -- : enter your name and password")
    login()

def login():
    username = input(" \t |-| Enter your username:  ")
    password = input(" \t |-| Enter your password: ")

    if username == "admin" and password == "admin":
        admin_menu()
        return

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
    print("Thanks! See you later ;>")

def afficher_solde(user):
    with open("userdata.txt", "r") as f3:
        for line in f3:
            data = line.strip().split(',')
            if len(data) >= 4 and data[1] == user.username and data[2] == user.cin:
                print(f"Your balance is: {data[5]}")
                break
        else:
            print("User not found .")

def faire_transfert(user):
    rib = input("\t |-| Enter recipient's RIB: ")
    amount = float(input("\t |-| Enter amount to transfer: "))
    user.transfert(rib, amount)

def afficher_historique(user):
    print(" -- Transaction History: -- ")
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
        print("\t\t\t\t\t\n Bank Application Menu:")
        print("\t\t\t\t\t┌─────────────────────────────┐")
        print("\t\t\t\t\t│ 1. View balance             │")
        print("\t\t\t\t\t│ 2. Transfer                 │")
        print("\t\t\t\t\t│ 3. Show transaction history │")
        print("\t\t\t\t\t│ 4. View client information  │")
        print("\t\t\t\t\t│ 5. View bank information    │")
        print("\t\t\t\t\t│ 6. Log out                  │")
        print("\t\t\t\t\t└─────────────────────────────┘")
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

def admin_menu():
    admin = Admin(bank)
    while True:
        print("\t\t\t\t\t\n Admin Menu:")
        print("\t\t\t\t\t┌─────────────────────────────┐")
        print("\t\t\t\t\t│ 1. Add balance to client     │")
        print("\t\t\t\t\t│ 2. Change interest rate      │")
        print("\t\t\t\t\t│ 3. Back to main menu         │")
        print("\t\t\t\t\t└─────────────────────────────┘")
        choice = input("Enter your choice: ")

        if choice == '1':
            rib = input("Enter client's RIB: ")
            amount = float(input("Enter amount to add: "))
            admin.add_balance(rib, amount)
        elif choice == '2':
            new_rate = float(input("Enter new interest rate: "))
            admin.change_interest_rate(new_rate)
        elif choice == '3':
            home()
        else:
            print("Invalid choice. Please try again.")


def gestion():
    username = input(" \t |-| Enter ADMIN username:  ")
    password = input(" \t |-| Enter ADMIN password: ")

    with open("admin.txt","r") as f2:
        for lines in f2:
            data = lines.strip().split(',')
            if  data[0] == username and data[1] == password:
                print("Login successful!")
                admin_menu()
                return
        print("Invalid username or password.")

bank = Bank("IARV", 0.15)

def home() :
    while True:
         print("\t\t\t\t\t*****************")
         print("\t\t\t\t\t| Welcome to BANK IARV! ;)")
         print("\t\t\t\t\t*****************")
         print("\t\t\t\t\t┌──────────────────────────────────┐")
         print("\t\t\t\t\t\t1. Create an account\n\t\t\t\t\t\t2. Login\n\t\t\t\t\t\t3. Login as admin\n\t\t\t\t\t\t4. Exit")
         print("\t\t\t\t\t└──────────────────────────────────┘")
         choice = input("Enter your choice: ")

         if choice == '1':
             create()
         elif choice == '2':
             login()
         elif choice == '3':
             gestion()
             break
         elif choice == '4':
             print("GOOD BYE")
             exit()
         else:
             print("Invalid choice, please try again.")

home()