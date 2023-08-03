
"""
larification
I would first make sure that I understand the problem correctly by asking clarifying questions:
Is the input n always a positive integer?
Is it guaranteed that there is at least one step (i.e., n >= 1)?
For n = 1, the number of ways to reach the top would be 1, right? For n = 2, would it be 2 (one step at a time or two steps at once), correct?
Identify Problem Type
The problem asks for the total number of "distinct ways" to climb to the top, which means the order of steps matters. The choices at each step depend on the previous steps, indicating that this problem can be solved using Dynamic Programming.
Define Approach
We can solve this problem using a bottom-up dynamic programming approach:
For n = 1, there is 1 way to climb to the top (climb 1 step)
For n = 2, there are 2 ways (climb 1 step twice or climb 2 steps once)
For n >= 3, the number of ways to reach the ith step would be the sum of the number of ways to reach the (i-1)th step (by climbing 1 step from (i-1)th step) and the (i-2)th step (by climbing 2 steps from (i-2)th step).

The time complexity is O(n) as we make one pass through from 3 to n. The space complexity is also O(n) because we keep an array of size n + 1 to store the solutions of subproblems.
"""
def climbstairs(n):
    if n<=2: return n
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
