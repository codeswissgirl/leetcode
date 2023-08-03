"""
1. clarification:
- to hte houses are in circle, the first and last houses are neighbors?
- maximum amount of money is 0 if hte list is empty?
-are all the input values non-negative integers?
-the robber cannot rob ajdacent houses,correct?

2. identify problem type:
- i belive that this problem is a variant of dynamic programming problem, with the added constraint that hte houses are arranged by circle

3. define appraoch
the presence of the circular condition means we have two cases to consider:
case 1: do not rob house 0, hence we can rob house 'n-1'
case 2: do not orb house 'n-1', hence we can rob house 0.


"""

def rob(nums):
    def rob_linear(nums):
        #linear case
        house1=house2=0
        for i in nums:
            house1,house2=house2,max(house1+i,house2)
        return house2
    
    if len(nums)==0: return 0
    elif len(nums)==1: return nums[0]
    else: #either the first house or the last house 
        return max(rob_linear[nums:-1], rob_linear[nums[1:]])
    
