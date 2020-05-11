#! /usr/bin/env python

# Variables!
game_Run = 1



# Welcome
print("Congratulations and Welcome to Infection The Game!")

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

# Character Setup including starting position, attributes of Class.
# Think dictionaries for assigning things if dict(key) = value in dict.
print("You awaken to find yourself freshly, wide-eyed daughter cell. Welcome to the world little one.")
print("")
print(" The next step is to get organized and figure out where you fit in and find your niche!")

type = "Bacteria"
species = input("Please choose your species type: ")
gram = input("Are you a gram negative or gram positive? ")
motile = input("Is your organism Motile? ")
weapon = input("Please choose your offensive advantage (weapon): ")
quorum = input("Does your microbe have an ultimate (True or False)? ")
chemotaxis = input("Can your microbe respond to stimulus (True or False)? ")
defense = input("What is your main defense mechanism? ")
location = input("What is your starting location? ")
special = input("What is your secret special ability? ")

user = Microbe(25, type, species, gram, motile, weapon, quorum, chemotaxis, defense, location, special)

class Microbe:
	def __init__(self, atp, type, gram, motile, weapon, quorum, chemotaxis, defense, location, special):
		self.atp = atp
		self.type = type
		self.species = species
		self.gram = gram
		self.motile = motile
		self.weapon = weapon
		self.quorum = quorum
		self.chemotaxis = chemotaxis
		self.defense = defense
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
	defense = "Pump, Enzyme"
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
	
def metabolism(atp, mod):
	total = atp + mod
	return total

def descibe(c):
	print("OooOooO")
	print("ATP amount: " + c.atp)
	print("Your type is:" + c.type)
	print("Your species is: " + c.species)
	print("You are gram " + c.gram)
	print("Is your microbe motile?" + c.motile)
	print("What is your weapon choice?" + c.weapon)
	print("Is quorum sensing acctive? " + c.quorum)
	print("Do you respond to chemotaxis? "+ c.chemotaxis)
	print("What is your defence? " + c.defense)
	print("What is your current location? " + c.location)
	print("What is your special ability? " + c.special)

# Make sure you know your checks to ensure game keeps going.
# Player has not types "q" or "quit"
# Player still has ATP to spend, maybe give a warning if "next turn" or "next check" ATP drops to zero or below.
# game should function where player can turn on/ turn off genes that require ATP upkeep.
# How can players increase upkeep? Maybe mutate efficient metabolism by turning things on/off?
# Like a real cell, very strict control systems, only use this UNDER THESE CIRCUMSTANCES
# Do not leave things "running" in the background.
# What currently requires ATP? Staying alive, motility, weapon, activating quorum sensing "ultimate"
while True:
	if(atp < 0):
		break
		print("You have run out of ATP, you have died!")
	if(player_Input == "Exit" or player_Input == "exit" or player_Input == "Quit" or player_Input == "q" or player_Input == "Q"):
		game_Run = 0
	player_Input = input("Are you an invader or a defender? ")
	player_input.lower()
	if(player_Input == "invader" or player_Type == "bacteria"):
		player_Type = player_Input
		print("Welcome Invader! Prepare your troops.")
	elif(player_Input == "defender" or player_Type == "Immune System"):
		player_Type = player_Input
		print("Welcome Defender! Prepare the defenses.")


