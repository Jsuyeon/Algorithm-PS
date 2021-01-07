in range(1,n):
    dp[i][0]=min(dp[i-1][0]+home[i][1],dp[i-1][0]+home[i][2])
    dp[i][1]=min(dp[i-1][1]+home[i][0],dp[i-1][1]+home[i][2])
    dp[i][2]=min(dp[i-1][2]+home[i][0],dp[i-1][2]+home[i][1])
print(dp)
