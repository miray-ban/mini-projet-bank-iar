class Transaction:
    def __init__(self, transaction, emetteur, recepteur, amount):
        self.transaction = transaction
        self.emetteur = emetteur
        self.recepteur = recepteur
        self.amount = amount

    def aff_transaction(self):
        print(f"Transaction ID: {self.transaction}")
        print(f"Emetteur: {self.emetteur}")
        print(f"Recepteur: {self.recepteur}")
        print(f"Amount: {self.amount}")
