class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self, proof):
        block = {
          'index': len(self.chain) + 1,
          'timstamp': time(),
          'transactions': self.current_transactions,
          'proof': proof,
          'previous_hash': self.hash(self.last_block())
        }
        self.chain.append(block)
        self.current_transactions = []
        return block
        pass

    def new_transaction(self, sender, recipient, amount):
        transaction = {
          'sender': sender,
          'recipient': recipient,
          'amount': amount
        }
        self.current_transactions.append(transaction)
        return self.last_block['index'] + 1
        pass

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        return self.chain[-1]
        pass
    