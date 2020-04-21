#! /usr/bin/env python

# Variables!
player_Type = ""
player_Name = ""
player_Input = ""
intro_Run = 1
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

# Character Setup
while(intro_Run > 0):
	print("You awaken to find yourself freshly, wide-eyed daughter cell. Welcome to the world.")
 	print("")


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
	def __init__(self, atp, type, gram, motile, weapon, quorum, chemotaxis, evasion, location, special):
		self.atp = atp
		self.type = type
		self.species = species
		self.gram = gram
		self.motile = motile
		self.weapon = weapon
		self.quorum = quorum
		self.chemotaxis = chemotaxis
		self.evasion = evasion
		self.location = location
		self.special = special

	atp = 25
	type = "Bacteria"
	species = ["Bacillus, Streptococcus"]
	gram = ["Positive", "Negative"]
	motile = False
	weapon = ["Exotoxin - Antibiotic", "Endotoxin"]
	quorum = False
	chemotaxis = False
	evasion = "Pump, Enzyme"
	location = ""
	special = ""


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



