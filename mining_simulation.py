# mining_simulation.py

import hashlib
import time

# Block class for mining simulation
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Hashing the block content with SHA-256
        block_content = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"\n Mining block with difficulty {difficulty} (hash must start with {'0' * difficulty})...")
        target = '0' * difficulty  # pattern for valid hash
        start_time = time.time()

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        print("Block mined successfully!")
        print(f"Nonce found: {self.nonce}")
        print(f"Hash      : {self.hash}")
        print(f"Time taken: {round(end_time - start_time, 4)} seconds")


# Start Mining Simulation

difficulty = 4  # We can increase to 5 or 6 to make it harder

# Creating block with sample data
block = Block(1, "Sample Transaction Data", "0000a1b2c3d4")

# Start mining 
block.mine_block(difficulty)
