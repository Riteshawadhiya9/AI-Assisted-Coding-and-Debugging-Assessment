# 2D Dynamic Programming & Matrix DP Problems (6 Questions: C, C++, Java)

DP2D_QUESTIONS = [
    {
        "id": "q_2ddp_unique_paths",
        "title": "Unique Paths in Grid",
        "problemStatement": "There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.\n\nGiven the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.\n\nThe test cases are generated so that the answer will be less than or equal to `2 * 10^9`.",
        "topic": "2ddp",
        "subtopic": "matrix-dp",
        "difficulty": "medium",
        "estimatedTime": 15,
        "primaryBugType": "incorrect initialization",
        "bugConcept": "Initializing first row and column to 0 instead of 1, propagating 0 throughout the entire grid",
        "intendedApproach": "Initialize first row dp[0][c] = 1 and first col dp[r][0] = 1 because there is exactly 1 way to travel purely straight. For r in 1..m-1, c in 1..n-1: dp[r][c] = dp[r-1][c] + dp[r][c-1].",
        "explanation": "Moving along the top boundary or leftmost column has only 1 choice (all right or all down). Initializing them to 0 causes every addition `dp[r-1][c] + dp[r][c-1]` to sum zeros.",
        "constraints": [
            "1 <= m, n <= 100",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "m = 3, n = 7",
                "expectedOutput": "28",
                "isHidden": False,
                "explanation": "There are 28 unique paths from top-left to bottom-right in a 3x7 grid.",
            },
            {
                "id": 2,
                "input": "m = 3, n = 2",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "From the top-left corner, there are a total of 3 ways to reach the bottom-right corner: 1. Right -> Down -> Down, 2. Down -> Down -> Right, 3. Down -> Right -> Down.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "m = 1, n = 1",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "m = 7, n = 3",
                "expectedOutput": "28",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "m = 3, n = 3",
                "expectedOutput": "6",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(M * N)",
        },
        "tags": [
            "2ddp",
            "matrix-dp",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Grid Path Combinations: 3x3",
            "data": [
                [
                    1,
                    1,
                    1,
                ],
                [
                    1,
                    2,
                    3,
                ],
                [
                    1,
                    3,
                    6,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "int uniquePaths(int m, int n) {\n    int dp[105][105] = {0};\n    dp[0][0] = 1;\n    for (int r = 1; r < m; r++) {\n        for (int c = 1; c < n; c++) {\n            dp[r][c] = dp[r - 1][c] + dp[r][c - 1];\n        }\n    }\n    return dp[m - 1][n - 1];\n}",
                "correctCode": "int uniquePaths(int m, int n) {\n    int dp[105][105] = {0};\n    for (int r = 0; r < m; r++) dp[r][0] = 1;\n    for (int c = 0; c < n; c++) dp[0][c] = 1;\n    for (int r = 1; r < m; r++) {\n        for (int c = 1; c < n; c++) {\n            dp[r][c] = dp[r - 1][c] + dp[r][c - 1];\n        }\n    }\n    return dp[m - 1][n - 1];\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nint uniquePaths(int m, int n) {\n    vector<vector<int>> dp(m, vector<int>(n, 0));\n    dp[0][0] = 1;\n    for (int r = 1; r < m; r++) {\n        for (int c = 1; c < n; c++) {\n            dp[r][c] = dp[r - 1][c] + dp[r][c - 1];\n        }\n    }\n    return dp[m - 1][n - 1];\n}",
                "correctCode": "#include <vector>\nusing namespace std;\n\nint uniquePaths(int m, int n) {\n    vector<vector<int>> dp(m, vector<int>(n, 1));\n    for (int r = 1; r < m; r++) {\n        for (int c = 1; c < n; c++) {\n            dp[r][c] = dp[r - 1][c] + dp[r][c - 1];\n        }\n    }\n    return dp[m - 1][n - 1];\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int uniquePaths(int m, int n) {\n        int[][] dp = new int[m][n];\n        dp[0][0] = 1;\n        for (int r = 1; r < m; r++) {\n            for (int c = 1; c < n; c++) {\n                dp[r][c] = dp[r - 1][c] + dp[r][c - 1];\n            }\n        }\n        return dp[m - 1][n - 1];\n    }\n}",
                "correctCode": "class Solution {\n    public int uniquePaths(int m, int n) {\n        int[][] dp = new int[m][n];\n        for (int r = 0; r < m; r++) dp[r][0] = 1;\n        for (int c = 0; c < n; c++) dp[0][c] = 1;\n        for (int r = 1; r < m; r++) {\n            for (int c = 1; c < n; c++) {\n                dp[r][c] = dp[r - 1][c] + dp[r][c - 1];\n            }\n        }\n        return dp[m - 1][n - 1];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_min_path_sum",
        "title": "Minimum Path Sum in Grid",
        "problemStatement": "Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.\n\nNote: You can only move either down or right at any point in time.",
        "topic": "2ddp",
        "subtopic": "matrix-dp",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "boundary",
        "bugConcept": "Incorrect accumulation of first row and column boundary costs (setting dp[r][0] = grid[r][0] instead of cumulative sum)",
        "intendedApproach": "Initialize dp[0][0] = grid[0][0]. Top row: dp[0][c] = dp[0][c-1] + grid[0][c]. Left col: dp[r][0] = dp[r-1][0] + grid[r][0]. Rest: dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c].",
        "explanation": "Along the first column, path sum must accumulate every cell from above. Setting `dp[r][0] = grid[r][0]` ignores previously accrued path costs from top cells.",
        "constraints": [
            "m == grid.length",
            "n == grid[i].length",
            "1 <= m, n <= 200",
            "0 <= grid[i][j] <= 200",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "grid = [[1,3,1],[1,5,1],[4,2,1]]",
                "expectedOutput": "7",
                "isHidden": False,
                "explanation": "Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum to 7.",
            },
            {
                "id": 2,
                "input": "grid = [[1,2,3],[4,5,6]]",
                "expectedOutput": "12",
                "isHidden": False,
                "explanation": "The path 1 -> 2 -> 3 -> 6 gives minimum sum 12.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "grid = [[5]]",
                "expectedOutput": "5",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "grid = [[1,2],[1,1]]",
                "expectedOutput": "3",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "grid = [[1,2,5],[3,2,1]]",
                "expectedOutput": "6",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(1) if in-place",
        },
        "tags": [
            "2ddp",
            "matrix-dp",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Grid Cell Weights",
            "data": [
                [
                    1,
                    3,
                    1,
                ],
                [
                    1,
                    5,
                    1,
                ],
                [
                    4,
                    2,
                    1,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "int minPathSum(int grid[200][200], int m, int n) {\n    int dp[200][200];\n    dp[0][0] = grid[0][0];\n    for (int c = 1; c < n; c++) dp[0][c] = grid[0][c];\n    for (int r = 1; r < m; r++) dp[r][0] = grid[r][0];\n    for (int r = 1; r < m; r++) {\n        for (int c = 1; c < n; c++) {\n            int minPrev = (dp[r - 1][c] < dp[r][c - 1]) ? dp[r - 1][c] : dp[r][c - 1];\n            dp[r][c] = minPrev + grid[r][c];\n        }\n    }\n    return dp[m - 1][n - 1];\n}",
                "correctCode": "int minPathSum(int grid[200][200], int m, int n) {\n    int dp[200][200];\n    dp[0][0] = grid[0][0];\n    for (int c = 1; c < n; c++) dp[0][c] = dp[0][c - 1] + grid[0][c];\n    for (int r = 1; r < m; r++) dp[r][0] = dp[r - 1][0] + grid[r][0];\n    for (int r = 1; r < m; r++) {\n        for (int c = 1; c < n; c++) {\n            int minPrev = (dp[r - 1][c] < dp[r][c - 1]) ? dp[r - 1][c] : dp[r][c - 1];\n            dp[r][c] = minPrev + grid[r][c];\n        }\n    }\n    return dp[m - 1][n - 1];\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint minPathSum(vector<vector<int>>& grid) {\n    int m = grid.size(), n = grid[0].size();\n    vector<vector<int>> dp(m, vector<int>(n, 0));\n    dp[0][0] = grid[0][0];\n    for (int c = 1; c < n; c++) dp[0][c] = grid[0][c];\n    for (int r = 1; r < m; r++) dp[r][0] = grid[r][0];\n    for (int r = 1; r < m; r++) {\n        for (int c = 1; c < n; c++) {\n            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c];\n        }\n    }\n    return dp[m - 1][n - 1];\n}",
                "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint minPathSum(vector<vector<int>>& grid) {\n    int m = grid.size(), n = grid[0].size();\n    vector<vector<int>> dp(m, vector<int>(n, 0));\n    dp[0][0] = grid[0][0];\n    for (int c = 1; c < n; c++) dp[0][c] = dp[0][c - 1] + grid[0][c];\n    for (int r = 1; r < m; r++) dp[r][0] = dp[r - 1][0] + grid[r][0];\n    for (int r = 1; r < m; r++) {\n        for (int c = 1; c < n; c++) {\n            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c];\n        }\n    }\n    return dp[m - 1][n - 1];\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int minPathSum(int[][] grid) {\n        int m = grid.length, n = grid[0].length;\n        int[][] dp = new int[m][n];\n        dp[0][0] = grid[0][0];\n        for (int c = 1; c < n; c++) dp[0][c] = grid[0][c];\n        for (int r = 1; r < m; r++) dp[r][0] = grid[r][0];\n        for (int r = 1; r < m; r++) {\n            for (int c = 1; c < n; c++) {\n                dp[r][c] = Math.min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c];\n            }\n        }\n        return dp[m - 1][n - 1];\n    }\n}",
                "correctCode": "class Solution {\n    public int minPathSum(int[][] grid) {\n        int m = grid.length, n = grid[0].length;\n        int[][] dp = new int[m][n];\n        dp[0][0] = grid[0][0];\n        for (int c = 1; c < n; c++) dp[0][c] = dp[0][c - 1] + grid[0][c];\n        for (int r = 1; r < m; r++) dp[r][0] = dp[r - 1][0] + grid[r][0];\n        for (int r = 1; r < m; r++) {\n            for (int c = 1; c < n; c++) {\n                dp[r][c] = Math.min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c];\n            }\n        }\n        return dp[m - 1][n - 1];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_lcs",
        "title": "Longest Common Subsequence (LCS)",
        "problemStatement": "Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.\n\nA subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.\n\nA common subsequence of two strings is a subsequence that is common to both strings.",
        "topic": "2ddp",
        "subtopic": "lcs",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Off-by-one 0-indexed string character alignment against 1-indexed DP matrix table (comparing text1[i] == text2[j] instead of text1[i-1] == text2[j-1])",
        "intendedApproach": "Use 2D table dp[m+1][n+1]. For i in 1..m and j in 1..n: if text1[i-1] == text2[j-1] dp[i][j] = 1 + dp[i-1][j-1]; else dp[i][j] = max(dp[i-1][j], dp[i][j-1]).",
        "explanation": "In 1-indexed DP array `dp[i][j]`, `dp[i]` corresponds to prefix of length `i`, whose last character is located at `text1[i-1]`. Using `text1[i]` causes array out of bounds and misaligned comparisons.",
        "constraints": [
            "1 <= text1.length, text2.length <= 1000",
            "text1 and text2 consist of only lowercase English characters.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "text1 = \"abcde\", text2 = \"ace\"",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "The longest common subsequence is \"ace\" and its length is 3.",
            },
            {
                "id": 2,
                "input": "text1 = \"abc\", text2 = \"abc\"",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "The longest common subsequence is \"abc\" and its length is 3.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "text1 = \"abc\", text2 = \"def\"",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "text1 = \"oxcp\", text2 = \"pomc\"",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "text1 = \"ezupkr\", text2 = \"ubmrapg\"",
                "expectedOutput": "2",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(M * N)",
        },
        "tags": [
            "2ddp",
            "lcs",
            "strings",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "LCS DP Table Alignment",
            "data": [
                [
                    0,
                    0,
                    0,
                    0,
                ],
                [
                    0,
                    1,
                    1,
                    1,
                ],
                [
                    0,
                    1,
                    1,
                    1,
                ],
                [
                    0,
                    1,
                    2,
                    2,
                ],
                [
                    0,
                    1,
                    2,
                    2,
                ],
                [
                    0,
                    1,
                    2,
                    3,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <string.h>\n#include <stdlib.h>\n\nint longestCommonSubsequence(char* text1, char* text2) {\n    int m = strlen(text1), n = strlen(text2);\n    int dp[1005][1005] = {0};\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (text1[i] == text2[j]) {\n                dp[i][j] = 1 + dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = (dp[i - 1][j] > dp[i][j - 1]) ? dp[i - 1][j] : dp[i][j - 1];\n            }\n        }\n    }\n    return dp[m][n];\n}",
                "correctCode": "#include <string.h>\n#include <stdlib.h>\n\nint longestCommonSubsequence(char* text1, char* text2) {\n    int m = strlen(text1), n = strlen(text2);\n    int dp[1005][1005] = {0};\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (text1[i - 1] == text2[j - 1]) {\n                dp[i][j] = 1 + dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = (dp[i - 1][j] > dp[i][j - 1]) ? dp[i - 1][j] : dp[i][j - 1];\n            }\n        }\n    }\n    return dp[m][n];\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint longestCommonSubsequence(string text1, string text2) {\n    int m = text1.size(), n = text2.size();\n    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (text1[i] == text2[j]) {\n                dp[i][j] = 1 + dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[m][n];\n}",
                "correctCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint longestCommonSubsequence(string text1, string text2) {\n    int m = text1.size(), n = text2.size();\n    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (text1[i - 1] == text2[j - 1]) {\n                dp[i][j] = 1 + dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[m][n];\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int longestCommonSubsequence(String text1, String text2) {\n        int m = text1.length(), n = text2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (i < m && j < n && text1.charAt(i) == text2.charAt(j)) {\n                    dp[i][j] = 1 + dp[i - 1][j - 1];\n                } else {\n                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);\n                }\n            }\n        }\n        return dp[m][n];\n    }\n}",
                "correctCode": "class Solution {\n    public int longestCommonSubsequence(String text1, String text2) {\n        int m = text1.length(), n = text2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {\n                    dp[i][j] = 1 + dp[i - 1][j - 1];\n                } else {\n                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);\n                }\n            }\n        }\n        return dp[m][n];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_edit_distance",
        "title": "Edit Distance (Levenshtein)",
        "problemStatement": "Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.\n\nYou have the following three operations permitted on a word:\n- Insert a character\n- Delete a character\n- Replace a character",
        "topic": "2ddp",
        "subtopic": "matrix-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Forgetting +1 operation cost on replace/diagonal state transition",
        "intendedApproach": "Base cases: dp[i][0] = i (deletions) and dp[0][j] = j (insertions). If word1[i-1] == word2[j-1] dp[i][j] = dp[i-1][j-1]. Else dp[i][j] = 1 + min(dp[i-1][j] (delete), dp[i][j-1] (insert), dp[i-1][j-1] (replace)).",
        "explanation": "When `word1[i-1] != word2[j-1]`, replacing a character requires 1 operation, so `dp[i-1][j-1] + 1` is needed. Omitting the `+ 1` counts character replacement as free of cost.",
        "constraints": [
            "0 <= word1.length, word2.length <= 500",
            "word1 and word2 consist of lowercase English letters.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "word1 = \"horse\", word2 = \"ros\"",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "horse -> rorse (replace 'h' with 'r'), rorse -> rose (remove 'r'), rose -> ros (remove 'e'). Total operations = 3.",
            },
            {
                "id": 2,
                "input": "word1 = \"intention\", word2 = \"execution\"",
                "expectedOutput": "5",
                "isHidden": False,
                "explanation": "intention -> inention (delete 't'), inention -> enention (replace 'i' with 'e'), enention -> exention (replace 'n' with 'x'), exention -> exection (replace 'n' with 'c'), exection -> execution (insert 'u'). Total = 5.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "word1 = \"\", word2 = \"a\"",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "word1 = \"abc\", word2 = \"\"",
                "expectedOutput": "3",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "word1 = \"sea\", word2 = \"eat\"",
                "expectedOutput": "2",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(M * N)",
        },
        "tags": [
            "2ddp",
            "matrix-dp",
            "strings",
            "hard",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Edit Matrix Transition Grid",
            "data": [
                [
                    0,
                    1,
                    2,
                    3,
                ],
                [
                    1,
                    1,
                    2,
                    3,
                ],
                [
                    2,
                    2,
                    1,
                    2,
                ],
                [
                    3,
                    2,
                    2,
                    2,
                ],
                [
                    4,
                    3,
                    3,
                    2,
                ],
                [
                    5,
                    4,
                    4,
                    3,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <string.h>\n#include <stdlib.h>\n\nint min3(int a, int b, int c) {\n    int m = (a < b) ? a : b;\n    return (m < c) ? m : c;\n}\n\nint minDistance(char* word1, char* word2) {\n    int m = strlen(word1), n = strlen(word2);\n    int dp[505][505];\n    for (int i = 0; i <= m; i++) dp[i][0] = i;\n    for (int j = 0; j <= n; j++) dp[0][j] = j;\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (word1[i - 1] == word2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = min3(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1]);\n            }\n        }\n    }\n    return dp[m][n];\n}",
                "correctCode": "#include <string.h>\n#include <stdlib.h>\n\nint min3(int a, int b, int c) {\n    int m = (a < b) ? a : b;\n    return (m < c) ? m : c;\n}\n\nint minDistance(char* word1, char* word2) {\n    int m = strlen(word1), n = strlen(word2);\n    int dp[505][505];\n    for (int i = 0; i <= m; i++) dp[i][0] = i;\n    for (int j = 0; j <= n; j++) dp[0][j] = j;\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (word1[i - 1] == word2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = 1 + min3(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);\n            }\n        }\n    }\n    return dp[m][n];\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint minDistance(string word1, string word2) {\n    int m = word1.size(), n = word2.size();\n    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));\n    for (int i = 0; i <= m; i++) dp[i][0] = i;\n    for (int j = 0; j <= n; j++) dp[0][j] = j;\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (word1[i - 1] == word2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = min({dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1]});\n            }\n        }\n    }\n    return dp[m][n];\n}",
                "correctCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint minDistance(string word1, string word2) {\n    int m = word1.size(), n = word2.size();\n    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));\n    for (int i = 0; i <= m; i++) dp[i][0] = i;\n    for (int j = 0; j <= n; j++) dp[0][j] = j;\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (word1[i - 1] == word2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});\n            }\n        }\n    }\n    return dp[m][n];\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int minDistance(String word1, String word2) {\n        int m = word1.length(), n = word2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 0; i <= m; i++) dp[i][0] = i;\n        for (int j = 0; j <= n; j++) dp[0][j] = j;\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else {\n                    dp[i][j] = Math.min(dp[i - 1][j] + 1, Math.min(dp[i][j - 1] + 1, dp[i - 1][j - 1]));\n                }\n            }\n        }\n        return dp[m][n];\n    }\n}",
                "correctCode": "class Solution {\n    public int minDistance(String word1, String word2) {\n        int m = word1.length(), n = word2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 0; i <= m; i++) dp[i][0] = i;\n        for (int j = 0; j <= n; j++) dp[0][j] = j;\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else {\n                    dp[i][j] = 1 + Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1]));\n                }\n            }\n        }\n        return dp[m][n];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_maximal_square",
        "title": "Maximal Square (Largest All-1 Square)",
        "problemStatement": "Given an `m x n` binary matrix filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area.",
        "topic": "2ddp",
        "subtopic": "matrix-dp",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "logical",
        "bugConcept": "Returning maximal side length instead of area (side * side)",
        "intendedApproach": "dp[r][c] represents the side length of maximal square whose bottom-right corner is at (r, c). When matrix[r][c] == '1', dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]). Return maxSide * maxSide.",
        "explanation": "The problem asks for the AREA of the maximal square. Returning the maximal square side length `maxSide` gives 2 instead of 4 for a 2x2 square.",
        "constraints": [
            "m == matrix.length",
            "n == matrix[i].length",
            "1 <= m, n <= 300",
            "matrix[i][j] is '0' or '1'.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "matrix = [[\"1\",\"0\",\"1\",\"0\",\"0\"],[\"1\",\"0\",\"1\",\"1\",\"1\"],[\"1\",\"1\",\"1\",\"1\",\"1\"],[\"1\",\"0\",\"0\",\"1\",\"0\"]",
                "expectedOutput": "4",
                "isHidden": False,
                "explanation": "The largest square of all 1s has side length 2, so the maximal area is 2 * 2 = 4.",
            },
            {
                "id": 2,
                "input": "matrix = [[\"0\",\"1\"],[\"1\",\"0\"]]",
                "expectedOutput": "1",
                "isHidden": False,
                "explanation": "The largest square of all 1s has side length 1, so the area is 1.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "matrix = [[\"0\"]]",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "matrix = [[\"1\",\"1\"],[\"1\",\"1\"]]",
                "expectedOutput": "4",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "matrix = [[\"1\",\"1\",\"1\"],[\"1\",\"1\",\"1\"],[\"1\",\"1\",\"1\"]]",
                "expectedOutput": "9",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(M * N)",
        },
        "tags": [
            "2ddp",
            "matrix-dp",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Binary 0/1 Matrix",
            "data": [
                [
                    "1",
                    "0",
                    "1",
                    "0",
                ],
                [
                    "1",
                    "1",
                    "1",
                    "1",
                ],
                [
                    "1",
                    "1",
                    "1",
                    "1",
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "int min3(int a, int b, int c) {\n    int m = (a < b) ? a : b;\n    return (m < c) ? m : c;\n}\n\nint maximalSquare(char matrix[300][300], int m, int n) {\n    int dp[305][305] = {0};\n    int maxSide = 0;\n    for (int r = 1; r <= m; r++) {\n        for (int c = 1; c <= n; c++) {\n            if (matrix[r - 1][c - 1] == '1') {\n                dp[r][c] = 1 + min3(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]);\n                if (dp[r][c] > maxSide) maxSide = dp[r][c];\n            }\n        }\n    }\n    return maxSide;\n}",
                "correctCode": "int min3(int a, int b, int c) {\n    int m = (a < b) ? a : b;\n    return (m < c) ? m : c;\n}\n\nint maximalSquare(char matrix[300][300], int m, int n) {\n    int dp[305][305] = {0};\n    int maxSide = 0;\n    for (int r = 1; r <= m; r++) {\n        for (int c = 1; c <= n; c++) {\n            if (matrix[r - 1][c - 1] == '1') {\n                dp[r][c] = 1 + min3(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]);\n                if (dp[r][c] > maxSide) maxSide = dp[r][c];\n            }\n        }\n    }\n    return maxSide * maxSide;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint maximalSquare(vector<vector<char>>& matrix) {\n    int m = matrix.size(), n = matrix[0].size();\n    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));\n    int maxSide = 0;\n    for (int r = 1; r <= m; r++) {\n        for (int c = 1; c <= n; c++) {\n            if (matrix[r - 1][c - 1] == '1') {\n                dp[r][c] = 1 + min({dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]});\n                maxSide = max(maxSide, dp[r][c]);\n            }\n        }\n    }\n    return maxSide;\n}",
                "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint maximalSquare(vector<vector<char>>& matrix) {\n    int m = matrix.size(), n = matrix[0].size();\n    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));\n    int maxSide = 0;\n    for (int r = 1; r <= m; r++) {\n        for (int c = 1; c <= n; c++) {\n            if (matrix[r - 1][c - 1] == '1') {\n                dp[r][c] = 1 + min({dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]});\n                maxSide = max(maxSide, dp[r][c]);\n            }\n        }\n    }\n    return maxSide * maxSide;\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int maximalSquare(char[][] matrix) {\n        int m = matrix.length, n = matrix[0].length;\n        int[][] dp = new int[m + 1][n + 1];\n        int maxSide = 0;\n        for (int r = 1; r <= m; r++) {\n            for (int c = 1; c <= n; c++) {\n                if (matrix[r - 1][c - 1] == '1') {\n                    dp[r][c] = 1 + Math.min(dp[r - 1][c], Math.min(dp[r][c - 1], dp[r - 1][c - 1]));\n                    maxSide = Math.max(maxSide, dp[r][c]);\n                }\n            }\n        }\n        return maxSide;\n    }\n}",
                "correctCode": "class Solution {\n    public int maximalSquare(char[][] matrix) {\n        int m = matrix.length, n = matrix[0].length;\n        int[][] dp = new int[m + 1][n + 1];\n        int maxSide = 0;\n        for (int r = 1; r <= m; r++) {\n            for (int c = 1; c <= n; c++) {\n                if (matrix[r - 1][c - 1] == '1') {\n                    dp[r][c] = 1 + Math.min(dp[r - 1][c], Math.min(dp[r][c - 1], dp[r - 1][c - 1]));\n                    maxSide = Math.max(maxSide, dp[r][c]);\n                }\n            }\n        }\n        return maxSide * maxSide;\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_dungeon_game",
        "title": "Dungeon Game (Knight Minimum Initial HP)",
        "problemStatement": "The demons had captured the princess and imprisoned her in the bottom-right corner of a `dungeon`. The dungeon consists of `m x n` rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.\n\nThe knight has an initial health point represented by a positive integer. If at any point his health point drops to `0` or below, he dies immediately.\n\nSome of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).\n\nTo reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.\n\nReturn the knight's minimum initial health so that he can rescue the princess.",
        "topic": "2ddp",
        "subtopic": "matrix-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect traversal",
        "bugConcept": "Computing top-down instead of bottom-up reverse DP, causing future damage constraints to be lost",
        "intendedApproach": "Bottom-up reverse DP starting at destination (m-1, n-1) back to (0, 0). dp[r][c] = max(1, min(dp[r+1][c], dp[r][c+1]) - dungeon[r][c]).",
        "explanation": "Top-down DP cannot decide whether taking a damage room with positive payoff later is preferable to taking a harmless room. Reverse DP from princess back to knight determines exact minimum health needed to survive remaining path.",
        "constraints": [
            "m == dungeon.length",
            "n == dungeon[i].length",
            "1 <= m, n <= 200",
            "-1000 <= dungeon[i][j] <= 1000",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]",
                "expectedOutput": "7",
                "isHidden": False,
                "explanation": "The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT -> RIGHT -> DOWN -> DOWN.",
            },
            {
                "id": 2,
                "input": "dungeon = [[0]]",
                "expectedOutput": "1",
                "isHidden": False,
                "explanation": "The knight needs at least 1 HP to enter a room with value 0.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "dungeon = [[100]]",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "dungeon = [[-3,5]]",
                "expectedOutput": "4",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]",
                "expectedOutput": "3",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(M * N)",
        },
        "tags": [
            "2ddp",
            "matrix-dp",
            "hard",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Dungeon Room Modifiers",
            "data": [
                [
                    -2,
                    -3,
                    3,
                ],
                [
                    -5,
                    -10,
                    1,
                ],
                [
                    10,
                    30,
                    -5,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <limits.h>\n\nint calculateMinimumHP(int dungeon[200][200], int m, int n) {\n    int dp[205][205];\n    for (int r = 0; r <= m; r++) for (int c = 0; c <= n; c++) dp[r][c] = INT_MAX;\n    dp[m][n - 1] = 1;\n    dp[m - 1][n] = 1;\n    for (int r = m - 1; r >= 0; r--) {\n        for (int c = n - 1; c >= 0; c--) {\n            int nextMin = (dp[r + 1][c] < dp[r][c + 1]) ? dp[r + 1][c] : dp[r][c + 1];\n            dp[r][c] = nextMin - dungeon[r][c];\n        }\n    }\n    return dp[0][0];\n}",
                "correctCode": "#include <limits.h>\n\nint calculateMinimumHP(int dungeon[200][200], int m, int n) {\n    int dp[205][205];\n    for (int r = 0; r <= m; r++) for (int c = 0; c <= n; c++) dp[r][c] = INT_MAX;\n    dp[m][n - 1] = 1;\n    dp[m - 1][n] = 1;\n    for (int r = m - 1; r >= 0; r--) {\n        for (int c = n - 1; c >= 0; c--) {\n            int nextMin = (dp[r + 1][c] < dp[r][c + 1]) ? dp[r + 1][c] : dp[r][c + 1];\n            int need = nextMin - dungeon[r][c];\n            dp[r][c] = (need <= 0) ? 1 : need;\n        }\n    }\n    return dp[0][0];\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <algorithm>\n#include <climits>\nusing namespace std;\n\nint calculateMinimumHP(vector<vector<int>>& dungeon) {\n    int m = dungeon.size(), n = dungeon[0].size();\n    vector<vector<int>> dp(m + 1, vector<int>(n + 1, INT_MAX));\n    dp[m][n - 1] = 1;\n    dp[m - 1][n] = 1;\n    for (int r = m - 1; r >= 0; r--) {\n        for (int c = n - 1; c >= 0; c--) {\n            int nextMin = min(dp[r + 1][c], dp[r][c + 1]);\n            dp[r][c] = nextMin - dungeon[r][c];\n        }\n    }\n    return dp[0][0];\n}",
                "correctCode": "#include <vector>\n#include <algorithm>\n#include <climits>\nusing namespace std;\n\nint calculateMinimumHP(vector<vector<int>>& dungeon) {\n    int m = dungeon.size(), n = dungeon[0].size();\n    vector<vector<int>> dp(m + 1, vector<int>(n + 1, INT_MAX));\n    dp[m][n - 1] = 1;\n    dp[m - 1][n] = 1;\n    for (int r = m - 1; r >= 0; r--) {\n        for (int c = n - 1; c >= 0; c--) {\n            int nextMin = min(dp[r + 1][c], dp[r][c + 1]);\n            dp[r][c] = max(1, nextMin - dungeon[r][c]);\n        }\n    }\n    return dp[0][0];\n}",
            },
            "java": {
                "buggyCode": "import java.util.Arrays;\n\nclass Solution {\n    public int calculateMinimumHP(int[][] dungeon) {\n        int m = dungeon.length, n = dungeon[0].length;\n        int[][] dp = new int[m + 1][n + 1];\n        for (int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE);\n        dp[m][n - 1] = 1;\n        dp[m - 1][n] = 1;\n        for (int r = m - 1; r >= 0; r--) {\n            for (int c = n - 1; c >= 0; c--) {\n                int nextMin = Math.min(dp[r + 1][c], dp[r][c + 1]);\n                dp[r][c] = nextMin - dungeon[r][c];\n            }\n        }\n        return dp[0][0];\n    }\n}",
                "correctCode": "import java.util.Arrays;\n\nclass Solution {\n    public int calculateMinimumHP(int[][] dungeon) {\n        int m = dungeon.length, n = dungeon[0].length;\n        int[][] dp = new int[m + 1][n + 1];\n        for (int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE);\n        dp[m][n - 1] = 1;\n        dp[m - 1][n] = 1;\n        for (int r = m - 1; r >= 0; r--) {\n            for (int c = n - 1; c >= 0; c--) {\n                int nextMin = Math.min(dp[r + 1][c], dp[r][c + 1]);\n                dp[r][c] = Math.max(1, nextMin - dungeon[r][c]);\n            }\n        }\n        return dp[0][0];\n    }\n}",
            },
        },
    },
]
