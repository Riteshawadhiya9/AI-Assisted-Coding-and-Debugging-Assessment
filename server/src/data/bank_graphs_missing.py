# Missing Graph Questions (10 Questions)

MISSING_GRAPH_QUESTIONS = [
    {
        "id": "q_graph_center_star",
        "title": "Find Center of Star Graph",
        "problemStatement": "There is an undirected star graph consisting of `n` nodes labeled from `1` to `n`. A star graph is a graph where there is one center node and exactly `n - 1` edges that connect the center node with every other node.\n\nYou are given a 2D integer array `edges` where each `edges[i] = [u_i, v_i]` indicates that there is an edge between the nodes `u_i` and `v_i`.\n\nReturn the center of the given star graph.",
        "topic": "graphs",
        "subtopic": "degrees",
        "difficulty": "easy",
        "estimatedTime": 10,
        "primaryBugType": "incorrect condition",
        "bugConcept": "Returning the non-matching peripheral node instead of the common center vertex",
        "intendedApproach": "Compare the endpoints of the first two edges. The node that appears in both edges is the center node.",
        "explanation": "If `edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]`, the common node is `edges[0][0]`. Returning `edges[0][1]` selects the outer peripheral node.",
        "constraints": [
            "3 <= n <= 10^5",
            "edges.length == n - 1",
            "edges[i].length == 2",
            "1 <= ui, vi <= n",
            "ui != vi",
            "The given edges represent a valid star graph.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "edges = [[1,2],[2,3],[4,2]]",
                "expectedOutput": "2",
                "isHidden": False,
                "explanation": "Node 2 is connected to every other node (1, 3, 4), so 2 is the center.",
            },
            {
                "id": 2,
                "input": "edges = [[1,2],[5,1],[1,3],[1,4]]",
                "expectedOutput": "1",
                "isHidden": False,
                "explanation": "Node 1 is present in every edge, so 1 is the center.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "edges = [[3,1],[3,2]]",
                "expectedOutput": "3",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "edges = [[4,1],[2,4],[3,4]]",
                "expectedOutput": "4",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(1)",
            "space": "O(1)",
        },
        "tags": [
            "graphs",
            "degrees",
            "easy",
        ],
        "visualData": {
            "type": "graph",
            "title": "Star Graph Topology",
            "data": {
                "nodes": [
                    {
                        "id": "1",
                    },
                    {
                        "id": "2",
                    },
                    {
                        "id": "3",
                    },
                    {
                        "id": "4",
                    },
                ],
                "edges": [
                    {
                        "from": "1",
                        "to": "2",
                    },
                    {
                        "from": "2",
                        "to": "3",
                    },
                    {
                        "from": "4",
                        "to": "2",
                    },
                ],
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "int findCenter(int** edges, int edgesSize, int* edgesColSize) {\n    if (edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]) {\n        return edges[0][1];\n    }\n    return edges[0][0];\n}",
                "correctCode": "int findCenter(int** edges, int edgesSize, int* edgesColSize) {\n    if (edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]) {\n        return edges[0][0];\n    }\n    return edges[0][1];\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int findCenter(vector<vector<int>>& edges) {\n        if (edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]) {\n            return edges[0][1];\n        }\n        return edges[0][0];\n    }\n};",
                "correctCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int findCenter(vector<vector<int>>& edges) {\n        if (edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]) {\n            return edges[0][0];\n        }\n        return edges[0][1];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int findCenter(int[][] edges) {\n        if (edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]) {\n            return edges[0][1];\n        }\n        return edges[0][0];\n    }\n}",
                "correctCode": "class Solution {\n    public int findCenter(int[][] edges) {\n        if (edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1]) {\n            return edges[0][0];\n        }\n        return edges[0][1];\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_path_exists",
        "title": "Find if Path Exists in Graph",
        "problemStatement": "There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (inclusive). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [u_i, v_i]` denotes a bi-directional edge between vertex `u_i` and vertex `v_i`. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.\n\nYou want to determine if there is a valid path that exists from vertex `source` to vertex `destination`.\n\nGiven `edges` and the integers `n`, `source`, and `destination`, return `true` if there is a valid path from `source` to `destination`, or `false` otherwise.",
        "topic": "graphs",
        "subtopic": "bfs-dfs",
        "difficulty": "easy",
        "estimatedTime": 15,
        "primaryBugType": "incorrect traversal",
        "bugConcept": "Building directed adjacency edges instead of bi-directional edges for undirected graph",
        "intendedApproach": "Construct an adjacency list with bidirectional edges for each [u, v]. Run BFS or DFS from source. Return true if destination is reached.",
        "explanation": "Only adding edge `u -> v` prevents paths where edge traversal requires moving in the `v -> u` direction.",
        "constraints": [
            "1 <= n <= 2 * 10^5",
            "0 <= edges.length <= 2 * 10^5",
            "edges[i].length == 2",
            "0 <= ui, vi <= n - 1",
            "ui != vi",
            "0 <= source, destination <= n - 1",
            "There are no duplicate edges or self-loops.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2",
                "expectedOutput": "true",
                "isHidden": False,
                "explanation": "There are two paths from vertex 0 to vertex 2: 0 -> 1 -> 2, and 0 -> 2.",
            },
            {
                "id": 2,
                "input": "n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5",
                "expectedOutput": "false",
                "isHidden": False,
                "explanation": "There is no path from vertex 0 to vertex 5.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "n = 1, edges = [], source = 0, destination = 0",
                "expectedOutput": "true",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "n = 3, edges = [[1,0],[2,1]], source = 0, destination = 2",
                "expectedOutput": "true",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(V + E)",
            "space": "O(V + E)",
        },
        "tags": [
            "graphs",
            "dfs",
            "bfs",
            "easy",
        ],
        "visualData": {
            "type": "graph",
            "title": "Graph Reachability",
            "data": {
                "nodes": [
                    {
                        "id": "0",
                    },
                    {
                        "id": "1",
                    },
                    {
                        "id": "2",
                    },
                ],
                "edges": [
                    {
                        "from": "0",
                        "to": "1",
                    },
                    {
                        "from": "1",
                        "to": "2",
                    },
                    {
                        "from": "2",
                        "to": "0",
                    },
                ],
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n#include <stdlib.h>\n\nstruct Edge { int to; struct Edge* next; };\n\nbool dfs(int node, int dst, struct Edge** adj, bool* visited) {\n    if (node == dst) return true;\n    visited[node] = true;\n    for (struct Edge* e = adj[node]; e; e = e->next) {\n        if (!visited[e->to] && dfs(e->to, dst, adj, visited)) return true;\n    }\n    return false;\n}\n\nbool validPath(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination) {\n    struct Edge** adj = (struct Edge**)calloc(n, sizeof(struct Edge*));\n    for (int i = 0; i < edgesSize; i++) {\n        int u = edges[i][0], v = edges[i][1];\n        struct Edge* e1 = (struct Edge*)malloc(sizeof(struct Edge));\n        e1->to = v; e1->next = adj[u]; adj[u] = e1;\n    }\n    bool* visited = (bool*)calloc(n, sizeof(bool));\n    bool res = dfs(source, destination, adj, visited);\n    free(visited);\n    return res;\n}",
                "correctCode": "#include <stdbool.h>\n#include <stdlib.h>\n\nstruct Edge { int to; struct Edge* next; };\n\nbool dfs(int node, int dst, struct Edge** adj, bool* visited) {\n    if (node == dst) return true;\n    visited[node] = true;\n    for (struct Edge* e = adj[node]; e; e = e->next) {\n        if (!visited[e->to] && dfs(e->to, dst, adj, visited)) return true;\n    }\n    return false;\n}\n\nbool validPath(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination) {\n    struct Edge** adj = (struct Edge**)calloc(n, sizeof(struct Edge*));\n    for (int i = 0; i < edgesSize; i++) {\n        int u = edges[i][0], v = edges[i][1];\n        struct Edge* e1 = (struct Edge*)malloc(sizeof(struct Edge));\n        e1->to = v; e1->next = adj[u]; adj[u] = e1;\n        struct Edge* e2 = (struct Edge*)malloc(sizeof(struct Edge));\n        e2->to = u; e2->next = adj[v]; adj[v] = e2;\n    }\n    bool* visited = (bool*)calloc(n, sizeof(bool));\n    bool res = dfs(source, destination, adj, visited);\n    free(visited);\n    return res;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {\n        if (source == destination) return true;\n        vector<vector<int>> adj(n);\n        for (auto& e : edges) {\n            adj[e[0]].push_back(e[1]);\n        }\n        vector<bool> visited(n, false);\n        queue<int> q;\n        q.push(source);\n        visited[source] = true;\n        while (!q.empty()) {\n            int u = q.front();\n            q.pop();\n            if (u == destination) return true;\n            for (int v : adj[u]) {\n                if (!visited[v]) {\n                    visited[v] = true;\n                    q.push(v);\n                }\n            }\n        }\n        return false;\n    }\n};",
                "correctCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {\n        if (source == destination) return true;\n        vector<vector<int>> adj(n);\n        for (auto& e : edges) {\n            adj[e[0]].push_back(e[1]);\n            adj[e[1]].push_back(e[0]);\n        }\n        vector<bool> visited(n, false);\n        queue<int> q;\n        q.push(source);\n        visited[source] = true;\n        while (!q.empty()) {\n            int u = q.front();\n            q.pop();\n            if (u == destination) return true;\n            for (int v : adj[u]) {\n                if (!visited[v]) {\n                    visited[v] = true;\n                    q.push(v);\n                }\n            }\n        }\n        return false;\n    }\n};",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    public boolean validPath(int n, int[][] edges, int source, int destination) {\n        if (source == destination) return true;\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());\n        for (int[] e : edges) {\n            adj.get(e[0]).add(e[1]);\n        }\n        boolean[] visited = new boolean[n];\n        Queue<Integer> q = new LinkedList<>();\n        q.add(source);\n        visited[source] = true;\n        while (!q.isEmpty()) {\n            int curr = q.poll();\n            if (curr == destination) return true;\n            for (int next : adj.get(curr)) {\n                if (!visited[next]) {\n                    visited[next] = true;\n                    q.add(next);\n                }\n            }\n        }\n        return false;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    public boolean validPath(int n, int[][] edges, int source, int destination) {\n        if (source == destination) return true;\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());\n        for (int[] e : edges) {\n            adj.get(e[0]).add(e[1]);\n            adj.get(e[1]).add(e[0]);\n        }\n        boolean[] visited = new boolean[n];\n        Queue<Integer> q = new LinkedList<>();\n        q.add(source);\n        visited[source] = true;\n        while (!q.isEmpty()) {\n            int curr = q.poll();\n            if (curr == destination) return true;\n            for (int next : adj.get(curr)) {\n                if (!visited[next]) {\n                    visited[next] = true;\n                    q.add(next);\n                }\n            }\n        }\n        return false;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_number_of_provinces",
        "title": "Number of Provinces",
        "problemStatement": "There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.\n\nA province is a group of directly or indirectly connected cities and no other cities outside of the group.\n\nYou are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i-th` city and the `j-th` city are directly connected, and `isConnected[i][j] = 0` otherwise.\n\nReturn the total number of provinces.",
        "topic": "graphs",
        "subtopic": "connected-components",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect traversal",
        "bugConcept": "Omitting visited mark at start of component DFS causing endless cycles",
        "intendedApproach": "Iterate through cities from 0 to n - 1. If city i is not visited, increment province count and launch DFS/BFS to visit all reachable cities, marking visited[curr] = true.",
        "explanation": "If `visited[city] = true` is omitted inside DFS, two mutually connected cities ping-pong back and forth leading to stack overflow.",
        "constraints": [
            "1 <= n <= 200",
            "n == isConnected.length",
            "n == isConnected[i].length",
            "isConnected[i][j] is 1 or 0.",
            "isConnected[i][i] == 1",
            "isConnected[i][j] == isConnected[j][i]",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "isConnected = [[1,1,0],[1,1,0],[0,0,1]]",
                "expectedOutput": "2",
                "isHidden": False,
                "explanation": "Cities 0 and 1 are connected, and city 2 is separate, forming 2 provinces.",
            },
            {
                "id": 2,
                "input": "isConnected = [[1,0,0],[0,1,0],[0,0,1]]",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "No cities are connected to each other, forming 3 separate provinces.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "isConnected = [[1]]",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "isConnected = [[1,1,1],[1,1,1],[1,1,1]]",
                "expectedOutput": "1",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N^2)",
            "space": "O(N)",
        },
        "tags": [
            "graphs",
            "dfs",
            "bfs",
            "union-find",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Province Adjacency Matrix",
            "data": [
                [
                    1,
                    1,
                    0,
                ],
                [
                    1,
                    1,
                    0,
                ],
                [
                    0,
                    0,
                    1,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n\nvoid dfs(int city, int** isConnected, int n, bool* visited) {\n    for (int j = 0; j < n; j++) {\n        if (isConnected[city][j] == 1 && !visited[j]) {\n            dfs(j, isConnected, n, visited);\n        }\n    }\n}\n\nint findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {\n    int n = isConnectedSize;\n    bool visited[205] = {false};\n    int provinces = 0;\n    for (int i = 0; i < n; i++) {\n        if (!visited[i]) {\n            provinces++;\n            dfs(i, isConnected, n, visited);\n        }\n    }\n    return provinces;\n}",
                "correctCode": "#include <stdbool.h>\n\nvoid dfs(int city, int** isConnected, int n, bool* visited) {\n    visited[city] = true;\n    for (int j = 0; j < n; j++) {\n        if (isConnected[city][j] == 1 && !visited[j]) {\n            dfs(j, isConnected, n, visited);\n        }\n    }\n}\n\nint findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {\n    int n = isConnectedSize;\n    bool visited[205] = {false};\n    int provinces = 0;\n    for (int i = 0; i < n; i++) {\n        if (!visited[i]) {\n            provinces++;\n            dfs(i, isConnected, n, visited);\n        }\n    }\n    return provinces;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\n    void dfs(int city, vector<vector<int>>& isConnected, vector<bool>& visited) {\n        for (int j = 0; j < (int)isConnected.size(); j++) {\n            if (isConnected[city][j] == 1 && !visited[j]) {\n                dfs(j, isConnected, visited);\n            }\n        }\n    }\npublic:\n    int findCircleNum(vector<vector<int>>& isConnected) {\n        int n = isConnected.size();\n        vector<bool> visited(n, false);\n        int provinces = 0;\n        for (int i = 0; i < n; i++) {\n            if (!visited[i]) {\n                provinces++;\n                dfs(i, isConnected, visited);\n            }\n        }\n        return provinces;\n    }\n};",
                "correctCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\n    void dfs(int city, vector<vector<int>>& isConnected, vector<bool>& visited) {\n        visited[city] = true;\n        for (int j = 0; j < (int)isConnected.size(); j++) {\n            if (isConnected[city][j] == 1 && !visited[j]) {\n                dfs(j, isConnected, visited);\n            }\n        }\n    }\npublic:\n    int findCircleNum(vector<vector<int>>& isConnected) {\n        int n = isConnected.size();\n        vector<bool> visited(n, false);\n        int provinces = 0;\n        for (int i = 0; i < n; i++) {\n            if (!visited[i]) {\n                provinces++;\n                dfs(i, isConnected, visited);\n            }\n        }\n        return provinces;\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    private void dfs(int city, int[][] isConnected, boolean[] visited) {\n        for (int j = 0; j < isConnected.length; j++) {\n            if (isConnected[city][j] == 1 && !visited[j]) {\n                dfs(j, isConnected, visited);\n            }\n        }\n    }\n    public int findCircleNum(int[][] isConnected) {\n        int n = isConnected.length;\n        boolean[] visited = new boolean[n];\n        int count = 0;\n        for (int i = 0; i < n; i++) {\n            if (!visited[i]) {\n                count++;\n                dfs(i, isConnected, visited);\n            }\n        }\n        return count;\n    }\n}",
                "correctCode": "class Solution {\n    private void dfs(int city, int[][] isConnected, boolean[] visited) {\n        visited[city] = true;\n        for (int j = 0; j < isConnected.length; j++) {\n            if (isConnected[city][j] == 1 && !visited[j]) {\n                dfs(j, isConnected, visited);\n            }\n        }\n    }\n    public int findCircleNum(int[][] isConnected) {\n        int n = isConnected.length;\n        boolean[] visited = new boolean[n];\n        int count = 0;\n        for (int i = 0; i < n; i++) {\n            if (!visited[i]) {\n                count++;\n                dfs(i, isConnected, visited);\n            }\n        }\n        return count;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_flood_fill",
        "title": "Flood Fill",
        "problemStatement": "An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.\n\nYou are also given three integers `sr`, `sc`, and `color`. You should perform a flood fill on the image starting from the pixel `image[sr][sc]`.\n\nTo perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `color`.\n\nReturn the modified image after performing the flood fill.",
        "topic": "graphs",
        "subtopic": "grid-dfs",
        "difficulty": "easy",
        "estimatedTime": 15,
        "primaryBugType": "edge case",
        "bugConcept": "Missing guard for when starting pixel already matches new target color",
        "intendedApproach": "Record original color = image[sr][sc]. If original color equals target color, return image immediately. Recursively paint adjacent 4-directional pixels of original color with newColor.",
        "explanation": "When `image[sr][sc] == color`, replacing each pixel with `color` leaves it equal to original color, triggering infinite recursive loops on adjacent cells.",
        "constraints": [
            "m == image.length",
            "n == image[i].length",
            "1 <= m, n <= 50",
            "0 <= image[i][j], color < 2^16",
            "0 <= sr < m",
            "0 <= sc < n",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2",
                "expectedOutput": "[[2,2,2],[2,2,0],[2,0,1]]",
                "isHidden": False,
                "explanation": "From the center of the image at coordinate (1, 1), all connected pixels with the same color are colored with 2.",
            },
            {
                "id": 2,
                "input": "image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0",
                "expectedOutput": "[[0,0,0],[0,0,0]]",
                "isHidden": False,
                "explanation": "The starting pixel is already of color 2 and has no neighboring pixels of the same old color, so no changes are made.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "image = [[0]], sr = 0, sc = 0, color = 2",
                "expectedOutput": "[[2]]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "image = [[1,1],[1,0]], sr = 0, sc = 0, color = 1",
                "expectedOutput": "[[1,1],[1,0]]",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(M * N)",
        },
        "tags": [
            "graphs",
            "dfs",
            "bfs",
            "matrix",
            "easy",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Flood Fill Grid",
            "data": [
                [
                    1,
                    1,
                    1,
                ],
                [
                    1,
                    1,
                    0,
                ],
                [
                    1,
                    0,
                    1,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "void dfs(int** image, int m, int n, int r, int c, int oldColor, int newColor) {\n    if (r < 0 || r >= m || c < 0 || c >= n || image[r][c] != oldColor) return;\n    image[r][c] = newColor;\n    dfs(image, m, n, r + 1, c, oldColor, newColor);\n    dfs(image, m, n, r - 1, c, oldColor, newColor);\n    dfs(image, m, n, r, c + 1, oldColor, newColor);\n    dfs(image, m, n, r, c - 1, oldColor, newColor);\n}\n\nint** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) {\n    *returnSize = imageSize;\n    *returnColumnSizes = imageColSize;\n    dfs(image, imageSize, imageColSize[0], sr, sc, image[sr][sc], color);\n    return image;\n}",
                "correctCode": "void dfs(int** image, int m, int n, int r, int c, int oldColor, int newColor) {\n    if (r < 0 || r >= m || c < 0 || c >= n || image[r][c] != oldColor) return;\n    image[r][c] = newColor;\n    dfs(image, m, n, r + 1, c, oldColor, newColor);\n    dfs(image, m, n, r - 1, c, oldColor, newColor);\n    dfs(image, m, n, r, c + 1, oldColor, newColor);\n    dfs(image, m, n, r, c - 1, oldColor, newColor);\n}\n\nint** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) {\n    *returnSize = imageSize;\n    *returnColumnSizes = imageColSize;\n    if (image[sr][sc] == color) return image;\n    dfs(image, imageSize, imageColSize[0], sr, sc, image[sr][sc], color);\n    return image;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\n    void dfs(vector<vector<int>>& image, int r, int c, int oldColor, int newColor) {\n        if (r < 0 || r >= (int)image.size() || c < 0 || c >= (int)image[0].size() || image[r][c] != oldColor) return;\n        image[r][c] = newColor;\n        dfs(image, r + 1, c, oldColor, newColor);\n        dfs(image, r - 1, c, oldColor, newColor);\n        dfs(image, r, c + 1, oldColor, newColor);\n        dfs(image, r, c - 1, oldColor, newColor);\n    }\npublic:\n    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {\n        dfs(image, sr, sc, image[sr][sc], color);\n        return image;\n    }\n};",
                "correctCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\n    void dfs(vector<vector<int>>& image, int r, int c, int oldColor, int newColor) {\n        if (r < 0 || r >= (int)image.size() || c < 0 || c >= (int)image[0].size() || image[r][c] != oldColor) return;\n        image[r][c] = newColor;\n        dfs(image, r + 1, c, oldColor, newColor);\n        dfs(image, r - 1, c, oldColor, newColor);\n        dfs(image, r, c + 1, oldColor, newColor);\n        dfs(image, r, c - 1, oldColor, newColor);\n    }\npublic:\n    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {\n        if (image[sr][sc] == color) return image;\n        dfs(image, sr, sc, image[sr][sc], color);\n        return image;\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    private void dfs(int[][] image, int r, int c, int oldColor, int newColor) {\n        if (r < 0 || r >= image.length || c < 0 || c >= image[0].length || image[r][c] != oldColor) return;\n        image[r][c] = newColor;\n        dfs(image, r + 1, c, oldColor, newColor);\n        dfs(image, r - 1, c, oldColor, newColor);\n        dfs(image, r, c + 1, oldColor, newColor);\n        dfs(image, r, c - 1, oldColor, newColor);\n    }\n    public int[][] floodFill(int[][] image, int sr, int sc, int color) {\n        dfs(image, sr, sc, image[sr][sc], color);\n        return image;\n    }\n}",
                "correctCode": "class Solution {\n    private void dfs(int[][] image, int r, int c, int oldColor, int newColor) {\n        if (r < 0 || r >= image.length || c < 0 || c >= image[0].length || image[r][c] != oldColor) return;\n        image[r][c] = newColor;\n        dfs(image, r + 1, c, oldColor, newColor);\n        dfs(image, r - 1, c, oldColor, newColor);\n        dfs(image, r, c + 1, oldColor, newColor);\n        dfs(image, r, c - 1, oldColor, newColor);\n    }\n    public int[][] floodFill(int[][] image, int sr, int sc, int color) {\n        if (image[sr][sc] == color) return image;\n        dfs(image, sr, sc, image[sr][sc], color);\n        return image;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_find_town_judge",
        "title": "Find the Town Judge",
        "problemStatement": "In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.\n\nIf the town judge exists, then:\n1. The town judge trusts nobody.\n2. Everybody (except for the town judge) trusts the town judge.\n3. There is exactly one person that satisfies properties 1 and 2.\n\nYou are given an array `trust` where `trust[i] = [a_i, b_i]` representing that the person labeled `a_i` trusts the person labeled `b_i`.\n\nReturn the label of the town judge if the town judge exists and can be identified, or return `-1` otherwise.",
        "topic": "graphs",
        "subtopic": "degrees",
        "difficulty": "easy",
        "estimatedTime": 15,
        "primaryBugType": "boundary",
        "bugConcept": "Requiring judge score to equal n instead of n - 1",
        "intendedApproach": "Count net trust score = indegree - outdegree for each person. The judge must have net score == n - 1 (trusted by all n - 1 other people, trusts 0 people).",
        "explanation": "Since the judge cannot trust themselves, maximum incoming trust is n - 1. Checking `score == n` guarantees no judge is ever identified.",
        "constraints": [
            "1 <= n <= 1000",
            "0 <= trust.length <= 10^4",
            "trust[i].length == 2",
            "All the pairs of trust are unique.",
            "ai != bi",
            "1 <= ai, bi <= n",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "n = 2, trust = [[1,2]]",
                "expectedOutput": "2",
                "isHidden": False,
                "explanation": "Person 1 trusts person 2, and person 2 trusts nobody. Person 2 is trusted by n-1 people.",
            },
            {
                "id": 2,
                "input": "n = 3, trust = [[1,3],[2,3]]",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "Person 1 and 2 trust person 3, and person 3 trusts nobody. Person 3 is the judge.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "n = 3, trust = [[1,3],[2,3],[3,1]]",
                "expectedOutput": "-1",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "n = 1, trust = []",
                "expectedOutput": "1",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N + E)",
            "space": "O(N)",
        },
        "tags": [
            "graphs",
            "degrees",
            "array",
            "easy",
        ],
        "visualData": {
            "type": "graph",
            "title": "Town Judge Trust Network",
            "data": {
                "nodes": [
                    {
                        "id": "1",
                    },
                    {
                        "id": "2",
                    },
                    {
                        "id": "3",
                    },
                ],
                "edges": [
                    {
                        "from": "1",
                        "to": "3",
                    },
                    {
                        "from": "2",
                        "to": "3",
                    },
                ],
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "int findJudge(int n, int** trust, int trustSize, int* trustColSize) {\n    int count[1005] = {0};\n    for (int i = 0; i < trustSize; i++) {\n        count[trust[i][0]]--;\n        count[trust[i][1]]++;\n    }\n    for (int i = 1; i <= n; i++) {\n        if (count[i] == n) return i;\n    }\n    return -1;\n}",
                "correctCode": "int findJudge(int n, int** trust, int trustSize, int* trustColSize) {\n    int count[1005] = {0};\n    for (int i = 0; i < trustSize; i++) {\n        count[trust[i][0]]--;\n        count[trust[i][1]]++;\n    }\n    for (int i = 1; i <= n; i++) {\n        if (count[i] == n - 1) return i;\n    }\n    return -1;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int findJudge(int n, vector<vector<int>>& trust) {\n        vector<int> count(n + 1, 0);\n        for (auto& t : trust) {\n            count[t[0]]--;\n            count[t[1]]++;\n        }\n        for (int i = 1; i <= n; i++) {\n            if (count[i] == n) return i;\n        }\n        return -1;\n    }\n};",
                "correctCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int findJudge(int n, vector<vector<int>>& trust) {\n        vector<int> count(n + 1, 0);\n        for (auto& t : trust) {\n            count[t[0]]--;\n            count[t[1]]++;\n        }\n        for (int i = 1; i <= n; i++) {\n            if (count[i] == n - 1) return i;\n        }\n        return -1;\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int findJudge(int n, int[][] trust) {\n        int[] count = new int[n + 1];\n        for (int[] t : trust) {\n            count[t[0]]--;\n            count[t[1]]++;\n        }\n        for (int i = 1; i <= n; i++) {\n            if (count[i] == n) return i;\n        }\n        return -1;\n    }\n}",
                "correctCode": "class Solution {\n    public int findJudge(int n, int[][] trust) {\n        int[] count = new int[n + 1];\n        for (int[] t : trust) {\n            count[t[0]]--;\n            count[t[1]]++;\n        }\n        for (int i = 1; i <= n; i++) {\n            if (count[i] == n - 1) return i;\n        }\n        return -1;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_clone_graph",
        "title": "Clone Graph",
        "problemStatement": "Given a reference of a node in a connected undirected graph.\n\nReturn a deep copy (clone) of the graph.\n\nEach node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.",
        "topic": "graphs",
        "subtopic": "bfs-dfs",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect data structure usage",
        "bugConcept": "Inserting cloned node into visited map after recursing over neighbors rather than before",
        "intendedApproach": "Use a map from original node to cloned node. Immediately clone node and place in map before iterating through its neighbors. Recurse or queue neighbors.",
        "explanation": "If the cloned node is stored in the map after iterating through neighbors, recursive calls back to this node encounter an unmapped node and recurse infinitely.",
        "constraints": [
            "The number of nodes in the graph is in the range [0, 100].",
            "1 <= Node.val <= 100",
            "Node.val is unique for each node.",
            "There are no repeated edges and no self-loops in the graph.",
            "The Graph is connected and all nodes can be visited starting from the given node.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "adjList = [[2,4],[1,3],[2,4],[1,3]]",
                "expectedOutput": "[[2,4],[1,3],[2,4],[1,3]]",
                "isHidden": False,
                "explanation": "The cloned graph has 4 nodes with identical values and adjacency topology as the original graph.",
            },
            {
                "id": 2,
                "input": "adjList = [[]]",
                "expectedOutput": "[[]]",
                "isHidden": False,
                "explanation": "A single isolated node is cloned with the same value 1 and empty neighbor list.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "adjList = []",
                "expectedOutput": "[]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "adjList = [[2],[1]]",
                "expectedOutput": "[[2],[1]]",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(V + E)",
            "space": "O(V)",
        },
        "tags": [
            "graphs",
            "dfs",
            "bfs",
            "hashmap",
            "medium",
        ],
        "visualData": {
            "type": "graph",
            "title": "Graph 4-Cycle Adjacency",
            "data": {
                "nodes": [
                    {
                        "id": "1",
                    },
                    {
                        "id": "2",
                    },
                    {
                        "id": "3",
                    },
                    {
                        "id": "4",
                    },
                ],
                "edges": [
                    {
                        "from": "1",
                        "to": "2",
                    },
                    {
                        "from": "1",
                        "to": "4",
                    },
                    {
                        "from": "2",
                        "to": "3",
                    },
                    {
                        "from": "3",
                        "to": "4",
                    },
                ],
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "struct Node { int val; int numNeighbors; struct Node** neighbors; };\n#include <stdlib.h>\n\nstruct Node* visited[105] = {NULL};\n\nstruct Node* cloneGraph(struct Node* s) {\n    if (!s) return NULL;\n    if (visited[s->val]) return visited[s->val];\n    struct Node* copy = (struct Node*)malloc(sizeof(struct Node));\n    copy->val = s->val;\n    copy->numNeighbors = s->numNeighbors;\n    copy->neighbors = (struct Node**)malloc(s->numNeighbors * sizeof(struct Node*));\n    for (int i = 0; i < s->numNeighbors; i++) {\n        copy->neighbors[i] = cloneGraph(s->neighbors[i]);\n    }\n    visited[s->val] = copy;\n    return copy;\n}",
                "correctCode": "struct Node { int val; int numNeighbors; struct Node** neighbors; };\n#include <stdlib.h>\n\nstruct Node* visited[105] = {NULL};\n\nstruct Node* cloneGraph(struct Node* s) {\n    if (!s) return NULL;\n    if (visited[s->val]) return visited[s->val];\n    struct Node* copy = (struct Node*)malloc(sizeof(struct Node));\n    copy->val = s->val;\n    copy->numNeighbors = s->numNeighbors;\n    copy->neighbors = (struct Node**)malloc(s->numNeighbors * sizeof(struct Node*));\n    visited[s->val] = copy;\n    for (int i = 0; i < s->numNeighbors; i++) {\n        copy->neighbors[i] = cloneGraph(s->neighbors[i]);\n    }\n    return copy;\n}",
            },
            "cpp": {
                "buggyCode": "struct Node { int val; vector<Node*> neighbors; };\n#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nclass Solution {\n    unordered_map<Node*, Node*> copies;\npublic:\n    Node* cloneGraph(Node* node) {\n        if (!node) return nullptr;\n        if (copies.count(node)) return copies[node];\n        Node* copy = new Node{node->val, {}};\n        for (Node* neighbor : node->neighbors) {\n            copy->neighbors.push_back(cloneGraph(neighbor));\n        }\n        copies[node] = copy;\n        return copy;\n    }\n};",
                "correctCode": "struct Node { int val; vector<Node*> neighbors; };\n#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nclass Solution {\n    unordered_map<Node*, Node*> copies;\npublic:\n    Node* cloneGraph(Node* node) {\n        if (!node) return nullptr;\n        if (copies.count(node)) return copies[node];\n        Node* copy = new Node{node->val, {}};\n        copies[node] = copy;\n        for (Node* neighbor : node->neighbors) {\n            copy->neighbors.push_back(cloneGraph(neighbor));\n        }\n        return copy;\n    }\n};",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Node { public int val; public List<Node> neighbors = new ArrayList<>(); public Node(int _val) { val = _val; } }\n\nclass Solution {\n    private Map<Node, Node> map = new HashMap<>();\n    public Node cloneGraph(Node node) {\n        if (node == null) return null;\n        if (map.containsKey(node)) return map.get(node);\n        Node clone = new Node(node.val);\n        for (Node neighbor : node.neighbors) {\n            clone.neighbors.add(cloneGraph(neighbor));\n        }\n        map.put(node, clone);\n        return clone;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Node { public int val; public List<Node> neighbors = new ArrayList<>(); public Node(int _val) { val = _val; } }\n\nclass Solution {\n    private Map<Node, Node> map = new HashMap<>();\n    public Node cloneGraph(Node node) {\n        if (node == null) return null;\n        if (map.containsKey(node)) return map.get(node);\n        Node clone = new Node(node.val);\n        map.put(node, clone);\n        for (Node neighbor : node.neighbors) {\n            clone.neighbors.add(cloneGraph(neighbor));\n        }\n        return clone;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_course_schedule_ii",
        "title": "Course Schedule II",
        "problemStatement": "There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.\n\nFor example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.\n\nReturn the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.",
        "topic": "graphs",
        "subtopic": "topological-sort",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "logical",
        "bugConcept": "Returning partially populated course ordering when topological sorting detects a cycle",
        "intendedApproach": "Compute in-degrees. Seed queue with in-degree 0 nodes. In BFS, record courses and decrement neighbor in-degrees. If order.size() != numCourses, cycle detected -> return empty array.",
        "explanation": "If a cycle prevents all courses from being scheduled, returning the incomplete list violates the requirement to return an empty array.",
        "constraints": [
            "1 <= numCourses <= 2000",
            "0 <= prerequisites.length <= numCourses * (numCourses - 1)",
            "prerequisites[i].length == 2",
            "0 <= ai, bi < numCourses",
            "ai != bi",
            "All the pairs [ai, bi] are distinct.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "numCourses = 2, prerequisites = [[1,0]]",
                "expectedOutput": "[0,1]",
                "isHidden": False,
                "explanation": "There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].",
            },
            {
                "id": 2,
                "input": "numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]",
                "expectedOutput": "[0,2,1,3]",
                "isHidden": False,
                "explanation": "Both [0,1,2,3] and [0,2,1,3] are valid topological orderings.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "numCourses = 2, prerequisites = [[0,1],[1,0]]",
                "expectedOutput": "[]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "numCourses = 1, prerequisites = []",
                "expectedOutput": "[0]",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(V + E)",
            "space": "O(V + E)",
        },
        "tags": [
            "graphs",
            "topological-sort",
            "bfs",
            "medium",
        ],
        "visualData": {
            "type": "graph",
            "title": "Course Dependency DAG",
            "data": {
                "nodes": [
                    {
                        "id": "0",
                    },
                    {
                        "id": "1",
                    },
                    {
                        "id": "2",
                    },
                    {
                        "id": "3",
                    },
                ],
                "edges": [
                    {
                        "from": "0",
                        "to": "1",
                    },
                    {
                        "from": "0",
                        "to": "2",
                    },
                    {
                        "from": "1",
                        "to": "3",
                    },
                    {
                        "from": "2",
                        "to": "3",
                    },
                ],
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdlib.h>\n\nstruct Edge { int to; struct Edge* next; };\n\nint* findOrder(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize, int* returnSize) {\n    int* indegree = (int*)calloc(numCourses, sizeof(int));\n    struct Edge** adj = (struct Edge**)calloc(numCourses, sizeof(struct Edge*));\n    for (int i = 0; i < prerequisitesSize; i++) {\n        int dest = prerequisites[i][0], src = prerequisites[i][1];\n        indegree[dest]++;\n        struct Edge* e = (struct Edge*)malloc(sizeof(struct Edge));\n        e->to = dest; e->next = adj[src]; adj[src] = e;\n    }\n    int* queue = (int*)malloc(numCourses * sizeof(int));\n    int head = 0, tail = 0;\n    for (int i = 0; i < numCourses; i++) {\n        if (indegree[i] == 0) queue[tail++] = i;\n    }\n    int* order = (int*)malloc(numCourses * sizeof(int));\n    int idx = 0;\n    while (head < tail) {\n        int u = queue[head++];\n        order[idx++] = u;\n        for (struct Edge* e = adj[u]; e; e = e->next) {\n            if (--indegree[e->to] == 0) queue[tail++] = e->to;\n        }\n    }\n    *returnSize = idx;\n    return order;\n}",
                "correctCode": "#include <stdlib.h>\n\nstruct Edge { int to; struct Edge* next; };\n\nint* findOrder(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize, int* returnSize) {\n    int* indegree = (int*)calloc(numCourses, sizeof(int));\n    struct Edge** adj = (struct Edge**)calloc(numCourses, sizeof(struct Edge*));\n    for (int i = 0; i < prerequisitesSize; i++) {\n        int dest = prerequisites[i][0], src = prerequisites[i][1];\n        indegree[dest]++;\n        struct Edge* e = (struct Edge*)malloc(sizeof(struct Edge));\n        e->to = dest; e->next = adj[src]; adj[src] = e;\n    }\n    int* queue = (int*)malloc(numCourses * sizeof(int));\n    int head = 0, tail = 0;\n    for (int i = 0; i < numCourses; i++) {\n        if (indegree[i] == 0) queue[tail++] = i;\n    }\n    int* order = (int*)malloc(numCourses * sizeof(int));\n    int idx = 0;\n    while (head < tail) {\n        int u = queue[head++];\n        order[idx++] = u;\n        for (struct Edge* e = adj[u]; e; e = e->next) {\n            if (--indegree[e->to] == 0) queue[tail++] = e->to;\n        }\n    }\n    if (idx != numCourses) {\n        *returnSize = 0;\n        return NULL;\n    }\n    *returnSize = numCourses;\n    return order;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {\n        vector<vector<int>> adj(numCourses);\n        vector<int> indegree(numCourses, 0);\n        for (auto& p : prerequisites) {\n            adj[p[1]].push_back(p[0]);\n            indegree[p[0]]++;\n        }\n        queue<int> q;\n        for (int i = 0; i < numCourses; i++) {\n            if (indegree[i] == 0) q.push(i);\n        }\n        vector<int> order;\n        while (!q.empty()) {\n            int u = q.front();\n            q.pop();\n            order.push_back(u);\n            for (int v : adj[u]) {\n                if (--indegree[v] == 0) q.push(v);\n            }\n        }\n        return order;\n    }\n};",
                "correctCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {\n        vector<vector<int>> adj(numCourses);\n        vector<int> indegree(numCourses, 0);\n        for (auto& p : prerequisites) {\n            adj[p[1]].push_back(p[0]);\n            indegree[p[0]]++;\n        }\n        queue<int> q;\n        for (int i = 0; i < numCourses; i++) {\n            if (indegree[i] == 0) q.push(i);\n        }\n        vector<int> order;\n        while (!q.empty()) {\n            int u = q.front();\n            q.pop();\n            order.push_back(u);\n            for (int v : adj[u]) {\n                if (--indegree[v] == 0) q.push(v);\n            }\n        }\n        if ((int)order.size() != numCourses) return {};\n        return order;\n    }\n};",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    public int[] findOrder(int numCourses, int[][] prerequisites) {\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());\n        int[] indegree = new int[numCourses];\n        for (int[] p : prerequisites) {\n            adj.get(p[1]).add(p[0]);\n            indegree[p[0]]++;\n        }\n        Queue<Integer> q = new LinkedList<>();\n        for (int i = 0; i < numCourses; i++) {\n            if (indegree[i] == 0) q.add(i);\n        }\n        int[] order = new int[numCourses];\n        int idx = 0;\n        while (!q.isEmpty()) {\n            int u = q.poll();\n            order[idx++] = u;\n            for (int v : adj.get(u)) {\n                if (--indegree[v] == 0) q.add(v);\n            }\n        }\n        return order;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    public int[] findOrder(int numCourses, int[][] prerequisites) {\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());\n        int[] indegree = new int[numCourses];\n        for (int[] p : prerequisites) {\n            adj.get(p[1]).add(p[0]);\n            indegree[p[0]]++;\n        }\n        Queue<Integer> q = new LinkedList<>();\n        for (int i = 0; i < numCourses; i++) {\n            if (indegree[i] == 0) q.add(i);\n        }\n        int[] order = new int[numCourses];\n        int idx = 0;\n        while (!q.isEmpty()) {\n            int u = q.poll();\n            order[idx++] = u;\n            for (int v : adj.get(u)) {\n                if (--indegree[v] == 0) q.add(v);\n            }\n        }\n        if (idx != numCourses) return new int[0];\n        return order;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_cheapest_flights_k_stops",
        "title": "Cheapest Flights Within K Stops",
        "problemStatement": "There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.\n\nYou are also given three integers `src`, `dst`, and `k`, return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.",
        "topic": "graphs",
        "subtopic": "shortest-path",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Updating shortest path distances array in-place rather than from previous step snapshot",
        "intendedApproach": "Run Bellman-Ford for k + 1 iterations. In each round, copy prices to tempPrices and update tempPrices[to] using prices[from] + price to enforce at most one flight per round.",
        "explanation": "Updating distances in-place can chain multiple flights within a single iteration, taking paths with more than k stops.",
        "constraints": [
            "1 <= n <= 100",
            "0 <= flights.length <= (n * (n - 1) / 2)",
            "flights[i].length == 3",
            "0 <= fromi, toi < n",
            "fromi != toi",
            "1 <= pricei <= 10^4",
            "There will not be any multiple flights between two cities in the same direction.",
            "0 <= src, dst < n",
            "src != dst",
            "0 <= k < n",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1",
                "expectedOutput": "700",
                "isHidden": False,
                "explanation": "The optimal path with at most 1 stop from city 0 to 3 is 0 -> 1 -> 3 with cost 100 + 600 = 700.",
            },
            {
                "id": 2,
                "input": "n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1",
                "expectedOutput": "200",
                "isHidden": False,
                "explanation": "The direct path 0 -> 2 has price 500, but taking 0 -> 1 -> 2 has price 100 + 100 = 200 with at most 1 stop.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0",
                "expectedOutput": "500",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "n = 2, flights = [[0,1,200]], src = 0, dst = 1, k = 0",
                "expectedOutput": "200",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(K * E)",
            "space": "O(N)",
        },
        "tags": [
            "graphs",
            "shortest-path",
            "dp",
            "bfs",
            "medium",
        ],
        "visualData": {
            "type": "graph",
            "title": "Constrained Flight Network",
            "data": {
                "nodes": [
                    {
                        "id": "0",
                    },
                    {
                        "id": "1",
                    },
                    {
                        "id": "2",
                    },
                    {
                        "id": "3",
                    },
                ],
                "edges": [
                    {
                        "from": "0",
                        "to": "1",
                    },
                    {
                        "from": "1",
                        "to": "2",
                    },
                    {
                        "from": "1",
                        "to": "3",
                    },
                    {
                        "from": "2",
                        "to": "3",
                    },
                ],
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <string.h>\n#define INF 100000000\n\nint findCheapestPrice(int n, int** flights, int flightsSize, int* flightsColSize, int src, int dst, int k) {\n    int dist[105];\n    for (int i = 0; i < n; i++) dist[i] = INF;\n    dist[src] = 0;\n    for (int i = 0; i <= k; i++) {\n        for (int j = 0; j < flightsSize; j++) {\n            int u = flights[j][0], v = flights[j][1], w = flights[j][2];\n            if (dist[u] != INF && dist[u] + w < dist[v]) {\n                dist[v] = dist[u] + w;\n            }\n        }\n    }\n    return dist[dst] == INF ? -1 : dist[dst];\n}",
                "correctCode": "#include <string.h>\n#define INF 100000000\n\nint findCheapestPrice(int n, int** flights, int flightsSize, int* flightsColSize, int src, int dst, int k) {\n    int dist[105];\n    for (int i = 0; i < n; i++) dist[i] = INF;\n    dist[src] = 0;\n    for (int i = 0; i <= k; i++) {\n        int temp[105];\n        memcpy(temp, dist, sizeof(dist));\n        for (int j = 0; j < flightsSize; j++) {\n            int u = flights[j][0], v = flights[j][1], w = flights[j][2];\n            if (dist[u] != INF && dist[u] + w < temp[v]) {\n                temp[v] = dist[u] + w;\n            }\n        }\n        memcpy(dist, temp, sizeof(dist));\n    }\n    return dist[dst] == INF ? -1 : dist[dst];\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <climits>\nusing namespace std;\n\nclass Solution {\npublic:\n    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {\n        vector<int> dist(n, 1e9);\n        dist[src] = 0;\n        for (int i = 0; i <= k; i++) {\n            for (auto& f : flights) {\n                int u = f[0], v = f[1], w = f[2];\n                if (dist[u] != 1e9 && dist[u] + w < dist[v]) {\n                    dist[v] = dist[u] + w;\n                }\n            }\n        }\n        return dist[dst] == 1e9 ? -1 : dist[dst];\n    }\n};",
                "correctCode": "#include <vector>\n#include <climits>\nusing namespace std;\n\nclass Solution {\npublic:\n    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {\n        vector<int> dist(n, 1e9);\n        dist[src] = 0;\n        for (int i = 0; i <= k; i++) {\n            vector<int> temp = dist;\n            for (auto& f : flights) {\n                int u = f[0], v = f[1], w = f[2];\n                if (dist[u] != 1e9 && dist[u] + w < temp[v]) {\n                    temp[v] = dist[u] + w;\n                }\n            }\n            dist = temp;\n        }\n        return dist[dst] == 1e9 ? -1 : dist[dst];\n    }\n};",
            },
            "java": {
                "buggyCode": "import java.util.Arrays;\n\nclass Solution {\n    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {\n        int[] dist = new int[n];\n        Arrays.fill(dist, (int)1e9);\n        dist[src] = 0;\n        for (int i = 0; i <= k; i++) {\n            for (int[] f : flights) {\n                int u = f[0], v = f[1], w = f[2];\n                if (dist[u] != (int)1e9 && dist[u] + w < dist[v]) {\n                    dist[v] = dist[u] + w;\n                }\n            }\n        }\n        return dist[dst] == (int)1e9 ? -1 : dist[dst];\n    }\n}",
                "correctCode": "import java.util.Arrays;\n\nclass Solution {\n    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {\n        int[] dist = new int[n];\n        Arrays.fill(dist, (int)1e9);\n        dist[src] = 0;\n        for (int i = 0; i <= k; i++) {\n            int[] temp = Arrays.copyOf(dist, n);\n            for (int[] f : flights) {\n                int u = f[0], v = f[1], w = f[2];\n                if (dist[u] != (int)1e9 && dist[u] + w < temp[v]) {\n                    temp[v] = dist[u] + w;\n                }\n            }\n            dist = temp;\n        }\n        return dist[dst] == (int)1e9 ? -1 : dist[dst];\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_alien_dictionary",
        "title": "Alien Dictionary",
        "problemStatement": "There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.\n\nYou are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are sorted lexicographically by the rules of this new language.\n\nReturn a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return `\"\"`. If there are multiple solutions, return any of them.",
        "topic": "graphs",
        "subtopic": "topological-sort",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "edge case",
        "bugConcept": "Missing check for prefix ordering violation where longer word precedes shorter prefix",
        "intendedApproach": "Compare adjacent words. If word1 starts with word2 and len(word1) > len(word2), order is invalid (return \"\"). Otherwise find first differing character, build directed edge and track indegrees. Run topological sort.",
        "explanation": "If `word1 = \"apple\"` and `word2 = \"app\"`, the longer word appearing before its own prefix is invalid by definition. Omitting this check outputs a bogus ordering.",
        "constraints": [
            "1 <= words.length <= 100",
            "1 <= words[i].length <= 100",
            "words[i] consists of only lowercase English letters.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "words = [\"wrt\",\"wrf\",\"er\",\"ett\",\"rftt\"]",
                "expectedOutput": "\"wertf\"",
                "isHidden": False,
                "explanation": "From \"wrt\" and \"wrf\", 't' < 'f'. From \"wrt\" and \"er\", 'w' < 'e'. From \"er\" and \"ett\", 'r' < 't'. From \"ett\" and \"rftt\", 'e' < 'r'. The order is \"wertf\".",
            },
            {
                "id": 2,
                "input": "words = [\"z\",\"x\"]",
                "expectedOutput": "\"zx\"",
                "isHidden": False,
                "explanation": "From \"z\" and \"x\", 'z' < 'x'. The order is \"zx\".",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "words = [\"z\",\"x\",\"z\"]",
                "expectedOutput": "\"\"",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "words = [\"abc\",\"ab\"]",
                "expectedOutput": "\"\"",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(C)",
            "space": "O(1)",
        },
        "tags": [
            "graphs",
            "topological-sort",
            "bfs",
            "dfs",
            "hard",
        ],
        "visualData": {
            "type": "graph",
            "title": "Character Precedence Ordering",
            "data": {
                "nodes": [
                    {
                        "id": "t",
                    },
                    {
                        "id": "f",
                    },
                    {
                        "id": "w",
                    },
                    {
                        "id": "e",
                    },
                    {
                        "id": "r",
                    },
                ],
                "edges": [
                    {
                        "from": "t",
                        "to": "f",
                    },
                    {
                        "from": "w",
                        "to": "e",
                    },
                    {
                        "from": "r",
                        "to": "t",
                    },
                    {
                        "from": "e",
                        "to": "r",
                    },
                ],
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <string.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\nchar* alienOrder(char** words, int wordsSize) {\n    int adj[26][26] = {0};\n    int indegree[26];\n    for (int i = 0; i < 26; i++) indegree[i] = -1;\n    for (int i = 0; i < wordsSize; i++) {\n        for (int j = 0; words[i][j]; j++) indegree[words[i][j] - 'a'] = 0;\n    }\n    for (int i = 0; i < wordsSize - 1; i++) {\n        char *w1 = words[i], *w2 = words[i + 1];\n        int len1 = strlen(w1), len2 = strlen(w2);\n        int minLen = len1 < len2 ? len1 : len2;\n        for (int j = 0; j < minLen; j++) {\n            if (w1[j] != w2[j]) {\n                if (!adj[w1[j] - 'a'][w2[j] - 'a']) {\n                    adj[w1[j] - 'a'][w2[j] - 'a'] = 1;\n                    indegree[w2[j] - 'a']++;\n                }\n                break;\n            }\n        }\n    }\n    char* res = (char*)malloc(27 * sizeof(char));\n    int idx = 0;\n    int q[26], head = 0, tail = 0, total = 0;\n    for (int i = 0; i < 26; i++) {\n        if (indegree[i] == 0) q[tail++] = i;\n        if (indegree[i] >= 0) total++;\n    }\n    while (head < tail) {\n        int u = q[head++];\n        res[idx++] = (char)(u + 'a');\n        for (int v = 0; v < 26; v++) {\n            if (adj[u][v] && --indegree[v] == 0) q[tail++] = v;\n        }\n    }\n    res[idx] = '\\0';\n    return idx == total ? res : \"\";\n}",
                "correctCode": "#include <string.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\nchar* alienOrder(char** words, int wordsSize) {\n    int adj[26][26] = {0};\n    int indegree[26];\n    for (int i = 0; i < 26; i++) indegree[i] = -1;\n    for (int i = 0; i < wordsSize; i++) {\n        for (int j = 0; words[i][j]; j++) indegree[words[i][j] - 'a'] = 0;\n    }\n    for (int i = 0; i < wordsSize - 1; i++) {\n        char *w1 = words[i], *w2 = words[i + 1];\n        int len1 = strlen(w1), len2 = strlen(w2);\n        int minLen = len1 < len2 ? len1 : len2;\n        bool diffFound = false;\n        for (int j = 0; j < minLen; j++) {\n            if (w1[j] != w2[j]) {\n                if (!adj[w1[j] - 'a'][w2[j] - 'a']) {\n                    adj[w1[j] - 'a'][w2[j] - 'a'] = 1;\n                    indegree[w2[j] - 'a']++;\n                }\n                diffFound = true;\n                break;\n            }\n        }\n        if (!diffFound && len1 > len2) return \"\";\n    }\n    char* res = (char*)malloc(27 * sizeof(char));\n    int idx = 0;\n    int q[26], head = 0, tail = 0, total = 0;\n    for (int i = 0; i < 26; i++) {\n        if (indegree[i] == 0) q[tail++] = i;\n        if (indegree[i] >= 0) total++;\n    }\n    while (head < tail) {\n        int u = q[head++];\n        res[idx++] = (char)(u + 'a');\n        for (int v = 0; v < 26; v++) {\n            if (adj[u][v] && --indegree[v] == 0) q[tail++] = v;\n        }\n    }\n    res[idx] = '\\0';\n    return idx == total ? res : \"\";\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\n#include <unordered_map>\n#include <unordered_set>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    string alienOrder(vector<string>& words) {\n        unordered_map<char, unordered_set<char>> adj;\n        unordered_map<char, int> indegree;\n        for (auto& w : words) {\n            for (char c : w) indegree[c] = 0;\n        }\n        for (int i = 0; i < (int)words.size() - 1; i++) {\n            string w1 = words[i], w2 = words[i + 1];\n            int len = min(w1.size(), w2.size());\n            for (int j = 0; j < len; j++) {\n                if (w1[j] != w2[j]) {\n                    if (!adj[w1[j]].count(w2[j])) {\n                        adj[w1[j]].insert(w2[j]);\n                        indegree[w2[j]]++;\n                    }\n                    break;\n                }\n            }\n        }\n        queue<char> q;\n        for (auto& p : indegree) {\n            if (p.second == 0) q.push(p.first);\n        }\n        string res = \"\";\n        while (!q.empty()) {\n            char c = q.front();\n            q.pop();\n            res += c;\n            for (char neighbor : adj[c]) {\n                if (--indegree[neighbor] == 0) q.push(neighbor);\n            }\n        }\n        return res.size() == indegree.size() ? res : \"\";\n    }\n};",
                "correctCode": "#include <string>\n#include <vector>\n#include <unordered_map>\n#include <unordered_set>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    string alienOrder(vector<string>& words) {\n        unordered_map<char, unordered_set<char>> adj;\n        unordered_map<char, int> indegree;\n        for (auto& w : words) {\n            for (char c : w) indegree[c] = 0;\n        }\n        for (int i = 0; i < (int)words.size() - 1; i++) {\n            string w1 = words[i], w2 = words[i + 1];\n            if (w1.size() > w2.size() && w1.rfind(w2, 0) == 0) return \"\";\n            int len = min(w1.size(), w2.size());\n            for (int j = 0; j < len; j++) {\n                if (w1[j] != w2[j]) {\n                    if (!adj[w1[j]].count(w2[j])) {\n                        adj[w1[j]].insert(w2[j]);\n                        indegree[w2[j]]++;\n                    }\n                    break;\n                }\n            }\n        }\n        queue<char> q;\n        for (auto& p : indegree) {\n            if (p.second == 0) q.push(p.first);\n        }\n        string res = \"\";\n        while (!q.empty()) {\n            char c = q.front();\n            q.pop();\n            res += c;\n            for (char neighbor : adj[c]) {\n                if (--indegree[neighbor] == 0) q.push(neighbor);\n            }\n        }\n        return res.size() == indegree.size() ? res : \"\";\n    }\n};",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    public String alienOrder(String[] words) {\n        Map<Character, Set<Character>> adj = new HashMap<>();\n        Map<Character, Integer> indegree = new HashMap<>();\n        for (String w : words) {\n            for (char c : w.toCharArray()) {\n                indegree.put(c, 0);\n                adj.putIfAbsent(c, new HashSet<>());\n            }\n        }\n        for (int i = 0; i < words.length - 1; i++) {\n            String w1 = words[i], w2 = words[i + 1];\n            int len = Math.min(w1.length(), w2.length());\n            for (int j = 0; j < len; j++) {\n                if (w1.charAt(j) != w2.charAt(j)) {\n                    char u = w1.charAt(j), v = w2.charAt(j);\n                    if (!adj.get(u).contains(v)) {\n                        adj.get(u).add(v);\n                        indegree.put(v, indegree.get(v) + 1);\n                    }\n                    break;\n                }\n            }\n        }\n        Queue<Character> q = new LinkedList<>();\n        for (char c : indegree.keySet()) {\n            if (indegree.get(c) == 0) q.add(c);\n        }\n        StringBuilder sb = new StringBuilder();\n        while (!q.isEmpty()) {\n            char c = q.poll();\n            sb.append(c);\n            for (char next : adj.get(c)) {\n                indegree.put(next, indegree.get(next) - 1);\n                if (indegree.get(next) == 0) q.add(next);\n            }\n        }\n        return sb.length() == indegree.size() ? sb.toString() : \"\";\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    public String alienOrder(String[] words) {\n        Map<Character, Set<Character>> adj = new HashMap<>();\n        Map<Character, Integer> indegree = new HashMap<>();\n        for (String w : words) {\n            for (char c : w.toCharArray()) {\n                indegree.put(c, 0);\n                adj.putIfAbsent(c, new HashSet<>());\n            }\n        }\n        for (int i = 0; i < words.length - 1; i++) {\n            String w1 = words[i], w2 = words[i + 1];\n            if (w1.length() > w2.length() && w1.startsWith(w2)) return \"\";\n            int len = Math.min(w1.length(), w2.length());\n            for (int j = 0; j < len; j++) {\n                if (w1.charAt(j) != w2.charAt(j)) {\n                    char u = w1.charAt(j), v = w2.charAt(j);\n                    if (!adj.get(u).contains(v)) {\n                        adj.get(u).add(v);\n                        indegree.put(v, indegree.get(v) + 1);\n                    }\n                    break;\n                }\n            }\n        }\n        Queue<Character> q = new LinkedList<>();\n        for (char c : indegree.keySet()) {\n            if (indegree.get(c) == 0) q.add(c);\n        }\n        StringBuilder sb = new StringBuilder();\n        while (!q.isEmpty()) {\n            char c = q.poll();\n            sb.append(c);\n            for (char next : adj.get(c)) {\n                indegree.put(next, indegree.get(next) - 1);\n                if (indegree.get(next) == 0) q.add(next);\n            }\n        }\n        return sb.length() == indegree.size() ? sb.toString() : \"\";\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_critical_connections",
        "title": "Critical Connections in a Network",
        "problemStatement": "There are `n` servers numbered from `0` to `n - 1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a_i, b_i]` represents a connection between servers `a_i` and `b_i`. Any server can reach other servers directly or indirectly through the network.\n\nA critical connection is a connection that, if removed, will make some servers unable to reach some other server.\n\nReturn all critical connections in the network in any order.",
        "topic": "graphs",
        "subtopic": "bridges",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect condition",
        "bugConcept": "Using greater-or-equal instead of strictly greater in Tarjan bridge condition",
        "intendedApproach": "Run Tarjan's bridge finding algorithm tracking discovery time tin[u] and lowest reachable ancestor low[u]. An edge (u, v) is a bridge if and only if low[v] > tin[u].",
        "explanation": "Checking `low[v] >= tin[u]` includes back-edges and simple cycles as critical connections, falsely identifying non-bridges as bridges.",
        "constraints": [
            "2 <= n <= 10^5",
            "n - 1 <= connections.length <= 10^5",
            "0 <= ai, bi <= n - 1",
            "ai != bi",
            "There are no repeated connections.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]",
                "expectedOutput": "[[1,3]]",
                "isHidden": False,
                "explanation": "Removing connection [1,3] disconnects server 3 from the rest of the network, making it a critical bridge connection.",
            },
            {
                "id": 2,
                "input": "n = 2, connections = [[0,1]]",
                "expectedOutput": "[[0,1]]",
                "isHidden": False,
                "explanation": "Removing [0,1] disconnects server 0 and server 1.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "n = 5, connections = [[0,1],[1,2],[2,3],[3,4],[4,0]]",
                "expectedOutput": "[]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "n = 3, connections = [[0,1],[1,2]]",
                "expectedOutput": "[[0,1],[1,2]]",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(V + E)",
            "space": "O(V + E)",
        },
        "tags": [
            "graphs",
            "dfs",
            "bridges",
            "hard",
        ],
        "visualData": {
            "type": "graph",
            "title": "Bridges and Cycle Topology",
            "data": {
                "nodes": [
                    {
                        "id": "0",
                    },
                    {
                        "id": "1",
                    },
                    {
                        "id": "2",
                    },
                    {
                        "id": "3",
                    },
                ],
                "edges": [
                    {
                        "from": "0",
                        "to": "1",
                    },
                    {
                        "from": "1",
                        "to": "2",
                    },
                    {
                        "from": "2",
                        "to": "0",
                    },
                    {
                        "from": "1",
                        "to": "3",
                    },
                ],
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdlib.h>\n#include <string.h>\n#define MIN(a, b) ((a) < (b) ? (a) : (b))\n\nstruct Edge { int to; struct Edge* next; };\nint timer = 0;\n\nvoid dfs(int u, int p, struct Edge** adj, int* tin, int* low, int** res, int* returnSize, int** returnColSizes) {\n    tin[u] = low[u] = ++timer;\n    for (struct Edge* e = adj[u]; e; e = e->next) {\n        int v = e->to;\n        if (v == p) continue;\n        if (tin[v]) {\n            low[u] = MIN(low[u], tin[v]);\n        } else {\n            dfs(v, u, adj, tin, low, res, returnSize, returnColSizes);\n            low[u] = MIN(low[u], low[v]);\n            if (low[v] >= tin[u]) {\n                res[*returnSize] = (int*)malloc(2 * sizeof(int));\n                res[*returnSize][0] = u; res[*returnSize][1] = v;\n                (*returnColSizes)[*returnSize] = 2;\n                (*returnSize)++;\n            }\n        }\n    }\n}",
                "correctCode": "#include <stdlib.h>\n#include <string.h>\n#define MIN(a, b) ((a) < (b) ? (a) : (b))\n\nstruct Edge { int to; struct Edge* next; };\nint timer = 0;\n\nvoid dfs(int u, int p, struct Edge** adj, int* tin, int* low, int** res, int* returnSize, int** returnColSizes) {\n    tin[u] = low[u] = ++timer;\n    for (struct Edge* e = adj[u]; e; e = e->next) {\n        int v = e->to;\n        if (v == p) continue;\n        if (tin[v]) {\n            low[u] = MIN(low[u], tin[v]);\n        } else {\n            dfs(v, u, adj, tin, low, res, returnSize, returnColSizes);\n            low[u] = MIN(low[u], low[v]);\n            if (low[v] > tin[u]) {\n                res[*returnSize] = (int*)malloc(2 * sizeof(int));\n                res[*returnSize][0] = u; res[*returnSize][1] = v;\n                (*returnColSizes)[*returnSize] = 2;\n                (*returnSize)++;\n            }\n        }\n    }\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\n    int timer = 0;\n    void dfs(int u, int p, vector<vector<int>>& adj, vector<int>& tin, vector<int>& low, vector<vector<int>>& bridges) {\n        tin[u] = low[u] = ++timer;\n        for (int v : adj[u]) {\n            if (v == p) continue;\n            if (tin[v]) {\n                low[u] = min(low[u], tin[v]);\n            } else {\n                dfs(v, u, adj, tin, low, bridges);\n                low[u] = min(low[u], low[v]);\n                if (low[v] >= tin[u]) {\n                    bridges.push_back({u, v});\n                }\n            }\n        }\n    }\npublic:\n    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {\n        vector<vector<int>> adj(n);\n        for (auto& e : connections) {\n            adj[e[0]].push_back(e[1]);\n            adj[e[1]].push_back(e[0]);\n        }\n        vector<int> tin(n, 0), low(n, 0);\n        vector<vector<int>> bridges;\n        dfs(0, -1, adj, tin, low, bridges);\n        return bridges;\n    }\n};",
                "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\n    int timer = 0;\n    void dfs(int u, int p, vector<vector<int>>& adj, vector<int>& tin, vector<int>& low, vector<vector<int>>& bridges) {\n        tin[u] = low[u] = ++timer;\n        for (int v : adj[u]) {\n            if (v == p) continue;\n            if (tin[v]) {\n                low[u] = min(low[u], tin[v]);\n            } else {\n                dfs(v, u, adj, tin, low, bridges);\n                low[u] = min(low[u], low[v]);\n                if (low[v] > tin[u]) {\n                    bridges.push_back({u, v});\n                }\n            }\n        }\n    }\npublic:\n    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {\n        vector<vector<int>> adj(n);\n        for (auto& e : connections) {\n            adj[e[0]].push_back(e[1]);\n            adj[e[1]].push_back(e[0]);\n        }\n        vector<int> tin(n, 0), low(n, 0);\n        vector<vector<int>> bridges;\n        dfs(0, -1, adj, tin, low, bridges);\n        return bridges;\n    }\n};",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    private int timer = 0;\n    private void dfs(int u, int p, List<List<Integer>> adj, int[] tin, int[] low, List<List<Integer>> bridges) {\n        tin[u] = low[u] = ++timer;\n        for (int v : adj.get(u)) {\n            if (v == p) continue;\n            if (tin[v] > 0) {\n                low[u] = Math.min(low[u], tin[v]);\n            } else {\n                dfs(v, u, adj, tin, low, bridges);\n                low[u] = Math.min(low[u], low[v]);\n                if (low[v] >= tin[u]) {\n                    bridges.add(Arrays.asList(u, v));\n                }\n            }\n        }\n    }\n    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());\n        for (List<Integer> edge : connections) {\n            adj.get(edge.get(0)).add(edge.get(1));\n            adj.get(edge.get(1)).add(edge.get(0));\n        }\n        int[] tin = new int[n];\n        int[] low = new int[n];\n        List<List<Integer>> bridges = new ArrayList<>();\n        dfs(0, -1, adj, tin, low, bridges);\n        return bridges;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    private int timer = 0;\n    private void dfs(int u, int p, List<List<Integer>> adj, int[] tin, int[] low, List<List<Integer>> bridges) {\n        tin[u] = low[u] = ++timer;\n        for (int v : adj.get(u)) {\n            if (v == p) continue;\n            if (tin[v] > 0) {\n                low[u] = Math.min(low[u], tin[v]);\n            } else {\n                dfs(v, u, adj, tin, low, bridges);\n                low[u] = Math.min(low[u], low[v]);\n                if (low[v] > tin[u]) {\n                    bridges.add(Arrays.asList(u, v));\n                }\n            }\n        }\n    }\n    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());\n        for (List<Integer> edge : connections) {\n            adj.get(edge.get(0)).add(edge.get(1));\n            adj.get(edge.get(1)).add(edge.get(0));\n        }\n        int[] tin = new int[n];\n        int[] low = new int[n];\n        List<List<Integer>> bridges = new ArrayList<>();\n        dfs(0, -1, adj, tin, low, bridges);\n        return bridges;\n    }\n}",
            },
        },
    },
]
