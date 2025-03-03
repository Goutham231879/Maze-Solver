from collections import deque
import matplotlib.pyplot as plt
import numpy as np


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start[0], start[1], [])])  
    visited = set()

    while queue:
        r, c, path = queue.popleft()

        if (r, c) == end:
            return path + [(r, c)]  

        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != 1:
                queue.append((nr, nc, path + [(r, c)]))

    return None 

def draw_maze(maze, path):
    maze_np = np.array(maze)
    fig, ax = plt.subplots()
    ax.imshow(maze_np, cmap="gray_r")

    
    for (r, c) in path:
        ax.scatter(c, r, color='red', s=100)

    plt.show()

def main():
    maze = [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    start = (0, 0)
    end = (0, 4)

    shortest_path = bfs_maze_solver(maze, start, end)

    if shortest_path:
        print("Shortest Path:", shortest_path)
        draw_maze(maze, shortest_path)
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
