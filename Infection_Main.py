#! /usr/bin/env python

# Potential Bacteria Class Attributes
# ATP (nrg to earn and spend), type, species, gram, motile, weapon, quorum, chemotaxis, defense, location, special, population size

# Potential Immune system cell Class Atributes
# Variables!
game_Run = 1

# Welcome to the Game
print("Congratulations and Welcome to Infection The Game!")

# Introduction
# Character Setup including starting position, attributes of Class.
# Think dictionaries for assigning things if dict(key) = value in dict.
print("You awaken to find yourself freshly, wide-eyed daughter cell. Welcome to the world little one.")
print("")
print(" The next step is to get organized and figure out where you fit in and find your niche!")

# The user class with variables. Need to make list variables so adding more genes (at cost of more nrg).
# Ex. Weapons, what happens if a new weapon is evolved, developed or genes found?
class Microbe:
	def __init__(self, atp, population):
		self.atp = atp
		self.population = population

	atp = 25
	population = 1

# Methods involved in the player derived microbe class

# Changing ATP
def metabolism(atp, mod):
	total = atp + mod
	print("Your new ATP is {0}", atp)
	return total

def reproduction(population):
	population = population * 2
	return population

# Print the current characteristics
def descibe(atp, population):
	print("Your current ATP is {0}", atp)
	print("Your current Population is {0}", population)

# NPC cell class to give enemies.
class cell:
	def __init__(self, atp, type, weapon, location, community):
		self.atp = atp
		self.type = type
		self.weapon = weapon
		self.location = location
		self.community = community
	atp = 50
	type = ["Macrophage", "Neutrophil", "Eosinophil", "T Cell", "B Cell"]
	weapon = ["Ingestion", "Antibody", "MAC Attack", "Web"]
	location = ["Organ", "Blood"]
	community = 1000

# Make sure you know your checks to ensure game keeps going.
# Player has not types "q" or "quit"
# Player still has ATP to spend, maybe give a warning if "next turn" or "next check" ATP drops to zero or below.
# game should function where player can turn on/ turn off genes that require ATP upkeep.
# How can players increase upkeep? Maybe mutate efficient metabolism by turning things on/off?
# Like a real cell, very strict control systems, only use this UNDER THESE CIRCUMSTANCES
# Do not leave things "running" in the background.
# What currently requires ATP? Staying alive, motility, weapon, activating quorum sensing "ultimate"

while game_Run:
	player_Input = ""
	if(player_Input == "Exit" or player_Input == "exit" or player_Input == "Quit" or player_Input == "q" or player_Input == "Q"):
		game_Run = 0
		player_Input = input("Are you an invader or a defender? ")
		player_Input.lower()
		if(player_Input == "invader" or player_Type == "bacteria"):
			player_Type = player_Input
			print("Welcome Invader! Prepare your troops.")
		elif(player_Input == "defender" or player_Type == "Immune System"):
			player_Type = player_Input
			print("Welcome Defender! Prepare the defenses.")
	# Create class with input variables.
	user = Microbe(25, 1)

