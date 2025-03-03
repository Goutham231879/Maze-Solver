
# 🏁 Maze Solver (BFS & DFS)

## 📌 Overview
The **Maze Solver** is an algorithmic project that finds the **shortest path** in a given maze using **Breadth-First Search (BFS)** and explores paths using **Depth-First Search (DFS)**. It takes a **2D grid** as input and outputs the path from the **start position** to the **end position**.

## 🔹 Features
✔️ Finds the **shortest path** using **BFS**  
✔️ Explores all possible paths using **DFS**  
✔️ Handles **obstacles** (walls) in the maze  
✔️ **Visual representation** of the solution using `matplotlib` (Python)  
✔️ Supports **user-defined mazes**  

## 📌 Algorithms Used
### 🔹 **Breadth-First Search (BFS) - Shortest Path**
- Uses a **queue** (FIFO) for level-wise exploration.
- Ensures the **shortest path** in an unweighted grid.
- **Time Complexity**: `O(N × M)`, where `N` and `M` are grid dimensions.

### 🔹 **Depth-First Search (DFS) - Alternative Path Finding**
- Uses **recursion** or a **stack** to explore deep paths first.
- **Not guaranteed** to find the shortest path.
- **Time Complexity**: `O(N × M)`.

---

## 📌 Project Structure
```
Maze-Solver/
│── maze_solver.py (Python implementation)
│── MazeSolver.java (Java implementation)
│── maze_solution.png (Generated solution image)
│── README.md (Project documentation)
│── requirements.txt (Python dependencies)

```

---

## 📌 Setup Instructions

### 🔹 **Python Setup**
1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/maze-solver.git
cd maze-solver
```

2️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

3️⃣ **Run the Python Code**
```sh
python maze_solver.py
```

4️⃣ **View the Solution Image**  
The solved maze will be saved as `maze_solution.png`. Open it to see the path.

---

### 🔹 **Java Setup**
1️⃣ **Compile and Run the Java Code**
```sh
javac MazeSolver.java
java MazeSolver
```

---

## 📌 Example Maze Representation
The maze is represented as a **2D grid**, where:
- `0` → Open path
- `1` → Wall (Blocked)
- `S` → Start position
- `E` → End position

### 🔹 **Example Input**
```plaintext
S  0  1  0  E
0  1  0  1  0
0  0  0  1  0
1  1  0  0  0
0  0  0  1  0
```

### 🔹 **Expected Output (BFS Shortest Path)**
```plaintext
Shortest Path:
[0, 0]
[0, 1]
[1, 1]
[2, 1]
[2, 2]
[3, 2]
[3, 3]
[3, 4]
[4, 4]
```

---

## 📌 Future Enhancements
🔹 Add **GUI version using Pygame** 🎮  
🔹 Implement **A* Algorithm** for optimized pathfinding  
🔹 Allow **random maze generation**  

---

## 📌 Contributors
💡 **Goutham Parveda**  
📧 gouth2a3m@gmail.com  
🔗 [GitHub](https://github.com/your-username)  
🔗 [LinkedIn](https://www.linkedin.com/in/goutham-parveda/)  

---



