# Maze_generation

![Apr-16-2023 22-33-38](https://github.com/ccxxyy23/Maze_generation/assets/119594609/cb220c4c-016f-47a5-bed2-6b7cb4b9e1b1)

implementation of maze generation by Python
There are slight differences in the implementation of maze generation using Prim's algorithm as compared to its original definition. The most significant deviation lies in the process of adding edges. In the original definition, the algorithm selects one vertex from the set and another not in the set, ensuring that the edge between these two vertices has the smallest weight to obtain the minimum spanning tree (MST). However, in maze generation, the 'original graph' has no weights assigned to its edges, rendering the comparison process unnecessary. Instead, the system randomly selects a neighbor edge to generate the maze. Having considered the disparity, I have made modifications to the algorithm.
Furthermore, I have also given great consideration to the initialization of the original graph in order to make the generated mazes more realistic. To achieve this, I created a graph with all vertices and no edges. During program execution, the system will create a list of all the adjacent walls and randomly select one to break and form an edge. The wall is the block between two grids, when the wall is broken, two vertices are connected and one edge is made. To avoid the addition of duplicate edges, a visit list has been implemented to keep track of visited walls.
I use the pixel package to visualize my program. At first, every white vertex exists with no edge. Black walls are also set. The Python code has been added in the Appendix.
The final project will look like this. The left picture is the original graph and the right one is a possible randomly generated maze using the Python program.
<img width="803" alt="Screenshot 2023-09-11 at 18 28 47" src="https://github.com/ccxxyy23/Maze_generation/assets/119594609/f26fc5a8-b490-480b-891b-5e59ff65e484">

The visualization of the randomized Prim's algorithm has been achieved by visually representing the steps of breaking the "walls". As a result, every vertex in the graph is connected, leaving only one path between any two vertices. This guarantees that regardless of the starting and ending points, there will always be only one path connecting them, which perfectly matches the logic of the maze game.

The time complexity of maze generation using Prim's algorithm depends on the implementation of the data structure. Generally, the algorithm uses a priority queue to trace the minimum-weight edges to add to the minimum spanning tree.
If we use an adjacency list to represent the graph, the time complexity for adding an edge to the priority queue is O(log V), where V is the number of vertices in the graph. Since we need to add E edges to the priority queue, the total time complexity of the algorithm is O(E log V).
Otherwise, if we use an adjacency matrix to represent the graph, the time complexity for adding an edge to the priority queue is O(V), meaning the total time complexity of the algorithm becomes O(V^2).
