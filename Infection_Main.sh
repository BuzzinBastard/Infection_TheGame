#! /usr/bin/env python

# Variables!
player_Type = "Bacteria"
player_Name = "Bugs" 
player_Input = "Run"
game_Run = 1



print ( "Congratulations and Welcome to Infection!" )

while(game_Run > 0):
	if(player_Input == "Exit" or player_Input == "exit" or player_Input == "Quit" or player_Input == "q"):
		game_Run = 0
	player_Input = input("Are you an invader or a defender? ")
	if(player_Input == "invader" or player_Type == "bacteria"):
		player_Type = player_Input
		print ( "Welcome Invader! Prepare your troops.")
	elif(player_Input == "defender" or player_Type == "Immune System"):
		player_Type = player_Input
		print ( "Welcome Defender! Prepare the defenses.")
