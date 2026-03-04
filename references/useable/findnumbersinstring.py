# Alternative Method (Iterative Parsing):
# You can also iterate through the string, grouping consecutive digits. 
from itertools import groupby

text = "wiaods92jopigr8eds"
# Groupby checks if characters are digits or not
parts = [''.join(g) for k, g in groupby(text, key=str.isdigit)]
# Filter to keep only the digit groups
numbers = [p for p in parts if p.isdigit()]

print(numbers) # Output: ['92', '8']

# Finding in general
    # Using itertools.groupby()
    # If you want to keep the original order and split the string exactly where it switches between characters and digits, use groupby. 
from itertools import groupby

text = "wiaods92jopigr8eds"

# Group consecutive characters by whether they are digits
groups = ["".join(g) for k, g in groupby(text, key=str.isdigit)]
# Output: ['wiaods', '92', 'jopigr', '8', 'eds']
