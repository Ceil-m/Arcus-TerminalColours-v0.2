# Arcus-TerminalColours-v0.2
Arcus-TerminalColours v0.2 (originally) by Ceil

***This is free software. Anyone can use, modify, and redistribute
(if you do modify and redistribute, credit is appreciated)*** 

Give your terminal applications some life!

USAGE
=====
How to import: 
-from arcus import * 

Usage Examples:
-print(green+"This text is green!")
-print(red+bold"WARNING!")
-print(bold+ul+"Cool Title!")

Notes:
-put a '+x' after you print if you wish to reset the colour/format: print(red+"Red!"+x)
-you can also put another '+' after the 'x' if you are still printing: print(red+"Red!"+x+"Normal!")
-you don't need to put these anywhere specific, as they can go anywhere in a print: print("Normal"+red)
this means that any text after that is red.

Colours:
red
green
orange
blue
purple
cyan
yellow
pink

Light Colours:
white/Dark
lred
lgreen
lblue
lcyan
lyellow
lgray
dgray

Layout:
x        -resets
bold     -bold
ul       -underline
dim      -dim text
inv      -invert
hide     -hide text

Random Options:
rcol     -random colours
rlay     -random layout
