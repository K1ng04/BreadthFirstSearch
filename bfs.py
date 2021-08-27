graph = {1: [2,3],
         2: [4, 5], 
         3: [6],
         4: [],
         5: [6],
         6: [7]    
}

visited = []
queue = [] 
def bfs(visited, graph, val):
    """
    Function used to illustrate the Breadth First Search Algorithm Using Python

                  1
                 / \
                2   3
               / \   \
              4   5-> 6
                       \
                        7
    """
    visited.append(val)
    queue.append(val)
    while queue:
        q = queue.pop(0)
        print(q)
        try:
            for neighbour in graph[q]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        except: 
            pass
bfs(visited, graph, 1)
    
