import random

class Point:
    def __init__(self, x, y, is_center=False):
        self.x = x
        self.y = y
        self.cluster = None
        self.is_center = is_center

class KMeansModified:
    def __init__(self, points, clusters, grid_size=30):
        self.points_count = points
        self.clusters_count = clusters
        self.grid_size = grid_size
        self.points = []
        self.centers = []
        self.grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
        self.start()

    def start(self):
        self.points = [Point(random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)) for _ in range(self.points_count)]
        self.centers = [Point(random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1), is_center=True) for _ in range(self.clusters_count)]

        while True:
            changed = False
            for p in self.points:
                min_dist = float('inf')
                assigned_cluster = None
                for idx, c in enumerate(self.centers):
                    dist = abs(c.x - p.x) + abs(c.y - p.y)  
                    if dist < min_dist:
                        min_dist = dist
                        assigned_cluster = idx
                if p.cluster != assigned_cluster:
                    changed = True
                    p.cluster = assigned_cluster

            for idx in range(self.clusters_count):
                cluster_points = [p for p in self.points if p.cluster == idx]
                if cluster_points:
                    avg_x = sum(p.x for p in cluster_points) // len(cluster_points)
                    avg_y = sum(p.y for p in cluster_points) // len(cluster_points)
                    self.centers[idx].x = avg_x
                    self.centers[idx].y = avg_y

            if not changed:
                break

        for p in self.points:
            self.grid[p.y][p.x] = str(p.cluster)

        for center in self.centers:
            self.grid[center.y][center.x] = '*'

        for idx, center in enumerate(self.centers):
            print(f"Cluster {idx + 1} Center - ({center.x}, {center.y})")

        for idx in range(self.clusters_count):
            cluster_points = [p for p in self.points if p.cluster == idx]
            intra_distance = sum(abs(p.x - self.centers[idx].x) + abs(p.y - self.centers[idx].y) for p in cluster_points)
            print(f"Cluster {idx + 1} Intra-distance = {intra_distance}")

        for p in self.points:
            print(f"Point ({p.x}, {p.y}) - Cluster {p.cluster + 1}")

        print("\nClustered Data Visualization:\n")
        for row in self.grid:
            print(' '.join(row))
        print("\nLegend: '*' = Center, '0-9' = Cluster numbers")

def main():
    points = int(input("Insert number of points: "))
    clusters = int(input("Insert number of clusters: "))
    kmeans = KMeansModified(points, clusters)

if __name__ == "__main__":
    main()
