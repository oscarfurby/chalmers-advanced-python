## Question 1: directory structure

## Question 2: graph representations
adj_list = {
    0: [1, 3, 2], 
    1: [0, 2], 
    2: [1, 0, 3], 
    3: [2]}

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

def mat2adj(mat, vertices):
    adj = {}
    for key in vertices:
        row = mat[key]
        for val in range(len(row)):
            if mat[key][val]: 
                if key in adj:
                    adj[key].append(val)
                else:
                    adj[key] = [val]
    return adj

print(mat2adj(adj2mat(adj_list), [0,1,2,3]))


## Question 3: equality between graphs


def equal(edges1, edges2):
    def included(edges1, edges2):   #helper function
        for (src, trg) in edges1:
            if (not (src, trg) in edges2) and (not (trg, src) in edges2):
                return False
        return True
    
    if len(edges1) != len(edges2):
        return False
    if included(edges1, edges2) and included(edges2, edges1):
        return True
    return False

print(equal([(1, 2), (2, 3)], [(3, 2), (2, 1)]))
print(equal([(1, 2), (2, 3)], [(3, 2), (2, 2)]))
print(equal([(1, 2), (2, 3)], [(3, 2), (2, 2), (2,1)]))


## Question 4: depth-first search
def bfs(graph, current_node, visit_complete=[]): #breadth-first-search
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
            
bfs(adj_list, 0)

''' PSEUDOCODE FROM WIKIPEDIA
    procedure DFS(G, v) is
        label v as discovered
        for all directed edges from v to w that are in G.adjacentEdges(v) do
            if vertex w is not labeled as discovered then
                recursively call DFS(G, w)
'''

def dfs(graph, current_node, visit_complete=[]): #depth-first-search
    print(current_node)
    visit_complete.append(current_node)
    for neighbour in graph[current_node]:
        if not neighbour in visit_complete:
            dfs(graph, neighbour, visit_complete)

dfs(adj_list, 3)

#Bonus: implement dfs iteratively


## Question 5: multigraphs

multi_edgelist = [(1, 2), (2, 3), (3, 2)]