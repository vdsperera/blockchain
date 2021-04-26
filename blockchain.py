class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []

    def new_block(self):
        pass

    def new_transaction(self, sender, recipient, amount):
        transaction = {
          'sender': sender,
          'recipient': recipient,
          'amount': amount
        }
        self.transactions.append(transaction)
        return self.last_block()
        pass

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        return self.chain[-1]
        pass
    