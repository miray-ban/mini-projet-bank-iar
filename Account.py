class Account:
    def __init__(self, rib, solde=0):
        self.rib = rib
        self.solde = solde
        self.transactions = []


    def get_solde(self):
        return self.solde

    def get_rib(self):
        return self.rib
