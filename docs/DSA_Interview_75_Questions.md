# Interview DSA Question Bank

**Topics:** Tree, BST, Graph, DP, 2D DP  
**Total:** 75 questions  
**Progression:** Easy → Medium → Hard

> This list focuses on frequently asked interview patterns rather than random problem coverage. LeetCode-style names are used where they are standard.

---

# 1. Tree — 15 Questions

## Easy

1. **Binary Tree Preorder Traversal** — [LeetCode 144](https://leetcode.com/problems/binary-tree-preorder-traversal/)
   - Pattern: DFS / recursion / stack
2. **Binary Tree Inorder Traversal** — [LeetCode 94](https://leetcode.com/problems/binary-tree-inorder-traversal/)
   - Pattern: DFS / recursion / stack
3. **Binary Tree Postorder Traversal** — [LeetCode 145](https://leetcode.com/problems/binary-tree-postorder-traversal/)
   - Pattern: DFS / recursion / stack
4. **Maximum Depth of Binary Tree** — [LeetCode 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
   - Pattern: recursion / height
5. **Same Tree** — [LeetCode 100](https://leetcode.com/problems/same-tree/)
   - Pattern: recursive tree comparison

## Medium

6. **Binary Tree Level Order Traversal** — [LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/)
   - Pattern: BFS / queue
7. **Invert Binary Tree** — [LeetCode 226](https://leetcode.com/problems/invert-binary-tree/)
   - Pattern: DFS / recursion
8. **Diameter of Binary Tree** — [LeetCode 543](https://leetcode.com/problems/diameter-of-binary-tree/)
   - Pattern: postorder DFS / height
9. **Balanced Binary Tree** — [LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/)
   - Pattern: bottom-up DFS
10. **Lowest Common Ancestor of a Binary Tree** — [LeetCode 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
    - Pattern: recursive DFS

## Hard

11. **Binary Tree Maximum Path Sum** — [LeetCode 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
    - Pattern: postorder DFS / global maximum
12. **Serialize and Deserialize Binary Tree** — [LeetCode 297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
    - Pattern: tree encoding / BFS or DFS
13. **Vertical Order Traversal of a Binary Tree** — [LeetCode 987](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)
    - Pattern: BFS/DFS + coordinates + sorting
14. **Binary Tree Cameras** — [LeetCode 968](https://leetcode.com/problems/binary-tree-cameras/)
    - Pattern: tree DP / greedy states
15. **Recover a Tree From Preorder Traversal** — [LeetCode 1028](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/)
    - Pattern: recursion / stack / depth reconstruction

---

# 2. BST — 15 Questions

## Easy

1. **Search in a Binary Search Tree** — [LeetCode 700](https://leetcode.com/problems/search-in-a-binary-search-tree/)
   - Pattern: BST property
2. **Minimum Absolute Difference in BST** — [LeetCode 530](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
   - Pattern: inorder traversal
3. **Convert Sorted Array to Binary Search Tree** — [LeetCode 108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
   - Pattern: divide and conquer
4. **Range Sum of BST** — [LeetCode 938](https://leetcode.com/problems/range-sum-of-bst/)
   - Pattern: BST pruning
5. **Two Sum IV - Input is a BST** — [LeetCode 653](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
   - Pattern: DFS + set / inorder

## Medium

6. **Validate Binary Search Tree** — [LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/)
   - Pattern: bounds / inorder
7. **Lowest Common Ancestor of a Binary Search Tree** — [LeetCode 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
   - Pattern: exploit BST ordering
8. **Kth Smallest Element in a BST** — [LeetCode 230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
   - Pattern: inorder traversal
9. **Delete Node in a BST** — [LeetCode 450](https://leetcode.com/problems/delete-node-in-a-bst/)
   - Pattern: BST deletion cases
10. **Insert into a Binary Search Tree** — [LeetCode 701](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
    - Pattern: recursive/iterative insertion

## Hard

11. **Recover Binary Search Tree** — [LeetCode 99](https://leetcode.com/problems/recover-binary-search-tree/)
    - Pattern: inorder + inversion detection
12. **Binary Search Tree Iterator** — [LeetCode 173](https://leetcode.com/problems/binary-search-tree-iterator/)
    - Pattern: controlled inorder traversal / stack
13. **Serialize and Deserialize BST** — [LeetCode 449](https://leetcode.com/problems/serialize-and-deserialize-bst/)
    - Pattern: preorder + BST bounds
14. **Count of Smaller Numbers After Self** — [LeetCode 315](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
    - Pattern: BST/Fenwick tree/merge sort
15. **Balance a Binary Search Tree** — [LeetCode 1382](https://leetcode.com/problems/balance-a-binary-search-tree/)
    - Pattern: inorder + balanced reconstruction

---

# 3. Graph — 15 Questions

## Easy

1. **Find Center of Star Graph** — [LeetCode 1791](https://leetcode.com/problems/find-center-of-star-graph/)
   - Pattern: degree / observation
2. **Find if Path Exists in Graph** — [LeetCode 1971](https://leetcode.com/problems/find-if-path-exists-in-graph/)
   - Pattern: DFS / BFS
3. **Number of Provinces** — [LeetCode 547](https://leetcode.com/problems/number-of-provinces/)
   - Pattern: connected components / DFS / BFS
4. **Flood Fill** — [LeetCode 733](https://leetcode.com/problems/flood-fill/)
   - Pattern: grid DFS/BFS
5. **Find the Town Judge** — [LeetCode 997](https://leetcode.com/problems/find-the-town-judge/)
   - Pattern: indegree/outdegree

## Medium

6. **Number of Islands** — [LeetCode 200](https://leetcode.com/problems/number-of-islands/)
   - Pattern: grid DFS/BFS
7. **Clone Graph** — [LeetCode 133](https://leetcode.com/problems/clone-graph/)
   - Pattern: DFS/BFS + hashmap
8. **Course Schedule** — [LeetCode 207](https://leetcode.com/problems/course-schedule/)
   - Pattern: cycle detection / topological sort
9. **Course Schedule II** — [LeetCode 210](https://leetcode.com/problems/course-schedule-ii/)
   - Pattern: topological ordering
10. **Rotting Oranges** — [LeetCode 994](https://leetcode.com/problems/rotting-oranges/)
    - Pattern: multi-source BFS

## Hard

11. **Word Ladder** — [LeetCode 127](https://leetcode.com/problems/word-ladder/)
    - Pattern: BFS / implicit graph
12. **Network Delay Time** — [LeetCode 743](https://leetcode.com/problems/network-delay-time/)
    - Pattern: Dijkstra
13. **Cheapest Flights Within K Stops** — [LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
    - Pattern: shortest path with constraints
14. **Alien Dictionary** — [LeetCode 269](https://leetcode.com/problems/alien-dictionary/)
    - Pattern: graph construction + topological sort
15. **Critical Connections in a Network** — [LeetCode 1192](https://leetcode.com/problems/critical-connections-in-a-network/)
    - Pattern: Tarjan's algorithm / bridges

---

# 4. DP — 15 Questions

> Here, **DP** primarily means classic 1D / sequence / decision-state dynamic programming.

## Easy

1. **Climbing Stairs** — [LeetCode 70](https://leetcode.com/problems/climbing-stairs/)
   - Pattern: Fibonacci-style DP
2. **Min Cost Climbing Stairs** — [LeetCode 746](https://leetcode.com/problems/min-cost-climbing-stairs/)
   - Pattern: minimum-cost state DP
3. **House Robber** — [LeetCode 198](https://leetcode.com/problems/house-robber/)
   - Pattern: take / skip DP
4. **Fibonacci Number** — [LeetCode 509](https://leetcode.com/problems/fibonacci-number/)
   - Pattern: basic state transition
5. **Maximum Subarray** — [LeetCode 53](https://leetcode.com/problems/maximum-subarray/)
   - Pattern: Kadane's algorithm / DP

## Medium

6. **House Robber II** — [LeetCode 213](https://leetcode.com/problems/house-robber-ii/)
   - Pattern: circular DP
7. **Coin Change** — [LeetCode 322](https://leetcode.com/problems/coin-change/)
   - Pattern: unbounded knapsack / minimum DP
8. **Decode Ways** — [LeetCode 91](https://leetcode.com/problems/decode-ways/)
   - Pattern: string DP
9. **Word Break** — [LeetCode 139](https://leetcode.com/problems/word-break/)
   - Pattern: prefix DP
10. **Longest Increasing Subsequence** — [LeetCode 300](https://leetcode.com/problems/longest-increasing-subsequence/)
    - Pattern: sequence DP / binary search optimization

## Hard

11. **Edit Distance** — [LeetCode 72](https://leetcode.com/problems/edit-distance/)
    - Pattern: 2-sequence state transition
12. **Distinct Subsequences** — [LeetCode 115](https://leetcode.com/problems/distinct-subsequences/)
    - Pattern: subsequence DP
13. **Regular Expression Matching** — [LeetCode 10](https://leetcode.com/problems/regular-expression-matching/)
    - Pattern: string DP
14. **Palindrome Partitioning II** — [LeetCode 132](https://leetcode.com/problems/palindrome-partitioning-ii/)
    - Pattern: interval/palindrome DP
15. **Burst Balloons** — [LeetCode 312](https://leetcode.com/problems/burst-balloons/)
    - Pattern: interval DP

---

# 5. 2D DP — 15 Questions

> **2D DP** here means DP where the state naturally depends on two dimensions, especially grids, two strings, and knapsack-style `(index, capacity)` states.

## Easy

1. **Unique Paths** — [LeetCode 62](https://leetcode.com/problems/unique-paths/)
   - Pattern: grid DP
2. **Unique Paths II** — [LeetCode 63](https://leetcode.com/problems/unique-paths-ii/)
   - Pattern: grid DP + obstacles
3. **Minimum Path Sum** — [LeetCode 64](https://leetcode.com/problems/minimum-path-sum/)
   - Pattern: grid min-cost DP
4. **Range Sum Query 2D - Immutable** — [LeetCode 304](https://leetcode.com/problems/range-sum-query-2d-immutable/)
   - Pattern: 2D prefix sum
5. **Maximal Square** — [LeetCode 221](https://leetcode.com/problems/maximal-square/)
   - Pattern: 2D grid DP

## Medium

6. **0/1 Knapsack**
   - Pattern: `(item, capacity)` DP
7. **Partition Equal Subset Sum** — [LeetCode 416](https://leetcode.com/problems/partition-equal-subset-sum/)
   - Pattern: 0/1 knapsack / subset-sum
8. **Target Sum** — [LeetCode 494](https://leetcode.com/problems/target-sum/)
   - Pattern: subset-sum transformation / DP
9. **Longest Common Subsequence** — [LeetCode 1143](https://leetcode.com/problems/longest-common-subsequence/)
   - Pattern: two-string 2D DP
10. **Longest Palindromic Subsequence** — [LeetCode 516](https://leetcode.com/problems/longest-palindromic-subsequence/)
    - Pattern: interval/string DP

## Hard

11. **Interleaving String** — [LeetCode 97](https://leetcode.com/problems/interleaving-string/)
    - Pattern: two-index string DP
12. **Scramble String** — [LeetCode 87](https://leetcode.com/problems/scramble-string/)
    - Pattern: interval + 3D-style state reasoning
13. **Minimum Cost to Cut a Stick** — [LeetCode 1547](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
    - Pattern: interval DP
14. **Stone Game III** — [LeetCode 1406](https://leetcode.com/problems/stone-game-iii/)
    - Pattern: game DP / optimal choice
15. **Regular Expression Matching** — [LeetCode 10](https://leetcode.com/problems/regular-expression-matching/)
    - Pattern: 2D string DP with branching transitions

---

# Recommended Interview Order

If your goal is **interview preparation**, don't solve these randomly. A good progression is:

1. **Tree basics**
   - Traversals
   - Height
   - BFS
   - Diameter
   - LCA

2. **BST**
   - Search
   - Validate
   - Inorder
   - Kth smallest
   - Delete
   - LCA

3. **Graph basics**
   - DFS/BFS
   - Connected components
   - Grid problems
   - Cycle detection
   - Topological sort

4. **Graph advanced**
   - Dijkstra
   - Shortest path
   - Bridges / Tarjan
   - Union-Find

5. **1D DP**
   - Fibonacci
   - Take/skip
   - Knapsack
   - Coin change
   - LIS
   - String DP

6. **2D DP**
   - Grid DP
   - 0/1 Knapsack
   - Subset Sum
   - LCS
   - Edit Distance
   - Interval DP

---

# High-Priority Problems

If you are short on time, prioritize these:

| Topic | Must-Do Problems |
|---|---|
| Tree | Level Order, Diameter, LCA, Maximum Path Sum, Serialize/Deserialize |
| BST | Validate BST, Kth Smallest, Delete Node, BST Iterator |
| Graph | Number of Islands, Course Schedule, Rotting Oranges, Word Ladder, Dijkstra |
| DP | House Robber, Coin Change, Word Break, LIS, Edit Distance |
| 2D DP | Unique Paths, 0/1 Knapsack, Partition Equal Subset Sum, LCS, Interval DP |

---

# Pattern Checklist

Before an interview, make sure you can recognize:

## Tree
- [ ] DFS recursion
- [ ] BFS / level order
- [ ] Preorder / inorder / postorder
- [ ] Height / depth
- [ ] Diameter
- [ ] LCA
- [ ] Tree serialization
- [ ] Tree DP

## BST
- [ ] BST ordering property
- [ ] Inorder = sorted order
- [ ] Bounds validation
- [ ] Kth smallest/largest
- [ ] Insert/delete
- [ ] BST iterator
- [ ] LCA using ordering

## Graph
- [ ] DFS
- [ ] BFS
- [ ] Connected components
- [ ] Cycle detection
- [ ] Topological sort
- [ ] Bipartite graph
- [ ] Union-Find
- [ ] Dijkstra
- [ ] Bellman-Ford
- [ ] Bridges / articulation points

## DP
- [ ] State definition
- [ ] Base case
- [ ] Transition
- [ ] Take / skip
- [ ] Memoization
- [ ] Tabulation
- [ ] Space optimization
- [ ] Knapsack pattern
- [ ] Sequence DP
- [ ] String DP

## 2D DP
- [ ] Grid DP
- [ ] `(i, j)` state
- [ ] `(index, capacity)` state
- [ ] Two-string DP
- [ ] Subset sum
- [ ] LCS
- [ ] Edit distance
- [ ] Interval DP

---

# Important Note

Some problems naturally overlap multiple categories. For example:

- **Edit Distance** → 2D DP + string DP
- **Regular Expression Matching** → 2D DP + string DP
- **Burst Balloons** → interval DP
- **0/1 Knapsack** → 2D DP conceptually, often optimized to 1D
- **Target Sum** → 2D DP conceptually, often optimized to 1D
- **Tree DP** → Tree + DP

That overlap is intentional because interviewers often test whether you can **identify the underlying pattern**, not whether you can memorize a category.
