import sys
input=sys.stdin.readline
###Jsuyeon###

from collections import deque
n,m=map(int,input().split())
maze=[]

for _ in range(n):
    temp=[]
    for val in input().rstrip():
        temp.append(int(val))
    maze.append(temp)



def bfs(graph,i,j,level,size=2):
    if visited[i][j]==True:
        return

    queue=deque([i,j])

    while queue:

        i=queue.popleft()
        j=queue.popleft()
        # print('queue',queue,visited[i][j],(i,j))
        size-=2
        if i==n-1 and j==m-1:
            return level
        if size==0:
            level+=1
        if visited[i][j]==False:
            visited[i][j]=True

        
            if i-1>-1:
                if graph[i-1][j]!=0 and visited[i-1][j]==False:

                    queue.extend([i-1,j])

            if i+1<n :
                if graph[i+1][j]!=0 and visited[i+1][j]==False:

                    queue.extend([i+1,j])

            if j+1<m:
                if graph[i][j+1]!=0 and visited[i][j+1]==False :

                    queue.extend([i,j+1])

            if j-1>-1:
                if graph[i][j-1]!=0 and visited[i][j-1]==False:

                    queue.extend([i,j-1])

        if size!=0:
            continue
        size=len(queue)



visited=[[False]*m for _ in range(n)]
print(bfs(maze,0,0,1))


