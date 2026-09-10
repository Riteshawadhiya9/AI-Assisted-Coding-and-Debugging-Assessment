import json
import os

questions = [
    # =========================================================================
    # 1. TREES (12 Questions: C, C++, Java)
    # =========================================================================

    # 1.1 Trees - Maximum Depth of Binary Tree (C - Easy)
    {
        "id": "q_tree_max_depth",
        "title": "Maximum Depth of Binary Tree",
        "problemStatement": "Given the root of a binary tree, return its maximum depth.\nA binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.",
        "language": "c",
        "topic": "trees",
        "subtopic": "depth-height",
        "difficulty": "easy",
        "estimatedTime": 15,
        "buggyCode": "struct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nint maxDepth(struct TreeNode* root) {\n    if (root == NULL) return 0;\n    int leftDepth = maxDepth(root->left);\n    int rightDepth = maxDepth(root->right);\n    return (leftDepth > rightDepth) ? leftDepth : rightDepth;\n}",
        "correctCode": "struct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nint maxDepth(struct TreeNode* root) {\n    if (root == NULL) return 0;\n    int leftDepth = maxDepth(root->left);\n    int rightDepth = maxDepth(root->right);\n    return 1 + ((leftDepth > rightDepth) ? leftDepth : rightDepth);\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Fails to include the current node in the depth calculation (+1), returning 0 for any tree.",
                "type": "incorrect recursion",
                "lineRange": "12"
            }
        ],
        "primaryBugType": "incorrect recursion",
        "explanation": "In recursive tree depth calculation, the depth of any subtree rooted at `root` is 1 plus the maximum depth of its left and right subtrees. The buggy code omits the `+ 1`, which propagates 0 all the way up from the base cases.",
        "intendedApproach": "Add 1 to the maximum of leftDepth and rightDepth before returning.",
        "constraints": ["The number of nodes in the tree is in the range [0, 10^4].", "-100 <= Node.val <= 100"],
        "visibleTestCases": [
            {"id": 1, "input": "[3,9,20,null,null,15,7]", "expectedOutput": "3", "isHidden": False},
            {"id": 2, "input": "[1,null,2]", "expectedOutput": "2", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[]", "expectedOutput": "0", "isHidden": True},
            {"id": 4, "input": "[0]", "expectedOutput": "1", "isHidden": True},
            {"id": 5, "input": "[1,2,3,4,null,null,5]", "expectedOutput": "3", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(H) where H is tree height"},
        "tags": ["trees", "recursion", "c", "easy"],
        "visualData": {
            "type": "tree",
            "title": "Binary Tree Structure (Max Depth = 3)",
            "data": [3, 9, 20, None, None, 15, 7]
        }
    },

    # 1.2 Trees - Invert Binary Tree (C - Easy)
    {
        "id": "q_tree_invert",
        "title": "Invert Binary Tree",
        "problemStatement": "Given the root of a binary tree, invert the tree (mirror all left and right subtrees) and return its root.",
        "language": "c",
        "topic": "trees",
        "subtopic": "tree-transformation",
        "difficulty": "easy",
        "estimatedTime": 15,
        "buggyCode": "struct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nstruct TreeNode* invertTree(struct TreeNode* root) {\n    if (root == NULL) return NULL;\n    root->left = invertTree(root->right);\n    root->right = invertTree(root->left);\n    return root;\n}",
        "correctCode": "struct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nstruct TreeNode* invertTree(struct TreeNode* root) {\n    if (root == NULL) return NULL;\n    struct TreeNode* left = invertTree(root->left);\n    struct TreeNode* right = invertTree(root->right);\n    root->left = right;\n    root->right = left;\n    return root;\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Overwrites root->left before inverting it, causing the original left subtree to be lost and right subtree to be mirrored twice.",
                "type": "incorrect state transition",
                "lineRange": "9-10"
            }
        ],
        "primaryBugType": "incorrect state transition",
        "explanation": "Assigning `root->left = invertTree(root->right)` destroys the reference to the original left subtree before it can be inverted. When `invertTree(root->left)` is subsequently called, it re-inverts the already-inverted right subtree.",
        "intendedApproach": "Store inverted subtrees in temporary variables `left` and `right` before swapping pointers.",
        "constraints": ["The number of nodes in the tree is in the range [0, 100].", "-100 <= Node.val <= 100"],
        "visibleTestCases": [
            {"id": 1, "input": "[4,2,7,1,3,6,9]", "expectedOutput": "[4,7,2,9,6,3,1]", "isHidden": False},
            {"id": 2, "input": "[2,1,3]", "expectedOutput": "[2,3,1]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[]", "expectedOutput": "[]", "isHidden": True},
            {"id": 4, "input": "[1]", "expectedOutput": "[1]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(H) where H is tree height"},
        "tags": ["trees", "pointer-swap", "c", "easy"],
        "visualData": {
            "type": "tree",
            "title": "Binary Tree to Invert",
            "data": [4, 2, 7, 1, 3, 6, 9]
        }
    },

    # 1.3 Trees - Validate Binary Search Tree (C++ - Medium)
    {
        "id": "q_tree_validate_bst",
        "title": "Validate Binary Search Tree",
        "problemStatement": "Given the root of a binary tree, determine if it is a valid binary search tree (BST).\nA valid BST is defined as follows:\n- The left subtree of a node contains only nodes with keys strictly less than the node's key.\n- The right subtree of a node contains only nodes with keys strictly greater than the node's key.\n- Both the left and right subtrees must also be binary search trees.",
        "language": "cpp",
        "topic": "trees",
        "subtopic": "bst-validation",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nclass Solution {\npublic:\n    bool isValidBST(TreeNode* root) {\n        if (!root) return true;\n        if (root->left && root->left->val >= root->val) return false;\n        if (root->right && root->right->val <= root->val) return false;\n        return isValidBST(root->left) && isValidBST(root->right);\n    }\n};",
        "correctCode": "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nclass Solution {\nprivate:\n    bool validate(TreeNode* node, long long minVal, long long maxVal) {\n        if (!node) return true;\n        if (node->val <= minVal || node->val >= maxVal) return false;\n        return validate(node->left, minVal, node->val) && validate(node->right, node->val, maxVal);\n    }\npublic:\n    bool isValidBST(TreeNode* root) {\n        return validate(root, -2147483649LL, 2147483648LL);\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Only compares each node against its direct children instead of enforcing the global ancestral (minVal, maxVal) interval.",
                "type": "logical",
                "lineRange": "12-14"
            }
        ],
        "primaryBugType": "logical",
        "explanation": "A node in the right subtree of a left child must still be strictly less than the grandparent root. Local child checks miss violations where a descendant violates ancestral bounds (e.g. tree [5, 1, 4, null, null, 3, 6] where 3 is in the right subtree of 5).",
        "intendedApproach": "Pass lower and upper bounds down the recursive calls to ensure all nodes conform to their ancestral BST ranges.",
        "constraints": ["The number of nodes in the tree is in the range [1, 10^4].", "-2^31 <= Node.val <= 2^31 - 1"],
        "visibleTestCases": [
            {"id": 1, "input": "[2,1,3]", "expectedOutput": "true", "isHidden": False},
            {"id": 2, "input": "[5,1,4,null,null,3,6]", "expectedOutput": "false", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[2147483647]", "expectedOutput": "true", "isHidden": True},
            {"id": 4, "input": "[10,5,15,null,null,6,20]", "expectedOutput": "false", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(H)"},
        "tags": ["trees", "bst", "cpp", "medium"],
        "visualData": {
            "type": "tree",
            "title": "Invalid BST Violation Example",
            "data": [5, 1, 4, None, None, 3, 6]
        }
    },

    # 1.4 Trees - Lowest Common Ancestor of a Binary Tree (Java - Medium)
    {
        "id": "q_tree_lca",
        "title": "Lowest Common Ancestor of a Binary Tree",
        "problemStatement": "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q.",
        "language": "java",
        "topic": "trees",
        "subtopic": "ancestor-traversal",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n        if (root == null || root == p || root == q) {\n            return root;\n        }\n        \n        TreeNode left = lowestCommonAncestor(root.left, p, q);\n        TreeNode right = lowestCommonAncestor(root.right, p, q);\n        \n        if (left != null && right != null) {\n            return left;\n        }\n        \n        return left != null ? left : right;\n    }\n}",
        "correctCode": "class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n        if (root == null || root == p || root == q) {\n            return root;\n        }\n        \n        TreeNode left = lowestCommonAncestor(root.left, p, q);\n        TreeNode right = lowestCommonAncestor(root.right, p, q);\n        \n        if (left != null && right != null) {\n            return root;\n        }\n        \n        return left != null ? left : right;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Returns the left subtree match instead of the current root node when p and q reside in opposite subtrees.",
                "type": "incorrect traversal",
                "lineRange": "17-19"
            }
        ],
        "primaryBugType": "incorrect traversal",
        "explanation": "When `left != null` and `right != null`, it means node `p` was found in one subtree and node `q` was found in the other. Therefore, the current `root` is their Lowest Common Ancestor. Returning `left` discards the actual LCA.",
        "intendedApproach": "Return `root` when both left and right recursive calls return non-null nodes.",
        "constraints": ["The number of nodes in the tree is in the range [2, 10^5].", "-10^9 <= Node.val <= 10^9", "All Node.val are unique.", "p != q", "p and q will exist in the tree."],
        "visibleTestCases": [
            {"id": 1, "input": "root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1", "expectedOutput": "3", "isHidden": False},
            {"id": 2, "input": "root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4", "expectedOutput": "5", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "root = [1,2], p = 1, q = 2", "expectedOutput": "1", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(H)"},
        "tags": ["trees", "lca", "java", "medium"],
        "visualData": {
            "type": "tree",
            "title": "Binary Tree LCA (p=5, q=1 -> LCA=3)",
            "data": [3, 5, 1, 6, 2, 0, 8]
        }
    },

    # 1.5 Trees - Binary Tree Level Order Traversal (Java - Medium)
    {
        "id": "q_tree_level_order",
        "title": "Binary Tree Level Order Traversal",
        "problemStatement": "Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).",
        "language": "java",
        "topic": "trees",
        "subtopic": "bfs-traversal",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        List<List<Integer>> result = new ArrayList<>();\n        if (root == null) return result;\n        \n        Queue<TreeNode> queue = new LinkedList<>();\n        queue.add(root);\n        \n        while (!queue.isEmpty()) {\n            List<Integer> level = new ArrayList<>();\n            for (int i = 0; i < queue.size(); i++) {\n                TreeNode node = queue.poll();\n                level.add(node.val);\n                if (node.left != null) queue.add(node.left);\n                if (node.right != null) queue.add(node.right);\n            }\n            result.add(level);\n        }\n        return result;\n    }\n}",
        "correctCode": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        List<List<Integer>> result = new ArrayList<>();\n        if (root == null) return result;\n        \n        Queue<TreeNode> queue = new LinkedList<>();\n        queue.add(root);\n        \n        while (!queue.isEmpty()) {\n            List<Integer> level = new ArrayList<>();\n            int levelSize = queue.size();\n            for (int i = 0; i < levelSize; i++) {\n                TreeNode node = queue.poll();\n                level.add(node.val);\n                if (node.left != null) queue.add(node.left);\n                if (node.right != null) queue.add(node.right);\n            }\n            result.add(level);\n        }\n        return result;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Uses dynamic queue.size() in the for-loop condition, which changes as children are enqueued and prematurely terminates or blends levels.",
                "type": "boundary",
                "lineRange": "20"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "Because `queue.poll()` removes elements and `queue.add()` inserts new children during iteration, `queue.size()` is recalculated every step. This corrupts the level boundaries, mixing nodes from different tree depths into the same inner list.",
        "intendedApproach": "Capture `int levelSize = queue.size();` before the inner loop begins.",
        "constraints": ["The number of nodes in the tree is in the range [0, 2000].", "-1000 <= Node.val <= 1000"],
        "visibleTestCases": [
            {"id": 1, "input": "[3,9,20,null,null,15,7]", "expectedOutput": "[[3],[9,20],[15,7]]", "isHidden": False},
            {"id": 2, "input": "[1]", "expectedOutput": "[[1]]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[]", "expectedOutput": "[]", "isHidden": True},
            {"id": 4, "input": "[1,2,3,4,5,6,7]", "expectedOutput": "[[1],[2,3],[4,5,6,7]]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(N)"},
        "tags": ["trees", "bfs", "queue", "java", "medium"]
    },

    # 1.6 Trees - Diameter of Binary Tree (C++ - Medium)
    {
        "id": "q_tree_diameter",
        "title": "Diameter of Binary Tree",
        "problemStatement": "Given the root of a binary tree, return the length of the diameter of the tree.\nThe diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.",
        "language": "cpp",
        "topic": "trees",
        "subtopic": "tree-paths",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nclass Solution {\nprivate:\n    int maxDiameter = 0;\n    \n    int maxDepth(TreeNode* root) {\n        if (!root) return 0;\n        int left = maxDepth(root->left);\n        int right = maxDepth(root->right);\n        if (left + right + 1 > maxDiameter) {\n            maxDiameter = left + right + 1;\n        }\n        return 1 + (left > right ? left : right);\n    }\npublic:\n    int diameterOfBinaryTree(TreeNode* root) {\n        maxDiameter = 0;\n        maxDepth(root);\n        return maxDiameter;\n    }\n};",
        "correctCode": "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nclass Solution {\nprivate:\n    int maxDiameter = 0;\n    \n    int maxDepth(TreeNode* root) {\n        if (!root) return 0;\n        int left = maxDepth(root->left);\n        int right = maxDepth(root->right);\n        if (left + right > maxDiameter) {\n            maxDiameter = left + right;\n        }\n        return 1 + (left > right ? left : right);\n    }\npublic:\n    int diameterOfBinaryTree(TreeNode* root) {\n        maxDiameter = 0;\n        maxDepth(root);\n        return maxDiameter;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Calculates diameter as number of nodes (left + right + 1) instead of number of edges (left + right), producing an off-by-one error.",
                "type": "off-by-one",
                "lineRange": "15-17"
            }
        ],
        "primaryBugType": "off-by-one",
        "explanation": "Diameter is defined as the length of the path in terms of number of edges between the two farthest nodes. Since a path with k nodes has k - 1 edges, the edge count through the current root is `left + right` (not `left + right + 1`).",
        "intendedApproach": "Update maxDiameter using `left + right`.",
        "constraints": ["The number of nodes in the tree is in the range [1, 10^4].", "-100 <= Node.val <= 100"],
        "visibleTestCases": [
            {"id": 1, "input": "[1,2,3,4,5]", "expectedOutput": "3", "isHidden": False},
            {"id": 2, "input": "[1,2]", "expectedOutput": "1", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[1]", "expectedOutput": "0", "isHidden": True},
            {"id": 4, "input": "[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]", "expectedOutput": "8", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(H)"},
        "tags": ["trees", "dfs", "cpp", "medium"]
    },

    # 1.7 Trees - Symmetric Tree (Java - Easy)
    {
        "id": "q_tree_symmetric",
        "title": "Symmetric Tree",
        "problemStatement": "Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).",
        "language": "java",
        "topic": "trees",
        "subtopic": "tree-symmetry",
        "difficulty": "easy",
        "estimatedTime": 15,
        "buggyCode": "class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    private boolean isMirror(TreeNode t1, TreeNode t2) {\n        if (t1 == null && t2 == null) return true;\n        if (t1 == null || t2 == null) return false;\n        if (t1.val != t2.val) return false;\n        return isMirror(t1.left, t2.left) && isMirror(t1.right, t2.right);\n    }\n    \n    public boolean isSymmetric(TreeNode root) {\n        if (root == null) return true;\n        return isMirror(root.left, root.right);\n    }\n}",
        "correctCode": "class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    private boolean isMirror(TreeNode t1, TreeNode t2) {\n        if (t1 == null && t2 == null) return true;\n        if (t1 == null || t2 == null) return false;\n        if (t1.val != t2.val) return false;\n        return isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left);\n    }\n    \n    public boolean isSymmetric(TreeNode root) {\n        if (root == null) return true;\n        return isMirror(root.left, root.right);\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Compares identical subtrees (t1.left with t2.left) instead of mirror subtrees (t1.left with t2.right).",
                "type": "incorrect traversal",
                "lineRange": "13"
            }
        ],
        "primaryBugType": "incorrect traversal",
        "explanation": "To check for tree symmetry around the vertical axis, the left child of `t1` must be identical to the right child of `t2`, and the right child of `t1` must be identical to the left child of `t2`. The buggy code checks tree equivalence rather than mirror symmetry.",
        "intendedApproach": "Compare `isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left)`.",
        "constraints": ["The number of nodes in the tree is in the range [1, 1000].", "-100 <= Node.val <= 100"],
        "visibleTestCases": [
            {"id": 1, "input": "[1,2,2,3,4,4,3]", "expectedOutput": "true", "isHidden": False},
            {"id": 2, "input": "[1,2,2,null,3,null,3]", "expectedOutput": "false", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[1]", "expectedOutput": "true", "isHidden": True},
            {"id": 4, "input": "[1,2,2,2,null,2]", "expectedOutput": "false", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(H)"},
        "tags": ["trees", "recursion", "java", "easy"]
    },

    # 1.8 Trees - Path Sum (C - Easy)
    {
        "id": "q_tree_path_sum",
        "title": "Path Sum",
        "problemStatement": "Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.",
        "language": "c",
        "topic": "trees",
        "subtopic": "tree-paths",
        "difficulty": "easy",
        "estimatedTime": 15,
        "buggyCode": "#include <stdbool.h>\n#include <stdlib.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nbool hasPathSum(struct TreeNode* root, int targetSum) {\n    if (root == NULL) return false;\n    \n    if (targetSum == root->val) return true;\n    \n    return hasPathSum(root->left, targetSum - root->val) || \n           hasPathSum(root->right, targetSum - root->val);\n}",
        "correctCode": "#include <stdbool.h>\n#include <stdlib.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nbool hasPathSum(struct TreeNode* root, int targetSum) {\n    if (root == NULL) return false;\n    \n    if (root->left == NULL && root->right == NULL) {\n        return targetSum == root->val;\n    }\n    \n    return hasPathSum(root->left, targetSum - root->val) || \n           hasPathSum(root->right, targetSum - root->val);\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Fails to verify if the node is a leaf before terminating with true on sum match.",
                "type": "boundary",
                "lineRange": "12"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "Path Sum requires the path to terminate at a leaf node (a node with no children). If an intermediate internal node's accumulated sum matches targetSum, the buggy code incorrectly returns true without reaching a leaf.",
        "intendedApproach": "Check `root->left == NULL && root->right == NULL` before comparing `targetSum == root->val`.",
        "constraints": ["The number of nodes in the tree is in the range [0, 5000].", "-1000 <= Node.val <= 1000", "-1000 <= targetSum <= 1000"],
        "visibleTestCases": [
            {"id": 1, "input": "root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22", "expectedOutput": "true", "isHidden": False},
            {"id": 2, "input": "root = [1,2,3], targetSum = 5", "expectedOutput": "false", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "root = [], targetSum = 0", "expectedOutput": "false", "isHidden": True},
            {"id": 4, "input": "root = [1,2], targetSum = 1", "expectedOutput": "false", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(H)"},
        "tags": ["trees", "recursion", "c", "easy"]
    },

    # 1.9 Trees - Kth Smallest Element in a BST (C++ - Medium)
    {
        "id": "q_tree_kth_smallest_bst",
        "title": "Kth Smallest Element in a BST",
        "problemStatement": "Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.",
        "language": "cpp",
        "topic": "trees",
        "subtopic": "bst-traversal",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nclass Solution {\nprivate:\n    int count = 0;\n    int result = -1;\n    \n    void inorder(TreeNode* node, int k) {\n        if (!node) return;\n        inorder(node->left, k);\n        count++;\n        if (count == k) {\n            result = node->val;\n        }\n        inorder(node->right, k);\n    }\npublic:\n    int kthSmallest(TreeNode* root, int k) {\n        count = 0;\n        result = -1;\n        inorder(root, k);\n        return result;\n    }\n};",
        "correctCode": "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nclass Solution {\nprivate:\n    int count = 0;\n    int result = -1;\n    \n    void inorder(TreeNode* node, int k) {\n        if (!node || count >= k) return;\n        inorder(node->left, k);\n        count++;\n        if (count == k) {\n            result = node->val;\n            return;\n        }\n        inorder(node->right, k);\n    }\npublic:\n    int kthSmallest(TreeNode* root, int k) {\n        count = 0;\n        result = -1;\n        inorder(root, k);\n        return result;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Fails to prune traversal once the kth element is discovered (missing early termination guard `count >= k`).",
                "type": "incorrect traversal",
                "lineRange": "12-20"
            }
        ],
        "primaryBugType": "incorrect traversal",
        "explanation": "In an in-order traversal of a BST, elements are visited in strictly ascending order. While `result` is assigned at `count == k`, the recursion continues traversing unnecessary nodes in the right subtree. Adding `if (count >= k) return;` prevents wasteful work.",
        "intendedApproach": "Halt further in-order recursion when count reaches or exceeds k.",
        "constraints": ["The number of nodes in the tree is n.", "1 <= k <= n <= 10^4", "0 <= Node.val <= 10^4"],
        "visibleTestCases": [
            {"id": 1, "input": "root = [3,1,4,null,2], k = 1", "expectedOutput": "1", "isHidden": False},
            {"id": 2, "input": "root = [5,3,6,2,4,null,null,1], k = 3", "expectedOutput": "3", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "root = [1], k = 1", "expectedOutput": "1", "isHidden": True},
            {"id": 4, "input": "root = [2,1,3], k = 2", "expectedOutput": "2", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(H + k)", "space": "O(H)"},
        "tags": ["trees", "bst", "inorder", "cpp", "medium"]
    },

    # 1.10 Trees - Binary Tree Maximum Path Sum (Java - Hard)
    {
        "id": "q_tree_max_path_sum",
        "title": "Binary Tree Maximum Path Sum",
        "problemStatement": "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.\nThe path sum of a path is the sum of the node's values in the path. Return the maximum path sum of any non-empty path.",
        "language": "java",
        "topic": "trees",
        "subtopic": "tree-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "buggyCode": "class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    private int maxSum = Integer.MIN_VALUE;\n    \n    private int maxGain(TreeNode node) {\n        if (node == null) return 0;\n        \n        int leftGain = maxGain(node.left);\n        int rightGain = maxGain(node.right);\n        \n        int currentPathSum = node.val + leftGain + rightGain;\n        maxSum = Math.max(maxSum, currentPathSum);\n        \n        return node.val + Math.max(leftGain, rightGain);\n    }\n    \n    public int maxPathSum(TreeNode root) {\n        maxSum = Integer.MIN_VALUE;\n        maxGain(root);\n        return maxSum;\n    }\n}",
        "correctCode": "class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    private int maxSum = Integer.MIN_VALUE;\n    \n    private int maxGain(TreeNode node) {\n        if (node == null) return 0;\n        \n        int leftGain = Math.max(0, maxGain(node.left));\n        int rightGain = Math.max(0, maxGain(node.right));\n        \n        int currentPathSum = node.val + leftGain + rightGain;\n        maxSum = Math.max(maxSum, currentPathSum);\n        \n        return node.val + Math.max(leftGain, rightGain);\n    }\n    \n    public int maxPathSum(TreeNode root) {\n        maxSum = Integer.MIN_VALUE;\n        maxGain(root);\n        return maxSum;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Propagates negative branch sums into the parent path without clipping them to 0 with Math.max(0, gain).",
                "type": "logical",
                "lineRange": "13-14"
            }
        ],
        "primaryBugType": "logical",
        "explanation": "If a subtree has a negative maximum path sum, adding it to the parent node reduces the total path sum. We should only include a child's contribution if it is strictly positive (`Math.max(0, gain)`).",
        "intendedApproach": "Clip negative child gains to 0: `Math.max(0, maxGain(node.left))`.",
        "constraints": ["The number of nodes in the tree is in the range [1, 3 * 10^4].", "-1000 <= Node.val <= 1000"],
        "visibleTestCases": [
            {"id": 1, "input": "[1,2,3]", "expectedOutput": "6", "isHidden": False},
            {"id": 2, "input": "[-10,9,20,null,null,15,7]", "expectedOutput": "42", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[-3]", "expectedOutput": "-3", "isHidden": True},
            {"id": 4, "input": "[2,-1]", "expectedOutput": "2", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(H)"},
        "tags": ["trees", "recursion", "dynamic-programming", "java", "hard"]
    },

    # 1.11 Trees - Construct Binary Tree from Preorder and Inorder Traversal (C++ - Hard)
    {
        "id": "q_tree_build_pre_in",
        "title": "Construct Tree from Preorder and Inorder Traversal",
        "problemStatement": "Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.",
        "language": "cpp",
        "topic": "trees",
        "subtopic": "tree-construction",
        "difficulty": "hard",
        "estimatedTime": 25,
        "buggyCode": "#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nclass Solution {\n    unordered_map<int, int> inMap;\n    \n    TreeNode* build(vector<int>& preorder, int preStart, int preEnd,\n                    vector<int>& inorder, int inStart, int inEnd) {\n        if (preStart > preEnd || inStart > inEnd) return nullptr;\n        \n        TreeNode* root = new TreeNode(preorder[preStart]);\n        int inRoot = inMap[root->val];\n        int numsLeft = inRoot - inStart;\n        \n        root->left = build(preorder, preStart + 1, preStart + numsLeft, inorder, inStart, inRoot - 1);\n        root->right = build(preorder, preStart + numsLeft, preEnd, inorder, inRoot + 1, inEnd);\n        \n        return root;\n    }\npublic:\n    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {\n        inMap.clear();\n        for (int i = 0; i < inorder.size(); i++) inMap[inorder[i]] = i;\n        return build(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);\n    }\n};",
        "correctCode": "#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nclass Solution {\n    unordered_map<int, int> inMap;\n    \n    TreeNode* build(vector<int>& preorder, int preStart, int preEnd,\n                    vector<int>& inorder, int inStart, int inEnd) {\n        if (preStart > preEnd || inStart > inEnd) return nullptr;\n        \n        TreeNode* root = new TreeNode(preorder[preStart]);\n        int inRoot = inMap[root->val];\n        int numsLeft = inRoot - inStart;\n        \n        root->left = build(preorder, preStart + 1, preStart + numsLeft, inorder, inStart, inRoot - 1);\n        root->right = build(preorder, preStart + numsLeft + 1, preEnd, inorder, inRoot + 1, inEnd);\n        \n        return root;\n    }\npublic:\n    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {\n        inMap.clear();\n        for (int i = 0; i < inorder.size(); i++) inMap[inorder[i]] = i;\n        return build(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Right subtree preorder start index overlaps with left subtree end index (preStart + numsLeft instead of preStart + numsLeft + 1).",
                "type": "off-by-one",
                "lineRange": "24"
            }
        ],
        "primaryBugType": "off-by-one",
        "explanation": "The left subtree occupies indices `[preStart + 1, preStart + numsLeft]` in preorder. Thus, the right subtree must begin strictly after the left subtree, at index `preStart + numsLeft + 1`. Starting at `preStart + numsLeft` duplicates the last node of the left subtree into the right subtree root.",
        "intendedApproach": "Pass `preStart + numsLeft + 1` for the right subtree's `preStart` argument.",
        "constraints": ["1 <= preorder.length <= 3000", "inorder.length == preorder.length", "-3000 <= preorder[i], inorder[i] <= 3000", "preorder and inorder consist of unique values."],
        "visibleTestCases": [
            {"id": 1, "input": "preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]", "expectedOutput": "[3,9,20,null,null,15,7]", "isHidden": False},
            {"id": 2, "input": "preorder = [-1], inorder = [-1]", "expectedOutput": "[-1]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "preorder = [1,2,3], inorder = [3,2,1]", "expectedOutput": "[1,2,null,3]", "isHidden": True},
            {"id": 4, "input": "preorder = [1,2], inorder = [1,2]", "expectedOutput": "[1,null,2]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(N)"},
        "tags": ["trees", "recursion", "cpp", "hard"]
    },

    # 1.12 Trees - Count Complete Tree Nodes (C - Medium)
    {
        "id": "q_tree_count_nodes",
        "title": "Count Complete Tree Nodes",
        "problemStatement": "Given the root of a complete binary tree, return the number of the nodes in the tree.",
        "language": "c",
        "topic": "trees",
        "subtopic": "complete-tree",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "struct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nint getLeftHeight(struct TreeNode* node) {\n    int h = 0;\n    while (node) {\n        h++;\n        node = node->left;\n    }\n    return h;\n}\n\nint getRightHeight(struct TreeNode* node) {\n    int h = 0;\n    while (node) {\n        h++;\n        node = node->right;\n    }\n    return h;\n}\n\nint countNodes(struct TreeNode* root) {\n    if (root == NULL) return 0;\n    int lh = getLeftHeight(root);\n    int rh = getRightHeight(root);\n    \n    if (lh == rh) {\n        return (1 << lh);\n    }\n    \n    return 1 + countNodes(root->left) + countNodes(root->right);\n}",
        "correctCode": "struct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nint getLeftHeight(struct TreeNode* node) {\n    int h = 0;\n    while (node) {\n        h++;\n        node = node->left;\n    }\n    return h;\n}\n\nint getRightHeight(struct TreeNode* node) {\n    int h = 0;\n    while (node) {\n        h++;\n        node = node->right;\n    }\n    return h;\n}\n\nint countNodes(struct TreeNode* root) {\n    if (root == NULL) return 0;\n    int lh = getLeftHeight(root);\n    int rh = getRightHeight(root);\n    \n    if (lh == rh) {\n        return (1 << lh) - 1;\n    }\n    \n    return 1 + countNodes(root->left) + countNodes(root->right);\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Full binary tree calculation uses (1 << lh) instead of (1 << lh) - 1, overcounting the node count by 1.",
                "type": "off-by-one",
                "lineRange": "29"
            }
        ],
        "primaryBugType": "off-by-one",
        "explanation": "A full binary tree of height `h` has `2^h - 1` nodes. Computing `1 << h` yields `2^h`, which overcounts by exactly 1 node for perfect complete subtrees.",
        "intendedApproach": "Return `(1 << lh) - 1` when `lh == rh`.",
        "constraints": ["The number of nodes in the tree is in the range [0, 5 * 10^4].", "0 <= Node.val <= 5 * 10^4", "The tree is guaranteed to be complete."],
        "visibleTestCases": [
            {"id": 1, "input": "[1,2,3,4,5,6]", "expectedOutput": "6", "isHidden": False},
            {"id": 2, "input": "[]", "expectedOutput": "0", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[1]", "expectedOutput": "1", "isHidden": True},
            {"id": 4, "input": "[1,2,3,4,5,6,7]", "expectedOutput": "7", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O((log N)^2)", "space": "O(log N)"},
        "tags": ["trees", "binary-search", "c", "medium"]
    },

    # =========================================================================
    # 2. GRAPHS (12 Questions: C, C++, Java)
    # =========================================================================

    # 2.1 Graphs - Cycle in Directed Graph (C++ - Medium)
    {
        "id": "q_graph_cycle_directed",
        "title": "Detect Cycle in a Directed Graph",
        "problemStatement": "Given a directed graph with V vertices and E edges represented as an adjacency list, determine whether the graph contains a cycle.",
        "language": "cpp",
        "topic": "graphs",
        "subtopic": "dfs-cycle",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\nprivate:\n    bool dfs(int u, vector<vector<int>>& adj, vector<bool>& visited, vector<bool>& recStack) {\n        visited[u] = true;\n        recStack[u] = true;\n        \n        for (int v : adj[u]) {\n            if (!visited[v] && dfs(v, adj, visited, recStack)) {\n                return true;\n            } else if (recStack[v]) {\n                return true;\n            }\n        }\n        return false;\n    }\npublic:\n    bool isCyclic(int V, vector<vector<int>> adj) {\n        vector<bool> visited(V, false);\n        vector<bool> recStack(V, false);\n        \n        for (int i = 0; i < V; i++) {\n            if (!visited[i]) {\n                if (dfs(i, adj, visited, recStack)) return true;\n            }\n        }\n        return false;\n    }\n};",
        "correctCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\nprivate:\n    bool dfs(int u, vector<vector<int>>& adj, vector<bool>& visited, vector<bool>& recStack) {\n        visited[u] = true;\n        recStack[u] = true;\n        \n        for (int v : adj[u]) {\n            if (!visited[v] && dfs(v, adj, visited, recStack)) {\n                return true;\n            } else if (recStack[v]) {\n                return true;\n            }\n        }\n        recStack[u] = false;\n        return false;\n    }\npublic:\n    bool isCyclic(int V, vector<vector<int>> adj) {\n        vector<bool> visited(V, false);\n        vector<bool> recStack(V, false);\n        \n        for (int i = 0; i < V; i++) {\n            if (!visited[i]) {\n                if (dfs(i, adj, visited, recStack)) return true;\n            }\n        }\n        return false;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Fails to backtrack recStack[u] = false when leaving the DFS recursion frame, falsely flagging diamond/converging DAG paths as cycles.",
                "type": "incorrect recursion",
                "lineRange": "16"
            }
        ],
        "primaryBugType": "incorrect recursion",
        "explanation": "In cycle detection for directed graphs, `recStack` tracks vertices currently in the active DFS recursion branch. If `recStack[u]` is not reset to `false` when backtracking, any vertex visited on an earlier separate path will remain marked as active, causing false cycle detections on acyclic graphs.",
        "intendedApproach": "Set `recStack[u] = false;` right before returning `false` from `dfs`.",
        "constraints": ["1 <= V, E <= 10^5", "0 <= u, v < V"],
        "visibleTestCases": [
            {"id": 1, "input": "V = 4, E = 4\n0 1\n1 2\n2 3\n3 3", "expectedOutput": "true", "isHidden": False},
            {"id": 2, "input": "V = 4, E = 3\n0 1\n1 2\n2 3", "expectedOutput": "false", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "V = 3, E = 3\n0 1\n0 2\n1 2", "expectedOutput": "false", "isHidden": True},
            {"id": 4, "input": "V = 2, E = 2\n0 1\n1 0", "expectedOutput": "true", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(V + E)", "space": "O(V)"},
        "tags": ["graphs", "dfs", "cycle-detection", "cpp", "medium"],
        "visualData": {
            "type": "graph",
            "title": "Directed Graph (Cycle: 1 -> 2 -> 3 -> 1)",
            "data": {
                "nodes": ["0", "1", "2", "3"],
                "edges": [["0", "1"], ["1", "2"], ["2", "3"], ["3", "1"]],
                "directed": True
            }
        }
    },

    # 2.2 Graphs - Number of Islands (Java - Medium)
    {
        "id": "q_graph_num_islands",
        "title": "Number of Islands",
        "problemStatement": "Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.\nAn island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.",
        "language": "java",
        "topic": "graphs",
        "subtopic": "grid-bfs",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "import java.util.*;\n\nclass Solution {\n    public int numIslands(char[][] grid) {\n        if (grid == null || grid.length == 0) return 0;\n        int m = grid.length, n = grid[0].length;\n        int islands = 0;\n        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};\n        \n        for (int r = 0; r < m; r++) {\n            for (int c = 0; c < n; c++) {\n                if (grid[r][c] == '1') {\n                    islands++;\n                    Queue<int[]> q = new LinkedList<>();\n                    q.offer(new int[]{r, c});\n                    \n                    while (!q.isEmpty()) {\n                        int[] curr = q.poll();\n                        int row = curr[0], col = curr[1];\n                        grid[row][col] = '0';\n                        \n                        for (int[] d : dirs) {\n                            int nr = row + d[0], nc = col + d[1];\n                            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == '1') {\n                                q.offer(new int[]{nr, nc});\n                            }\n                        }\n                    }\n                }\n            }\n        }\n        return islands;\n    }\n}",
        "correctCode": "import java.util.*;\n\nclass Solution {\n    public int numIslands(char[][] grid) {\n        if (grid == null || grid.length == 0) return 0;\n        int m = grid.length, n = grid[0].length;\n        int islands = 0;\n        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};\n        \n        for (int r = 0; r < m; r++) {\n            for (int c = 0; c < n; c++) {\n                if (grid[r][c] == '1') {\n                    islands++;\n                    grid[r][c] = '0';\n                    Queue<int[]> q = new LinkedList<>();\n                    q.offer(new int[]{r, c});\n                    \n                    while (!q.isEmpty()) {\n                        int[] curr = q.poll();\n                        int row = curr[0], col = curr[1];\n                        \n                        for (int[] d : dirs) {\n                            int nr = row + d[0], nc = col + d[1];\n                            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == '1') {\n                                grid[nr][nc] = '0';\n                                q.offer(new int[]{nr, nc});\n                            }\n                        }\n                    }\n                }\n            }\n        }\n        return islands;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Marks grid cells as visited only when dequeued instead of when enqueued, leading to repeated queuing of the same cell and exponential performance degradation.",
                "type": "incorrect traversal",
                "lineRange": "19"
            }
        ],
        "primaryBugType": "incorrect traversal",
        "explanation": "In BFS on a grid, if a cell is not immediately marked visited (`'0'`) upon being pushed into the queue, its neighboring cells will continually re-enqueue it, causing memory blowup and Time Limit Exceeded (TLE) on large land components.",
        "intendedApproach": "Mark `grid[nr][nc] = '0'` immediately when offering the coordinate into the queue.",
        "constraints": ["m == grid.length", "n == grid[i].length", "1 <= m, n <= 300", "grid[i][j] is '0' or '1'."],
        "visibleTestCases": [
            {"id": 1, "input": "[[\"1\",\"1\",\"1\",\"1\",\"0\"],[\"1\",\"1\",\"0\",\"1\",\"0\"],[\"1\",\"1\",\"0\",\"0\",\"0\"],[\"0\",\"0\",\"0\",\"0\",\"0\"]", "expectedOutput": "1", "isHidden": False},
            {"id": 2, "input": "[[\"1\",\"1\",\"0\",\"0\",\"0\"],[\"1\",\"1\",\"0\",\"0\",\"0\"],[\"0\",\"0\",\"1\",\"0\",\"0\"],[\"0\",\"0\",\"0\",\"1\",\"1\"]", "expectedOutput": "3", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[[\"1\"]]", "expectedOutput": "1", "isHidden": True},
            {"id": 4, "input": "[[\"0\"]]", "expectedOutput": "0", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(M * N)", "space": "O(min(M, N))"},
        "tags": ["graphs", "bfs", "matrix", "java", "medium"],
        "visualData": {
            "type": "matrix",
            "title": "4x5 Binary Land Map",
            "data": [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
        }
    },

    # 2.3 Graphs - Course Schedule (Topological Sort) (C++ - Medium)
    {
        "id": "q_graph_course_schedule",
        "title": "Course Schedule (Topological Sort)",
        "problemStatement": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.\nReturn true if you can finish all courses. Otherwise, return false.",
        "language": "cpp",
        "topic": "graphs",
        "subtopic": "topological-sort",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n        vector<vector<int>> adj(numCourses);\n        vector<int> inDegree(numCourses, 0);\n        \n        for (auto& p : prerequisites) {\n            adj[p[1]].push_back(p[0]);\n            inDegree[p[0]]++;\n        }\n        \n        queue<int> q;\n        for (int i = 0; i < numCourses; i++) {\n            if (inDegree[i] == 0) q.push(i);\n        }\n        \n        int count = 0;\n        while (!q.empty()) {\n            int curr = q.front();\n            q.pop();\n            count++;\n            \n            for (int nextCourse : adj[curr]) {\n                inDegree[nextCourse]--;\n                q.push(nextCourse);\n            }\n        }\n        return count == numCourses;\n    }\n};",
        "correctCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n        vector<vector<int>> adj(numCourses);\n        vector<int> inDegree(numCourses, 0);\n        \n        for (auto& p : prerequisites) {\n            adj[p[1]].push_back(p[0]);\n            inDegree[p[0]]++;\n        }\n        \n        queue<int> q;\n        for (int i = 0; i < numCourses; i++) {\n            if (inDegree[i] == 0) q.push(i);\n        }\n        \n        int count = 0;\n        while (!q.empty()) {\n            int curr = q.front();\n            q.pop();\n            count++;\n            \n            for (int nextCourse : adj[curr]) {\n                inDegree[nextCourse]--;\n                if (inDegree[nextCourse] == 0) {\n                    q.push(nextCourse);\n                }\n            }\n        }\n        return count == numCourses;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Enqueues dependent courses before all their incoming prerequisite constraints (inDegree == 0) are met.",
                "type": "logical",
                "lineRange": "29"
            }
        ],
        "primaryBugType": "logical",
        "explanation": "Kahn's algorithm for topological sorting requires that a vertex is only added to the process queue once its in-degree reaches 0 (all prerequisite courses have been completed). Pushing prematurely allows invalid cycles to be processed as valid courses.",
        "intendedApproach": "Wrap `q.push(nextCourse)` inside `if (inDegree[nextCourse] == 0)`.",
        "constraints": ["1 <= numCourses <= 2000", "0 <= prerequisites.length <= 5000", "prerequisites[i].length == 2", "All the pairs prerequisites[i] are unique."],
        "visibleTestCases": [
            {"id": 1, "input": "numCourses = 2, prerequisites = [[1,0]]", "expectedOutput": "true", "isHidden": False},
            {"id": 2, "input": "numCourses = 2, prerequisites = [[1,0],[0,1]]", "expectedOutput": "false", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "numCourses = 3, prerequisites = [[1,0],[2,1]]", "expectedOutput": "true", "isHidden": True},
            {"id": 4, "input": "numCourses = 4, prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]", "expectedOutput": "false", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(V + E)", "space": "O(V + E)"},
        "tags": ["graphs", "topological-sort", "bfs", "cpp", "medium"]
    },

    # 2.4 Graphs - Dijkstra Shortest Path (C++ - Hard)
    {
        "id": "q_graph_dijkstra",
        "title": "Dijkstra's Shortest Path",
        "problemStatement": "Given a weighted directed graph with V vertices and an adjacency list representation where edges have non-negative weights, return an array of shortest distances from the source vertex 0 to all other vertices. If a vertex is unreachable, its distance is -1.",
        "language": "cpp",
        "topic": "graphs",
        "subtopic": "shortest-path",
        "difficulty": "hard",
        "estimatedTime": 25,
        "buggyCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> dijkstra(int V, vector<vector<pair<int, int>>>& adj, int S) {\n        vector<int> dist(V, 1e9);\n        priority_queue<pair<int, int>> pq; // (dist, u)\n        \n        dist[S] = 0;\n        pq.push({0, S});\n        \n        while (!pq.empty()) {\n            int d = pq.top().first;\n            int u = pq.top().second;\n            pq.pop();\n            \n            if (d > dist[u]) continue;\n            \n            for (auto& edge : adj[u]) {\n                int v = edge.first;\n                int weight = edge.second;\n                \n                if (dist[u] + weight < dist[v]) {\n                    dist[v] = dist[u] + weight;\n                    pq.push({dist[v], v});\n                }\n            }\n        }\n        \n        for (int i = 0; i < V; i++) {\n            if (dist[i] == 1e9) dist[i] = -1;\n        }\n        return dist;\n    }\n};",
        "correctCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> dijkstra(int V, vector<vector<pair<int, int>>>& adj, int S) {\n        vector<int> dist(V, 1e9);\n        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;\n        \n        dist[S] = 0;\n        pq.push({0, S});\n        \n        while (!pq.empty()) {\n            int d = pq.top().first;\n            int u = pq.top().second;\n            pq.pop();\n            \n            if (d > dist[u]) continue;\n            \n            for (auto& edge : adj[u]) {\n                int v = edge.first;\n                int weight = edge.second;\n                \n                if (dist[u] + weight < dist[v]) {\n                    dist[v] = dist[u] + weight;\n                    pq.push({dist[v], v});\n                }\n            }\n        }\n        \n        for (int i = 0; i < V; i++) {\n            if (dist[i] == 1e9) dist[i] = -1;\n        }\n        return dist;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Initializes standard priority_queue (max-heap) instead of min-heap, processing the longest distances first and violating Dijkstra greediness.",
                "type": "incorrect data structure usage",
                "lineRange": "9"
            }
        ],
        "primaryBugType": "incorrect data structure usage",
        "explanation": "In C++, `std::priority_queue<T>` is a max-heap by default. Dijkstra's algorithm strictly relies on extracting the minimum distance node first. Operating on the maximum distance produces exponential vertex expansions and incorrect path relaxations.",
        "intendedApproach": "Use `priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>>`.",
        "constraints": ["1 <= V <= 10^5", "0 <= E <= 3 * 10^5", "0 <= weight <= 1000", "0 <= S < V"],
        "visibleTestCases": [
            {"id": 1, "input": "V = 3, E = 3, S = 2\nadj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]", "expectedOutput": "[4, 3, 0]", "isHidden": False},
            {"id": 2, "input": "V = 2, E = 1, S = 0\nadj = [[[1, 9]], []]", "expectedOutput": "[0, 9]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "V = 1, E = 0, S = 0\nadj = [[]]", "expectedOutput": "[0]", "isHidden": True},
            {"id": 4, "input": "V = 4, E = 4, S = 0\nadj = [[[1, 1], [2, 4]], [[2, 2], [3, 5]], [[3, 1]], []]", "expectedOutput": "[0, 1, 3, 4]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O((V + E) log V)", "space": "O(V + E)"},
        "tags": ["graphs", "dijkstra", "heap", "cpp", "hard"]
    },

    # 2.5 Graphs - Shortest Path in Unweighted Graph (C - Medium)
    {
        "id": "q_graph_bfs_shortest_path",
        "title": "Shortest Path in Unweighted Graph",
        "problemStatement": "Given an unweighted undirected graph with V vertices and a source node src, compute the shortest path distance from src to all other vertices. Return -1 for unreachable nodes.",
        "language": "c",
        "topic": "graphs",
        "subtopic": "bfs-distance",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <stdlib.h>\n\nint* shortestPath(int V, int** adj, int* adjSize, int src) {\n    int* dist = (int*)malloc(V * sizeof(int));\n    int* queue = (int*)malloc(V * sizeof(int));\n    int front = 0, back = 0;\n    \n    for (int i = 0; i < V; i++) dist[i] = 0;\n    \n    dist[src] = 0;\n    queue[back++] = src;\n    \n    while (front < back) {\n        int u = queue[front++];\n        for (int i = 0; i < adjSize[u]; i++) {\n            int v = adj[u][i];\n            if (dist[v] == 0 && v != src) {\n                dist[v] = dist[u] + 1;\n                queue[back++] = v;\n            }\n        }\n    }\n    \n    free(queue);\n    return dist;\n}",
        "correctCode": "#include <stdlib.h>\n\nint* shortestPath(int V, int** adj, int* adjSize, int src) {\n    int* dist = (int*)malloc(V * sizeof(int));\n    int* queue = (int*)malloc(V * sizeof(int));\n    int front = 0, back = 0;\n    \n    for (int i = 0; i < V; i++) dist[i] = -1;\n    \n    dist[src] = 0;\n    queue[back++] = src;\n    \n    while (front < back) {\n        int u = queue[front++];\n        for (int i = 0; i < adjSize[u]; i++) {\n            int v = adj[u][i];\n            if (dist[v] == -1) {\n                dist[v] = dist[u] + 1;\n                queue[back++] = v;\n            }\n        }\n    }\n    \n    free(queue);\n    return dist;\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Initializes distance array to 0 instead of -1, conflating unvisited nodes with 0-distance nodes.",
                "type": "incorrect initialization",
                "lineRange": "8"
            }
        ],
        "primaryBugType": "incorrect initialization",
        "explanation": "If distances start at 0, an unvisited node cannot be cleanly differentiated from the source node (which has distance 0). Any unreachable node will mistakenly be reported as distance 0 instead of -1.",
        "intendedApproach": "Initialize all elements in `dist` to -1.",
        "constraints": ["1 <= V <= 10^4", "0 <= E <= 5 * 10^4", "0 <= src < V"],
        "visibleTestCases": [
            {"id": 1, "input": "V = 4, src = 0, edges = [[0,1],[1,2],[2,3]]", "expectedOutput": "[0, 1, 2, 3]", "isHidden": False},
            {"id": 2, "input": "V = 4, src = 0, edges = [[0,1],[1,2]]", "expectedOutput": "[0, 1, 2, -1]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "V = 1, src = 0, edges = []", "expectedOutput": "[0]", "isHidden": True},
            {"id": 4, "input": "V = 5, src = 2, edges = [[2,0],[2,1],[0,3],[1,4]]", "expectedOutput": "[1, 1, 0, 2, 2]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(V + E)", "space": "O(V)"},
        "tags": ["graphs", "bfs", "c", "medium"]
    },

    # 2.6 Graphs - Flood Fill (C - Easy)
    {
        "id": "q_graph_flood_fill",
        "title": "Flood Fill",
        "problemStatement": "An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.\nPerform a flood fill on the image starting from the pixel (sr, sc) replacing connected components of color with color.",
        "language": "c",
        "topic": "graphs",
        "subtopic": "grid-dfs",
        "difficulty": "easy",
        "estimatedTime": 15,
        "buggyCode": "void dfs(int** image, int m, int n, int r, int c, int oldColor, int newColor) {\n    if (r < 0 || r >= m || c < 0 || c >= n || image[r][c] != oldColor) {\n        return;\n    }\n    image[r][c] = newColor;\n    dfs(image, m, n, r + 1, c, oldColor, newColor);\n    dfs(image, m, n, r - 1, c, oldColor, newColor);\n    dfs(image, m, n, r, c + 1, oldColor, newColor);\n    dfs(image, m, n, r, c - 1, oldColor, newColor);\n}\n\nint** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) {\n    int oldColor = image[sr][sc];\n    dfs(image, imageSize, *imageColSize, sr, sc, oldColor, color);\n    *returnSize = imageSize;\n    *returnColumnSizes = imageColSize;\n    return image;\n}",
        "correctCode": "void dfs(int** image, int m, int n, int r, int c, int oldColor, int newColor) {\n    if (r < 0 || r >= m || c < 0 || c >= n || image[r][c] != oldColor) {\n        return;\n    }\n    image[r][c] = newColor;\n    dfs(image, m, n, r + 1, c, oldColor, newColor);\n    dfs(image, m, n, r - 1, c, oldColor, newColor);\n    dfs(image, m, n, r, c + 1, oldColor, newColor);\n    dfs(image, m, n, r, c - 1, oldColor, newColor);\n}\n\nint** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) {\n    int oldColor = image[sr][sc];\n    if (oldColor != color) {\n        dfs(image, imageSize, *imageColSize, sr, sc, oldColor, color);\n    }\n    *returnSize = imageSize;\n    *returnColumnSizes = imageColSize;\n    return image;\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Does not handle the edge case where the starting pixel already has the target color (oldColor == color), triggering stack overflow infinite recursion.",
                "type": "edge case",
                "lineRange": "15-16"
            }
        ],
        "primaryBugType": "edge case",
        "explanation": "If `oldColor == color`, setting `image[r][c] = newColor` does not change the cell value. The boundary check `image[r][c] != oldColor` will never trigger, leading to an infinite cycle between neighboring pixels.",
        "intendedApproach": "Add `if (oldColor != color)` before initiating DFS traversal.",
        "constraints": ["m == image.length", "n == image[i].length", "1 <= m, n <= 50", "0 <= image[i][j], color < 65536", "0 <= sr < m", "0 <= sc < n"],
        "visibleTestCases": [
            {"id": 1, "input": "image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2", "expectedOutput": "[[2,2,2],[2,2,0],[2,0,1]]", "isHidden": False},
            {"id": 2, "input": "image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0", "expectedOutput": "[[0,0,0],[0,0,0]]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "image = [[1]], sr = 0, sc = 0, color = 2", "expectedOutput": "[[2]]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(M * N)", "space": "O(M * N)"},
        "tags": ["graphs", "dfs", "matrix", "c", "easy"]
    },

    # 2.7 Graphs - Is Graph Bipartite? (Java - Medium)
    {
        "id": "q_graph_bipartite",
        "title": "Is Graph Bipartite?",
        "problemStatement": "There is an undirected graph with n nodes. Return true if and only if it is bipartite.\nA graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.",
        "language": "java",
        "topic": "graphs",
        "subtopic": "graph-coloring",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "import java.util.*;\n\nclass Solution {\n    public boolean isBipartite(int[][] graph) {\n        int n = graph.length;\n        int[] colors = new int[n]; // 0: uncolored, 1: red, -1: blue\n        \n        Queue<Integer> q = new LinkedList<>();\n        q.offer(0);\n        colors[0] = 1;\n        \n        while (!q.isEmpty()) {\n            int node = q.poll();\n            for (int neighbor : graph[node]) {\n                if (colors[neighbor] == 0) {\n                    colors[neighbor] = -colors[node];\n                    q.offer(neighbor);\n                } else if (colors[neighbor] == colors[node]) {\n                    return false;\n                }\n            }\n        }\n        return true;\n    }\n}",
        "correctCode": "import java.util.*;\n\nclass Solution {\n    public boolean isBipartite(int[][] graph) {\n        int n = graph.length;\n        int[] colors = new int[n]; // 0: uncolored, 1: red, -1: blue\n        \n        for (int i = 0; i < n; i++) {\n            if (colors[i] != 0) continue;\n            \n            Queue<Integer> q = new LinkedList<>();\n            q.offer(i);\n            colors[i] = 1;\n            \n            while (!q.isEmpty()) {\n                int node = q.poll();\n                for (int neighbor : graph[node]) {\n                    if (colors[neighbor] == 0) {\n                        colors[neighbor] = -colors[node];\n                        q.offer(neighbor);\n                    } else if (colors[neighbor] == colors[node]) {\n                        return false;\n                    }\n                }\n            }\n        }\n        return true;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Only launches BFS from vertex 0, failing to validate odd cycles located in disconnected graph components.",
                "type": "boundary",
                "lineRange": "8-11"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "Graphs may consist of multiple disjoint components. Running BFS only from node 0 leaves unvisited components uncolored, allowing invalid odd cycles in other components to go undetected.",
        "intendedApproach": "Iterate through all vertices `0` to `n - 1` with an outer loop to initiate BFS on any uncolored node.",
        "constraints": ["graph.length == n", "1 <= n <= 100", "0 <= graph[u].length < n", "graph[u] does not contain u."],
        "visibleTestCases": [
            {"id": 1, "input": "[[1,2,3],[0,2],[0,1,3],[0,2]]", "expectedOutput": "false", "isHidden": False},
            {"id": 2, "input": "[[1,3],[0,2],[1,3],[0,2]]", "expectedOutput": "true", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]", "expectedOutput": "false", "isHidden": True},
            {"id": 4, "input": "[[]]", "expectedOutput": "true", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(V + E)", "space": "O(V)"},
        "tags": ["graphs", "bfs", "graph-coloring", "java", "medium"]
    },

    # 2.8 Graphs - Clone Graph (Java - Medium)
    {
        "id": "q_graph_clone",
        "title": "Clone Graph",
        "problemStatement": "Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.\nEach node in the graph contains a value (int) and a list (List[Node]) of its neighbors.",
        "language": "java",
        "topic": "graphs",
        "subtopic": "graph-traversal",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "import java.util.*;\n\nclass Node {\n    public int val;\n    public List<Node> neighbors;\n    public Node(int _val) { val = _val; neighbors = new ArrayList<>(); }\n}\n\nclass Solution {\n    public Node cloneGraph(Node node) {\n        if (node == null) return null;\n        \n        Node clone = new Node(node.val);\n        for (Node neighbor : node.neighbors) {\n            clone.neighbors.add(cloneGraph(neighbor));\n        }\n        return clone;\n    }\n}",
        "correctCode": "import java.util.*;\n\nclass Node {\n    public int val;\n    public List<Node> neighbors;\n    public Node(int _val) { val = _val; neighbors = new ArrayList<>(); }\n}\n\nclass Solution {\n    private Map<Node, Node> visited = new HashMap<>();\n    \n    public Node cloneGraph(Node node) {\n        if (node == null) return null;\n        if (visited.containsKey(node)) {\n            return visited.get(node);\n        }\n        \n        Node clone = new Node(node.val);\n        visited.put(node, clone);\n        \n        for (Node neighbor : node.neighbors) {\n            clone.neighbors.add(cloneGraph(neighbor));\n        }\n        return clone;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Lacks a visited map to track already cloned nodes, causing infinite recursion on cyclic undirected edges.",
                "type": "incorrect recursion",
                "lineRange": "12-18"
            }
        ],
        "primaryBugType": "incorrect recursion",
        "explanation": "Because undirected graphs contain bidirectional edges (cycles between adjacent nodes), recursively calling `cloneGraph` without memoizing previously created clone nodes produces an infinite call stack and `StackOverflowError`.",
        "intendedApproach": "Use a `Map<Node, Node> visited` to return already cloned instances immediately.",
        "constraints": ["The number of nodes in the graph is in the range [0, 100].", "1 <= Node.val <= 100", "Node.val is unique for each node."],
        "visibleTestCases": [
            {"id": 1, "input": "[[2,4],[1,3],[2,4],[1,3]]", "expectedOutput": "[[2,4],[1,3],[2,4],[1,3]]", "isHidden": False},
            {"id": 2, "input": "[[]]", "expectedOutput": "[[]]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[]", "expectedOutput": "[]", "isHidden": True},
            {"id": 4, "input": "[[2],[1]]", "expectedOutput": "[[2],[1]]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(V + E)", "space": "O(V)"},
        "tags": ["graphs", "hash-table", "dfs", "java", "medium"]
    },

    # 2.9 Graphs - Redundant Connection (Disjoint Set Union) (C++ - Medium)
    {
        "id": "q_graph_redundant_connection",
        "title": "Redundant Connection (DSU)",
        "problemStatement": "In this problem, a tree is an undirected graph that is connected and has no cycles.\nYou are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. Return an edge that can be removed so that the resulting graph is a tree.",
        "language": "cpp",
        "topic": "graphs",
        "subtopic": "dsu-union-find",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\nprivate:\n    int find(vector<int>& parent, int x) {\n        if (parent[x] != x) {\n            return parent[x];\n        }\n        return x;\n    }\npublic:\n    vector<int> findRedundantConnection(vector<vector<int>>& edges) {\n        int n = edges.size();\n        vector<int> parent(n + 1);\n        for (int i = 1; i <= n; i++) parent[i] = i;\n        \n        for (auto& edge : edges) {\n            int rootU = find(parent, edge[0]);\n            int rootV = find(parent, edge[1]);\n            \n            if (rootU == rootV) {\n                return edge;\n            }\n            parent[rootU] = rootV;\n        }\n        return {};\n    }\n};",
        "correctCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\nprivate:\n    int find(vector<int>& parent, int x) {\n        if (parent[x] != x) {\n            parent[x] = find(parent, parent[x]);\n        }\n        return parent[x];\n    }\npublic:\n    vector<int> findRedundantConnection(vector<vector<int>>& edges) {\n        int n = edges.size();\n        vector<int> parent(n + 1);\n        for (int i = 1; i <= n; i++) parent[i] = i;\n        \n        for (auto& edge : edges) {\n            int rootU = find(parent, edge[0]);\n            int rootV = find(parent, edge[1]);\n            \n            if (rootU == rootV) {\n                return edge;\n            }\n            parent[rootU] = rootV;\n        }\n        return {};\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Find operation only looks up the immediate parent instead of recursively traversing to the root with path compression.",
                "type": "logical",
                "lineRange": "8"
            }
        ],
        "primaryBugType": "logical",
        "explanation": "Without recursion (`find(parent, parent[x])`), `parent[x]` only stores the direct parent rather than the root representative of the disjoint set. Chains of length >= 2 fail to detect connected components.",
        "intendedApproach": "Use recursive root search with path compression `parent[x] = find(parent, parent[x])`.",
        "constraints": ["n == edges.length", "3 <= n <= 1000", "edges[i].length == 2", "1 <= ai < bi <= edges.length"],
        "visibleTestCases": [
            {"id": 1, "input": "[[1,2],[1,3],[2,3]]", "expectedOutput": "[2,3]", "isHidden": False},
            {"id": 2, "input": "[[1,2],[2,3],[3,4],[1,4],[1,5]]", "expectedOutput": "[1,4]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[[1,4],[3,4],[1,3],[1,2],[4,5]]", "expectedOutput": "[1,3]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N * α(N))", "space": "O(N)"},
        "tags": ["graphs", "union-find", "dsu", "cpp", "medium"]
    },

    # 2.10 Graphs - Word Ladder (BFS) (Java - Hard)
    {
        "id": "q_graph_word_ladder",
        "title": "Word Ladder",
        "problemStatement": "A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that every adjacent pair of words differs by a single letter. Return the number of words in the shortest transformation sequence, or 0 if no such sequence exists.",
        "language": "java",
        "topic": "graphs",
        "subtopic": "bfs-shortest-path",
        "difficulty": "hard",
        "estimatedTime": 25,
        "buggyCode": "import java.util.*;\n\nclass Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        Set<String> wordSet = new HashSet<>(wordList);\n        if (!wordSet.contains(endWord)) return 0;\n        \n        Queue<String> queue = new LinkedList<>();\n        queue.offer(beginWord);\n        int steps = 0;\n        \n        while (!queue.isEmpty()) {\n            int size = queue.size();\n            steps++;\n            \n            for (int i = 0; i < size; i++) {\n                String curr = queue.poll();\n                if (curr.equals(endWord)) return steps;\n                \n                char[] chars = curr.toCharArray();\n                for (int j = 0; j < chars.length; j++) {\n                    char original = chars[j];\n                    for (char c = 'a'; c <= 'z'; c++) {\n                        chars[j] = c;\n                        String nextWord = new String(chars);\n                        if (wordSet.contains(nextWord)) {\n                            queue.offer(nextWord);\n                        }\n                    }\n                    chars[j] = original;\n                }\n            }\n        }\n        return 0;\n    }\n}",
        "correctCode": "import java.util.*;\n\nclass Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        Set<String> wordSet = new HashSet<>(wordList);\n        if (!wordSet.contains(endWord)) return 0;\n        \n        Queue<String> queue = new LinkedList<>();\n        queue.offer(beginWord);\n        int steps = 0;\n        \n        while (!queue.isEmpty()) {\n            int size = queue.size();\n            steps++;\n            \n            for (int i = 0; i < size; i++) {\n                String curr = queue.poll();\n                if (curr.equals(endWord)) return steps;\n                \n                char[] chars = curr.toCharArray();\n                for (int j = 0; j < chars.length; j++) {\n                    char original = chars[j];\n                    for (char c = 'a'; c <= 'z'; c++) {\n                        chars[j] = c;\n                        String nextWord = new String(chars);\n                        if (wordSet.contains(nextWord)) {\n                            wordSet.remove(nextWord);\n                            queue.offer(nextWord);\n                        }\n                    }\n                    chars[j] = original;\n                }\n            }\n        }\n        return 0;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Fails to mark words as visited by removing them from wordSet upon enqueuing, resulting in cyclic state expansions.",
                "type": "incorrect state transition",
                "lineRange": "28"
            }
        ],
        "primaryBugType": "incorrect state transition",
        "explanation": "In BFS shortest path exploration, any node added to the queue must be immediately marked as visited (or removed from the available dictionary set) so it is never re-processed at deeper tree levels.",
        "intendedApproach": "Add `wordSet.remove(nextWord)` immediately when pushing to the queue.",
        "constraints": ["1 <= beginWord.length <= 10", "endWord.length == beginWord.length", "1 <= wordList.length <= 5000", "beginWord != endWord"],
        "visibleTestCases": [
            {"id": 1, "input": "beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "expectedOutput": "5", "isHidden": False},
            {"id": 2, "input": "beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]", "expectedOutput": "0", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "beginWord = \"a\", endWord = \"c\", wordList = [\"a\",\"b\",\"c\"]", "expectedOutput": "2", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N * M * 26)", "space": "O(N * M)"},
        "tags": ["graphs", "bfs", "hash-table", "java", "hard"]
    },

    # 2.11 Graphs - All Paths From Source to Target (Java - Medium)
    {
        "id": "q_graph_all_paths",
        "title": "All Paths From Source to Target",
        "problemStatement": "Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.",
        "language": "java",
        "topic": "graphs",
        "subtopic": "backtracking-dfs",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "import java.util.*;\n\nclass Solution {\n    private void dfs(int node, int target, int[][] graph, List<Integer> path, List<List<Integer>> result) {\n        path.add(node);\n        if (node == target) {\n            result.add(new ArrayList<>(path));\n            return;\n        }\n        \n        for (int next : graph[node]) {\n            dfs(next, target, graph, path, result);\n        }\n        path.remove(path.size() - 1);\n    }\n    \n    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {\n        List<List<Integer>> result = new ArrayList<>();\n        dfs(0, graph.length - 1, graph, new ArrayList<>(), result);\n        return result;\n    }\n}",
        "correctCode": "import java.util.*;\n\nclass Solution {\n    private void dfs(int node, int target, int[][] graph, List<Integer> path, List<List<Integer>> result) {\n        path.add(node);\n        if (node == target) {\n            result.add(new ArrayList<>(path));\n            path.remove(path.size() - 1);\n            return;\n        }\n        \n        for (int next : graph[node]) {\n            dfs(next, target, graph, path, result);\n        }\n        path.remove(path.size() - 1);\n    }\n    \n    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {\n        List<List<Integer>> result = new ArrayList<>();\n        dfs(0, graph.length - 1, graph, new ArrayList<>(), result);\n        return result;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Leaves the target node in the path list upon hitting the base case return, corrupting sibling path generations.",
                "type": "incorrect traversal",
                "lineRange": "8"
            }
        ],
        "primaryBugType": "incorrect traversal",
        "explanation": "When the base case `node == target` is reached, returning directly without removing the last element leaves `target` at the end of `path`. Backtracking in parent frames subsequently deletes the wrong node.",
        "intendedApproach": "Call `path.remove(path.size() - 1)` before returning from the base case.",
        "constraints": ["n == graph.length", "2 <= n <= 15", "0 <= graph[i][j] < n", "The input graph is guaranteed to be a DAG."],
        "visibleTestCases": [
            {"id": 1, "input": "[[1,2],[3],[3],[]]", "expectedOutput": "[[0,1,3],[0,2,3]]", "isHidden": False},
            {"id": 2, "input": "[[4,3,1],[3,2,4],[3],[4],[]]", "expectedOutput": "[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[[1],[]]", "expectedOutput": "[[0,1]]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(2^V * V)", "space": "O(V)"},
        "tags": ["graphs", "backtracking", "dfs", "java", "medium"]
    },

    # 2.12 Graphs - Minimum Cost to Connect All Points (Prim's / Kruskal's) (C++ - Hard)
    {
        "id": "q_graph_min_cost_points",
        "title": "Minimum Cost to Connect All Points",
        "problemStatement": "You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].\nThe cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance: |xi - xj| + |yi - yj|.\nReturn the minimum cost to make all points connected.",
        "language": "cpp",
        "topic": "graphs",
        "subtopic": "mst-prim",
        "difficulty": "hard",
        "estimatedTime": 25,
        "buggyCode": "#include <vector>\n#include <queue>\n#include <cmath>\nusing namespace std;\n\nclass Solution {\npublic:\n    int minCostConnectPoints(vector<vector<int>>& points) {\n        int n = points.size();\n        int totalCost = 0;\n        int connected = 0;\n        vector<bool> inMST(n, false);\n        \n        // (cost, u)\n        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;\n        pq.push({0, 0});\n        \n        while (!pq.empty() && connected < n) {\n            auto [cost, u] = pq.top();\n            pq.pop();\n            \n            if (inMST[u]) continue;\n            inMST[u] = true;\n            totalCost += cost;\n            connected++;\n            \n            for (int v = 0; v < n; v++) {\n                if (!inMST[v]) {\n                    int dist = (points[u][0] - points[v][0]) * (points[u][0] - points[v][0]) + \n                               (points[u][1] - points[v][1]) * (points[u][1] - points[v][1]);\n                    pq.push({dist, v});\n                }\n            }\n        }\n        return totalCost;\n    }\n};",
        "correctCode": "#include <vector>\n#include <queue>\n#include <cmath>\nusing namespace std;\n\nclass Solution {\npublic:\n    int minCostConnectPoints(vector<vector<int>>& points) {\n        int n = points.size();\n        int totalCost = 0;\n        int connected = 0;\n        vector<bool> inMST(n, false);\n        \n        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;\n        pq.push({0, 0});\n        \n        while (!pq.empty() && connected < n) {\n            auto [cost, u] = pq.top();\n            pq.pop();\n            \n            if (inMST[u]) continue;\n            inMST[u] = true;\n            totalCost += cost;\n            connected++;\n            \n            for (int v = 0; v < n; v++) {\n                if (!inMST[v]) {\n                    int dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]);\n                    pq.push({dist, v});\n                }\n            }\n        }\n        return totalCost;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Calculates squared Euclidean distance rather than Manhattan distance abs(x1 - x2) + abs(y1 - y2).",
                "type": "logical",
                "lineRange": "29-30"
            }
        ],
        "primaryBugType": "logical",
        "explanation": "The problem specification defines edge weights strictly as the Manhattan distance `|xi - xj| + |yi - yj|`. Using `(x1 - x2)^2 + (y1 - y2)^2` squares differences and heavily inflates the MST weight.",
        "intendedApproach": "Compute distance with `abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])`.",
        "constraints": ["1 <= points.length <= 1000", "-10^6 <= xi, yi <= 10^6", "All pairs (xi, yi) are distinct."],
        "visibleTestCases": [
            {"id": 1, "input": "[[0,0],[2,2],[3,10],[5,2],[7,0]]", "expectedOutput": "20", "isHidden": False},
            {"id": 2, "input": "[[3,12],[-2,5],[-4,1]]", "expectedOutput": "18", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[[0,0]]", "expectedOutput": "0", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N^2 log N)", "space": "O(N^2)"},
        "tags": ["graphs", "mst", "prim", "cpp", "hard"]
    },

    # =========================================================================
    # 3. 2D DYNAMIC PROGRAMMING (8 Questions: C, C++, Java)
    # =========================================================================

    # 3.1 2D DP - Unique Paths (C++ - Medium)
    {
        "id": "q_2ddp_unique_paths",
        "title": "Unique Paths",
        "problemStatement": "There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]) and attempts to move to the bottom-right corner (grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.\nGiven the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.",
        "language": "cpp",
        "topic": "2ddp",
        "subtopic": "grid-paths",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int uniquePaths(int m, int n) {\n        vector<vector<int>> dp(m, vector<int>(n, 0));\n        \n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (i == 0 || j == 0) {\n                    dp[i][j] = 0;\n                } else {\n                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];\n                }\n            }\n        }\n        return dp[m - 1][n - 1];\n    }\n};",
        "correctCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int uniquePaths(int m, int n) {\n        vector<vector<int>> dp(m, vector<int>(n, 1));\n        \n        for (int i = 1; i < m; i++) {\n            for (int j = 1; j < n; j++) {\n                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];\n            }\n        }\n        return dp[m - 1][n - 1];\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Initializes boundary rows and columns to 0 instead of 1, resulting in all cells evaluating to 0.",
                "type": "incorrect initialization",
                "lineRange": "11"
            }
        ],
        "primaryBugType": "incorrect initialization",
        "explanation": "There is exactly 1 valid path to any cell along the first row (only moving right) and first column (only moving down). Initializing these base cases to 0 causes the addition `dp[i-1][j] + dp[i][j-1]` to produce 0 everywhere.",
        "intendedApproach": "Initialize the DP table with 1s for all boundary cells and start the nested DP loops at index 1.",
        "constraints": ["1 <= m, n <= 100"],
        "visibleTestCases": [
            {"id": 1, "input": "m = 3, n = 7", "expectedOutput": "28", "isHidden": False},
            {"id": 2, "input": "m = 3, n = 2", "expectedOutput": "3", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "m = 1, n = 1", "expectedOutput": "1", "isHidden": True},
            {"id": 4, "input": "m = 10, n = 10", "expectedOutput": "48620", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(M * N)", "space": "O(M * N)"},
        "tags": ["2ddp", "grid", "cpp", "medium"],
        "visualData": {
            "type": "matrix",
            "title": "3x4 Grid Way Counts",
            "data": [[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 6, 10]]
        }
    },

    # 3.2 2D DP - Minimum Path Sum (Java - Medium)
    {
        "id": "q_2ddp_min_path_sum",
        "title": "Minimum Path Sum",
        "problemStatement": "Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.",
        "language": "java",
        "topic": "2ddp",
        "subtopic": "grid-paths",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "class Solution {\n    public int minPathSum(int[][] grid) {\n        int m = grid.length;\n        int n = grid[0].length;\n        int[][] dp = new int[m][n];\n        \n        dp[0][0] = grid[0][0];\n        \n        for (int j = 1; j < n; j++) {\n            dp[0][j] = grid[0][j];\n        }\n        for (int i = 1; i < m; i++) {\n            dp[i][0] = grid[i][0];\n        }\n        \n        for (int i = 1; i < m; i++) {\n            for (int j = 1; j < n; j++) {\n                dp[i][j] = grid[i][j] + Math.min(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n        return dp[m - 1][n - 1];\n    }\n}",
        "correctCode": "class Solution {\n    public int minPathSum(int[][] grid) {\n        int m = grid.length;\n        int n = grid[0].length;\n        int[][] dp = new int[m][n];\n        \n        dp[0][0] = grid[0][0];\n        \n        for (int j = 1; j < n; j++) {\n            dp[0][j] = dp[0][j - 1] + grid[0][j];\n        }\n        for (int i = 1; i < m; i++) {\n            dp[i][0] = dp[i - 1][0] + grid[i][0];\n        }\n        \n        for (int i = 1; i < m; i++) {\n            for (int j = 1; j < n; j++) {\n                dp[i][j] = grid[i][j] + Math.min(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n        return dp[m - 1][n - 1];\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Boundary initializations set dp[0][j] = grid[0][j] instead of accumulating dp[0][j-1] + grid[0][j].",
                "type": "incorrect initialization",
                "lineRange": "10-14"
            }
        ],
        "primaryBugType": "incorrect initialization",
        "explanation": "Moving along the first row or first column can only come from the single adjacent preceding cell. Therefore, the minimum cost to reach `(0, j)` is the cumulative sum `dp[0][j-1] + grid[0][j]`.",
        "intendedApproach": "Accumulate previous costs: `dp[0][j] = dp[0][j - 1] + grid[0][j]` and `dp[i][0] = dp[i - 1][0] + grid[i][0]`.",
        "constraints": ["m == grid.length", "n == grid[i].length", "1 <= m, n <= 200", "0 <= grid[i][j] <= 200"],
        "visibleTestCases": [
            {"id": 1, "input": "[[1,3,1],[1,5,1],[4,2,1]]", "expectedOutput": "7", "isHidden": False},
            {"id": 2, "input": "[[1,2,3],[4,5,6]]", "expectedOutput": "12", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[[5]]", "expectedOutput": "5", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(M * N)", "space": "O(M * N)"},
        "tags": ["2ddp", "matrix", "java", "medium"],
        "visualData": {
            "type": "matrix",
            "title": "Grid Cost Matrix (Min Path = 1 -> 3 -> 1 -> 1 -> 1 = 7)",
            "data": [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        }
    },

    # 3.3 2D DP - Longest Common Subsequence (C - Medium)
    {
        "id": "q_2ddp_lcs",
        "title": "Longest Common Subsequence",
        "problemStatement": "Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.",
        "language": "c",
        "topic": "2ddp",
        "subtopic": "lcs",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <string.h>\n#include <stdlib.h>\n\nint max(int a, int b) { return a > b ? a : b; }\n\nint longestCommonSubsequence(char* text1, char* text2) {\n    int m = strlen(text1);\n    int n = strlen(text2);\n    int dp[1005][1005];\n    \n    for (int i = 0; i <= m; i++) {\n        for (int j = 0; j <= n; j++) {\n            if (i == 0 || j == 0) {\n                dp[i][j] = 0;\n            } else if (text1[i] == text2[j]) {\n                dp[i][j] = dp[i - 1][j - 1] + 1;\n            } else {\n                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[m][n];\n}",
        "correctCode": "#include <string.h>\n#include <stdlib.h>\n\nint max(int a, int b) { return a > b ? a : b; }\n\nint longestCommonSubsequence(char* text1, char* text2) {\n    int m = strlen(text1);\n    int n = strlen(text2);\n    int dp[1005][1005];\n    \n    for (int i = 0; i <= m; i++) {\n        for (int j = 0; j <= n; j++) {\n            if (i == 0 || j == 0) {\n                dp[i][j] = 0;\n            } else if (text1[i - 1] == text2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1] + 1;\n            } else {\n                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[m][n];\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Compares text1[i] and text2[j] instead of text1[i-1] and text2[j-1], causing off-by-one string access and reading uninitialized out-of-bound memory at i=m, j=n.",
                "type": "off-by-one",
                "lineRange": "16"
            }
        ],
        "primaryBugType": "off-by-one",
        "explanation": "Since the 2D DP table uses 1-based indexing (where row 0 and column 0 represent empty prefixes), `dp[i][j]` corresponds to character `text1[i - 1]` and `text2[j - 1]`. Using `text1[i]` reads one character ahead and reads past the null terminator at `i = m`.",
        "intendedApproach": "Index strings as `text1[i - 1] == text2[j - 1]`.",
        "constraints": ["1 <= text1.length, text2.length <= 1000", "text1 and text2 consist of only lowercase English characters."],
        "visibleTestCases": [
            {"id": 1, "input": "text1 = \"abcde\", text2 = \"ace\"", "expectedOutput": "3", "isHidden": False},
            {"id": 2, "input": "text1 = \"abc\", text2 = \"abc\"", "expectedOutput": "3", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "text1 = \"abc\", text2 = \"def\"", "expectedOutput": "0", "isHidden": True},
            {"id": 4, "input": "text1 = \"bsbininm\", text2 = \"jmjkbkjkv\"", "expectedOutput": "1", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(M * N)", "space": "O(M * N)"},
        "tags": ["2ddp", "strings", "lcs", "c", "medium"]
    },

    # 3.4 2D DP - 0/1 Knapsack Problem (C++ - Medium)
    {
        "id": "q_2ddp_knapsack01",
        "title": "0/1 Knapsack Problem",
        "problemStatement": "Given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Each item can either be picked once (0/1) or not picked.",
        "language": "cpp",
        "topic": "2ddp",
        "subtopic": "knapsack-01",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int knapSack(int W, vector<int>& wt, vector<int>& val, int n) {\n        vector<int> dp(W + 1, 0);\n        \n        for (int i = 0; i < n; i++) {\n            for (int w = wt[i]; w <= W; w++) {\n                dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);\n            }\n        }\n        return dp[W];\n    }\n};",
        "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int knapSack(int W, vector<int>& wt, vector<int>& val, int n) {\n        vector<int> dp(W + 1, 0);\n        \n        for (int i = 0; i < n; i++) {\n            for (int w = W; w >= wt[i]; w--) {\n                dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);\n            }\n        }\n        return dp[W];\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Iterates capacity forwards from wt[i] to W in 1D DP, turning 0/1 knapsack into unbounded knapsack by reusing the same item multiple times.",
                "type": "boundary",
                "lineRange": "11"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "When space-optimizing 0/1 Knapsack to a 1D array, iterating capacity in increasing order (`w = wt[i]; w <= W`) overwrites `dp[w - wt[i]]` before higher capacities read it, allowing item `i` to be used repeatedly. Iterating in reverse (`w = W; w >= wt[i]; w--`) preserves the prior state.",
        "intendedApproach": "Iterate the inner loop backwards: `for (int w = W; w >= wt[i]; w--)`.",
        "constraints": ["1 <= N <= 1000", "1 <= W <= 1000", "1 <= wt[i] <= 1000", "1 <= val[i] <= 1000"],
        "visibleTestCases": [
            {"id": 1, "input": "W = 4, wt = [4, 5, 1], val = [1, 2, 3], n = 3", "expectedOutput": "3", "isHidden": False},
            {"id": 2, "input": "W = 3, wt = [1, 2, 3], val = [10, 15, 40], n = 3", "expectedOutput": "40", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "W = 5, wt = [2, 3], val = [10, 20], n = 2", "expectedOutput": "30", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N * W)", "space": "O(W)"},
        "tags": ["2ddp", "knapsack", "cpp", "medium"]
    },

    # 3.5 2D DP - Edit Distance (Java - Hard)
    {
        "id": "q_2ddp_edit_distance",
        "title": "Edit Distance (Levenshtein Distance)",
        "problemStatement": "Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.\nYou have the following three operations permitted on a word:\n- Insert a character\n- Delete a character\n- Replace a character",
        "language": "java",
        "topic": "2ddp",
        "subtopic": "matrix-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "buggyCode": "class Solution {\n    public int minDistance(String word1, String word2) {\n        int m = word1.length();\n        int n = word2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        \n        for (int i = 0; i <= m; i++) dp[i][0] = i;\n        for (int j = 0; j <= n; j++) dp[0][j] = j;\n        \n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {\n                    dp[i][j] = dp[i - 1][j - 1] + 1;\n                } else {\n                    dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], \n                                   Math.min(dp[i - 1][j], dp[i][j - 1]));\n                }\n            }\n        }\n        return dp[m][n];\n    }\n}",
        "correctCode": "class Solution {\n    public int minDistance(String word1, String word2) {\n        int m = word1.length();\n        int n = word2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        \n        for (int i = 0; i <= m; i++) dp[i][0] = i;\n        for (int j = 0; j <= n; j++) dp[0][j] = j;\n        \n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else {\n                    dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], \n                                   Math.min(dp[i - 1][j], dp[i][j - 1]));\n                }\n            }\n        }\n        return dp[m][n];\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Increments edit operations (+1) when characters are already identical instead of taking 0 cost dp[i-1][j-1].",
                "type": "incorrect state transition",
                "lineRange": "14"
            }
        ],
        "primaryBugType": "incorrect state transition",
        "explanation": "If `word1[i - 1] == word2[j - 1]`, no edit operation is required to match these characters, so the cost must carry forward unchanged from `dp[i - 1][j - 1]`. Adding 1 artificially inflates the distance for identical characters.",
        "intendedApproach": "Set `dp[i][j] = dp[i - 1][j - 1]` when characters match.",
        "constraints": ["0 <= word1.length, word2.length <= 500", "word1 and word2 consist of lowercase English letters."],
        "visibleTestCases": [
            {"id": 1, "input": "word1 = \"horse\", word2 = \"ros\"", "expectedOutput": "3", "isHidden": False},
            {"id": 2, "input": "word1 = \"intention\", word2 = \"execution\"", "expectedOutput": "5", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "word1 = \"\", word2 = \"a\"", "expectedOutput": "1", "isHidden": True},
            {"id": 4, "input": "word1 = \"abc\", word2 = \"abc\"", "expectedOutput": "0", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(M * N)", "space": "O(M * N)"},
        "tags": ["2ddp", "strings", "matrix-dp", "java", "hard"]
    },

    # 3.6 2D DP - Maximal Square (C++ - Medium)
    {
        "id": "q_2ddp_maximal_square",
        "title": "Maximal Square",
        "problemStatement": "Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.",
        "language": "cpp",
        "topic": "2ddp",
        "subtopic": "matrix-dp",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int maximalSquare(vector<vector<char>>& matrix) {\n        if (matrix.empty()) return 0;\n        int m = matrix.size(), n = matrix[0].size();\n        vector<vector<int>> dp(m, vector<int>(n, 0));\n        int maxSide = 0;\n        \n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (matrix[i][j] == '1') {\n                    if (i == 0 || j == 0) {\n                        dp[i][j] = 1;\n                    } else {\n                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1]);\n                    }\n                    maxSide = max(maxSide, dp[i][j]);\n                }\n            }\n        }\n        return maxSide;\n    }\n};",
        "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int maximalSquare(vector<vector<char>>& matrix) {\n        if (matrix.empty()) return 0;\n        int m = matrix.size(), n = matrix[0].size();\n        vector<vector<int>> dp(m, vector<int>(n, 0));\n        int maxSide = 0;\n        \n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (matrix[i][j] == '1') {\n                    if (i == 0 || j == 0) {\n                        dp[i][j] = 1;\n                    } else {\n                        dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});\n                    }\n                    maxSide = max(maxSide, dp[i][j]);\n                }\n            }\n        }\n        return maxSide * maxSide;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "DP state transition misses the top-left diagonal cell (dp[i-1][j-1]) and returns side length rather than area.",
                "type": "incorrect state transition",
                "lineRange": "19-24"
            }
        ],
        "primaryBugType": "incorrect state transition",
        "explanation": "To form a square of side k at `(i, j)`, the top `(i-1, j)`, left `(i, j-1)`, and diagonal `(i-1, j-1)` sub-squares must all be of side k-1. Additionally, the problem asks for total area (`maxSide * maxSide`), not edge length.",
        "intendedApproach": "Use `min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1` and return `maxSide * maxSide`.",
        "constraints": ["m == matrix.length", "n == matrix[i].length", "1 <= m, n <= 300", "matrix[i][j] is '0' or '1'."],
        "visibleTestCases": [
            {"id": 1, "input": "[[\"1\",\"0\",\"1\",\"0\",\"0\"],[\"1\",\"0\",\"1\",\"1\",\"1\"],[\"1\",\"1\",\"1\",\"1\",\"1\"],[\"1\",\"0\",\"0\",\"1\",\"0\"]", "expectedOutput": "4", "isHidden": False},
            {"id": 2, "input": "[[\"0\",\"1\"],[\"1\",\"0\"]]", "expectedOutput": "1", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[[\"0\"]]", "expectedOutput": "0", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(M * N)", "space": "O(M * N)"},
        "tags": ["2ddp", "matrix", "cpp", "medium"]
    },

    # 3.7 2D DP - Coin Change II (Java - Medium)
    {
        "id": "q_2ddp_coin_change_2",
        "title": "Coin Change II (Number of Combinations)",
        "problemStatement": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.\nReturn the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.",
        "language": "java",
        "topic": "2ddp",
        "subtopic": "unbounded-knapsack",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "class Solution {\n    public int change(int amount, int[] coins) {\n        int[] dp = new int[amount + 1];\n        dp[0] = 1;\n        \n        for (int i = 1; i <= amount; i++) {\n            for (int coin : coins) {\n                if (i >= coin) {\n                    dp[i] += dp[i - coin];\n                }\n            }\n        }\n        return dp[amount];\n    }\n}",
        "correctCode": "class Solution {\n    public int change(int amount, int[] coins) {\n        int[] dp = new int[amount + 1];\n        dp[0] = 1;\n        \n        for (int coin : coins) {\n            for (int i = coin; i <= amount; i++) {\n                dp[i] += dp[i - coin];\n            }\n        }\n        return dp[amount];\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Loops over amount in the outer loop and coins in the inner loop, calculating permutations (order matters) instead of distinct coin combinations.",
                "type": "boundary",
                "lineRange": "7-13"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "Iterating `amount` on the outer loop treats sequences with different orders as distinct results (e.g. [1, 2] and [2, 1] for sum 3). For combination counting, each coin type must be considered sequentially by placing `coins` in the outer loop.",
        "intendedApproach": "Place `for (int coin : coins)` in the outer loop and `for (int i = coin; i <= amount; i++)` in the inner loop.",
        "constraints": ["1 <= coins.length <= 300", "1 <= coins[i] <= 5000", "0 <= amount <= 5000"],
        "visibleTestCases": [
            {"id": 1, "input": "amount = 5, coins = [1,2,5]", "expectedOutput": "4", "isHidden": False},
            {"id": 2, "input": "amount = 3, coins = [2]", "expectedOutput": "0", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "amount = 10, coins = [10]", "expectedOutput": "1", "isHidden": True},
            {"id": 4, "input": "amount = 0, coins = [7]", "expectedOutput": "1", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N * amount)", "space": "O(amount)"},
        "tags": ["2ddp", "combinations", "unbounded-knapsack", "java", "medium"]
    },

    # 3.8 2D DP - Target Sum (C - Medium)
    {
        "id": "q_2ddp_target_sum",
        "title": "Target Sum Subsets",
        "problemStatement": "You are given an integer array nums and an integer target. Build an expression using '+' and '-' operators before each integer in nums such that the evaluated result equals target. Return the number of different expressions.",
        "language": "c",
        "topic": "2ddp",
        "subtopic": "subset-sum",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <stdlib.h>\n#include <string.h>\n\nint findTargetSumWays(int* nums, int numsSize, int target) {\n    int sum = 0;\n    for (int i = 0; i < numsSize; i++) sum += nums[i];\n    \n    // P - N = target and P + N = sum -> 2P = sum + target -> P = (sum + target) / 2\n    if ((sum + target) % 2 != 0) return 0;\n    \n    int s1 = (sum + target) / 2;\n    if (s1 < 0) return 0;\n    \n    int dp[2005] = {0};\n    dp[0] = 1;\n    \n    for (int i = 0; i < numsSize; i++) {\n        for (int j = s1; j >= nums[i]; j--) {\n            dp[j] += dp[j - nums[i]];\n        }\n    }\n    return dp[s1];\n}",
        "correctCode": "#include <stdlib.h>\n#include <string.h>\n\nint findTargetSumWays(int* nums, int numsSize, int target) {\n    int sum = 0;\n    for (int i = 0; i < numsSize; i++) sum += nums[i];\n    \n    if (abs(target) > sum || (sum + target) % 2 != 0) return 0;\n    \n    int s1 = (sum + target) / 2;\n    if (s1 < 0) return 0;\n    \n    int dp[2005] = {0};\n    dp[0] = 1;\n    \n    for (int i = 0; i < numsSize; i++) {\n        for (int j = s1; j >= nums[i]; j--) {\n            dp[j] += dp[j - nums[i]];\n        }\n    }\n    return dp[s1];\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Fails to check if abs(target) > sum, which causes incorrect subset evaluation on unreachable targets.",
                "type": "boundary",
                "lineRange": "10"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "If `abs(target) > sum`, it is impossible to achieve `target` even if all numbers are given the same sign. Failing to validate this condition early can cause invalid array indexing or erroneous modulo evaluation.",
        "intendedApproach": "Guard with `if (abs(target) > sum || (sum + target) % 2 != 0) return 0;`.",
        "constraints": ["1 <= nums.length <= 20", "0 <= nums[i] <= 1000", "0 <= sum(nums[i]) <= 1000", "-1000 <= target <= 1000"],
        "visibleTestCases": [
            {"id": 1, "input": "nums = [1,1,1,1,1], target = 3", "expectedOutput": "5", "isHidden": False},
            {"id": 2, "input": "nums = [1], target = 1", "expectedOutput": "1", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "nums = [1,2,1], target = 0", "expectedOutput": "2", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N * S)", "space": "O(S)"},
        "tags": ["2ddp", "subset-sum", "c", "medium"]
    },

    # =========================================================================
    # 4. ADVANCED DSA (8 Questions: C, C++, Java)
    # =========================================================================

    # 4.1 Adv DSA - Search in Rotated Sorted Array (C++ - Medium)
    {
        "id": "q_adv_search_rotated",
        "title": "Search in Rotated Sorted Array",
        "problemStatement": "There is an integer array nums sorted in ascending order (with distinct values) that is rotated at an unknown pivot index. Given the array nums and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.\nYou must write an algorithm with O(log n) runtime complexity.",
        "language": "cpp",
        "topic": "advanced-dsa",
        "subtopic": "binary-search",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        int low = 0, high = nums.size() - 1;\n        \n        while (low <= high) {\n            int mid = low + (high - low) / 2;\n            if (nums[mid] == target) return mid;\n            \n            if (nums[low] > nums[mid]) {\n                // Right half is sorted\n                if (nums[mid] < target && target <= nums[high]) {\n                    low = mid + 1;\n                } else {\n                    high = mid - 1;\n                }\n            } else {\n                // Left half is sorted\n                if (nums[low] <= target && target < nums[mid]) {\n                    high = mid - 1;\n                } else {\n                    low = mid + 1;\n                }\n            }\n        }\n        return -1;\n    }\n};",
        "correctCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int search(vector<int>& nums, int target) {\n        int low = 0, high = nums.size() - 1;\n        \n        while (low <= high) {\n            int mid = low + (high - low) / 2;\n            if (nums[mid] == target) return mid;\n            \n            if (nums[low] <= nums[mid]) {\n                // Left half is sorted\n                if (nums[low] <= target && target < nums[mid]) {\n                    high = mid - 1;\n                } else {\n                    low = mid + 1;\n                }\n            } else {\n                // Right half is sorted\n                if (nums[mid] < target && target <= nums[high]) {\n                    low = mid + 1;\n                } else {\n                    high = mid - 1;\n                }\n            }\n        }\n        return -1;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Uses inverted condition nums[low] > nums[mid] without handling equality low == mid, corrupting binary search partition branches.",
                "type": "boundary",
                "lineRange": "12"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "When `low == mid` (which happens whenever 2 elements remain), `nums[low] == nums[mid]` is true. Treating `nums[low] <= nums[mid]` as the left sorted condition properly includes single-element left halves.",
        "intendedApproach": "Check `if (nums[low] <= nums[mid])` to identify the sorted half.",
        "constraints": ["1 <= nums.length <= 5000", "-10^4 <= nums[i] <= 10^4", "All values of nums are unique.", "nums is an ascending array that is possibly rotated."],
        "visibleTestCases": [
            {"id": 1, "input": "nums = [4,5,6,7,0,1,2], target = 0", "expectedOutput": "4", "isHidden": False},
            {"id": 2, "input": "nums = [4,5,6,7,0,1,2], target = 3", "expectedOutput": "-1", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "nums = [1], target = 0", "expectedOutput": "-1", "isHidden": True},
            {"id": 4, "input": "nums = [3,1], target = 1", "expectedOutput": "1", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(log N)", "space": "O(1)"},
        "tags": ["advanced-dsa", "binary-search", "cpp", "medium"]
    },

    # 4.2 Adv DSA - Daily Temperatures (Monotonic Stack) (Java - Medium)
    {
        "id": "q_adv_daily_temperatures",
        "title": "Daily Temperatures (Monotonic Stack)",
        "problemStatement": "Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.",
        "language": "java",
        "topic": "advanced-dsa",
        "subtopic": "monotonic-stack",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "import java.util.*;\n\nclass Solution {\n    public int[] dailyTemperatures(int[] temperatures) {\n        int n = temperatures.length;\n        int[] answer = new int[n];\n        Stack<Integer> stack = new Stack<>();\n        \n        for (int i = 0; i < n; i++) {\n            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {\n                int prevIndex = stack.pop();\n                answer[prevIndex] = i - prevIndex;\n            }\n            stack.push(temperatures[i]); // Pushes temperature value instead of index i\n        }\n        return answer;\n    }\n}",
        "correctCode": "import java.util.*;\n\nclass Solution {\n    public int[] dailyTemperatures(int[] temperatures) {\n        int n = temperatures.length;\n        int[] answer = new int[n];\n        Stack<Integer> stack = new Stack<>();\n        \n        for (int i = 0; i < n; i++) {\n            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {\n                int prevIndex = stack.pop();\n                answer[prevIndex] = i - prevIndex;\n            }\n            stack.push(i);\n        }\n        return answer;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Pushes the temperature value (temperatures[i]) into the stack instead of index (i), causing ArrayIndexOutOfBoundsException when popping.",
                "type": "incorrect data structure usage",
                "lineRange": "15"
            }
        ],
        "primaryBugType": "incorrect data structure usage",
        "explanation": "To compute day intervals `i - prevIndex`, the stack must store the indices of previous days. Pushing the raw temperature value causes `temperatures[stack.peek()]` to use temperatures as array indices, throwing out-of-bounds errors or computing incorrect day differences.",
        "intendedApproach": "Push index `i` onto the monotonic stack: `stack.push(i)`.",
        "constraints": ["1 <= temperatures.length <= 10^5", "30 <= temperatures[i] <= 100"],
        "visibleTestCases": [
            {"id": 1, "input": "[73,74,75,71,69,72,76,73]", "expectedOutput": "[1,1,4,2,1,1,0,0]", "isHidden": False},
            {"id": 2, "input": "[30,40,50,60]", "expectedOutput": "[1,1,1,0]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[30,60,90]", "expectedOutput": "[1,1,0]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(N)"},
        "tags": ["advanced-dsa", "stack", "monotonic-stack", "java", "medium"]
    },

    # 4.3 Adv DSA - Sliding Window Maximum (C++ - Hard)
    {
        "id": "q_adv_sliding_window_max",
        "title": "Sliding Window Maximum",
        "problemStatement": "You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.\nReturn the max sliding window.",
        "language": "cpp",
        "topic": "advanced-dsa",
        "subtopic": "sliding-window",
        "difficulty": "hard",
        "estimatedTime": 25,
        "buggyCode": "#include <vector>\n#include <deque>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> maxSlidingWindow(vector<int>& nums, int k) {\n        deque<int> dq; // stores indices\n        vector<int> result;\n        \n        for (int i = 0; i < nums.size(); i++) {\n            \n            while (!dq.empty() && nums[dq.back()] < nums[i]) {\n                dq.pop_back();\n            }\n            dq.push_back(i);\n            \n            if (i >= k - 1) {\n                result.push_back(nums[dq.front()]);\n            }\n        }\n        return result;\n    }\n};",
        "correctCode": "#include <vector>\n#include <deque>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> maxSlidingWindow(vector<int>& nums, int k) {\n        deque<int> dq;\n        vector<int> result;\n        \n        for (int i = 0; i < nums.size(); i++) {\n            if (!dq.empty() && dq.front() <= i - k) {\n                dq.pop_front();\n            }\n            \n            while (!dq.empty() && nums[dq.back()] < nums[i]) {\n                dq.pop_back();\n            }\n            dq.push_back(i);\n            \n            if (i >= k - 1) {\n                result.push_back(nums[dq.front()]);\n            }\n        }\n        return result;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Omits window boundary check `if (!dq.empty() && dq.front() <= i - k) dq.pop_front()`, retaining expired out-of-window maximums.",
                "type": "boundary",
                "lineRange": "12"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "A monotonic deque for sliding window maximum must maintain two properties: strictly decreasing values and indices within `[i - k + 1, i]`. Without removing elements that slide out of the window (`dq.front() <= i - k`), old elements persist at `dq.front()`.",
        "intendedApproach": "Add `if (!dq.empty() && dq.front() <= i - k) dq.pop_front();` at the beginning of each iteration.",
        "constraints": ["1 <= nums.length <= 10^5", "-10^4 <= nums[i] <= 10^4", "1 <= k <= nums.length"],
        "visibleTestCases": [
            {"id": 1, "input": "nums = [1,3,-1,-3,5,3,6,7], k = 3", "expectedOutput": "[3,3,5,5,6,7]", "isHidden": False},
            {"id": 2, "input": "nums = [1], k = 1", "expectedOutput": "[1]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "nums = [7,2,4], k = 2", "expectedOutput": "[7,4]", "isHidden": True},
            {"id": 4, "input": "nums = [1,-1], k = 1", "expectedOutput": "[1,-1]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(k)"},
        "tags": ["advanced-dsa", "sliding-window", "deque", "cpp", "hard"]
    },

    # 4.4 Adv DSA - Top K Frequent Elements (Min Heap) (Java - Medium)
    {
        "id": "q_adv_top_k_frequent",
        "title": "Top K Frequent Elements (Min-Heap)",
        "problemStatement": "Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.",
        "language": "java",
        "topic": "advanced-dsa",
        "subtopic": "heap",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "import java.util.*;\n\nclass Solution {\n    public int[] topKFrequent(int[] nums, int k) {\n        Map<Integer, Integer> countMap = new HashMap<>();\n        for (int n : nums) {\n            countMap.put(n, countMap.getOrDefault(n, 0) + 1);\n        }\n        \n        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> countMap.get(b) - countMap.get(a));\n        \n        for (int key : countMap.keySet()) {\n            heap.add(key);\n            if (heap.size() > k) {\n                heap.poll();\n            }\n        }\n        \n        int[] result = new int[k];\n        for (int i = 0; i < k; i++) {\n            result[i] = heap.poll();\n        }\n        return result;\n    }\n}",
        "correctCode": "import java.util.*;\n\nclass Solution {\n    public int[] topKFrequent(int[] nums, int k) {\n        Map<Integer, Integer> countMap = new HashMap<>();\n        for (int n : nums) {\n            countMap.put(n, countMap.getOrDefault(n, 0) + 1);\n        }\n        \n        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> countMap.get(a) - countMap.get(b));\n        \n        for (int key : countMap.keySet()) {\n            heap.add(key);\n            if (heap.size() > k) {\n                heap.poll();\n            }\n        }\n        \n        int[] result = new int[k];\n        for (int i = 0; i < k; i++) {\n            result[i] = heap.poll();\n        }\n        return result;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Comparator order is reversed to descending, creating a Max-Heap that evicts the most frequent element whenever heap size exceeds k.",
                "type": "incorrect data structure usage",
                "lineRange": "11"
            }
        ],
        "primaryBugType": "incorrect data structure usage",
        "explanation": "To keep the top K largest elements using a size-K heap, we must maintain a Min-Heap (`a.count - b.count`). A Min-Heap discards the lowest frequency element when `heap.size() > k`. Using a Max-Heap comparator discards the highest frequency elements instead.",
        "intendedApproach": "Order ascending in the comparator: `(a, b) -> countMap.get(a) - countMap.get(b)`.",
        "constraints": ["1 <= nums.length <= 10^5", "-10^4 <= nums[i] <= 10^4", "k is in the range [1, the number of unique elements in the array]."],
        "visibleTestCases": [
            {"id": 1, "input": "nums = [1,1,1,2,2,3], k = 2", "expectedOutput": "[1,2]", "isHidden": False},
            {"id": 2, "input": "nums = [1], k = 1", "expectedOutput": "[1]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "nums = [4,1,-1,2,-1,2,3], k = 2", "expectedOutput": "[-1,2]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N log k)", "space": "O(N + k)"},
        "tags": ["advanced-dsa", "heap", "hash-table", "java", "medium"]
    },

    # 4.5 Adv DSA - Subarray Sum Equals K (Prefix Sum Hash) (C++ - Medium)
    {
        "id": "q_adv_subarray_sum_k",
        "title": "Subarray Sum Equals K",
        "problemStatement": "Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.\nA subarray is a contiguous non-empty sequence of elements within an array.",
        "language": "cpp",
        "topic": "advanced-dsa",
        "subtopic": "prefix-sum",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nclass Solution {\npublic:\n    int subarraySum(vector<int>& nums, int k) {\n        unordered_map<int, int> prefixMap;\n        int sum = 0;\n        int count = 0;\n        \n        for (int num : nums) {\n            sum += num;\n            if (prefixMap.find(sum - k) != prefixMap.end()) {\n                count += prefixMap[sum - k];\n            }\n            prefixMap[sum]++;\n        }\n        return count;\n    }\n};",
        "correctCode": "#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nclass Solution {\npublic:\n    int subarraySum(vector<int>& nums, int k) {\n        unordered_map<int, int> prefixMap;\n        prefixMap[0] = 1;\n        int sum = 0;\n        int count = 0;\n        \n        for (int num : nums) {\n            sum += num;\n            if (prefixMap.find(sum - k) != prefixMap.end()) {\n                count += prefixMap[sum - k];\n            }\n            prefixMap[sum]++;\n        }\n        return count;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Fails to initialize prefixMap[0] = 1, omitting subarrays whose sum equals k directly from index 0.",
                "type": "incorrect initialization",
                "lineRange": "8"
            }
        ],
        "primaryBugType": "incorrect initialization",
        "explanation": "If a prefix sum `sum` equals `k` exactly, `sum - k` is 0. If `prefixMap[0] = 1` is not preset to represent an empty prefix, any valid subarray starting at index 0 will not be counted.",
        "intendedApproach": "Initialize `prefixMap[0] = 1` before beginning the loop.",
        "constraints": ["1 <= nums.length <= 2 * 10^4", "-1000 <= nums[i] <= 1000", "-10^7 <= k <= 10^7"],
        "visibleTestCases": [
            {"id": 1, "input": "nums = [1,1,1], k = 2", "expectedOutput": "2", "isHidden": False},
            {"id": 2, "input": "nums = [1,2,3], k = 3", "expectedOutput": "2", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "nums = [3], k = 3", "expectedOutput": "1", "isHidden": True},
            {"id": 4, "input": "nums = [-1,-1,1], k = 0", "expectedOutput": "1", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N)", "space": "O(N)"},
        "tags": ["advanced-dsa", "prefix-sum", "hash-table", "cpp", "medium"]
    },

    # 4.6 Adv DSA - Merge Overlapping Intervals (C - Medium)
    {
        "id": "q_adv_merge_intervals",
        "title": "Merge Overlapping Intervals",
        "problemStatement": "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.",
        "language": "c",
        "topic": "advanced-dsa",
        "subtopic": "intervals-sorting",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "#include <stdlib.h>\n\nint compare(const void* a, const void* b) {\n    int* intA = *(int**)a;\n    int* intB = *(int**)b;\n    return intA[0] - intB[0];\n}\n\nint** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes) {\n    if (intervalsSize <= 0) {\n        *returnSize = 0;\n        return NULL;\n    }\n    \n    qsort(intervals, intervalsSize, sizeof(int*), compare);\n    \n    int** result = (int**)malloc(intervalsSize * sizeof(int*));\n    *returnColumnSizes = (int*)malloc(intervalsSize * sizeof(int));\n    int count = 0;\n    \n    result[0] = (int*)malloc(2 * sizeof(int));\n    result[0][0] = intervals[0][0];\n    result[0][1] = intervals[0][1];\n    (*returnColumnSizes)[0] = 2;\n    count = 1;\n    \n    for (int i = 1; i < intervalsSize; i++) {\n        if (intervals[i][0] <= result[count - 1][1]) {\n            result[count - 1][1] = intervals[i][1];\n        } else {\n            result[count] = (int*)malloc(2 * sizeof(int));\n            result[count][0] = intervals[i][0];\n            result[count][1] = intervals[i][1];\n            (*returnColumnSizes)[count] = 2;\n            count++;\n        }\n    }\n    \n    *returnSize = count;\n    return result;\n}",
        "correctCode": "#include <stdlib.h>\n\nint compare(const void* a, const void* b) {\n    int* intA = *(int**)a;\n    int* intB = *(int**)b;\n    return intA[0] - intB[0];\n}\n\nint** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes) {\n    if (intervalsSize <= 0) {\n        *returnSize = 0;\n        return NULL;\n    }\n    \n    qsort(intervals, intervalsSize, sizeof(int*), compare);\n    \n    int** result = (int**)malloc(intervalsSize * sizeof(int*));\n    *returnColumnSizes = (int*)malloc(intervalsSize * sizeof(int));\n    int count = 0;\n    \n    result[0] = (int*)malloc(2 * sizeof(int));\n    result[0][0] = intervals[0][0];\n    result[0][1] = intervals[0][1];\n    (*returnColumnSizes)[0] = 2;\n    count = 1;\n    \n    for (int i = 1; i < intervalsSize; i++) {\n        if (intervals[i][0] <= result[count - 1][1]) {\n            if (intervals[i][1] > result[count - 1][1]) {\n                result[count - 1][1] = intervals[i][1];\n            }\n        } else {\n            result[count] = (int*)malloc(2 * sizeof(int));\n            result[count][0] = intervals[i][0];\n            result[count][1] = intervals[i][1];\n            (*returnColumnSizes)[count] = 2;\n            count++;\n        }\n    }\n    \n    *returnSize = count;\n    return result;\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Overwrites interval end with intervals[i][1] without checking if previous end was larger (missing max operation when an interval completely encloses the next).",
                "type": "boundary",
                "lineRange": "29"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "If an interval completely encloses the subsequent interval (e.g. `[1, 5]` and `[2, 3]`), simply assigning `result[count - 1][1] = 3` incorrectly shortens the merged interval from 5 down to 3.",
        "intendedApproach": "Update end boundary using `max(result[count - 1][1], intervals[i][1])`.",
        "constraints": ["1 <= intervals.length <= 10^4", "intervals[i].length == 2", "0 <= starti <= endi <= 10^4"],
        "visibleTestCases": [
            {"id": 1, "input": "[[1,3],[2,6],[8,10],[15,18]]", "expectedOutput": "[[1,6],[8,10],[15,18]]", "isHidden": False},
            {"id": 2, "input": "[[1,4],[4,5]]", "expectedOutput": "[[1,5]]", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "[[1,4],[2,3]]", "expectedOutput": "[[1,4]]", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N log N)", "space": "O(N)"},
        "tags": ["advanced-dsa", "sorting", "intervals", "c", "medium"]
    },

    # 4.7 Adv DSA - Word Search (Backtracking) (Java - Medium)
    {
        "id": "q_adv_word_search",
        "title": "Word Search (Backtracking)",
        "problemStatement": "Given an m x n grid of characters board and a string word, return true if word exists in the grid.\nThe word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.",
        "language": "java",
        "topic": "advanced-dsa",
        "subtopic": "backtracking",
        "difficulty": "medium",
        "estimatedTime": 20,
        "buggyCode": "class Solution {\n    private boolean dfs(char[][] board, String word, int r, int c, int index) {\n        if (index == word.length()) return true;\n        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(index)) {\n            return false;\n        }\n        \n        char temp = board[r][c];\n        board[r][c] = '#'; // mark visited\n        \n        boolean found = dfs(board, word, r + 1, c, index + 1) ||\n                        dfs(board, word, r - 1, c, index + 1) ||\n                        dfs(board, word, r, c + 1, index + 1) ||\n                        dfs(board, word, r, c - 1, index + 1);\n                        \n        return found;\n    }\n    \n    public boolean exist(char[][] board, String word) {\n        int m = board.length, n = board[0].length;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (dfs(board, word, i, j, 0)) return true;\n            }\n        }\n        return false;\n    }\n}",
        "correctCode": "class Solution {\n    private boolean dfs(char[][] board, String word, int r, int c, int index) {\n        if (index == word.length()) return true;\n        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(index)) {\n            return false;\n        }\n        \n        char temp = board[r][c];\n        board[r][c] = '#';\n        \n        boolean found = dfs(board, word, r + 1, c, index + 1) ||\n                        dfs(board, word, r - 1, c, index + 1) ||\n                        dfs(board, word, r, c + 1, index + 1) ||\n                        dfs(board, word, r, c - 1, index + 1);\n                        \n        board[r][c] = temp;\n        return found;\n    }\n    \n    public boolean exist(char[][] board, String word) {\n        int m = board.length, n = board[0].length;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (dfs(board, word, i, j, 0)) return true;\n            }\n        }\n        return false;\n    }\n}",
        "bugList": [
            {
                "id": 1,
                "description": "Fails to revert board[r][c] back from '#' when unwinding the recursion stack, permanently destroying board state for subsequent searches.",
                "type": "incorrect traversal",
                "lineRange": "16"
            }
        ],
        "primaryBugType": "incorrect traversal",
        "explanation": "Backtracking algorithms require cleaning up state modifications upon exiting a search branch. Leaving cells permanently marked as `#` prevents other candidate search paths from visiting those letters.",
        "intendedApproach": "Restore `board[r][c] = temp;` before returning `found`.",
        "constraints": ["m == board.length", "n = board[i].length", "1 <= m, n <= 6", "1 <= word.length <= 15", "board and word consist of only lowercase and uppercase English letters."],
        "visibleTestCases": [
            {"id": 1, "input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCCED\"", "expectedOutput": "true", "isHidden": False},
            {"id": 2, "input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"SEE\"", "expectedOutput": "true", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCB\"", "expectedOutput": "false", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(N * 3^L)", "space": "O(L)"},
        "tags": ["advanced-dsa", "backtracking", "matrix", "java", "medium"]
    },

    # 4.8 Adv DSA - Median of Two Sorted Arrays (Binary Search) (C++ - Hard)
    {
        "id": "q_adv_median_two_sorted",
        "title": "Median of Two Sorted Arrays",
        "problemStatement": "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.\nThe overall run time complexity should be O(log (m+n)).",
        "language": "cpp",
        "topic": "advanced-dsa",
        "subtopic": "binary-search",
        "difficulty": "hard",
        "estimatedTime": 25,
        "buggyCode": "#include <vector>\n#include <algorithm>\n#include <climits>\nusing namespace std;\n\nclass Solution {\npublic:\n    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {\n        int m = nums1.size(), n = nums2.size();\n        int low = 0, high = m;\n        \n        while (low <= high) {\n            int i = (low + high) / 2;\n            int j = (m + n + 1) / 2 - i;\n            \n            int maxLeft1 = (i == 0) ? INT_MIN : nums1[i - 1];\n            int minRight1 = (i == m) ? INT_MAX : nums1[i];\n            \n            int maxLeft2 = (j == 0) ? INT_MIN : nums2[j - 1];\n            int minRight2 = (j == n) ? INT_MAX : nums2[j];\n            \n            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {\n                if ((m + n) % 2 == 0) {\n                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;\n                } else {\n                    return max(maxLeft1, maxLeft2);\n                }\n            } else if (maxLeft1 > minRight2) {\n                high = i - 1;\n            } else {\n                low = i + 1;\n            }\n        }\n        return 0.0;\n    }\n};",
        "correctCode": "#include <vector>\n#include <algorithm>\n#include <climits>\nusing namespace std;\n\nclass Solution {\npublic:\n    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {\n        if (nums1.size() > nums2.size()) {\n            return findMedianSortedArrays(nums2, nums1);\n        }\n        \n        int m = nums1.size(), n = nums2.size();\n        int low = 0, high = m;\n        \n        while (low <= high) {\n            int i = (low + high) / 2;\n            int j = (m + n + 1) / 2 - i;\n            \n            int maxLeft1 = (i == 0) ? INT_MIN : nums1[i - 1];\n            int minRight1 = (i == m) ? INT_MAX : nums1[i];\n            \n            int maxLeft2 = (j == 0) ? INT_MIN : nums2[j - 1];\n            int minRight2 = (j == n) ? INT_MAX : nums2[j];\n            \n            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {\n                if ((m + n) % 2 == 0) {\n                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;\n                } else {\n                    return max(maxLeft1, maxLeft2);\n                }\n            } else if (maxLeft1 > minRight2) {\n                high = i - 1;\n            } else {\n                low = i + 1;\n            }\n        }\n        return 0.0;\n    }\n};",
        "bugList": [
            {
                "id": 1,
                "description": "Fails to ensure binary search runs on the smaller array (m <= n), causing j = (m + n + 1)/2 - i to become negative or out of bounds.",
                "type": "boundary",
                "lineRange": "8"
            }
        ],
        "primaryBugType": "boundary",
        "explanation": "In partition binary search for median of two sorted arrays, `j = (m + n + 1) / 2 - i` can become negative if `m > n` and `i` is near `m`. The binary search must always be performed on the shorter array by swapping `nums1` and `nums2` if `nums1.size() > nums2.size()`.",
        "intendedApproach": "Add `if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);` at the entry point.",
        "constraints": ["nums1.length == m", "nums2.length == n", "0 <= m <= 1000", "0 <= n <= 1000", "1 <= m + n <= 2000", "-10^6 <= nums1[i], nums2[i] <= 10^6"],
        "visibleTestCases": [
            {"id": 1, "input": "nums1 = [1,3], nums2 = [2]", "expectedOutput": "2.0", "isHidden": False},
            {"id": 2, "input": "nums1 = [1,2], nums2 = [3,4]", "expectedOutput": "2.5", "isHidden": False}
        ],
        "hiddenTestCases": [
            {"id": 3, "input": "nums1 = [], nums2 = [1]", "expectedOutput": "1.0", "isHidden": True},
            {"id": 4, "input": "nums1 = [2], nums2 = []", "expectedOutput": "2.0", "isHidden": True}
        ],
        "expectedComplexity": {"time": "O(log(min(M, N)))", "space": "O(1)"},
        "tags": ["advanced-dsa", "binary-search", "cpp", "hard"]
    }
]

# Write to questions.json
data_dir = os.path.dirname(__file__)
out_file = os.path.join(data_dir, 'questions.json')
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f"Successfully generated {len(questions)} high quality questions in {out_file}")
