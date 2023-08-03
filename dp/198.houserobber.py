"""
clarification
First, I would make sure that I understand the problem by asking clarifying questions:
-Are all the values in the input list non-negative integers?
-If the input list is empty, the maximum amount of money is 0, correct?
-So, the robber cannot rob adjacent houses, right?

Identify Problem Type
This is a dynamic programming problem. The task is to find an optimal solution (maximum amount of money),
Define Appraoch:
We can solve this problem using a dynamic programming approach. Let's denote dp[i] as the maximum amount of money that can be robbed considering the first i houses. The transition function will be dp[i] = max(dp[i-2] + nums[i], dp[i-1]), meaning at the ith house, we can either choose to rob it (in which case we add the current house's money to the max money of i-2th house), or not rob it (then the max money will be the max money robbed from the previous house).

"""


def rob(nums):
    if not nums: return 0
    n=len(nums)
    if n==1: return nums[0]
    dp=[0]*n
    dp[0],dp[1]=nums[0], max(nums[0],nums[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+nums[i])

    return dp[-1]
