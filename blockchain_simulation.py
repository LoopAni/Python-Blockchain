# blockchain_simulation.py

import hashlib
import time

# Block Class Definition

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(block_content.encode()).hexdigest()

    def display_block(self):
        print(f"\nBlock #{self.index}")
        print(f"Timestamp     : {self.timestamp}")
        print(f"Data          : {self.data}")
        print(f"Nonce         : {self.nonce}")
        print(f"Previous Hash : {self.previous_hash}")
        print(f"Hash          : {self.hash}")

# Step 1: Create Genesis Block
block0 = Block(0, time.time(), "Genesis Block", "0")

# Step 2: Create Block 1
block1 = Block(1, time.time(), "Transaction A to B", block0.hash)

# Step 3: Create Block 2
block2 = Block(2, time.time(), "Transaction C to D", block1.hash)

# Display the blockchain
block0.display_block()
block1.display_block()
block2.display_block()

# Tamper with Block 1
print("\n Tampering Block 1's data...")
block1.data = "Tampered Data"
block1.hash = block1.calculate_hash()

# Display blocks again after tampering
block1.display_block()
print("\n Checking if Block 2 is still valid...")
if block2.previous_hash != block1.hash:
    print(" Block 2 is INVALID because its previous hash doesn't match Block 1's new hash.")
else:
    print(" Block 2 is still valid.")
