import sys
input=sys.stdin.readline


n=int(input())
dangi=[]
for _ in range(n):
    temp=[]
    for val in input().rstrip():
        temp.append(int(val))
    dangi.append(temp)

for val in dangi:
    print(val)

def dfs(graph,i,j,visited=[]):
    if visited[i][j]==True:
        return
    visited=visited+[i,j]
    graph[i][j]=0
    if i+1<n:
        print('아래')
        if visited[i+1][j]==False and graph[i+1][j]==1:
            dfs(graph,i+1,j,visited)
    if i-1>-1:
        print('위')
        if visited[i-1][j]==False and graph[i-1][j]==1:
            dfs(graph,i-1,j,visited)
    if j+1<n:
        print('오')
        if visited[i][j+1]==False and graph[i][j+1]==1:
            dfs(graph,i,j+1,visited)
    if j-1>-1:
        print('왼')
        if visited[i][j-1]==False and graph[i][j-1]==1:
            dfs(graph,i,j-1,visited)
    return visited

visited=[[False]*n for _ in range(n)]

a=[]
cnt=0
for i in range(n):
    for j in range(n):
        if dangi[i][j]==0:
            continue
        ans=dfs(dangi,i,j,visited=[])
        if ans==None:
            pass
        else:
            a.append(ans)
print(a)


