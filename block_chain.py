import hashlib
import time

class Block:
    def __init__(self, model, data, results, previous_hash):
        self.timestamp = time.strftime("%d-%m-%Y, %H:%M")
        self.model = hashlib.sha256(model.encode()).hexdigest()
        self.data = hashlib.sha256(data.encode()).hexdigest()
        self.results = results
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_contents = str(self.timestamp) + self.model + self.data + str(self.results) + self.previous_hash
        return hashlib.sha256(block_contents.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block("Genesis Model", "Genesis Data", "Genesis Results", "0")
    
    def add_block(self, model, data, results):
        previous_block = self.chain[-1]
        new_block = Block(model, data, results, previous_block.hash)
        self.chain.append(new_block)

    def print_blockchain(self):
        for block in self.chain:
            print(f"Timestamp: {block.timestamp}")
            print(f"Model used: {block.model}")
            print(f"Input data: {block.data}")
            print(f"Results: {block.results}\n")