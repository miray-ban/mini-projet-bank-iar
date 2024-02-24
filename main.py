from bank import Bank
from client import Client
from Account import Account


def main():
        while True:
            print ("welcome in BANK IARV: ;)")
            print("\n\t,******* 1- crate account \n*********** 2- login \n ********** 3- exit ")
            choice=input("enter your choice :")

            if choice =='1' :
                create()

            elif choice == '2' :
                login()

            elif choice == '3' :
                exit()
                break

            else:
                print(" you wrong , please try again ")




def create():
    username = input("enter your username :")
    cin = input("enter your cin:")
    password = input("enter your password :")

def login():
    username = input("entre your username :")
    password = input("enter password :")

def exit():
    print(" thanks see you later :] ")


if __name__ == "__main__":
    main()



