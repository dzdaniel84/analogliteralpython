"""
Written by Daniel Zhang on February 6, 2017.

An implementation of this infamous article (http://www.eelis.net/C++/analogliterals.xhtml) in Python.
Import this into all your code for some extra fun :^)
Since idea is not mine, feel free to do whatever with this code if you want.
Only use {'O', 'L', '-', '|', '/'} in your analog literals, please.
"""

def length(str):
	"""Returns the length of a line written in ASCII.

	Must include 'O', '-'.
	>>> length("O-----------O")
	11.0
	"""
	return str.count('-')

def area(str):
	"""Returns the area of a rectangle written in ASCII.

	Must include 'O', '-', '|'.
	"""
	return (str.count('-') * str.count('|')) / 4

def volume(str):
	"""Returns the volume of a rectangular prism written in ASCII.

	Must include 'O', 'L', '-', '|'.
	"""
	return (str.count('|') * str.count('-') * str.count('L'))/27

def hvolume(str):
	"""Returns the 4-volume of a hypercube written in ASCII.

	Must include 'O', 'L', '-', '|', "/".
	"""
	return (str.count('|') * str.count('-') * str.count('L') * str.count('/'))/256

# These examples are included below because their format means they can't be included in traditional
# doctests.
assert(area("""
O----O
|    |
|    |
|    |
|    |
O----O
""") == 16)

assert(volume("""
O-----------O
|L           L
| L           L
|  L           L
|   L           L
O    O-----------O
 L   |           |
  L  |           |
   L |           |
    L|           |
     O-----------O
""") == 176)

assert(hvolume("""
     O-----------O      
    / L           L     
   /   L           L
  /     L           L   
 /       O-----------O 
O       /           /|  
|L     /           / |  
| L   /           /  |  
|  L /           /   |  
|   O-----------O    |  
|   |           |    O  
O   |           |   /   
 L  |           |  /    
  L |           | /     
   L|           |/
    O-----------O
""") == 660)
