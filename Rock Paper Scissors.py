import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors.\n").lower()
    while user not in ['r', 'p', 's']:
        user = input("Invalid input. Please enter 'r' for rock, 'p' for paper, 's' for scissors.\n").lower()
    computer = random.choice(['r','s','p'])
    
    if user == computer:
        return "Tie"
    
    if is_win(user, computer):
        return f"You won!!! Computers choice was {computer}."
    
    return f"You Lost! Computers choice was {computer}." 
    
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") or (player == "s" and opponent == "p"):
        return True
    return False

print(play())