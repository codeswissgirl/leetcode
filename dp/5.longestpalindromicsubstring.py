"""
1. clarification 
2. appraoch to solve this problem:
a) initiliaze: a 2d array dp of size nxn whre n is the lenght of the string. set all the elements of the dp array to False
b) single character strings: -all single character strings are palindromes, so we set dp[i][i] = to True for all i
c) douple character strings: for all substrings of lenght 2, we set dp[i][i+1] to True i the two characters are the same
d) substrings of lenght 3 and more: 
For substrings of length 3 and more, we check if s[i] == s[j] and dp[i+1][j-1] is True. If yes, we set dp[i][j] to True.
This solution has a time complexity of O(n^2), where n is the length of the string because it has to fill the 2D dp array. The space complexity is also O(n^2) due to the 2D dp array.
"""

def longestpalindrome(s):
    if not s: return ''
    n=len(s)
    dp=[[False]*n for _ in range(n)]
    max_lenght=1
    start=0

    for i in range(n):
        dp[i][i]=True
    #check substrings of length 3 and more
    for length in range(3,n+1):
        for i in range(n-length+1):
            j=i+length-1
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j]=True
                start=i
                max_lenght=length
    return s[start:start+max_lenght]
