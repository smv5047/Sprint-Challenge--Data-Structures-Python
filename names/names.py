import time


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # if no self.left exist, make self.left = value
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        if value > self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        if value == self.value:
            duplicates[:-1] = value


names_bst = BSTNode('test')
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Use BST
# Add all names to BST
# when inserting, if duplicate, add to list


for name_1 in names_1:
    names_bst.insert(name_1)
for name_2 in names_2:
    names_bst.insert(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# Original big O is Quadratic time or O(n^2) this is because it is a nested for loop


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
