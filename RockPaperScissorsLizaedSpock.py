import random

results = [("rock", "scissors"), ("scissors", "paper"),("paper", "rock"), ("rock", "lizard"), ("lizard","spock"),
           ("spock", "scissors"), ("scissors", "lizard"), ("lizard", "paper"), ("paper", "spock"), ("spock", "rock")]
moves = [result[0] for result in results]

player_score, computer_score =(0, 0)
player = input("Enter rock / paper / scissors / lizard / spock / quit: ").lower()
while player != "quit":
    computer = random.choice(moves)
    print("You Chose {}, I Chose {}".format(player,computer))
    if player == computer:
       print("Its a Tie!")
    elif(player, computer) in results:
        print("You Win")
        player_score += 1
    elif(computer, player) in results:
        print("I Win!")
        computer_score += 1
    else:
        print("Invalid Input")
    player = input(" Enter rock / paper / scissors / lizard / spock /quit: ").lower()

print("FINAL SCORE")
print("You: {}  Me: {}".format(player_score, computer_score))