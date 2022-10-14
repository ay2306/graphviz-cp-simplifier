# Graphvis-CP-Simplifier

This is an open source project for creating animated graphs.
The project currently supports three types of animation:
1. Depth First Search Animation (DFS)
2. Breadth First Search Animation (BFS)
3. Cycle Detection in a Directed Graph

Currently the project generates random graphs. A new graph is generated each time the page is refreshed.

## How to run?

1. Download the files and save it
2. Open the terminal and navigate to /graphviz-cp-simplifier/dsa_animator
3. Use this command to run the server
    ```bash
    $ python3 manage.py runserver
    ```
4. Open the browser and navigate to 
   1. DFS: http://127.0.0.1:8000/animate/ 
   2. BFS: http://127.0.0.1:8000/animate/multi_source_bfs
   3. Cycle Detection in a Directed Graph: http://127.0.0.1:8000/animate/cycle_detection_direct

