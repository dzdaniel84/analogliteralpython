"""
Written by Daniel Zhang on February 6, 2017.

An implementation of this infamous article (http://www.eelis.net/C++/analogliterals.xhtml) in Python.
Import this into all your code for some extra fun :^)
Since idea is not mine, feel free to do whatever with this code if you want.
Only use {'O', 'L', '-', '|'} in your analog literals, please.
"""

"""
Returns the length of a line written in ASCII.

Must include 'O', '-'.
>>> area("O-----------O")
11.0
"""
def length(str):
	return str.count('-')

"""
Returns the area of a rectangle written in ASCII.

Must include 'O', '-', '|'.
>>> area("""
O----O
|    |
|    |
|    |
|    |
O----O
""")
16.0
"""
def area(str):
	return (str.count('-') * str.count('|')) / 4

"""
Returns the volume of a rectangular prism written in ASCII.

Must include 'O', 'L', '-', '|'.
>>> volume("""
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
""")
176.0
"""
def volume(str):
	return (str.count('|') * str.count('-') * str.count('L'))/27

