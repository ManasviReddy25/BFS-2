# Problem 1: Binary Tree Right Side View (https://leetcode.com/problems/binary-tree-right-side-view/)
# Time Complexity: O(n),n = total number of nodes in the tree
# Every node enters the queue once and gets popped once, so we touch each node exactly once

# Space Complexity: O(n)
#The queue holds at most one full level at a time
# In the worst case the bottom level of a perfect binary tree has n/2 nodes
# The result list stores one value per level, which is at most n values

# Approach:
# We process the tree level by level using BFS and a queue
# At the start of each level we snapshot how many nodes are in the queue (size)
# This tells us exactly how many nodes belong to the current level
# We process all of them one by one, and only the last one (i == size - 1) is visible from the right side
# We save that last node's value into result and move on to the next level

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []                 # stores the rightmost node value for each level

        if root is None:            # if the tree is empty there is nothing to see
            return result

        queue = deque()
        queue.append(root)          # start BFS with just the root in the queue

        while queue:                # keep looping as long as there are nodes to process

            size = len(queue)       # how many nodes are on this level right now
                                    # we snapshot this before the for loop because
                                    # the loop itself adds next level nodes into the queue

            for i in range(size):   # process exactly the nodes that belong to this level

                current = queue.popleft()   # take the next node from the front of the queue

                if i == size - 1:           # is this the last node on this level?
                    result.append(current.val)  # yes, so this is what we see from the right side

                if current.left:            # if this node has a left child
                    queue.append(current.left)  # add it so it gets processed in the next level

                if current.right:           # if this node has a right child
                    queue.append(current.right) # add it so it gets processed in the next level

        return result               # one value per level from top to bottom