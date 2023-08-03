"""
Clarification
-First, I would make sure that I understand the problem by asking clarifying questions:
-Is the cost array always non-empty?
-Can the cost of a step be negative?
-Can the cost array contain only one element?
-So I can either start at index 0 or 1, and at each step, I can choose to climb one step or two steps, correct?
Identify Problem type:
-this is a dynamic programming problem as we are looking to minimize a cost function based on previous decisions
Approach:
-the key is to realize that the minimum cost to reach step 'i' is the cost of step'i' plus the minimum of the cost to reach step 'i-1' and 'i-2'.

"""
def minCostClimbingstairs(cost):
    n=len(cost)
    if n==1: return cost[0]
    dp=[0]*n
    dp[0],dp[1]=cost[0],cost[1]
    for i in range(2,n):
        dp[i]=cost[n]+min(dp[i-1]+dp[i-2])
    return min(dp[-1],dp[-2])
