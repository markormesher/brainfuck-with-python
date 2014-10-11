# Usage: bf.py [file name]

import sys
import read_char as rc

def start(file):
	reader = open(file, "r")
	brainfuck(reader.read())
	reader.close()

def brainfuck(input_code):
	# let's get some space
	print "----------"

	# sanitize code
	commands = filter(lambda x: x in ['+', '-', '.', ',', '>', '<', '[', ']'], list(input_code))

	# create a map of loops ( '[' and ']' )
	loop_map = {}

	# store the working stack of open brackets
	working_stack = []

	# loop through commands
	for position, command in enumerate(commands):
		# push the location of open brackets onto the stack
		if (command == "["):
			working_stack.append(position)

		# when a closing bracket is found, get the starting position and store the start/end pair
		if (command == "]"):
			start = working_stack.pop()
			loop_map[start] = position
			loop_map[position] = start
	
	# initialise things
	cells = [0]
	current_cell = 0
	current_command = 0

	# loop commands
	while (current_command < len(commands)):
		command = commands[current_command]
		
		# increment current cell
		if (command == "+"):
			cells[current_cell] += 1

		# decrement current cell
		if (command == "-"):
			cells[current_cell] -= 1

		# print to console
		if (command == "."):
			sys.stdout.write(chr(cells[current_cell]))

		# read from console
		if (command == ","):
			cells[current_cell] = ord(rc.read_char())

		# move to next cell
		if (command == ">"):
			current_cell += 1
			if (current_cell == len(cells)):
				cells.append(0)

		# move to previous cell
		if (command == "<"):
			current_cell -= 1
			if (current_cell < 0):
				print "Fatal error: tried to move to cell -1"
				exit()

		# start loop
		if (command == "[" and cells[current_cell] == 0):
			current_command = loop_map[current_command]

		# end of loop
		if (command == "]" and cells[current_cell] != 0):
			current_command = loop_map[current_command]

		current_command += 1

	# let's get some more space
	print "\n----------"


def main():
	if (len(sys.argv) == 2):
		start(sys.argv[1])
	else:
		print "Invalid arguments supplied"
		print "Usage: " + sys.argv[0] + " [file name]"


if (__name__ == "__main__"):
	main()
