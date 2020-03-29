print("Rock...")
print("Paper...")
print("Scissors...")

player_1 = input("player_1 make a move: ")
player_2 = input("player_2 make a move: ")

# print(player_1)
# print(player_2)

if player_1 == "rock" and player_2 == "scissors":
	print("player_1 wins!")

elif (player_1 == "paper") and (player_2 == "rock"):
	print("player_1 wins")

elif (player_1 == "scissors") and player_2 == "paper":
	print("player_1 wins")

elif (player_1 == "rock") and (player_2 == "paper"):
	print("player_2 wins")

elif (player_1 == "paper") and (player_2 == "scissors"):
	print("player_2 wins")

elif (player_1 == "scissors") and (player_2 == "rock"):
	print("player_2 wins")

elif player_1 == player_2:
	print("Its a tie")

else:
	print("Please input either Rock, Paper or Scissors")

