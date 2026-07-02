## Problem 2: Cousins in binary tree (https://leetcode.com/problems/cousins-in-binary-tree/)
# Time Complexity: O(n),n = total number of nodes in the tree
# Every node enters the queue once and is popped once, O(1) work per node

# Space Complexity: O(n)
# The queue holds at most one full level at a time
# In the worst case a level can have up to n/2 nodes
# We only use two extra boolean variables which are O(1)

# Approach:
# We use BFS to process the tree level by level
# For two nodes to be cousins they must be on the same level AND have different parents
# We check the different-parents condition while processing each node:
# if a node has both left and right children and one is x and the other is y, they share the same parent so they cannot be cousins, return False immediately
# We check the same-level condition using two flags x_found and y_found
# If both flags are True after finishing a level, they were found on the same level and we already ruled out same parent, so they are cousins, return True
# If only one flag is True after a level, they are on different levels, return False

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        q = deque()
        q.append(root)          # start BFS from the root

        x_found = False         # becomes True when we see node x on the current level
        y_found = False         # becomes True when we see node y on the current level

        while q:                # keep going as long as there are nodes to process

            size = len(q)       # snapshot how many nodes are on this level right now

            for i in range(size):       # process exactly the nodes on this level

                curr = q.popleft()      # take the next node from the front of the queue

                if curr.left is not None and curr.right is not None:
                    # this node has BOTH a left and right child
                    # that means its two children share the same parent (curr)
                    # if one child is x and the other is y, they are siblings not cousins
                    if curr.left.val == x and curr.right.val == y:
                        return False    # x and y have the same parent, not cousins
                    if curr.right.val == x and curr.left.val == y:
                        return False    # same check, just x and y swapped sides

                if curr.val == x:       # did we just land on node x?
                    x_found = True      # mark that x exists on this level

                if curr.val == y:       # did we just land on node y?
                    y_found = True      # mark that y exists on this level

                if curr.left is not None:       # if this node has a left child
                    q.append(curr.left)         # add it to process in the next level

                if curr.right is not None:      # if this node has a right child
                    q.append(curr.right)        # add it to process in the next level

            # we just finished processing every node on this level
            # now check what we found

            if x_found and y_found:     # both x and y were on this level
                return True             # same level + already confirmed different parents above = cousins

            if x_found or y_found:      # only one of them was on this level
                return False            # they are on different levels, cannot be cousins

            # if neither was found on this level, continue to the next level

        return True     # safety return, never actually reached on valid input