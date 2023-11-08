## Question 1: directory structure

## Question 2: graph representations
adj_list = {0: [1, 3, 2], 1: [0, 2], 2: [1, 0, 3], 3: [2]}

def adj2mat(adj):
    n = len(adj)
    matrix = []
    for _ in range(n):
        matrix.append([False] * n)
    for (key, values) in adj.items():
        for value in values:
            matrix[key][value] = True
    return matrix

print(adj2mat(adj_list))

#Bonus: write a function that checks that the resulting matrix is n*n

def mat2adj(mat):
    

## Question 3: equality between graphs
def equal(edges1, edges2):
    pass

## Question 4: depth-first search
def bfs(graph, current_node, visit_complete=[]):
    visit_complete.append(current_node)
    queue = []
    queue.append(current_node)
 
    while queue:
        s = queue.pop(0)
        print(s)
 
        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)

''' PSEUDOCODE FROM WIKIPEDIA
    procedure DFS(G, v) is
        label v as discovered
        for all directed edges from v to w that are in G.adjacentEdges(v) do
            if vertex w is not labeled as discovered then
                recursively call DFS(G, w)
'''

def dfs():
    pass

## Question 5: multigraphs
