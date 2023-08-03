"""
Clarifying Questions:
Can I assume that the tree is not empty?
Can I assume that the values of the nodes are integers?
Can the tree contain negative values?
Do I count only paths from the root to the leaves, or can a path end at any node?
Explain Approach:
We can use a Depth-First Search (DFS) to traverse the tree.
For each node, we will keep track of all the possible sums from the root to the current node.
Each time we visit a node, we check if the current sum minus the target is in our sum history (this means there is a sub-path summing to target), and increment the global count if so.
We will need to decrement the count of the current sum in our sum history when we're done with the current node to avoid counting paths crossing over different branches.
"""

from collections import defaultdict
def pathSum(root,target):
    sum_count=defaultdict(int)
    sum_count[0]=1
    res=[0]
    def dfs(node,curr_sum):
        if node is None: return 
        curr_sum+=node.val
        res[0]+=sum_count[curr_sum-target]
        sum_count[curr_sum]+=1
        dfs(node.left,curr_sum)
        dfs(node.right,curr_sum)
        sum_count[curr_sum]-=1
    dfs(root,0)
    return result[0]
