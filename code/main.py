def add_edge(g,a,b):
    g[a].append(b)

def cycle_detect_util(n,g,visited,crnt_stack):
    if crnt_stack[n]:
        return True
    if visited[n]:
        return False
    
    for i in g[n]:
        if not visited[i]:
            visited[i] = True 
            crnt_stack[i] = True 
            cycle_detect_util(i,g,visited,crnt_stack)
    crnt_stack[n] = False
    return False

def detect_cycle(g,v):
    print("cycle detection: ")
    visited = [False] * v 
    crnt_stack = [False] * v
    for i in range(v):
        if not visited[i] and cycle_detect_util(i,g,visited,crnt_stack):
           return True 
    else:
        return False

def dfs_util(i,g,v):
    v[i] = True 
    print(i, end=" ")
    for n in g[i]:
        if(v[n] == False):
            dfs_util(n,g,v)
    
def dfs(g,len):
    visited = [False for i in range(len)]
    for i in range(len):
        if not visited[i]:
            dfs_util(i,g,visited)

if __name__ == "__main__":
    v,e = map(int, input().split())
    g = [[] for i in range(v)]
    for i in range(e):
        a,b = map(int,input().split())
        add_edge(g,a,b)
    dfs(g,v)
    print()
    if detect_cycle(g,v):
        print("Cycle Detected")
    else:
        print("There is no cycle in the graph")