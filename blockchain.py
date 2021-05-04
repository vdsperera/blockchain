from time import time
import hashlib
from uuid import uuid4
from textwrap import dedent
import json
import requests
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, previous_hash, proof):
        block = {
          'index': len(self.chain) + 1,
          'timstamp': time(),
          'transactions': self.current_transactions,
          'proof': proof,
          'previous_hash': previous_hash
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

    @staticmethod
    def valid_proof(previous_proof, check_proof):
      guess_answer = f'{previous_proof}{check_proof}'.encode()
      guess_hash = hashlib.sha256(guess_answer).hexdigest()
      return guess_hash[:4] == '0000'
      pass

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
        pass



app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

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
  # if not all(for value in values:)

  for r in required:
    if (r in values) == False:
        return 'missing values'

  index = blockchain.new_transaction(values['sender'],
    values['recipient'], values['amount'])

  response = f'The transaction will be added to block {index}'
  return response
  pass

@app.route('/mine', methods=['GET'])
def mine():
  last_block = blockchain.last_block
  previous_proof = last_block['proof']
  proof = blockchain.proof_of_work(previous_proof)

  blockchain.new_transaction(sender='0',
    recipient=node_identifier, amount=1)

  previous_hash = blockchain.hash(last_block)
  block = blockchain.new_block(previous_hash, proof)

  # response = {
  #     'message': "New Block Forged",
  #     'index': block['index'],
  #     'transactions': block['transactions'],
  #     'proof': block['proof'],
  #     'previous_hash': block['previous_hash'],
  # }

  response = {
    'message': 'New block was forged',
    'index': block['index'],
    'transactions': block['transactions'],
    'proof': block['proof'],
    'previous_hash': block['previous_hash']
  }
  return jsonify(response)
  pass

@app.route('/chain', methods=['GET'])
def full_chain():
  response = {
    'chain': blockchain.chain,
    'length': len(blockchain.chain)
  }
  return jsonify(response)
  pass

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)