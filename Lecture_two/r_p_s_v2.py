import random

print("Rock...")
print("Paper...")
print("Scissors...")

rand = random.randint(0,2)

if rand == 0:
	computer = "rock"
elif rand == 1:
	computer = "paper"
else:
	computer = "scissors"


player = input("player make a move: ")

if player == computer:
	print("Its a tie!")

elif player == "rock":
	if computer == "scissors":
		print("player wins")
	else:
		print("computer wins")

elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")

elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins")

print(f"Computer played {computer}")
