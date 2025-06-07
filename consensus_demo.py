# consensus_demo.py

import random


# PoW: Proof of Work Simulation

def proof_of_work():
    print("\n PoW (Proof of Work) Selection:")
    # Simulate 3 miners with random computational power
    miners = {
        "Miner_A": random.randint(1, 100),
        "Miner_B": random.randint(1, 100),
        "Miner_C": random.randint(1, 100)
    }
    print("Miners and their power:", miners)

    # Select miner with highest power
    selected = max(miners, key=miners.get)
    print(f" Selected Miner: {selected} (Highest Power: {miners[selected]})")


# PoS: Proof of Stake Simulation

def proof_of_stake():
    print("\n PoS (Proof of Stake) Selection:")
    # Simulate 3 stakers with random stake values
    stakers = {
        "Staker_X": random.randint(1, 100),
        "Staker_Y": random.randint(1, 100),
        "Staker_Z": random.randint(1, 100)
    }
    print("Stakers and their stake:", stakers)

    # Select staker with highest stake
    selected = max(stakers, key=stakers.get)
    print(f" Selected Staker: {selected} (Highest Stake: {stakers[selected]})")


# DPoS: Delegated Proof of Stake Simulation

def delegated_proof_of_stake():
    print("\n DPoS (Delegated Proof of Stake) Selection:")
    # Simulate votes from 3 accounts
    votes = {
        "Delegate_1": random.randint(0, 10),
        "Delegate_2": random.randint(0, 10),
        "Delegate_3": random.randint(0, 10)
    }
    print("Delegates and their votes:", votes)

    # Randomly choose one among the most-voted delegates
    max_votes = max(votes.values())
    top_delegates = [d for d, v in votes.items() if v == max_votes]
    selected = random.choice(top_delegates)
    print(f" Selected Delegate: {selected} (Votes: {votes[selected]})")


# Run All Simulations

print(" Consensus Mechanism Simulation")
proof_of_work()
proof_of_stake()
delegated_proof_of_stake()

print("\n Task Complete: You’ve now compared PoW, PoS, and DPoS logic.")
