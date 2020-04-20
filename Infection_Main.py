#! /usr/bin/env python

# Variables!
player_Type = ""
player_Name = ""
player_Input = ""
game_Run = 1


# Welcome
print ("Congratulations and Welcome to Infection The Game!")

#Introduction
print("Welcome to the Tree of Life")
print("Bacteria        Archaea             Eukarya")
print("    \              |                   /   ")
print("     \             |                 /    ")
print("      \            |               /    ")
print("       \           |             /    ")
print("         \          |           /    ")
print("          \         |         /    ")
print("           \        |       /    ")
print("             \      |     /    ")
print("              \     |    |   ")
print("               \    |   /  ")
print("                \   |  /")
print("                  \ | /  ")
print("                    |   ")
print("                    |   ")
print("            Last Common Ancestor ")


while(game_Run > 0):
	if(player_Input == "Exit" or player_Input == "exit" or player_Input == "Quit" or player_Input == "q" or player_Input = "Q"):
		game_Run = 0
	player_Input = input("Are you an invader or a defender? ")
	if(player_Input == "invader" or player_Type == "bacteria"):
		player_Type = player_Input
		print ( "Welcome Invader! Prepare your troops.")
	elif(player_Input == "defender" or player_Type == "Immune System"):
		player_Type = player_Input
		print ( "Welcome Defender! Prepare the defenses.")

class microbe:
	def __init__(self, atp, type, gram, motile, weapon):
		self.atp = atp
		self.type = type
		self.species = species
		self.gram = gram
		self.motile = motile
		self.weapon = weapon
		self.quorum = quorum
		self.chemotaxis = chemotaxis

	atp = 25
	type = "Bacteria"
	species = ["Bacillus, Streptococcus"]
	gram = ["Positive", "Negative"]
	motile = False
	weapon = ["Exotoxin - Antibiotic", "Endotoxin"]
	quorum = False
	chemotaxis = False


class cell:
	def __init__(self, atp, type, weapon, location):
		self.atp = atp
		self.type = type
		self.weapon = weapon
		self.location = location

	atp = 50
	type = ["Macrophage", "Neutrophil", "Eosinophil", "T Cell", "B Cell"]
	weapon = ["Ingestion", "Antibody", "MAC Attack", "Web"]
	location = ["Organ", "Blood"]



