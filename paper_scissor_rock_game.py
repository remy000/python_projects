import random

while True:

    choices=["paper","rock","scissor"]
    
    computer=random.choice(choices)
    player=None
     
    while player not in choices:
        player=input("paper, rock, or scissor?: ").lower()
        
        if computer == player:
            print(computer)
            print(player)
            print("tie")
        elif computer == "rock":
            if player == "paper":
                print(computer)
                print(player)
                print("you win")
            elif player == "scissor":
                print(computer)
                print(player)
                print("you lose")
        
                
                
        elif computer == "paper":
            if player == "rock":
                print(computer)
                print(player)
                print("you lose")
            elif player == "scissor":
                print(computer)
                print(player)
                print("you win")
        else:
            if player == "rock":
                print(computer)
                print(player)
                print("you win")
            elif player == "paper":
                print(computer)
                print(player)
                print("you lose")
    play_again=input("play again yes/no: ")
        
    if play_again != "yes":
            break
        
print("Byeee")