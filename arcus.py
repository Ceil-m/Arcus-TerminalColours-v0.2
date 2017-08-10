#!/usr/bin/python3
import random
#print("Arcus-TerminalColours v0.2 (originally) by Ceil")
'''
	Arcus-TerminalColours v0.2 (originally) by Ceil

	***This is free software. Anyone can use, modify, and redistribute
	(if you do modify and redistribute, credit is appreciated)*** 


	USAGE
	=====
	How to import: 
	from arcus import * 

	Usage Examples:
	*print(green+"This text is green!")
	*print(red+bold"WARNING!")
	*print(bold+ul+"Cool Title!")

	Notes:
	*put a '+x' after you print if you wish to reset the colour/format: print(red+"Red!"+x)
	*you can also put another '+' after the 'x' if you are still printing: print(red+"Red!"+x+"Normal!")
	*you don't need to put these anywhere specific, as they can go anywhere in a print: print("Normal"+red)
	this means that any text after that is red.
'''

#Colours
red = '\033[31m'			#red
green = '\033[32m'			#green
orange = '\033[33m'			#orange
blue = '\033[34m'			#blue
purple = '\033[35m'			#purlpe
cyan = '\033[36m'			#cyan
yellow = '\033[93m'			#yellow
pink = '\033[95m'			#pink

#Random Colours
colours = [red, green, orange, blue, purple, cyan, yellow, pink] #list of colours for random selection
rcol = random.choice(colours) #random colour

#Light/dark Colours
white = '\033[97m'			#white
lred = '\033[91m'			#light red
lgreen = '\033[92m'			#light green
lblue = '\033[94m'			#light blue
lcyan = '\033[96m'			#light cyan
lyellow = '\033[93m'		#light yellow
lgray = '\033[37m'			#light gray
dgray = '\033[90m'			#dark gray

#Layout
x = '\033[0m'				#reset colour
bold = '\033[1m'			#bold
ul = '\033[04m'				#underline
dim = '\033[2m'				#dim
inv = '\033[7m'				#reverse
hide = '\033[8m'			#hidden (DO NOT USE FOR PASSWORDS)

#Random Layout
layouts = [bold, ul, dim, inv, hide] #list of layouts for random selection
rlay = random.choice(layouts) #random layout
