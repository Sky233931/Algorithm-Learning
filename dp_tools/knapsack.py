#0/1背包
def knapsack(velu,weight,capacity):
    n=len(weight)
    dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(capacity+1):
            dp[i][j]=dp[i-1][j]
            if j>=weight[i-1]:
                dp[i][j]=max(dp[i][j],dp[i-1][j-weight[i-1]]+velu[i-1])
    return dp

