import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_tree(self):
        current = self

        print('TOP:\n' + str(current.value))

        print('\nLEFT:\n')
        while current.left is not None:
            current = current.left

            print(current.value)

        current = self

        print('\nRIGHT:\n')
        while current.right is not None:
            current = current.right

            print(current.value)

    # Insert the given value into the tree
    def insert(self, value):
        if not self.left and not self.right:
            if value < self.value:
                self.left = BinarySearchTree(value)
                return
            else:
                self.right = BinarySearchTree(value)
                return

        elif value < self.value:
            if not self.left == None:
                self.left.insert(value)
            else: 
                self.left = BinarySearchTree(value)
                return

        elif value > self.value:
            if not self.right == None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                return


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
        else:
            if self.right is not None:
                return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        current = self

        while current.right is not None:
            current = current.right

        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)    

        if self.left is not None:
            self.left.for_each(cb)

        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

BST = BinarySearchTree(5)

BST.insert(10)
BST.insert(20)

BST.insert(3)
BST.insert(1)

BST.insert(50)

BST.print_tree()
print(BST.get_max())
print(BST.contains(11))