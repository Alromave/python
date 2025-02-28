#02 Checkpoint: Calling Functions
#Purpose
"""
Check your understanding of calling built-in Python functions and functionsthat are in a
standard Python module.
"""
#Problem Statement
"""
In our modern world economy, many items are manufactured in large factories, then
packed in boxes and shipped to distribution centers and retailstores. A common question
for employees who pack itemsis "How many boxes do we need?"
"""
#Assignment
"""
A manufacturing company needs a program that will help its employees pack
manufactured itemsinto boxesforshipping. Write a Python program named boxes.py
that asksthe user for two integers:
1. the number of manufactured items
2. the number of itemsthat the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items.
This must be a whole number. Note that the last box may be packed with fewer items
than the other boxes.
"""

import math
number_items = int(input("Enter the number of items: "))
items_box = int(input("Enter the number of items per box: "))
boxes = (math.ceil(number_items / items_box))


print(f"For {number_items}, packing {items_box} in each box, you will need {boxes} boxes")
