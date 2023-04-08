# https://www.hackerrank.com/challenges/absolute-permutation/problem?isFullScreen=true

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def set_next_nodes(self, left, right):
        self.set_left_node(left)
        self.set_right_node(right)
    
    def set_left_node(self, value):
        self.left = Node(value)
        
    def set_right_node(self, value):
        self.right = Node(value)


def valid_absolute_permutation(n, k):
    
    # create a binary tree, given the head node
    # with left and right nodes given values from the pairs dict
    # for each pos/level of the tree
    def fill_tree(node, pos=0):
        pos += 1
        if pos in pairs:
            left, right = pairs[pos]
            # print(f"val:{node.value} / pos:{pos} / left:{left} / right:{right}")
            node.set_next_nodes(left, right)
            fill_tree(node.left, pos)
            fill_tree(node.right, pos)
    
    
    # traverse the tree through a valid path
    def traverse_tree(node, array, permutation):
        def traverse_tree_helper(node, array, permutation):
            if node is not None and node.value in array:
                node_val = node.value
                
                new_permutation = permutation[:]
                new_permutation.append(node_val)
                
                new_array = array[:]
                new_array.remove(node_val)
                
                traverse_tree(node, new_array, new_permutation)
                
        left_node, right_node = node.left, node.right
        
        traverse_tree_helper(left_node, array, permutation)
        traverse_tree_helper(right_node, array, permutation)
    
        # reached the end of a branch, confirming a permutation
        if left_node is None and right_node is None:
            permutations.append(permutation)
    
    
    array = [i for i in range(1, n + 1)]
    pairs = {}
    for idx in range(len(array)):
        pos = idx + 1
        paired_values = [abs(pos + k), abs(pos - k)]
        
        # print(pos, paired_values)
        pairs[pos] = paired_values
    
    head = Node(0)
    fill_tree(head)
    
    permutations = []
    traverse_tree(head, array[:], [])
    
    if len(permutations) > 0:
        return permutations[0]
    
    return -1


test1 = [4, 2] # [3, 4, 1, 2]
test2 = [2, 1] # [2, 1]
test3 = [3, 0] # [1, 2, 3]
test4 = [3, 2] # -1
rand_n = random.randint(1, 10)
rand_k = random.randint(1, 5)
rand_test = [rand_n, rand_k]
print(rand_test)
tests = [test1, test2, test3, test4, rand_test]
for test in tests:
    print(valid_absolute_permutation(*test))


# n = 4, k = 2
# [1, 2, 3, 4] # 3-1 2-4 1-3, 4-2
# pos 1 / 1-2, 1+2 == 1, 3
# pos 2 / 2-2, 2+2 == 0, 4
# pos 3 / 3-2, 3+2 == 1, 5
# pos 4 / 4-2, 4+2 == 2, 6