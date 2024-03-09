from bank import Bank
import operator


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def add_balance(self, rib, amount):
        with open("userdata.txt", "r") as file:
            lines = file.readlines()
            with open("userdata.txt", "w") as file:
                for line in lines:
                    data = line.strip().split(',')
                    line = f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{(data[5])}\n"
                    if len(data) >= 6 and data[4] == rib:
                        line = f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{float(data[5]) + amount}\n"
                        file.write(line)
                        print(f"Added {amount} to the balance of account of : {data[1]} with RIB :{rib}")
                    else:
                        file.write(line)
                        print("Client not found.")
        return

    def change_interest_rate(self, new_rate):
        self.bank.tauxin = new_rate
        print(f"Changed interest rate to: {new_rate}")


