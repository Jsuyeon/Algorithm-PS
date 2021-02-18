import sys
input=sys.stdin.readline

#11053
#algorithm : dp
#가장 긴 증가하는 부분 수열의 길이를 출력하라
n=int(input()) # 수열 a의 크기
a=list(map(int,input().split()))


dp=[0]*(n)
dp[0]=1

for i in range(1,n):
    subdp=[dp[k] for k in range(i) if a[k] < a[i]]
    ai=[a[k] for k in range(i) if a[k] < a[i]]
    if subdp:
        dp[i]=max(subdp)+1
        maxi=ai
    else:
        dp[i]=1

print(max(dp))
print(maxi)
    

