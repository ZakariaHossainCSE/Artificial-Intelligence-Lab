def is_safe(graph, color, v, c):
    """Check if color c can be assigned to vertex v"""
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, k, color, v):
    """Backtracking utility function"""
    if v == len(graph):
        return True
    
    for c in range(1, k+1):
        if is_safe(graph, color, v, c):
            color[v] = c
            if graph_coloring_util(graph, k, color, v+1):
                return True
            color[v] = 0  # Backtrack
    
    return False

def solve_graph_coloring():
    """Main function to handle input and output"""
    print("Enter graph details:")
    # Read N, M, K
    while True:
        try:
            first_line = input().strip()
            if first_line:
                N, M, K = map(int, first_line.split())
                break
        except:
            print("Invalid input. Please enter N M K on first line")
    
    # Read edges
    edges = []
    print("Enter edges (one per line):")
    for _ in range(M):
        while True:
            try:
                line = input().strip()
                if line:
                    u, v = map(int, line.split())
                    edges.append((u, v))
                    break
            except:
                print("Invalid edge. Please enter u v")
    
    # Create adjacency matrix
    graph = [[0]*N for _ in range(N)]
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1
    
    color = [0] * N
    
    if graph_coloring_util(graph, K, color, 0):
        print("\nColoring Possible with", K, "Colors")
        print("Color Assignment:", color)
    else:
        print("\nColoring Not Possible with", K, "Colors")

def main():
   
    while True:
        solve_graph_coloring()
        print("\nWould you like to solve another case? (y/n)")
        if input().strip().lower() != 'y':
            break

if __name__ == "__main__":
    main()