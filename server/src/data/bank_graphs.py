# Graph Debugging Problems (10 Questions: C, C++, Java)

GRAPH_QUESTIONS = [
    {
        "id": "q_graph_number_of_islands",
        "title": "Number of Islands",
        "problemStatement": "Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.\n\nAn island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.",
        "topic": "graphs",
        "subtopic": "dfs",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "boundary",
        "bugConcept": "Missing boundary check for bottom grid row (r >= m or c >= n) leading to index out-of-bounds / infinite recursion",
        "intendedApproach": "Iterate through each cell. When finding '1', increment island count and trigger DFS/BFS sink to flood-fill all connected '1's to '0'.",
        "explanation": "If the DFS boundary condition checks `r < 0 || c < 0` but omits `r >= m` or `c >= n`, moving downward past the bottom row accesses invalid memory or causes infinite recursion.",
        "constraints": [
            "m == grid.length",
            "n == grid[i].length",
            "1 <= m, n <= 300",
            "grid[i][j] is '0' or '1'.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "grid = [[\"1\",\"1\",\"1\",\"1\",\"0\"],[\"1\",\"1\",\"0\",\"1\",\"0\"],[\"1\",\"1\",\"0\",\"0\",\"0\"],[\"0\",\"0\",\"0\",\"0\",\"0\"]",
                "expectedOutput": "1",
                "isHidden": False,
                "explanation": "All '1's are connected horizontally or vertically into a single island.",
            },
            {
                "id": 2,
                "input": "grid = [[\"1\",\"1\",\"0\",\"0\",\"0\"],[\"1\",\"1\",\"0\",\"0\",\"0\"],[\"0\",\"0\",\"1\",\"0\",\"0\"],[\"0\",\"0\",\"0\",\"1\",\"1\"]",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "There are 3 separate connected components of '1's representing 3 islands.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "grid = [[\"1\"]]",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "grid = [[\"0\"]]",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "grid = [[\"1\",\"0\"],[\"0\",\"1\"]]",
                "expectedOutput": "2",
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
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Island Grid Map: 4x5",
            "data": [
                [
                    "1",
                    "1",
                    "1",
                    "1",
                    "0",
                ],
                [
                    "1",
                    "1",
                    "0",
                    "1",
                    "0",
                ],
                [
                    "1",
                    "1",
                    "0",
                    "0",
                    "0",
                ],
                [
                    "0",
                    "0",
                    "0",
                    "0",
                    "0",
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "void sink(char grid[300][300], int m, int n, int r, int c) {\n    if (r < 0 || c < 0 || c >= n || grid[r][c] != '1') return;\n    grid[r][c] = '0';\n    sink(grid, m, n, r + 1, c);\n    sink(grid, m, n, r - 1, c);\n    sink(grid, m, n, r, c + 1);\n    sink(grid, m, n, r, c - 1);\n}\n\nint numIslands(char grid[300][300], int m, int n) {\n    int count = 0;\n    for (int r = 0; r < m; r++) {\n        for (int c = 0; c < n; c++) {\n            if (grid[r][c] == '1') {\n                count++;\n                sink(grid, m, n, r, c);\n            }\n        }\n    }\n    return count;\n}",
                "correctCode": "void sink(char grid[300][300], int m, int n, int r, int c) {\n    if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != '1') return;\n    grid[r][c] = '0';\n    sink(grid, m, n, r + 1, c);\n    sink(grid, m, n, r - 1, c);\n    sink(grid, m, n, r, c + 1);\n    sink(grid, m, n, r, c - 1);\n}\n\nint numIslands(char grid[300][300], int m, int n) {\n    int count = 0;\n    for (int r = 0; r < m; r++) {\n        for (int c = 0; c < n; c++) {\n            if (grid[r][c] == '1') {\n                count++;\n                sink(grid, m, n, r, c);\n            }\n        }\n    }\n    return count;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nvoid dfs(vector<vector<char>>& grid, int r, int c) {\n    if (r < 0 || c < 0 || c >= (int)grid[0].size() || grid[r][c] != '1') return;\n    grid[r][c] = '0';\n    dfs(grid, r + 1, c);\n    dfs(grid, r - 1, c);\n    dfs(grid, r, c + 1);\n    dfs(grid, r, c - 1);\n}\n\nint numIslands(vector<vector<char>>& grid) {\n    int count = 0;\n    for (size_t r = 0; r < grid.size(); r++) {\n        for (size_t c = 0; c < grid[0].size(); c++) {\n            if (grid[r][c] == '1') {\n                count++;\n                dfs(grid, r, c);\n            }\n        }\n    }\n    return count;\n}",
                "correctCode": "#include <vector>\nusing namespace std;\n\nvoid dfs(vector<vector<char>>& grid, int r, int c) {\n    if (r < 0 || r >= (int)grid.size() || c < 0 || c >= (int)grid[0].size() || grid[r][c] != '1') return;\n    grid[r][c] = '0';\n    dfs(grid, r + 1, c);\n    dfs(grid, r - 1, c);\n    dfs(grid, r, c + 1);\n    dfs(grid, r, c - 1);\n}\n\nint numIslands(vector<vector<char>>& grid) {\n    int count = 0;\n    for (size_t r = 0; r < grid.size(); r++) {\n        for (size_t c = 0; c < grid[0].size(); c++) {\n            if (grid[r][c] == '1') {\n                count++;\n                dfs(grid, r, c);\n            }\n        }\n    }\n    return count;\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    private void dfs(char[][] grid, int r, int c) {\n        if (r < 0 || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;\n        grid[r][c] = '0';\n        dfs(grid, r + 1, c);\n        dfs(grid, r - 1, c);\n        dfs(grid, r, c + 1);\n        dfs(grid, r, c - 1);\n    }\n    public int numIslands(char[][] grid) {\n        int count = 0;\n        for (int r = 0; r < grid.length; r++) {\n            for (int c = 0; c < grid[0].length; c++) {\n                if (grid[r][c] == '1') {\n                    count++;\n                    dfs(grid, r, c);\n                }\n            }\n        }\n        return count;\n    }\n}",
                "correctCode": "class Solution {\n    private void dfs(char[][] grid, int r, int c) {\n        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;\n        grid[r][c] = '0';\n        dfs(grid, r + 1, c);\n        dfs(grid, r - 1, c);\n        dfs(grid, r, c + 1);\n        dfs(grid, r, c - 1);\n    }\n    public int numIslands(char[][] grid) {\n        int count = 0;\n        for (int r = 0; r < grid.length; r++) {\n            for (int c = 0; c < grid[0].length; c++) {\n                if (grid[r][c] == '1') {\n                    count++;\n                    dfs(grid, r, c);\n                }\n            }\n        }\n        return count;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_course_schedule",
        "title": "Course Schedule (Cycle Detection)",
        "problemStatement": "There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.\n\nFor example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.\n\nReturn `true` if you can finish all courses. Otherwise, return `false`.",
        "topic": "graphs",
        "subtopic": "topological-sort",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect traversal",
        "bugConcept": "Failure to remove node from active recursion stack (inStack/visiting state) after DFS explores all neighbors",
        "intendedApproach": "Use 3-color state tracking: 0 = unvisited, 1 = visiting (in recursion stack), 2 = fully processed. If DFS reaches a node in state 1, a cycle exists. Once all neighbors finish, set state = 2.",
        "explanation": "If `inStack[node]` is set to `true` but not reset to `false` when backtracking, cross-edges between separate DFS branches will falsely be detected as back-edges (cycles).",
        "constraints": [
            "1 <= numCourses <= 2000",
            "0 <= prerequisites.length <= 5000",
            "prerequisites[i].length == 2",
            "0 <= a_i, b_i < numCourses",
            "All prerequisite pairs are unique.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "numCourses = 2, prerequisites = [[1,0]]",
                "expectedOutput": "true",
                "isHidden": False,
                "explanation": "There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.",
            },
            {
                "id": 2,
                "input": "numCourses = 2, prerequisites = [[1,0],[0,1]]",
                "expectedOutput": "false",
                "isHidden": False,
                "explanation": "To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible due to a cycle.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]",
                "expectedOutput": "false",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]",
                "expectedOutput": "true",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "numCourses = 1, prerequisites = []",
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
            "topological-sort",
            "medium",
        ],
        "visualData": {
            "type": "graph",
            "title": "Dependency DAG",
            "data": {
                "nodes": [
                    "0",
                    "1",
                    "2",
                    "3",
                ],
                "edges": [
                    [
                        "0",
                        "1",
                    ],
                    [
                        "0",
                        "2",
                    ],
                    [
                        "1",
                        "3",
                    ],
                    [
                        "2",
                        "3",
                    ],
                ],
                "directed": True,
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n\nbool hasCycle(int node, int adj[2000][20], int* deg, bool* visited, bool* inStack) {\n    visited[node] = true;\n    inStack[node] = true;\n    for (int i = 0; i < deg[node]; i++) {\n        int next = adj[node][i];\n        if (inStack[next]) return true;\n        if (!visited[next] && hasCycle(next, adj, deg, visited, inStack)) return true;\n    }\n    return false;\n}",
                "correctCode": "#include <stdbool.h>\n\nbool hasCycle(int node, int adj[2000][20], int* deg, bool* visited, bool* inStack) {\n    visited[node] = true;\n    inStack[node] = true;\n    for (int i = 0; i < deg[node]; i++) {\n        int next = adj[node][i];\n        if (inStack[next]) return true;\n        if (!visited[next] && hasCycle(next, adj, deg, visited, inStack)) return true;\n    }\n    inStack[node] = false;\n    return false;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nbool hasCycle(int u, const vector<vector<int>>& adj, vector<int>& state) {\n    state[u] = 1; // 1 = visiting\n    for (int v : adj[u]) {\n        if (state[v] == 1) return true;\n        if (state[v] == 0 && hasCycle(v, adj, state)) return true;\n    }\n    return false;\n}\n\nbool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n    vector<vector<int>> adj(numCourses);\n    for (auto& p : prerequisites) adj[p[1]].push_back(p[0]);\n    vector<int> state(numCourses, 0);\n    for (int i = 0; i < numCourses; i++) {\n        if (state[i] == 0 && hasCycle(i, adj, state)) return false;\n    }\n    return true;\n}",
                "correctCode": "#include <vector>\nusing namespace std;\n\nbool hasCycle(int u, const vector<vector<int>>& adj, vector<int>& state) {\n    state[u] = 1; // 1 = visiting\n    for (int v : adj[u]) {\n        if (state[v] == 1) return true;\n        if (state[v] == 0 && hasCycle(v, adj, state)) return true;\n    }\n    state[u] = 2; // 2 = visited\n    return false;\n}\n\nbool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n    vector<vector<int>> adj(numCourses);\n    for (auto& p : prerequisites) adj[p[1]].push_back(p[0]);\n    vector<int> state(numCourses, 0);\n    for (int i = 0; i < numCourses; i++) {\n        if (state[i] == 0 && hasCycle(i, adj, state)) return false;\n    }\n    return true;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    private boolean hasCycle(int u, List<List<Integer>> adj, int[] state) {\n        state[u] = 1; // 1 = visiting\n        for (int v : adj.get(u)) {\n            if (state[v] == 1) return true;\n            if (state[v] == 0 && hasCycle(v, adj, state)) return true;\n        }\n        return false;\n    }\n    public boolean canFinish(int numCourses, int[][] prerequisites) {\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());\n        for (int[] p : prerequisites) adj.get(p[1]).add(p[0]);\n        int[] state = new int[numCourses];\n        for (int i = 0; i < numCourses; i++) {\n            if (state[i] == 0 && hasCycle(i, adj, state)) return false;\n        }\n        return true;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    private boolean hasCycle(int u, List<List<Integer>> adj, int[] state) {\n        state[u] = 1; // 1 = visiting\n        for (int v : adj.get(u)) {\n            if (state[v] == 1) return true;\n            if (state[v] == 0 && hasCycle(v, adj, state)) return true;\n        }\n        state[u] = 2; // 2 = visited\n        return false;\n    }\n    public boolean canFinish(int numCourses, int[][] prerequisites) {\n        List<List<Integer>> adj = new ArrayList<>();\n        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());\n        for (int[] p : prerequisites) adj.get(p[1]).add(p[0]);\n        int[] state = new int[numCourses];\n        for (int i = 0; i < numCourses; i++) {\n            if (state[i] == 0 && hasCycle(i, adj, state)) return false;\n        }\n        return true;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_rotting_oranges",
        "title": "Rotting Oranges (Multi-Source BFS)",
        "problemStatement": "You are given an `m x n` `grid` where each cell can have one of three values:\n- `0` representing an empty cell,\n- `1` representing a fresh orange, or\n- `2` representing a rotten orange.\n\nEvery minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.\n\nReturn the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.",
        "topic": "graphs",
        "subtopic": "bfs",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "boundary",
        "bugConcept": "Incrementing minute timer even when no new fresh oranges were infected in the current BFS level",
        "intendedApproach": "Count total fresh oranges. Push all initially rotten oranges (2) into BFS queue. While queue has elements and fresh > 0: increment minutes; process current level size; infect adjacent fresh oranges (1 -> 2), decrement fresh count, and push to queue. Return fresh == 0 ? minutes : -1.",
        "explanation": "If the BFS loop increments `minutes` unconditionally for the final empty queue pass, the answer is overcounted by 1 minute.",
        "constraints": [
            "m == grid.length",
            "n == grid[i].length",
            "1 <= m, n <= 10",
            "grid[i][j] is 0, 1, or 2.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "grid = [[2,1,1],[1,1,0],[0,1,1]]",
                "expectedOutput": "4",
                "isHidden": False,
                "explanation": "After 4 minutes, all fresh oranges become rotten through adjacent spread.",
            },
            {
                "id": 2,
                "input": "grid = [[2,1,1],[0,1,1],[1,0,1]]",
                "expectedOutput": "-1",
                "isHidden": False,
                "explanation": "The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "grid = [[0,2]]",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "grid = [[1]]",
                "expectedOutput": "-1",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "grid = [[2,2],[1,1],[0,0],[2,0]]",
                "expectedOutput": "1",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(M * N)",
        },
        "tags": [
            "graphs",
            "bfs",
            "matrix",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Orange Grid State: 3x3",
            "data": [
                [
                    2,
                    1,
                    1,
                ],
                [
                    1,
                    1,
                    0,
                ],
                [
                    0,
                    1,
                    1,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "int orangesRotting(int grid[10][10], int m, int n) {\n    int q[100][2], head = 0, tail = 0;\n    int fresh = 0;\n    for (int r = 0; r < m; r++) {\n        for (int c = 0; c < n; c++) {\n            if (grid[r][c] == 2) { q[tail][0] = r; q[tail++][1] = c; }\n            if (grid[r][c] == 1) fresh++;\n        }\n    }\n    int minutes = 0;\n    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};\n    while (head < tail) {\n        minutes++;\n        int size = tail - head;\n        for (int i = 0; i < size; i++) {\n            int r = q[head][0], c = q[head++][1];\n            for (int d = 0; d < 4; d++) {\n                int nr = r + dirs[d][0], nc = c + dirs[d][1];\n                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {\n                    grid[nr][nc] = 2;\n                    fresh--;\n                    q[tail][0] = nr; q[tail++][1] = nc;\n                }\n            }\n        }\n    }\n    return fresh == 0 ? minutes : -1;\n}",
                "correctCode": "int orangesRotting(int grid[10][10], int m, int n) {\n    int q[100][2], head = 0, tail = 0;\n    int fresh = 0;\n    for (int r = 0; r < m; r++) {\n        for (int c = 0; c < n; c++) {\n            if (grid[r][c] == 2) { q[tail][0] = r; q[tail++][1] = c; }\n            if (grid[r][c] == 1) fresh++;\n        }\n    }\n    int minutes = 0;\n    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};\n    while (head < tail && fresh > 0) {\n        minutes++;\n        int size = tail - head;\n        for (int i = 0; i < size; i++) {\n            int r = q[head][0], c = q[head++][1];\n            for (int d = 0; d < 4; d++) {\n                int nr = r + dirs[d][0], nc = c + dirs[d][1];\n                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {\n                    grid[nr][nc] = 2;\n                    fresh--;\n                    q[tail][0] = nr; q[tail++][1] = nc;\n                }\n            }\n        }\n    }\n    return fresh == 0 ? minutes : -1;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nint orangesRotting(vector<vector<int>>& grid) {\n    int m = grid.size(), n = grid[0].size(), fresh = 0;\n    queue<pair<int, int>> q;\n    for (int r = 0; r < m; r++) {\n        for (int c = 0; c < n; c++) {\n            if (grid[r][c] == 2) q.push({r, c});\n            if (grid[r][c] == 1) fresh++;\n        }\n    }\n    int minutes = 0;\n    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};\n    while (!q.empty()) {\n        minutes++;\n        int size = q.size();\n        for (int i = 0; i < size; i++) {\n            auto [r, c] = q.front(); q.pop();\n            for (auto& d : dirs) {\n                int nr = r + d[0], nc = c + d[1];\n                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {\n                    grid[nr][nc] = 2;\n                    fresh--;\n                    q.push({nr, nc});\n                }\n            }\n        }\n    }\n    return fresh == 0 ? minutes : -1;\n}",
                "correctCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nint orangesRotting(vector<vector<int>>& grid) {\n    int m = grid.size(), n = grid[0].size(), fresh = 0;\n    queue<pair<int, int>> q;\n    for (int r = 0; r < m; r++) {\n        for (int c = 0; c < n; c++) {\n            if (grid[r][c] == 2) q.push({r, c});\n            if (grid[r][c] == 1) fresh++;\n        }\n    }\n    int minutes = 0;\n    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};\n    while (!q.empty() && fresh > 0) {\n        minutes++;\n        int size = q.size();\n        for (int i = 0; i < size; i++) {\n            auto [r, c] = q.front(); q.pop();\n            for (auto& d : dirs) {\n                int nr = r + d[0], nc = c + d[1];\n                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {\n                    grid[nr][nc] = 2;\n                    fresh--;\n                    q.push({nr, nc});\n                }\n            }\n        }\n    }\n    return fresh == 0 ? minutes : -1;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    public int orangesRotting(int[][] grid) {\n        int m = grid.length, n = grid[0].length, fresh = 0;\n        Queue<int[]> q = new LinkedList<>();\n        for (int r = 0; r < m; r++) {\n            for (int c = 0; c < n; c++) {\n                if (grid[r][c] == 2) q.offer(new int[]{r, c});\n                if (grid[r][c] == 1) fresh++;\n            }\n        }\n        int minutes = 0;\n        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};\n        while (!q.isEmpty()) {\n            minutes++;\n            int size = q.size();\n            for (int i = 0; i < size; i++) {\n                int[] cell = q.poll();\n                for (int[] d : dirs) {\n                    int nr = cell[0] + d[0], nc = cell[1] + d[1];\n                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {\n                        grid[nr][nc] = 2;\n                        fresh--;\n                        q.offer(new int[]{nr, nc});\n                    }\n                }\n            }\n        }\n        return fresh == 0 ? minutes : -1;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    public int orangesRotting(int[][] grid) {\n        int m = grid.length, n = grid[0].length, fresh = 0;\n        Queue<int[]> q = new LinkedList<>();\n        for (int r = 0; r < m; r++) {\n            for (int c = 0; c < n; c++) {\n                if (grid[r][c] == 2) q.offer(new int[]{r, c});\n                if (grid[r][c] == 1) fresh++;\n            }\n        }\n        int minutes = 0;\n        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};\n        while (!q.isEmpty() && fresh > 0) {\n            minutes++;\n            int size = q.size();\n            for (int i = 0; i < size; i++) {\n                int[] cell = q.poll();\n                for (int[] d : dirs) {\n                    int nr = cell[0] + d[0], nc = cell[1] + d[1];\n                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {\n                        grid[nr][nc] = 2;\n                        fresh--;\n                        q.offer(new int[]{nr, nc});\n                    }\n                }\n            }\n        }\n        return fresh == 0 ? minutes : -1;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_network_delay_dijkstra",
        "title": "Network Delay Time (Dijkstra)",
        "problemStatement": "You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u_i, v_i, w_i)`, where `u_i` is the source node, `v_i` is the target node, and `w_i` is the time it takes for a signal to travel from source to target.\n\nWe will send a signal from a given node `k`. Return the minimum time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.",
        "topic": "graphs",
        "subtopic": "shortest-path",
        "difficulty": "medium",
        "estimatedTime": 25,
        "primaryBugType": "boundary",
        "bugConcept": "1-indexed vs 0-indexed node array offset when checking if all nodes are reached (skipping index n or checking index 0)",
        "intendedApproach": "Run Dijkstra's algorithm from node `k`. Maintain distance array dist[1..n] initialized to INF. Take maximum distance across all nodes 1..n. If any dist[i] == INF, return -1.",
        "explanation": "Because nodes are labeled 1 to n, distance array must be size n+1. Checking max distance over indices 0 to n-1 misses node n and incorrectly inspects unreached dummy index 0.",
        "constraints": [
            "1 <= k <= n <= 100",
            "1 <= times.length <= 6000",
            "times[i].length == 3",
            "1 <= u_i, v_i <= n",
            "u_i != v_i",
            "0 <= w_i <= 100",
            "All pairs (u_i, v_i) are unique.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2",
                "expectedOutput": "2",
                "isHidden": False,
                "explanation": "The signal sent from node 2 reaches node 1 in 1 unit of time, node 3 in 1 unit of time, and node 4 in 2 units of time (via node 3). Maximum time = 2.",
            },
            {
                "id": 2,
                "input": "times = [[1,2,1]], n = 2, k = 1",
                "expectedOutput": "1",
                "isHidden": False,
                "explanation": "Node 2 cannot reach node 1 because the edge is directed from 1 to 2.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "times = [[1,2,1]], n = 2, k = 2",
                "expectedOutput": "-1",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "times = [[1,2,1],[2,3,2],[1,3,4]], n = 3, k = 1",
                "expectedOutput": "3",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "times = [[1,2,1],[2,1,3]], n = 2, k = 2",
                "expectedOutput": "3",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(E log V)",
            "space": "O(V + E)",
        },
        "tags": [
            "graphs",
            "dijkstra",
            "shortest-path",
            "heap",
            "medium",
        ],
        "visualData": {
            "type": "graph",
            "title": "Weighted Directed Network",
            "data": {
                "nodes": [
                    "1",
                    "2",
                    "3",
                    "4",
                ],
                "edges": [
                    [
                        "2",
                        "1",
                        1,
                    ],
                    [
                        "2",
                        "3",
                        1,
                    ],
                    [
                        "3",
                        "4",
                        1,
                    ],
                ],
                "directed": True,
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <limits.h>\n\nint networkDelayTime(int times[][3], int timesSize, int n, int k) {\n    int dist[105];\n    for (int i = 1; i <= n; i++) dist[i] = 1000000;\n    dist[k] = 0;\n    for (int iter = 1; iter <= n - 1; iter++) {\n        for (int i = 0; i < timesSize; i++) {\n            int u = times[i][0], v = times[i][1], w = times[i][2];\n            if (dist[u] != 1000000 && dist[u] + w < dist[v]) {\n                dist[v] = dist[u] + w;\n            }\n        }\n    }\n    int maxD = 0;\n    for (int i = 0; i < n; i++) {\n        if (dist[i] > maxD) maxD = dist[i];\n    }\n    return maxD == 1000000 ? -1 : maxD;\n}",
                "correctCode": "#include <limits.h>\n\nint networkDelayTime(int times[][3], int timesSize, int n, int k) {\n    int dist[105];\n    for (int i = 1; i <= n; i++) dist[i] = 1000000;\n    dist[k] = 0;\n    for (int iter = 1; iter <= n - 1; iter++) {\n        for (int i = 0; i < timesSize; i++) {\n            int u = times[i][0], v = times[i][1], w = times[i][2];\n            if (dist[u] != 1000000 && dist[u] + w < dist[v]) {\n                dist[v] = dist[u] + w;\n            }\n        }\n    }\n    int maxD = 0;\n    for (int i = 1; i <= n; i++) {\n        if (dist[i] > maxD) maxD = dist[i];\n    }\n    return maxD == 1000000 ? -1 : maxD;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <queue>\n#include <algorithm>\nusing namespace std;\n\nint networkDelayTime(vector<vector<int>>& times, int n, int k) {\n    vector<vector<pair<int, int>>> adj(n + 1);\n    for (auto& t : times) adj[t[0]].push_back({t[1], t[2]});\n    vector<int> dist(n + 1, 1e9);\n    dist[k] = 0;\n    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;\n    pq.push({0, k});\n    while (!pq.empty()) {\n        auto [d, u] = pq.top(); pq.pop();\n        if (d > dist[u]) continue;\n        for (auto& edge : adj[u]) {\n            int v = edge.first, w = edge.second;\n            if (dist[u] + w < dist[v]) {\n                dist[v] = dist[u] + w;\n                pq.push({dist[v], v});\n            }\n        }\n    }\n    int maxD = 0;\n    for (int i = 0; i < n; i++) {\n        maxD = max(maxD, dist[i]);\n    }\n    return maxD >= 1e9 ? -1 : maxD;\n}",
                "correctCode": "#include <vector>\n#include <queue>\n#include <algorithm>\nusing namespace std;\n\nint networkDelayTime(vector<vector<int>>& times, int n, int k) {\n    vector<vector<pair<int, int>>> adj(n + 1);\n    for (auto& t : times) adj[t[0]].push_back({t[1], t[2]});\n    vector<int> dist(n + 1, 1e9);\n    dist[k] = 0;\n    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;\n    pq.push({0, k});\n    while (!pq.empty()) {\n        auto [d, u] = pq.top(); pq.pop();\n        if (d > dist[u]) continue;\n        for (auto& edge : adj[u]) {\n            int v = edge.first, w = edge.second;\n            if (dist[u] + w < dist[v]) {\n                dist[v] = dist[u] + w;\n                pq.push({dist[v], v});\n            }\n        }\n    }\n    int maxD = 0;\n    for (int i = 1; i <= n; i++) {\n        maxD = max(maxD, dist[i]);\n    }\n    return maxD >= 1e9 ? -1 : maxD;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    public int networkDelayTime(int[][] times, int n, int k) {\n        List<List<int[]>> adj = new ArrayList<>();\n        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());\n        for (int[] t : times) adj.get(t[0]).add(new int[]{t[1], t[2]});\n        int[] dist = new int[n + 1];\n        Arrays.fill(dist, Integer.MAX_VALUE);\n        dist[k] = 0;\n        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));\n        pq.offer(new int[]{0, k});\n        while (!pq.isEmpty()) {\n            int[] top = pq.poll();\n            int d = top[0], u = top[1];\n            if (d > dist[u]) continue;\n            for (int[] edge : adj.get(u)) {\n                int v = edge[0], w = edge[1];\n                if (dist[u] + w < dist[v]) {\n                    dist[v] = dist[u] + w;\n                    pq.offer(new int[]{dist[v], v});\n                }\n            }\n        }\n        int maxD = 0;\n        for (int i = 0; i < n; i++) {\n            maxD = Math.max(maxD, dist[i]);\n        }\n        return maxD == Integer.MAX_VALUE ? -1 : maxD;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    public int networkDelayTime(int[][] times, int n, int k) {\n        List<List<int[]>> adj = new ArrayList<>();\n        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());\n        for (int[] t : times) adj.get(t[0]).add(new int[]{t[1], t[2]});\n        int[] dist = new int[n + 1];\n        Arrays.fill(dist, Integer.MAX_VALUE);\n        dist[k] = 0;\n        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));\n        pq.offer(new int[]{0, k});\n        while (!pq.isEmpty()) {\n            int[] top = pq.poll();\n            int d = top[0], u = top[1];\n            if (d > dist[u]) continue;\n            for (int[] edge : adj.get(u)) {\n                int v = edge[0], w = edge[1];\n                if (dist[u] + w < dist[v]) {\n                    dist[v] = dist[u] + w;\n                    pq.offer(new int[]{dist[v], v});\n                }\n            }\n        }\n        int maxD = 0;\n        for (int i = 1; i <= n; i++) {\n            maxD = Math.max(maxD, dist[i]);\n        }\n        return maxD == Integer.MAX_VALUE ? -1 : maxD;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_redundant_connection",
        "title": "Redundant Connection (Cycle Edge via DSU)",
        "problemStatement": "In this problem, a tree is an undirected graph that is connected and has no cycles.\n\nYou are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the graph.\n\nReturn an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.",
        "topic": "graphs",
        "subtopic": "cycle-detection",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "logical",
        "bugConcept": "Missing recursive path compression in Disjoint Set Find function (parent[x] = find(parent[x]))",
        "intendedApproach": "Initialize Disjoint Set Union (DSU) where parent[i] = i. For each edge (u, v): find root(u) and root(v). If root(u) == root(v), this edge creates a cycle, return [u, v]. Otherwise union(root(u), root(v)).",
        "explanation": "If the `find` function does `return parent[x]` without recursing or path-compressing, deep disjoint trees report immediate parents instead of the true set representative root, failing to detect cycle-forming connections.",
        "constraints": [
            "n == edges.length",
            "3 <= n <= 1000",
            "edges[i].length == 2",
            "1 <= u_i < v_i <= n",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "edges = [[1,2],[1,3],[2,3]]",
                "expectedOutput": "[2,3]",
                "isHidden": False,
                "explanation": "Removing edge [2,3] leaves a connected tree connecting all nodes 1, 2, and 3.",
            },
            {
                "id": 2,
                "input": "edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]",
                "expectedOutput": "[1,4]",
                "isHidden": False,
                "explanation": "The edge [1,4] creates a redundant cycle and occurs last in the input.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "edges = [[1,2],[2,3],[3,1]]",
                "expectedOutput": "[3,1]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "edges = [[1,3],[3,4],[1,5],[3,5],[2,3]]",
                "expectedOutput": "[3,5]",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]",
                "expectedOutput": "[1,3]",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N * alpha(N))",
            "space": "O(N)",
        },
        "tags": [
            "graphs",
            "dsu",
            "union-find",
            "cycle-detection",
            "medium",
        ],
        "visualData": {
            "type": "graph",
            "title": "Redundant Edge Cycle: [2, 3]",
            "data": {
                "nodes": [
                    "1",
                    "2",
                    "3",
                ],
                "edges": [
                    [
                        "1",
                        "2",
                    ],
                    [
                        "1",
                        "3",
                    ],
                    [
                        "2",
                        "3",
                    ],
                ],
                "directed": False,
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "int findParent(int* parent, int x) {\n    if (parent[x] == x) return x;\n    return parent[x];\n}\n\nvoid findRedundantConnection(int edges[][2], int n, int* out1, int* out2) {\n    int parent[1005];\n    for (int i = 1; i <= n; i++) parent[i] = i;\n    for (int i = 0; i < n; i++) {\n        int rootU = findParent(parent, edges[i][0]);\n        int rootV = findParent(parent, edges[i][1]);\n        if (rootU == rootV) {\n            *out1 = edges[i][0]; *out2 = edges[i][1]; return;\n        }\n        parent[rootU] = rootV;\n    }\n}",
                "correctCode": "int findParent(int* parent, int x) {\n    if (parent[x] == x) return x;\n    return parent[x] = findParent(parent, parent[x]);\n}\n\nvoid findRedundantConnection(int edges[][2], int n, int* out1, int* out2) {\n    int parent[1005];\n    for (int i = 1; i <= n; i++) parent[i] = i;\n    for (int i = 0; i < n; i++) {\n        int rootU = findParent(parent, edges[i][0]);\n        int rootV = findParent(parent, edges[i][1]);\n        if (rootU == rootV) {\n            *out1 = edges[i][0]; *out2 = edges[i][1]; return;\n        }\n        parent[rootU] = rootV;\n    }\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nint findParent(vector<int>& parent, int x) {\n    if (parent[x] == x) return x;\n    return parent[x];\n}\n\nvector<int> findRedundantConnection(vector<vector<int>>& edges) {\n    int n = edges.size();\n    vector<int> parent(n + 1);\n    for (int i = 1; i <= n; i++) parent[i] = i;\n    for (auto& edge : edges) {\n        int rootU = findParent(parent, edge[0]);\n        int rootV = findParent(parent, edge[1]);\n        if (rootU == rootV) return edge;\n        parent[rootU] = rootV;\n    }\n    return {};\n}",
                "correctCode": "#include <vector>\nusing namespace std;\n\nint findParent(vector<int>& parent, int x) {\n    if (parent[x] == x) return x;\n    return parent[x] = findParent(parent, parent[x]);\n}\n\nvector<int> findRedundantConnection(vector<vector<int>>& edges) {\n    int n = edges.size();\n    vector<int> parent(n + 1);\n    for (int i = 1; i <= n; i++) parent[i] = i;\n    for (auto& edge : edges) {\n        int rootU = findParent(parent, edge[0]);\n        int rootV = findParent(parent, edge[1]);\n        if (rootU == rootV) return edge;\n        parent[rootU] = rootV;\n    }\n    return {};\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    private int findParent(int[] parent, int x) {\n        if (parent[x] == x) return x;\n        return parent[x];\n    }\n    public int[] findRedundantConnection(int[][] edges) {\n        int n = edges.length;\n        int[] parent = new int[n + 1];\n        for (int i = 1; i <= n; i++) parent[i] = i;\n        for (int[] edge : edges) {\n            int rootU = findParent(parent, edge[0]);\n            int rootV = findParent(parent, edge[1]);\n            if (rootU == rootV) return edge;\n            parent[rootU] = rootV;\n        }\n        return new int[0];\n    }\n}",
                "correctCode": "class Solution {\n    private int findParent(int[] parent, int x) {\n        if (parent[x] == x) return x;\n        return parent[x] = findParent(parent, parent[x]);\n    }\n    public int[] findRedundantConnection(int[][] edges) {\n        int n = edges.length;\n        int[] parent = new int[n + 1];\n        for (int i = 1; i <= n; i++) parent[i] = i;\n        for (int[] edge : edges) {\n            int rootU = findParent(parent, edge[0]);\n            int rootV = findParent(parent, edge[1]);\n            if (rootU == rootV) return edge;\n            parent[rootU] = rootV;\n        }\n        return new int[0];\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_pacific_atlantic",
        "title": "Pacific Atlantic Water Flow",
        "problemStatement": "There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.\n\nThe island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.\n\nThe island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.\n\nReturn a 2D list of grid coordinates `result` where `result[i] = [r_i, c_i]` denotes that rain water can flow from cell `(r_i, c_i)` to both the Pacific and Atlantic oceans.",
        "topic": "graphs",
        "subtopic": "dfs",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect condition",
        "bugConcept": "Inverted flow condition in reverse BFS/DFS (checking heights[nr][nc] < heights[r][c] instead of >= when moving uphill from oceans)",
        "intendedApproach": "Reverse flow search: Start DFS/BFS from ocean borders uphill. Ocean water can reach adjacent cell if `heights[nr][nc] >= heights[r][c]`. Mark reachable cells in pacific[m][n] and atlantic[m][n]. Intersect.",
        "explanation": "Because we trace water flow backwards starting from the ocean onto the island, water can only flow backwards uphill (`heights[neighbor] >= heights[current]`). Using `<` inverts the logic.",
        "constraints": [
            "m == heights.length",
            "n == heights[r].length",
            "1 <= m, n <= 200",
            "0 <= heights[r][c] <= 10^5",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]",
                "expectedOutput": "[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]",
                "isHidden": False,
                "explanation": "Water from cells [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]] can flow to both Pacific (top/left) and Atlantic (bottom/right) oceans.",
            },
            {
                "id": 2,
                "input": "heights = [[1]]",
                "expectedOutput": "[[0,0]]",
                "isHidden": False,
                "explanation": "The only cell in the grid connects to both oceans.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "heights = [[2,1],[1,2]]",
                "expectedOutput": "[[0,0],[0,1],[1,0],[1,1]]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "heights = [[1,2,3],[8,9,4],[7,6,5]]",
                "expectedOutput": "[[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]",
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
            "matrix",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Island Elevation Heights",
            "data": [
                [
                    1,
                    2,
                    2,
                    3,
                    5,
                ],
                [
                    3,
                    2,
                    3,
                    4,
                    4,
                ],
                [
                    2,
                    4,
                    5,
                    3,
                    1,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n\nvoid dfs(int heights[200][200], int m, int n, int r, int c, bool visited[200][200]) {\n    visited[r][c] = true;\n    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};\n    for (int d = 0; d < 4; d++) {\n        int nr = r + dirs[d][0], nc = c + dirs[d][1];\n        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] && heights[nr][nc] < heights[r][c]) {\n            dfs(heights, m, n, nr, nc, visited);\n        }\n    }\n}",
                "correctCode": "#include <stdbool.h>\n\nvoid dfs(int heights[200][200], int m, int n, int r, int c, bool visited[200][200]) {\n    visited[r][c] = true;\n    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};\n    for (int d = 0; d < 4; d++) {\n        int nr = r + dirs[d][0], nc = c + dirs[d][1];\n        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] && heights[nr][nc] >= heights[r][c]) {\n            dfs(heights, m, n, nr, nc, visited);\n        }\n    }\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nvoid dfs(const vector<vector<int>>& heights, int r, int c, vector<vector<bool>>& visited) {\n    visited[r][c] = true;\n    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};\n    for (auto& d : dirs) {\n        int nr = r + d[0], nc = c + d[1];\n        if (nr >= 0 && nr < (int)heights.size() && nc >= 0 && nc < (int)heights[0].size() && !visited[nr][nc] && heights[nr][nc] < heights[r][c]) {\n            dfs(heights, nr, nc, visited);\n        }\n    }\n}",
                "correctCode": "#include <vector>\nusing namespace std;\n\nvoid dfs(const vector<vector<int>>& heights, int r, int c, vector<vector<bool>>& visited) {\n    visited[r][c] = true;\n    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};\n    for (auto& d : dirs) {\n        int nr = r + d[0], nc = c + d[1];\n        if (nr >= 0 && nr < (int)heights.size() && nc >= 0 && nc < (int)heights[0].size() && !visited[nr][nc] && heights[nr][nc] >= heights[r][c]) {\n            dfs(heights, nr, nc, visited);\n        }\n    }\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    private void dfs(int[][] heights, int r, int c, boolean[][] visited) {\n        visited[r][c] = true;\n        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};\n        for (int[] d : dirs) {\n            int nr = r + d[0], nc = c + d[1];\n            if (nr >= 0 && nr < heights.length && nc >= 0 && nc < heights[0].length && !visited[nr][nc] && heights[nr][nc] < heights[r][c]) {\n                dfs(heights, nr, nc, visited);\n            }\n        }\n    }\n}",
                "correctCode": "class Solution {\n    private void dfs(int[][] heights, int r, int c, boolean[][] visited) {\n        visited[r][c] = true;\n        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};\n        for (int[] d : dirs) {\n            int nr = r + d[0], nc = c + d[1];\n            if (nr >= 0 && nr < heights.length && nc >= 0 && nc < heights[0].length && !visited[nr][nc] && heights[nr][nc] >= heights[r][c]) {\n                dfs(heights, nr, nc, visited);\n            }\n        }\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_word_ladder",
        "title": "Word Ladder (Shortest Transformation Sequence)",
        "problemStatement": "A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:\n- Every adjacent pair of words differs by a single letter.\n- Every `s_i` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.\n- `s_k == endWord`\n\nGiven two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.",
        "topic": "graphs",
        "subtopic": "bfs",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect traversal",
        "bugConcept": "Forgetting to erase transformed word from wordSet upon pushing to queue, resulting in duplicate visits and cyclic infinite BFS loops",
        "intendedApproach": "Store wordList in a HashSet. Use BFS queue initialized with beginWord, level = 1. For each word in level, try changing each character 'a'..'z'. If matching word in set: if word == endWord return level + 1; else erase word from set and push to queue.",
        "explanation": "If a visited valid word is not deleted from `wordSet`, subsequent BFS branches will discover it again, causing repeated cycles and memory explosion / timeout.",
        "constraints": [
            "1 <= beginWord.length <= 10",
            "endWord.length == beginWord.length",
            "1 <= wordList.length <= 5000",
            "wordList[i].length == beginWord.length",
            "All strings consist of lowercase English letters.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]",
                "expectedOutput": "5",
                "isHidden": False,
                "explanation": "One shortest transformation sequence is \"hit\" -> \"hot\" -> \"dot\" -> \"dog\" -> \"cog\", which is 5 words long.",
            },
            {
                "id": 2,
                "input": "beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]",
                "expectedOutput": "0",
                "isHidden": False,
                "explanation": "The endWord \"cog\" is not in wordList, therefore there is no valid transformation sequence.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "beginWord = \"a\", endWord = \"c\", wordList = [\"a\",\"b\",\"c\"]",
                "expectedOutput": "2",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "beginWord = \"hot\", endWord = \"dog\", wordList = [\"hot\",\"dog\"]",
                "expectedOutput": "0",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N * L * 26)",
            "space": "O(N * L)",
        },
        "tags": [
            "graphs",
            "bfs",
            "shortest-path",
            "hard",
        ],
        "visualData": {
            "type": "graph",
            "title": "Transformation Word Graph",
            "data": {
                "nodes": [
                    "hit",
                    "hot",
                    "dot",
                    "dog",
                    "cog",
                ],
                "edges": [
                    [
                        "hit",
                        "hot",
                    ],
                    [
                        "hot",
                        "dot",
                    ],
                    [
                        "dot",
                        "dog",
                    ],
                    [
                        "dog",
                        "cog",
                    ],
                ],
                "directed": True,
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <string.h>\n#include <stdbool.h>\n\n// Word ladder queue BFS simulator\nint ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize) {\n    bool inList = false;\n    for (int i = 0; i < wordListSize; i++) if (strcmp(wordList[i], endWord) == 0) inList = true;\n    if (!inList) return 0;\n    bool visited[5000] = {false};\n    char queue[5000][12];\n    int head = 0, tail = 0, level = 1;\n    strcpy(queue[tail++], beginWord);\n    while (head < tail) {\n        int size = tail - head;\n        for (int i = 0; i < size; i++) {\n            char* curr = queue[head++];\n            if (strcmp(curr, endWord) == 0) return level;\n            for (int j = 0; j < wordListSize; j++) {\n                int diff = 0;\n                for (int k = 0; curr[k] != '\\0'; k++) if (curr[k] != wordList[j][k]) diff++;\n                if (diff == 1) {\n                    strcpy(queue[tail++], wordList[j]);\n                }\n            }\n        }\n        level++;\n    }\n    return 0;\n}",
                "correctCode": "#include <string.h>\n#include <stdbool.h>\n\nint ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize) {\n    bool inList = false;\n    for (int i = 0; i < wordListSize; i++) if (strcmp(wordList[i], endWord) == 0) inList = true;\n    if (!inList) return 0;\n    bool visited[5000] = {false};\n    char queue[5000][12];\n    int head = 0, tail = 0, level = 1;\n    strcpy(queue[tail++], beginWord);\n    while (head < tail) {\n        int size = tail - head;\n        for (int i = 0; i < size; i++) {\n            char* curr = queue[head++];\n            if (strcmp(curr, endWord) == 0) return level;\n            for (int j = 0; j < wordListSize; j++) {\n                if (!visited[j]) {\n                    int diff = 0;\n                    for (int k = 0; curr[k] != '\\0'; k++) if (curr[k] != wordList[j][k]) diff++;\n                    if (diff == 1) {\n                        visited[j] = true;\n                        strcpy(queue[tail++], wordList[j]);\n                    }\n                }\n            }\n        }\n        level++;\n    }\n    return 0;\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\n#include <queue>\n#include <unordered_set>\nusing namespace std;\n\nint ladderLength(string beginWord, string endWord, vector<string>& wordList) {\n    unordered_set<string> dict(wordList.begin(), wordList.end());\n    if (!dict.count(endWord)) return 0;\n    queue<string> q;\n    q.push(beginWord);\n    int level = 1;\n    while (!q.empty()) {\n        int size = q.size();\n        for (int i = 0; i < size; i++) {\n            string word = q.front(); q.pop();\n            if (word == endWord) return level;\n            for (size_t j = 0; j < word.length(); j++) {\n                char orig = word[j];\n                for (char c = 'a'; c <= 'z'; c++) {\n                    word[j] = c;\n                    if (dict.count(word)) {\n                        q.push(word);\n                    }\n                }\n                word[j] = orig;\n            }\n        }\n        level++;\n    }\n    return 0;\n}",
                "correctCode": "#include <string>\n#include <vector>\n#include <queue>\n#include <unordered_set>\nusing namespace std;\n\nint ladderLength(string beginWord, string endWord, vector<string>& wordList) {\n    unordered_set<string> dict(wordList.begin(), wordList.end());\n    if (!dict.count(endWord)) return 0;\n    queue<string> q;\n    q.push(beginWord);\n    int level = 1;\n    while (!q.empty()) {\n        int size = q.size();\n        for (int i = 0; i < size; i++) {\n            string word = q.front(); q.pop();\n            if (word == endWord) return level;\n            for (size_t j = 0; j < word.length(); j++) {\n                char orig = word[j];\n                for (char c = 'a'; c <= 'z'; c++) {\n                    word[j] = c;\n                    if (dict.count(word)) {\n                        q.push(word);\n                        dict.erase(word);\n                    }\n                }\n                word[j] = orig;\n            }\n        }\n        level++;\n    }\n    return 0;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        Set<String> dict = new HashSet<>(wordList);\n        if (!dict.contains(endWord)) return 0;\n        Queue<String> q = new LinkedList<>();\n        q.offer(beginWord);\n        int level = 1;\n        while (!q.isEmpty()) {\n            int size = q.size();\n            for (int i = 0; i < size; i++) {\n                String word = q.poll();\n                if (word.equals(endWord)) return level;\n                char[] chs = word.toCharArray();\n                for (int j = 0; j < chs.length; j++) {\n                    char orig = chs[j];\n                    for (char c = 'a'; c <= 'z'; c++) {\n                        chs[j] = c;\n                        String nextWord = new String(chs);\n                        if (dict.contains(nextWord)) {\n                            q.offer(nextWord);\n                        }\n                    }\n                    chs[j] = orig;\n                }\n            }\n            level++;\n        }\n        return 0;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        Set<String> dict = new HashSet<>(wordList);\n        if (!dict.contains(endWord)) return 0;\n        Queue<String> q = new LinkedList<>();\n        q.offer(beginWord);\n        int level = 1;\n        while (!q.isEmpty()) {\n            int size = q.size();\n            for (int i = 0; i < size; i++) {\n                String word = q.poll();\n                if (word.equals(endWord)) return level;\n                char[] chs = word.toCharArray();\n                for (int j = 0; j < chs.length; j++) {\n                    char orig = chs[j];\n                    for (char c = 'a'; c <= 'z'; c++) {\n                        chs[j] = c;\n                        String nextWord = new String(chs);\n                        if (dict.contains(nextWord)) {\n                            q.offer(nextWord);\n                            dict.remove(nextWord);\n                        }\n                    }\n                    chs[j] = orig;\n                }\n            }\n            level++;\n        }\n        return 0;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_valid_tree",
        "title": "Graph Valid Tree",
        "problemStatement": "You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [a_i, b_i]` indicates that there is an undirected edge between nodes `a_i` and `b_i` in the graph.\n\nReturn `true` if the edges of the given graph make up a valid tree, and `false` otherwise.\n\nA valid tree is an undirected graph that is fully connected and contains no cycles.",
        "topic": "graphs",
        "subtopic": "cycle-detection",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "boundary",
        "bugConcept": "Missing edge count check (edges.length != n - 1), incorrectly classifying disconnected graphs as valid trees",
        "intendedApproach": "A graph of n nodes is a tree if and only if it has exactly n-1 edges and contains no cycles (or all nodes are connected in a single component).",
        "explanation": "If a graph has n=4 nodes and edges [[0,1],[2,3]], there is no cycle, but the graph is disconnected into 2 separate components. Checking only for cycles without verifying `edges.length == n - 1` fails on disconnected graphs.",
        "constraints": [
            "1 <= n <= 2000",
            "0 <= edges.length <= 5000",
            "edges[i].length == 2",
            "0 <= u_i, v_i < n",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]",
                "expectedOutput": "true",
                "isHidden": False,
                "explanation": "The graph contains 5 nodes and 4 edges with no cycles and connects all nodes, which forms a valid tree.",
            },
            {
                "id": 2,
                "input": "n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]",
                "expectedOutput": "false",
                "isHidden": False,
                "explanation": "The edges [1,2], [2,3], [1,3] form a cycle, so the graph is not a tree.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "n = 4, edges = [[0,1],[2,3]]",
                "expectedOutput": "false",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "n = 1, edges = []",
                "expectedOutput": "true",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "n = 3, edges = [[0,1]]",
                "expectedOutput": "false",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(V + E)",
            "space": "O(V)",
        },
        "tags": [
            "graphs",
            "dsu",
            "bfs",
            "dfs",
            "medium",
        ],
        "visualData": {
            "type": "graph",
            "title": "Tree Graph: n=5",
            "data": {
                "nodes": [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                ],
                "edges": [
                    [
                        "0",
                        "1",
                    ],
                    [
                        "0",
                        "2",
                    ],
                    [
                        "0",
                        "3",
                    ],
                    [
                        "1",
                        "4",
                    ],
                ],
                "directed": False,
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n\nint find(int* parent, int i) {\n    if (parent[i] == i) return i;\n    return parent[i] = find(parent, parent[i]);\n}\n\nbool validTree(int n, int edges[][2], int edgeCount) {\n    int parent[2005];\n    for (int i = 0; i < n; i++) parent[i] = i;\n    for (int i = 0; i < edgeCount; i++) {\n        int rootU = find(parent, edges[i][0]);\n        int rootV = find(parent, edges[i][1]);\n        if (rootU == rootV) return false;\n        parent[rootU] = rootV;\n    }\n    return true;\n}",
                "correctCode": "#include <stdbool.h>\n\nint find(int* parent, int i) {\n    if (parent[i] == i) return i;\n    return parent[i] = find(parent, parent[i]);\n}\n\nbool validTree(int n, int edges[][2], int edgeCount) {\n    if (edgeCount != n - 1) return false;\n    int parent[2005];\n    for (int i = 0; i < n; i++) parent[i] = i;\n    for (int i = 0; i < edgeCount; i++) {\n        int rootU = find(parent, edges[i][0]);\n        int rootV = find(parent, edges[i][1]);\n        if (rootU == rootV) return false;\n        parent[rootU] = rootV;\n    }\n    return true;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nint find(vector<int>& parent, int i) {\n    if (parent[i] == i) return i;\n    return parent[i] = find(parent, parent[i]);\n}\n\nbool validTree(int n, vector<vector<int>>& edges) {\n    vector<int> parent(n);\n    for (int i = 0; i < n; i++) parent[i] = i;\n    for (auto& edge : edges) {\n        int rootU = find(parent, edge[0]);\n        int rootV = find(parent, edge[1]);\n        if (rootU == rootV) return false;\n        parent[rootU] = rootV;\n    }\n    return true;\n}",
                "correctCode": "#include <vector>\nusing namespace std;\n\nint find(vector<int>& parent, int i) {\n    if (parent[i] == i) return i;\n    return parent[i] = find(parent, parent[i]);\n}\n\nbool validTree(int n, vector<vector<int>>& edges) {\n    if ((int)edges.size() != n - 1) return false;\n    vector<int> parent(n);\n    for (int i = 0; i < n; i++) parent[i] = i;\n    for (auto& edge : edges) {\n        int rootU = find(parent, edge[0]);\n        int rootV = find(parent, edge[1]);\n        if (rootU == rootV) return false;\n        parent[rootU] = rootV;\n    }\n    return true;\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    private int find(int[] parent, int i) {\n        if (parent[i] == i) return i;\n        return parent[i] = find(parent, parent[i]);\n    }\n    public boolean validTree(int n, int[][] edges) {\n        int[] parent = new int[n];\n        for (int i = 0; i < n; i++) parent[i] = i;\n        for (int[] edge : edges) {\n            int rootU = find(parent, edge[0]);\n            int rootV = find(parent, edge[1]);\n            if (rootU == rootV) return false;\n            parent[rootU] = rootV;\n        }\n        return true;\n    }\n}",
                "correctCode": "class Solution {\n    private int find(int[] parent, int i) {\n        if (parent[i] == i) return i;\n        return parent[i] = find(parent, parent[i]);\n    }\n    public boolean validTree(int n, int[][] edges) {\n        if (edges.length != n - 1) return false;\n        int[] parent = new int[n];\n        for (int i = 0; i < n; i++) parent[i] = i;\n        for (int[] edge : edges) {\n            int rootU = find(parent, edge[0]);\n            int rootV = find(parent, edge[1]);\n            if (rootU == rootV) return false;\n            parent[rootU] = rootV;\n        }\n        return true;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_is_bipartite",
        "title": "Is Graph Bipartite? (Two-Coloring)",
        "problemStatement": "There is an undirected graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to.\n\nA graph is bipartite if the nodes can be partitioned into two independent sets `A` and `B` such that every edge in the graph connects a node in set `A` and a node in set `B`.\n\nReturn `true` if and only if it is bipartite.",
        "topic": "graphs",
        "subtopic": "bfs",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "boundary",
        "bugConcept": "Only running coloring BFS from node 0, failing to check disconnected graph components",
        "intendedApproach": "Use a color array initialized to 0 (uncolored). For each node i from 0 to n-1: if color[i] == 0, start BFS with color 1. Alternate colors 1 and -1 for neighbors. If neighbor has same color, return false.",
        "explanation": "If the graph has multiple disconnected components (e.g. {0, 1} and {2, 3}), running BFS only starting at node 0 leaves component {2, 3} uninspected, missing conflicting odd cycles.",
        "constraints": [
            "graph.length == n",
            "1 <= n <= 100",
            "0 <= graph[u].length < n",
            "0 <= graph[u][i] <= n - 1",
            "graph[u] does not contain u and no duplicate edges.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "graph = [[1,2,3],[0,2],[0,1,3],[0,2]]",
                "expectedOutput": "false",
                "isHidden": False,
                "explanation": "We can divide the vertices into two groups: {0, 3} and {1, 2}. Every edge connects a vertex from the first group to the second.",
            },
            {
                "id": 2,
                "input": "graph = [[1,3],[0,2],[1,3],[0,2]]",
                "expectedOutput": "true",
                "isHidden": False,
                "explanation": "We cannot divide the vertices into two independent sets because nodes 0, 1, 2 form an odd-length cycle of 3 edges.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]",
                "expectedOutput": "false",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "graph = [[1],[0],[3],[2]]",
                "expectedOutput": "true",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "graph = [[]]",
                "expectedOutput": "true",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(V + E)",
            "space": "O(V)",
        },
        "tags": [
            "graphs",
            "bfs",
            "dfs",
            "bipartite",
            "medium",
        ],
        "visualData": {
            "type": "graph",
            "title": "Bipartite 2-Color Graph",
            "data": {
                "nodes": [
                    "0",
                    "1",
                    "2",
                    "3",
                ],
                "edges": [
                    [
                        "0",
                        "1",
                    ],
                    [
                        "1",
                        "2",
                    ],
                    [
                        "2",
                        "3",
                    ],
                    [
                        "3",
                        "0",
                    ],
                ],
                "directed": False,
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n\nbool isBipartite(int graph[100][100], int* colSizes, int n) {\n    int color[105] = {0};\n    int q[105], head = 0, tail = 0;\n    color[0] = 1;\n    q[tail++] = 0;\n    while (head < tail) {\n        int u = q[head++];\n        for (int i = 0; i < colSizes[u]; i++) {\n            int v = graph[u][i];\n            if (color[v] == color[u]) return false;\n            if (color[v] == 0) {\n                color[v] = -color[u];\n                q[tail++] = v;\n            }\n        }\n    }\n    return true;\n}",
                "correctCode": "#include <stdbool.h>\n\nbool isBipartite(int graph[100][100], int* colSizes, int n) {\n    int color[105] = {0};\n    for (int start = 0; start < n; start++) {\n        if (color[start] != 0) continue;\n        int q[105], head = 0, tail = 0;\n        color[start] = 1;\n        q[tail++] = start;\n        while (head < tail) {\n            int u = q[head++];\n            for (int i = 0; i < colSizes[u]; i++) {\n                int v = graph[u][i];\n                if (color[v] == color[u]) return false;\n                if (color[v] == 0) {\n                    color[v] = -color[u];\n                    q[tail++] = v;\n                }\n            }\n        }\n    }\n    return true;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nbool isBipartite(vector<vector<int>>& graph) {\n    int n = graph.size();\n    vector<int> color(n, 0);\n    queue<int> q;\n    color[0] = 1;\n    q.push(0);\n    while (!q.empty()) {\n        int u = q.front(); q.pop();\n        for (int v : graph[u]) {\n            if (color[v] == color[u]) return false;\n            if (color[v] == 0) {\n                color[v] = -color[u];\n                q.push(v);\n            }\n        }\n    }\n    return true;\n}",
                "correctCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nbool isBipartite(vector<vector<int>>& graph) {\n    int n = graph.size();\n    vector<int> color(n, 0);\n    for (int start = 0; start < n; start++) {\n        if (color[start] != 0) continue;\n        queue<int> q;\n        color[start] = 1;\n        q.push(start);\n        while (!q.empty()) {\n            int u = q.front(); q.pop();\n            for (int v : graph[u]) {\n                if (color[v] == color[u]) return false;\n                if (color[v] == 0) {\n                    color[v] = -color[u];\n                    q.push(v);\n                }\n            }\n        }\n    }\n    return true;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    public boolean isBipartite(int[][] graph) {\n        int n = graph.length;\n        int[] color = new int[n];\n        Queue<Integer> q = new LinkedList<>();\n        color[0] = 1;\n        q.offer(0);\n        while (!q.isEmpty()) {\n            int u = q.poll();\n            for (int v : graph[u]) {\n                if (color[v] == color[u]) return false;\n                if (color[v] == 0) {\n                    color[v] = -color[u];\n                    q.offer(v);\n                }\n            }\n        }\n        return true;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    public boolean isBipartite(int[][] graph) {\n        int n = graph.length;\n        int[] color = new int[n];\n        for (int start = 0; start < n; start++) {\n            if (color[start] != 0) continue;\n            Queue<Integer> q = new LinkedList<>();\n            color[start] = 1;\n            q.offer(start);\n            while (!q.isEmpty()) {\n                int u = q.poll();\n                for (int v : graph[u]) {\n                    if (color[v] == color[u]) return false;\n                    if (color[v] == 0) {\n                        color[v] = -color[u];\n                        q.offer(v);\n                    }\n                }\n            }\n        }\n        return true;\n    }\n}",
            },
        },
    },
    {
        "id": "q_graph_min_spanning_tree",
        "title": "Minimum Spanning Tree (Kruskal)",
        "problemStatement": "Given a weighted, undirected, and connected graph of `V` vertices and `E` edges, find the sum of weights of the edges of the Minimum Spanning Tree (MST).\n\nA minimum spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.",
        "topic": "graphs",
        "subtopic": "shortest-path",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "logical",
        "bugConcept": "Forgetting to sort edges by weight in ascending order before greedily adding via Disjoint Set Union",
        "intendedApproach": "Sort all edges by weight in ascending order. Initialize DSU. For each edge (u, v, w): if find(u) != find(v), union(u, v) and add w to total MST weight.",
        "explanation": "Kruskal's greedy algorithm requires edges to be processed in non-decreasing order of weight. Processing edges in arbitrary input order adds costly cycle-free edges instead of the minimum spanning edges.",
        "constraints": [
            "2 <= V <= 1000",
            "1 <= E <= 10^4",
            "1 <= weight <= 1000",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "V = 3, edges = [[0,1,5],[1,2,3],[0,2,1]]",
                "expectedOutput": "4",
                "isHidden": False,
                "explanation": "The edges in the MST are (0,1) with weight 5 and (1,2) with weight 10. Total weight = 15.",
            },
            {
                "id": 2,
                "input": "V = 2, edges = [[0,1,5]]",
                "expectedOutput": "5",
                "isHidden": False,
                "explanation": "The MST contains edges with weights 1, 2, and 2, giving total weight 5.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "V = 4, edges = [[0,1,1],[1,2,2],[2,3,3],[0,3,4],[0,2,5]]",
                "expectedOutput": "6",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "V = 3, edges = [[0,1,10],[1,2,10],[0,2,5]]",
                "expectedOutput": "15",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(E log E)",
            "space": "O(V)",
        },
        "tags": [
            "graphs",
            "kruskal",
            "dsu",
            "greedy",
            "medium",
        ],
        "visualData": {
            "type": "graph",
            "title": "Weighted Graph MST Selection",
            "data": {
                "nodes": [
                    "0",
                    "1",
                    "2",
                ],
                "edges": [
                    [
                        "0",
                        "1",
                        5,
                    ],
                    [
                        "1",
                        "2",
                        3,
                    ],
                    [
                        "0",
                        "2",
                        1,
                    ],
                ],
                "directed": False,
            },
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdlib.h>\n\nstruct Edge { int u; int v; int w; };\n\nint find(int* p, int i) {\n    if (p[i] == i) return i;\n    return p[i] = find(p, p[i]);\n}\n\nint spanningTree(int V, struct Edge* edges, int E) {\n    int p[1005];\n    for (int i = 0; i < V; i++) p[i] = i;\n    int mstWeight = 0, count = 0;\n    for (int i = 0; i < E; i++) {\n        int u = find(p, edges[i].u);\n        int v = find(p, edges[i].v);\n        if (u != v) {\n            p[u] = v;\n            mstWeight += edges[i].w;\n            if (++count == V - 1) break;\n        }\n    }\n    return mstWeight;\n}",
                "correctCode": "#include <stdlib.h>\n\nstruct Edge { int u; int v; int w; };\n\nint cmp(const void* a, const void* b) {\n    return ((struct Edge*)a)->w - ((struct Edge*)b)->w;\n}\n\nint find(int* p, int i) {\n    if (p[i] == i) return i;\n    return p[i] = find(p, p[i]);\n}\n\nint spanningTree(int V, struct Edge* edges, int E) {\n    qsort(edges, E, sizeof(struct Edge), cmp);\n    int p[1005];\n    for (int i = 0; i < V; i++) p[i] = i;\n    int mstWeight = 0, count = 0;\n    for (int i = 0; i < E; i++) {\n        int u = find(p, edges[i].u);\n        int v = find(p, edges[i].v);\n        if (u != v) {\n            p[u] = v;\n            mstWeight += edges[i].w;\n            if (++count == V - 1) break;\n        }\n    }\n    return mstWeight;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint find(vector<int>& p, int i) {\n    if (p[i] == i) return i;\n    return p[i] = find(p, p[i]);\n}\n\nint spanningTree(int V, vector<vector<int>>& edges) {\n    vector<int> p(V);\n    for (int i = 0; i < V; i++) p[i] = i;\n    int mstWeight = 0, count = 0;\n    for (auto& e : edges) {\n        int u = find(p, e[0]);\n        int v = find(p, e[1]);\n        if (u != v) {\n            p[u] = v;\n            mstWeight += e[2];\n            if (++count == V - 1) break;\n        }\n    }\n    return mstWeight;\n}",
                "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint find(vector<int>& p, int i) {\n    if (p[i] == i) return i;\n    return p[i] = find(p, p[i]);\n}\n\nint spanningTree(int V, vector<vector<int>>& edges) {\n    sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {\n        return a[2] < b[2];\n    });\n    vector<int> p(V);\n    for (int i = 0; i < V; i++) p[i] = i;\n    int mstWeight = 0, count = 0;\n    for (auto& e : edges) {\n        int u = find(p, e[0]);\n        int v = find(p, e[1]);\n        if (u != v) {\n            p[u] = v;\n            mstWeight += e[2];\n            if (++count == V - 1) break;\n        }\n    }\n    return mstWeight;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    private int find(int[] p, int i) {\n        if (p[i] == i) return i;\n        return p[i] = find(p, p[i]);\n    }\n    public int spanningTree(int V, int[][] edges) {\n        int[] p = new int[V];\n        for (int i = 0; i < V; i++) p[i] = i;\n        int mstWeight = 0, count = 0;\n        for (int[] e : edges) {\n            int u = find(p, e[0]);\n            int v = find(p, e[1]);\n            if (u != v) {\n                p[u] = v;\n                mstWeight += e[2];\n                if (++count == V - 1) break;\n            }\n        }\n        return mstWeight;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    private int find(int[] p, int i) {\n        if (p[i] == i) return i;\n        return p[i] = find(p, p[i]);\n    }\n    public int spanningTree(int V, int[][] edges) {\n        Arrays.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));\n        int[] p = new int[V];\n        for (int i = 0; i < V; i++) p[i] = i;\n        int mstWeight = 0, count = 0;\n        for (int[] e : edges) {\n            int u = find(p, e[0]);\n            int v = find(p, e[1]);\n            if (u != v) {\n                p[u] = v;\n                mstWeight += e[2];\n                if (++count == V - 1) break;\n            }\n        }\n        return mstWeight;\n    }\n}",
            },
        },
    },
]
