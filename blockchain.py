from time import time
import hashlib
from uuid import uuid4
import json
from flask import Flask

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

    def proof_of_work(self, previous_proof):
      check_proof = 0
      while self.valid_proof(previous_proof, check_proof) is False:
        check_proof = check_proof + 1
      return check_proof
      pass

    def valid_proof(previous_proof, check_proof):
      guess_answer = f'{previous_proof}{check_proof}'.encode()
      guess_hash = hashlib.sha256(guess_answer).hexdigest()
      return guess_hash[:4] == '0000'
      pass

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        return self.chain[-1]
        pass
    
app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
  # request = {
  #   'sender': '',
  #   'recipient': '',
  #   'amount': ''
  # }
  values = request.get_json()
  required = ['sender', 'recipient', 'amount']
  if not all(for value in values:)
  pass

@app.route('/mine', methods=['GET'])
def mine():
  pass

@app.route('/chain', methods=['GET'])
def full_chain():
  response = {
    'chain': blockchain.chain,
    'length': len(blockchain.chain)
  }
  return response
  pass

if __name__ == '__main__':
  app.run(host='0:0:0:0', port=5000)