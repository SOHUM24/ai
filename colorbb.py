def is_colorable(graph, node, visited, color, c):
    visited[node] = 1
    color[node] = c
    for child in graph[node]:
        if not visited[child]:
            tmp = is_colorable(graph, child, visited, color, c^1)
            # ^ is xor operator if 1 then 0 if 0 then 1
            if tmp == False:
                return False
        else :
            if color[node] == color[child]:
                return False
    return True

# ipt = [[1,2],[2,4],[4,3],[3,1],[2,5],[4,5]]
# n=5
ipt = [[1,2],[2,3],[3,6],[6,5],[5,4],[1,4]]
n=6
graph={}
visited={}
color={}

for i in range(1,n+1):
    graph[i]=[]
    visited[i]=0
    color[i]=None

for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)

temp = (is_colorable(graph,1,visited,color,0))

if temp:
    print("Valid coloring in Graph")
else:
    print("Not valid coloring in Graph")