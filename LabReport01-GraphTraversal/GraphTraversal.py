import random

class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = 999999
        self.grid = []
        self.visited = []
        self.path = []
        self.topological_order = []

    def init(self):
        
        self.N = random.randint(4, 7)
        
        self.grid = [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.N)]
        
        self.source = self.get_random_non_obstacle()
        self.goal = self.get_random_non_obstacle()
        
        while self.source == self.goal:
            self.goal = self.get_random_non_obstacle()
        
        self.visited = [[False for _ in range(self.N)] for _ in range(self.N)]
        
        print("Generated Grid:")
        self.print_grid()
        print(f"Source: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal.x}, {self.goal.y})")
        
        self.st_dfs(self.source)
        
        if self.found:
            print("\nGoal found!")
            print("DFS Path:")
            self.print_path()
            print("\nTopological Order of Node Traversal:")
            self.print_topological_order()
        else:
            print("\nGoal cannot be reached from the starting block.")

    def get_random_non_obstacle(self):
        while True:
            x = random.randint(0, self.N - 1)
            y = random.randint(0, self.N - 1)
            if self.grid[x][y] == 1:
                return Node(x, y, 0)

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def print_path(self):
        path_str = ", ".join([f"({node.x}, {node.y})" for node in self.path])
        print(path_str)

    def print_topological_order(self):
        order_str = ", ".join([f"({node.x}, {node.y})" for node in self.topological_order])
        print(order_str)

    def st_dfs(self, u):
        self.visited[u.x][u.y] = True
        self.topological_order.append(u)
        
        if u.x == self.goal.x and u.y == self.goal.y:
            self.found = True
            self.goal.depth = u.depth
            self.path = self.topological_order.copy()
            return
        
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            
            if (0 <= v_x < self.N) and (0 <= v_y < self.N):
                if self.grid[v_x][v_y] == 1 and not self.visited[v_x][v_y]:
                    v_depth = u.depth + 1
                    child = Node(v_x, v_y, v_depth)
                    self.st_dfs(child)
                    if self.found:
                        return

def main():
    d = DFS()
    d.init()

if __name__ == "__main__":
    main()