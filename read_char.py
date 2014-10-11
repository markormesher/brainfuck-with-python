# Adapted from http://code.activestate.com/recipes/134892

# Reads a single character from standard input

class Read_Char:
	
	def __init__(self):
		try:
			self.instance = Read_Char_Win()
		except ImportError:
			self.instance = Read_Char_Nix()

	def __call__(self):
		return self.instance()


class Read_Char_Win():

	def __init__(self):
		import msvcrt

	def __call__(self):
		import msvcrt
		return msvcrt.getch()


class Read_Char_Nix():

	def __init__(self):
		import sys, tty

	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, settings)
		return ch

read_char = Read_Char()
