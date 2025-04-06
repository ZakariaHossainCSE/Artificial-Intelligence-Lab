4refdef iddfs_maze_solver(grid, start, target):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    max_depth = rows * cols
    
    for depth in range(1, max_depth + 1):
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        stack = [(start[0], start[1], 0, [start])] 
        
        while stack:
            row, col, current_depth, path = stack.pop()
            
            if row == target[0] and col == target[1]:
                return True, path, depth
            
            if current_depth >= depth:
                continue
                
            if not (0 <= row < rows and 0 <= col < cols):
                continue
                
            if grid[row][col] == 1 or visited[row][col]:
                continue
                
            visited[row][col] = True
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    stack.append((new_row, new_col, current_depth + 1, path + [(new_row, new_col)]))
    
    return False, None, max_depth

def main():
    print("Enter maze dimensions (rows columns):")
    rows, cols = map(int, input().split())
    
    print(f"Enter {rows} rows with {cols} numbers:")
    grid = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} numbers, got {len(row)}")
            return
        grid.append(row)
    
    print("Enter start coordinates (row column):")
    start = tuple(map(int, input().split()))
    
    print("Enter target coordinates (row column):")
    target = tuple(map(int, input().split()))
    
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        print("Error: Start position is out of bounds")
        return
    if not (0 <= target[0] < rows and 0 <= target[1] < cols):
        print("Error: Target position is out of bounds")
        return
    if grid[start[0]][start[1]] == 1:
        print("Error: Start position is a wall")
        return
    if grid[target[0]][target[1]] == 1:
        print("Error: Target position is a wall")
        return
    
    found, path, depth = iddfs_maze_solver(grid, start, target)
    
    if found:
        print(f"\nPath found at depth {depth} using IDDFS")
        print("Traversal Order:", path)
    else:
        print(f"\nPath not found at max depth {depth} using IDDFS")

if __name__ == "__main__":
    main()