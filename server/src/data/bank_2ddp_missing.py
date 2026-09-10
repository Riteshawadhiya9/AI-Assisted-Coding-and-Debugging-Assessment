# Missing 2D DP Questions (8 Questions)

MISSING_2DDP_QUESTIONS = [
    {
        "id": "q_2ddp_unique_paths_ii",
        "title": "Unique Paths II",
        "problemStatement": "You are given an `m x n` integer array `obstacleGrid`. There is a robot initially located at the top-left corner (i.e., `obstacleGrid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `obstacleGrid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.\n\nAn obstacle and space are marked as `1` or `0` respectively in `obstacleGrid`. A path that the robot takes cannot include any square that is an obstacle.\n\nReturn the number of possible unique paths that the robot can take to reach the bottom-right corner.",
        "topic": "2ddp",
        "subtopic": "grid-dp",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "boundary",
        "bugConcept": "Initializing start cell to 1 path even when starting location contains an obstacle",
        "intendedApproach": "If obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1, return 0. Set dp[0][0] = 1. If obstacleGrid[i][j] == 1, dp[i][j] = 0; otherwise dp[i][j] = dp[i-1][j] + dp[i][j-1].",
        "explanation": "Initializing `dp[0][0] = 1` without first checking if `obstacleGrid[0][0] == 1` causes blocked starting cells to generate valid path counts.",
        "constraints": [
            "m == obstacleGrid.length",
            "n == obstacleGrid[i].length",
            "1 <= m, n <= 100",
            "obstacleGrid[i][j] is 0 or 1.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]",
                "expectedOutput": "2",
                "isHidden": False,
                "explanation": "There is one obstacle in the middle of the 3x3 grid above. There are two paths to the bottom-right: 1. Right -> Right -> Down -> Down, 2. Down -> Down -> Right -> Right.",
            },
            {
                "id": 2,
                "input": "obstacleGrid = [[0,1],[0,0]]",
                "expectedOutput": "1",
                "isHidden": False,
                "explanation": "There is an obstacle at (0,1), leaving only 1 valid path: Down -> Right.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "obstacleGrid = [[1,0]]",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "obstacleGrid = [[0,0],[1,1],[0,0]]",
                "expectedOutput": "0",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(N)",
        },
        "tags": [
            "2ddp",
            "matrix",
            "grid-dp",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Grid Obstacle Map",
            "data": [
                [
                    0,
                    0,
                    0,
                ],
                [
                    0,
                    1,
                    0,
                ],
                [
                    0,
                    0,
                    0,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize) {\n    int m = obstacleGridSize, n = obstacleGridColSize[0];\n    long long dp[105] = {0};\n    dp[0] = 1;\n    for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n            if (obstacleGrid[i][j] == 1) {\n                dp[j] = 0;\n            } else if (j > 0) {\n                dp[j] += dp[j - 1];\n            }\n        }\n    }\n    return (int)dp[n - 1];\n}",
                "correctCode": "int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize) {\n    int m = obstacleGridSize, n = obstacleGridColSize[0];\n    if (obstacleGrid[0][0] == 1 || obstacleGrid[m - 1][n - 1] == 1) return 0;\n    long long dp[105] = {0};\n    dp[0] = 1;\n    for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n            if (obstacleGrid[i][j] == 1) {\n                dp[j] = 0;\n            } else if (j > 0) {\n                dp[j] += dp[j - 1];\n            }\n        }\n    }\n    return (int)dp[n - 1];\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {\n        int m = obstacleGrid.size(), n = obstacleGrid[0].size();\n        vector<long long> dp(n, 0);\n        dp[0] = 1;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (obstacleGrid[i][j] == 1) {\n                    dp[j] = 0;\n                } else if (j > 0) {\n                    dp[j] += dp[j - 1];\n                }\n            }\n        }\n        return dp[n - 1];\n    }\n};",
                "correctCode": "#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {\n        int m = obstacleGrid.size(), n = obstacleGrid[0].size();\n        if (obstacleGrid[0][0] == 1 || obstacleGrid[m - 1][n - 1] == 1) return 0;\n        vector<long long> dp(n, 0);\n        dp[0] = 1;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (obstacleGrid[i][j] == 1) {\n                    dp[j] = 0;\n                } else if (j > 0) {\n                    dp[j] += dp[j - 1];\n                }\n            }\n        }\n        return dp[n - 1];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int uniquePathsWithObstacles(int[][] obstacleGrid) {\n        int m = obstacleGrid.length, n = obstacleGrid[0].length;\n        long[] dp = new long[n];\n        dp[0] = 1;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (obstacleGrid[i][j] == 1) {\n                    dp[j] = 0;\n                } else if (j > 0) {\n                    dp[j] += dp[j - 1];\n                }\n            }\n        }\n        return (int)dp[n - 1];\n    }\n}",
                "correctCode": "class Solution {\n    public int uniquePathsWithObstacles(int[][] obstacleGrid) {\n        int m = obstacleGrid.length, n = obstacleGrid[0].length;\n        if (obstacleGrid[0][0] == 1 || obstacleGrid[m - 1][n - 1] == 1) return 0;\n        long[] dp = new long[n];\n        dp[0] = 1;\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                if (obstacleGrid[i][j] == 1) {\n                    dp[j] = 0;\n                } else if (j > 0) {\n                    dp[j] += dp[j - 1];\n                }\n            }\n        }\n        return (int)dp[n - 1];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_range_sum_2d",
        "title": "Range Sum Query 2D - Immutable",
        "problemStatement": "Given a 2D matrix `matrix`, handle multiple queries of the following type:\n\nCalculate the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.\n\nImplement the `NumMatrix` class:\n- `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.\n- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.",
        "topic": "2ddp",
        "subtopic": "prefix-sum",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "logical",
        "bugConcept": "Subtracting instead of adding the doubly-subtracted top-left overlap in 2D inclusion-exclusion",
        "intendedApproach": "Build 2D prefix sum prefix[r+1][c+1] = matrix[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]. Query region: prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1].",
        "explanation": "Subtracting `prefix[r1][c1]` in `sumRegion` subtracts the top-left intersection a third time instead of adding it back to cancel double subtraction.",
        "constraints": [
            "m == matrix.length",
            "n == matrix[i].length",
            "1 <= m, n <= 200",
            "-10^4 <= matrix[i][j] <= 10^4",
            "0 <= row1 <= row2 < m",
            "0 <= col1 <= col2 < n",
            "At most 10^4 calls will be made to sumRegion.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]], query = [2,1,4,3]",
                "expectedOutput": "8",
                "isHidden": False,
                "explanation": "The region sum for rectangle (2,1) to (4,3) adds the elements inside that subgrid to 8.",
            },
            {
                "id": 2,
                "input": "matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]], query = [1,1,2,2]",
                "expectedOutput": "11",
                "isHidden": False,
                "explanation": "The region sum for rectangle (1,1) to (2,2) equals 11.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "matrix = [[1]], query = [0,0,0,0]",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "matrix = [[1,2],[3,4]], query = [0,0,1,1]",
                "expectedOutput": "10",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(1) query, O(M * N) precomputation",
            "space": "O(M * N)",
        },
        "tags": [
            "2ddp",
            "matrix",
            "prefix-sum",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "2D Matrix Grid",
            "data": [
                [
                    3,
                    0,
                    1,
                    4,
                    2,
                ],
                [
                    5,
                    6,
                    3,
                    2,
                    1,
                ],
                [
                    1,
                    2,
                    0,
                    1,
                    5,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdlib.h>\n\ntypedef struct {\n    int** pref;\n    int m, n;\n} NumMatrix;\n\nNumMatrix* numMatrixCreate(int** matrix, int matrixSize, int* matrixColSize) {\n    NumMatrix* obj = (NumMatrix*)malloc(sizeof(NumMatrix));\n    int m = matrixSize, n = matrixColSize[0];\n    obj->m = m; obj->n = n;\n    obj->pref = (int**)malloc((m + 1) * sizeof(int*));\n    for (int i = 0; i <= m; i++) {\n        obj->pref[i] = (int*)calloc(n + 1, sizeof(int));\n    }\n    for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n            obj->pref[i + 1][j + 1] = matrix[i][j] + obj->pref[i][j + 1] + obj->pref[i + 1][j] - obj->pref[i][j];\n        }\n    }\n    return obj;\n}\n\nint numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) {\n    return obj->pref[row2 + 1][col2 + 1] - obj->pref[row1][col2 + 1] - obj->pref[row2 + 1][col1] - obj->pref[row1][col1];\n}",
                "correctCode": "#include <stdlib.h>\n\ntypedef struct {\n    int** pref;\n    int m, n;\n} NumMatrix;\n\nNumMatrix* numMatrixCreate(int** matrix, int matrixSize, int* matrixColSize) {\n    NumMatrix* obj = (NumMatrix*)malloc(sizeof(NumMatrix));\n    int m = matrixSize, n = matrixColSize[0];\n    obj->m = m; obj->n = n;\n    obj->pref = (int**)malloc((m + 1) * sizeof(int*));\n    for (int i = 0; i <= m; i++) {\n        obj->pref[i] = (int*)calloc(n + 1, sizeof(int));\n    }\n    for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n            obj->pref[i + 1][j + 1] = matrix[i][j] + obj->pref[i][j + 1] + obj->pref[i + 1][j] - obj->pref[i][j];\n        }\n    }\n    return obj;\n}\n\nint numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) {\n    return obj->pref[row2 + 1][col2 + 1] - obj->pref[row1][col2 + 1] - obj->pref[row2 + 1][col1] + obj->pref[row1][col1];\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nclass NumMatrix {\n    vector<vector<int>> pref;\npublic:\n    NumMatrix(vector<vector<int>>& matrix) {\n        int m = matrix.size(), n = matrix[0].size();\n        pref.assign(m + 1, vector<int>(n + 1, 0));\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                pref[i + 1][j + 1] = matrix[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j];\n            }\n        }\n    }\n    int sumRegion(int row1, int col1, int row2, int col2) {\n        return pref[row2 + 1][col2 + 1] - pref[row1][col2 + 1] - pref[row2 + 1][col1] - pref[row1][col1];\n    }\n};",
                "correctCode": "#include <vector>\nusing namespace std;\n\nclass NumMatrix {\n    vector<vector<int>> pref;\npublic:\n    NumMatrix(vector<vector<int>>& matrix) {\n        int m = matrix.size(), n = matrix[0].size();\n        pref.assign(m + 1, vector<int>(n + 1, 0));\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                pref[i + 1][j + 1] = matrix[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j];\n            }\n        }\n    }\n    int sumRegion(int row1, int col1, int row2, int col2) {\n        return pref[row2 + 1][col2 + 1] - pref[row1][col2 + 1] - pref[row2 + 1][col1] + pref[row1][col1];\n    }\n};",
            },
            "java": {
                "buggyCode": "class NumMatrix {\n    private int[][] pref;\n    public NumMatrix(int[][] matrix) {\n        int m = matrix.length, n = matrix[0].length;\n        pref = new int[m + 1][n + 1];\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                pref[i + 1][j + 1] = matrix[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j];\n            }\n        }\n    }\n    public int sumRegion(int row1, int col1, int row2, int col2) {\n        return pref[row2 + 1][col2 + 1] - pref[row1][col2 + 1] - pref[row2 + 1][col1] - pref[row1][col1];\n    }\n}",
                "correctCode": "class NumMatrix {\n    private int[][] pref;\n    public NumMatrix(int[][] matrix) {\n        int m = matrix.length, n = matrix[0].length;\n        pref = new int[m + 1][n + 1];\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                pref[i + 1][j + 1] = matrix[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j];\n            }\n        }\n    }\n    public int sumRegion(int row1, int col1, int row2, int col2) {\n        return pref[row2 + 1][col2 + 1] - pref[row1][col2 + 1] - pref[row2 + 1][col1] + pref[row1][col1];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_target_sum",
        "title": "Target Sum",
        "problemStatement": "You are given an integer array `nums` and an integer `target`.\n\nYou want to build an expression out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.\n\nFor example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `\"+2-1\"`.\n\nReturn the number of different expressions that you can build, which evaluates to `target`.",
        "topic": "2ddp",
        "subtopic": "subset-sum",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Iterating 1D knapsack capacity forwards, transforming 0/1 knapsack into unbounded knapsack",
        "intendedApproach": "Reduce to subset sum problem: P = (sum + target) / 2. If (sum + target) is negative or odd, return 0. Use 0/1 knapsack iterating capacity downwards from P to num.",
        "explanation": "Iterating `for (int j = num; j <= subsetSum; j++)` allows the same element to be included multiple times, corrupting 0/1 subset sum combinations.",
        "constraints": [
            "1 <= nums.length <= 20",
            "0 <= nums[i] <= 1000",
            "0 <= sum(nums[i]) <= 1000",
            "-1000 <= target <= 1000",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "nums = [1,1,1,1,1], target = 3",
                "expectedOutput": "5",
                "isHidden": False,
                "explanation": "There are 5 ways to assign symbols to make the sum of nums be target 3: -1+1+1+1+1 = 3, +1-1+1+1+1 = 3, +1+1-1+1+1 = 3, +1+1+1-1+1 = 3, +1+1+1+1-1 = 3.",
            },
            {
                "id": 2,
                "input": "nums = [1], target = 1",
                "expectedOutput": "1",
                "isHidden": False,
                "explanation": "Only +1 yields sum 1.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "nums = [1], target = 2",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "nums = [0,0,0,0,0,0,0,0,1], target = 1",
                "expectedOutput": "256",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N * Sum)",
            "space": "O(Sum)",
        },
        "tags": [
            "2ddp",
            "knapsack",
            "subset-sum",
            "medium",
        ],
        "visualData": {
            "type": "array",
            "title": "Target Sum Subsets",
            "data": [
                1,
                1,
                1,
                1,
                1,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdlib.h>\n\nint findTargetSumWays(int* nums, int numsSize, int target) {\n    int sum = 0;\n    for (int i = 0; i < numsSize; i++) sum += nums[i];\n    if (abs(target) > sum || (sum + target) % 2 != 0) return 0;\n    int s = (sum + target) / 2;\n    int dp[1005] = {0};\n    dp[0] = 1;\n    for (int i = 0; i < numsSize; i++) {\n        int num = nums[i];\n        for (int j = num; j <= s; j++) {\n            dp[j] += dp[j - num];\n        }\n    }\n    return dp[s];\n}",
                "correctCode": "#include <stdlib.h>\n\nint findTargetSumWays(int* nums, int numsSize, int target) {\n    int sum = 0;\n    for (int i = 0; i < numsSize; i++) sum += nums[i];\n    if (abs(target) > sum || (sum + target) % 2 != 0) return 0;\n    int s = (sum + target) / 2;\n    int dp[1005] = {0};\n    dp[0] = 1;\n    for (int i = 0; i < numsSize; i++) {\n        int num = nums[i];\n        for (int j = s; j >= num; j--) {\n            dp[j] += dp[j - num];\n        }\n    }\n    return dp[s];\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <numeric>\n#include <cmath>\nusing namespace std;\n\nclass Solution {\npublic:\n    int findTargetSumWays(vector<int>& nums, int target) {\n        int sum = accumulate(nums.begin(), nums.end(), 0);\n        if (abs(target) > sum || (sum + target) % 2 != 0) return 0;\n        int s = (sum + target) / 2;\n        vector<int> dp(s + 1, 0);\n        dp[0] = 1;\n        for (int num : nums) {\n            for (int j = num; j <= s; j++) {\n                dp[j] += dp[j - num];\n            }\n        }\n        return dp[s];\n    }\n};",
                "correctCode": "#include <vector>\n#include <numeric>\n#include <cmath>\nusing namespace std;\n\nclass Solution {\npublic:\n    int findTargetSumWays(vector<int>& nums, int target) {\n        int sum = accumulate(nums.begin(), nums.end(), 0);\n        if (abs(target) > sum || (sum + target) % 2 != 0) return 0;\n        int s = (sum + target) / 2;\n        vector<int> dp(s + 1, 0);\n        dp[0] = 1;\n        for (int num : nums) {\n            for (int j = s; j >= num; j--) {\n                dp[j] += dp[j - num];\n            }\n        }\n        return dp[s];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int findTargetSumWays(int[] nums, int target) {\n        int sum = 0;\n        for (int n : nums) sum += n;\n        if (Math.abs(target) > sum || (sum + target) % 2 != 0) return 0;\n        int s = (sum + target) / 2;\n        int[] dp = new int[s + 1];\n        dp[0] = 1;\n        for (int num : nums) {\n            for (int j = num; j <= s; j++) {\n                dp[j] += dp[j - num];\n            }\n        }\n        return dp[s];\n    }\n}",
                "correctCode": "class Solution {\n    public int findTargetSumWays(int[] nums, int target) {\n        int sum = 0;\n        for (int n : nums) sum += n;\n        if (Math.abs(target) > sum || (sum + target) % 2 != 0) return 0;\n        int s = (sum + target) / 2;\n        int[] dp = new int[s + 1];\n        dp[0] = 1;\n        for (int num : nums) {\n            for (int j = s; j >= num; j--) {\n                dp[j] += dp[j - num];\n            }\n        }\n        return dp[s];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_longest_palindromic_subseq",
        "title": "Longest Palindromic Subsequence",
        "problemStatement": "Given a string `s`, find the longest palindromic subsequence's length in `s`.\n\nA subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.",
        "topic": "2ddp",
        "subtopic": "interval-dp",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Adding 1 instead of 2 when matched endpoint characters form palindromic ends",
        "intendedApproach": "Let dp[i][j] be longest palindromic subsequence in s[i..j]. Base case: dp[i][i] = 1. If s[i] == s[j], dp[i][j] = dp[i+1][j-1] + 2. Else dp[i][j] = max(dp[i+1][j], dp[i][j-1]).",
        "explanation": "Matching both outer characters s[i] and s[j] contributes 2 characters to the palindrome. Adding only 1 counts only one of the matched pair.",
        "constraints": [
            "1 <= s.length <= 1000",
            "s consists only of lowercase English letters.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "s = \"bbbab\"",
                "expectedOutput": "4",
                "isHidden": False,
                "explanation": "One possible longest palindromic subsequence is \"bbbb\".",
            },
            {
                "id": 2,
                "input": "s = \"cbbd\"",
                "expectedOutput": "2",
                "isHidden": False,
                "explanation": "One possible longest palindromic subsequence is \"bb\".",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "s = \"a\"",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "s = \"character\"",
                "expectedOutput": "5",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N^2)",
            "space": "O(N^2)",
        },
        "tags": [
            "2ddp",
            "strings",
            "interval-dp",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Interval Palindrome Matrix",
            "data": [
                [
                    1,
                    2,
                    3,
                ],
                [
                    0,
                    1,
                    2,
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
                "buggyCode": "#include <string.h>\n#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nint longestPalindromeSubseq(char* s) {\n    int n = strlen(s);\n    int dp[1005][1005] = {0};\n    for (int i = n - 1; i >= 0; i--) {\n        dp[i][i] = 1;\n        for (int j = i + 1; j < n; j++) {\n            if (s[i] == s[j]) {\n                dp[i][j] = dp[i + 1][j - 1] + 1;\n            } else {\n                dp[i][j] = MAX(dp[i + 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[0][n - 1];\n}",
                "correctCode": "#include <string.h>\n#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nint longestPalindromeSubseq(char* s) {\n    int n = strlen(s);\n    int dp[1005][1005] = {0};\n    for (int i = n - 1; i >= 0; i--) {\n        dp[i][i] = 1;\n        for (int j = i + 1; j < n; j++) {\n            if (s[i] == s[j]) {\n                dp[i][j] = dp[i + 1][j - 1] + 2;\n            } else {\n                dp[i][j] = MAX(dp[i + 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[0][n - 1];\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int longestPalindromeSubseq(string s) {\n        int n = s.size();\n        vector<vector<int>> dp(n, vector<int>(n, 0));\n        for (int i = n - 1; i >= 0; i--) {\n            dp[i][i] = 1;\n            for (int j = i + 1; j < n; j++) {\n                if (s[i] == s[j]) {\n                    dp[i][j] = dp[i + 1][j - 1] + 1;\n                } else {\n                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);\n                }\n            }\n        }\n        return dp[0][n - 1];\n    }\n};",
                "correctCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int longestPalindromeSubseq(string s) {\n        int n = s.size();\n        vector<vector<int>> dp(n, vector<int>(n, 0));\n        for (int i = n - 1; i >= 0; i--) {\n            dp[i][i] = 1;\n            for (int j = i + 1; j < n; j++) {\n                if (s[i] == s[j]) {\n                    dp[i][j] = dp[i + 1][j - 1] + 2;\n                } else {\n                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);\n                }\n            }\n        }\n        return dp[0][n - 1];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int longestPalindromeSubseq(String s) {\n        int n = s.length();\n        int[][] dp = new int[n][n];\n        for (int i = n - 1; i >= 0; i--) {\n            dp[i][i] = 1;\n            for (int j = i + 1; j < n; j++) {\n                if (s.charAt(i) == s.charAt(j)) {\n                    dp[i][j] = dp[i + 1][j - 1] + 1;\n                } else {\n                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);\n                }\n            }\n        }\n        return dp[0][n - 1];\n    }\n}",
                "correctCode": "class Solution {\n    public int longestPalindromeSubseq(String s) {\n        int n = s.length();\n        int[][] dp = new int[n][n];\n        for (int i = n - 1; i >= 0; i--) {\n            dp[i][i] = 1;\n            for (int j = i + 1; j < n; j++) {\n                if (s.charAt(i) == s.charAt(j)) {\n                    dp[i][j] = dp[i + 1][j - 1] + 2;\n                } else {\n                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);\n                }\n            }\n        }\n        return dp[0][n - 1];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_interleaving_string",
        "title": "Interleaving String",
        "problemStatement": "Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.\n\nAn interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:\n- `s = s_1 + s_2 + ... + s_n`\n- `t = t_1 + t_2 + ... + t_m`\n- `|n - m| <= 1`\n- The interleaving is `s_1 + t_1 + s_2 + t_2 + ...` or `t_1 + s_1 + t_2 + s_2 + ...`",
        "topic": "2ddp",
        "subtopic": "string-dp",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "boundary",
        "bugConcept": "Missing total length consistency check between source strings and target string",
        "intendedApproach": "If len(s1) + len(s2) != len(s3) return false. dp[i][j] is true if s1[0..i-1] and s2[0..j-1] interleave to form s3[0..i+j-1].",
        "explanation": "If s3 is longer or shorter than len(s1) + len(s2), checking prefixes without the total length check produces false positives on partial substrings.",
        "constraints": [
            "0 <= s1.length, s2.length <= 100",
            "0 <= s3.length <= 200",
            "s1, s2, and s3 consist of lowercase English letters.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "s1 = \"aabcc\", s2 = \"dbbca\", s3 = \"aadbbcbcac\"",
                "expectedOutput": "true",
                "isHidden": False,
                "explanation": "s1 = \"aabcc\", s2 = \"dbbca\", s3 = \"aadbbcbcac\". Split s1 = \"aa\" + \"bc\" + \"c\", s2 = \"dbbc\" + \"a\". Interleaving gives \"aadbbcbcac\".",
            },
            {
                "id": 2,
                "input": "s1 = \"aabcc\", s2 = \"dbbca\", s3 = \"aadbbbaccc\"",
                "expectedOutput": "false",
                "isHidden": False,
                "explanation": "It is impossible to interleave s1 and s2 to obtain s3 because character counts or relative orderings do not match.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "s1 = \"\", s2 = \"\", s3 = \"\"",
                "expectedOutput": "true",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "s1 = \"a\", s2 = \"b\", s3 = \"a\"",
                "expectedOutput": "false",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(M * N)",
        },
        "tags": [
            "2ddp",
            "strings",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Interleaving String Grid",
            "data": [
                [
                    True,
                    False,
                ],
                [
                    True,
                    True,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n#include <string.h>\n\nbool isInterleave(char* s1, char* s2, char* s3) {\n    int m = strlen(s1), n = strlen(s2);\n    bool dp[105][105] = {false};\n    dp[0][0] = true;\n    for (int i = 1; i <= m; i++) {\n        dp[i][0] = dp[i - 1][0] && (s1[i - 1] == s3[i - 1]);\n    }\n    for (int j = 1; j <= n; j++) {\n        dp[0][j] = dp[0][j - 1] && (s2[j - 1] == s3[j - 1]);\n    }\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) ||\n                       (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);\n        }\n    }\n    return dp[m][n];\n}",
                "correctCode": "#include <stdbool.h>\n#include <string.h>\n\nbool isInterleave(char* s1, char* s2, char* s3) {\n    int m = strlen(s1), n = strlen(s2), l = strlen(s3);\n    if (m + n != l) return false;\n    bool dp[105][105] = {false};\n    dp[0][0] = true;\n    for (int i = 1; i <= m; i++) {\n        dp[i][0] = dp[i - 1][0] && (s1[i - 1] == s3[i - 1]);\n    }\n    for (int j = 1; j <= n; j++) {\n        dp[0][j] = dp[0][j - 1] && (s2[j - 1] == s3[j - 1]);\n    }\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) ||\n                       (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);\n        }\n    }\n    return dp[m][n];\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    bool isInterleave(string s1, string s2, string s3) {\n        int m = s1.size(), n = s2.size();\n        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));\n        dp[0][0] = true;\n        for (int i = 1; i <= m; i++) {\n            dp[i][0] = dp[i - 1][0] && (s1[i - 1] == s3[i - 1]);\n        }\n        for (int j = 1; j <= n; j++) {\n            dp[0][j] = dp[0][j - 1] && (s2[j - 1] == s3[j - 1]);\n        }\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) ||\n                           (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);\n            }\n        }\n        return dp[m][n];\n    }\n};",
                "correctCode": "#include <string>\n#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    bool isInterleave(string s1, string s2, string s3) {\n        int m = s1.size(), n = s2.size();\n        if (m + n != (int)s3.size()) return false;\n        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));\n        dp[0][0] = true;\n        for (int i = 1; i <= m; i++) {\n            dp[i][0] = dp[i - 1][0] && (s1[i - 1] == s3[i - 1]);\n        }\n        for (int j = 1; j <= n; j++) {\n            dp[0][j] = dp[0][j - 1] && (s2[j - 1] == s3[j - 1]);\n        }\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) ||\n                           (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);\n            }\n        }\n        return dp[m][n];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public boolean isInterleave(String s1, String s2, String s3) {\n        int m = s1.length(), n = s2.length();\n        boolean[][] dp = new boolean[m + 1][n + 1];\n        dp[0][0] = true;\n        for (int i = 1; i <= m; i++) {\n            dp[i][0] = dp[i - 1][0] && (s1.charAt(i - 1) == s3.charAt(i - 1));\n        }\n        for (int j = 1; j <= n; j++) {\n            dp[0][j] = dp[0][j - 1] && (s2.charAt(j - 1) == s3.charAt(j - 1));\n        }\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                dp[i][j] = (dp[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1)) ||\n                           (dp[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1));\n            }\n        }\n        return dp[m][n];\n    }\n}",
                "correctCode": "class Solution {\n    public boolean isInterleave(String s1, String s2, String s3) {\n        int m = s1.length(), n = s2.length();\n        if (m + n != s3.length()) return false;\n        boolean[][] dp = new boolean[m + 1][n + 1];\n        dp[0][0] = true;\n        for (int i = 1; i <= m; i++) {\n            dp[i][0] = dp[i - 1][0] && (s1.charAt(i - 1) == s3.charAt(i - 1));\n        }\n        for (int j = 1; j <= n; j++) {\n            dp[0][j] = dp[0][j - 1] && (s2.charAt(j - 1) == s3.charAt(j - 1));\n        }\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                dp[i][j] = (dp[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1)) ||\n                           (dp[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1));\n            }\n        }\n        return dp[m][n];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_scramble_string",
        "title": "Scramble String",
        "problemStatement": "We can scramble a string s to get a string t using the following algorithm:\n1. If the length of the string is 1, stop.\n2. If the length of the string is > 1, do the following:\n   - Split the string into two non-empty substrings at a random index.\n   - Randomly decide whether to swap the two substrings or to keep them in their original order.\n   - Apply step 1 recursively on each of the two substrings.\n\nGiven two strings `s1` and `s2` of the same length, return `true` if `s2` is a scrambled string of `s1`, otherwise, return `false`.",
        "topic": "2ddp",
        "subtopic": "interval-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect condition",
        "bugConcept": "Wrong substring slice offset in the swapped children recursive branch",
        "intendedApproach": "For each partition length i from 1 to n - 1, test non-swapped: isScramble(s1[0..i], s2[0..i]) && isScramble(s1[i..], s2[i..]), and swapped: isScramble(s1[0..i], s2[n-i..]) && isScramble(s1[i..], s2[0..n-i]).",
        "explanation": "Extracting `s2.substr(0, i)` instead of `s2.substr(n - i, i)` when testing swapped subtrees compares against the wrong partition of s2.",
        "constraints": [
            "s1.length == s2.length",
            "1 <= s1.length <= 30",
            "s1 and s2 consist of lowercase English letters.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "s1 = \"great\", s2 = \"rgeat\"",
                "expectedOutput": "true",
                "isHidden": False,
                "explanation": "\"great\" can be split into \"gr\" and \"eat\", then swapped and recursively partitioned to form \"rgeat\".",
            },
            {
                "id": 2,
                "input": "s1 = \"abcde\", s2 = \"caebd\"",
                "expectedOutput": "false",
                "isHidden": False,
                "explanation": "\"abcde\" cannot be scrambled into \"caebd\" through valid binary splits.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "s1 = \"a\", s2 = \"a\"",
                "expectedOutput": "true",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "s1 = \"abcdbdac\", s2 = \"bdacabcd\"",
                "expectedOutput": "true",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N^4)",
            "space": "O(N^3)",
        },
        "tags": [
            "2ddp",
            "strings",
            "recursion",
            "hard",
        ],
        "visualData": {
            "type": "tree",
            "title": "Scramble Substring Tree",
            "data": [
                1,
                2,
                3,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n#include <string.h>\n\nbool isScramble(char* s1, char* s2) {\n    int n = strlen(s1);\n    if (n != strlen(s2)) return false;\n    if (strcmp(s1, s2) == 0) return true;\n    int count[26] = {0};\n    for (int i = 0; i < n; i++) {\n        count[s1[i] - 'a']++;\n        count[s2[i] - 'a']--;\n    }\n    for (int i = 0; i < 26; i++) if (count[i] != 0) return false;\n    for (int i = 1; i < n; i++) {\n        char s1_left[35] = {0}, s1_right[35] = {0};\n        char s2_left[35] = {0}, s2_right[35] = {0};\n        strncpy(s1_left, s1, i);\n        strcpy(s1_right, s1 + i);\n        strncpy(s2_left, s2, i);\n        strcpy(s2_right, s2 + i);\n        if (isScramble(s1_left, s2_left) && isScramble(s1_right, s2_right)) return true;\n        char s2_swap_left[35] = {0}, s2_swap_right[35] = {0};\n        strncpy(s2_swap_left, s2, i);\n        strcpy(s2_swap_right, s2 + i);\n        if (isScramble(s1_left, s2_swap_left) && isScramble(s1_right, s2_swap_right)) return true;\n    }\n    return false;\n}",
                "correctCode": "#include <stdbool.h>\n#include <string.h>\n\nbool isScramble(char* s1, char* s2) {\n    int n = strlen(s1);\n    if (n != strlen(s2)) return false;\n    if (strcmp(s1, s2) == 0) return true;\n    int count[26] = {0};\n    for (int i = 0; i < n; i++) {\n        count[s1[i] - 'a']++;\n        count[s2[i] - 'a']--;\n    }\n    for (int i = 0; i < 26; i++) if (count[i] != 0) return false;\n    for (int i = 1; i < n; i++) {\n        char s1_left[35] = {0}, s1_right[35] = {0};\n        char s2_left[35] = {0}, s2_right[35] = {0};\n        strncpy(s1_left, s1, i);\n        strcpy(s1_right, s1 + i);\n        strncpy(s2_left, s2, i);\n        strcpy(s2_right, s2 + i);\n        if (isScramble(s1_left, s2_left) && isScramble(s1_right, s2_right)) return true;\n        char s2_swap_left[35] = {0}, s2_swap_right[35] = {0};\n        strncpy(s2_swap_left, s2 + n - i, i);\n        strncpy(s2_swap_right, s2, n - i);\n        if (isScramble(s1_left, s2_swap_left) && isScramble(s1_right, s2_swap_right)) return true;\n    }\n    return false;\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <unordered_map>\nusing namespace std;\n\nclass Solution {\n    unordered_map<string, bool> memo;\npublic:\n    bool isScramble(string s1, string s2) {\n        if (s1 == s2) return true;\n        int n = s1.size();\n        string key = s1 + \"_\" + s2;\n        if (memo.count(key)) return memo[key];\n        int count[26] = {0};\n        for (int i = 0; i < n; i++) {\n            count[s1[i] - 'a']++;\n            count[s2[i] - 'a']--;\n        }\n        for (int i = 0; i < 26; i++) if (count[i] != 0) return memo[key] = false;\n        for (int i = 1; i < n; i++) {\n            if (isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i), s2.substr(i))) {\n                return memo[key] = true;\n            }\n            if (isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i), s2.substr(i))) {\n                return memo[key] = true;\n            }\n        }\n        return memo[key] = false;\n    }\n};",
                "correctCode": "#include <string>\n#include <unordered_map>\nusing namespace std;\n\nclass Solution {\n    unordered_map<string, bool> memo;\npublic:\n    bool isScramble(string s1, string s2) {\n        if (s1 == s2) return true;\n        int n = s1.size();\n        string key = s1 + \"_\" + s2;\n        if (memo.count(key)) return memo[key];\n        int count[26] = {0};\n        for (int i = 0; i < n; i++) {\n            count[s1[i] - 'a']++;\n            count[s2[i] - 'a']--;\n        }\n        for (int i = 0; i < 26; i++) if (count[i] != 0) return memo[key] = false;\n        for (int i = 1; i < n; i++) {\n            if (isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i), s2.substr(i))) {\n                return memo[key] = true;\n            }\n            if (isScramble(s1.substr(0, i), s2.substr(n - i)) && isScramble(s1.substr(i), s2.substr(0, n - i))) {\n                return memo[key] = true;\n            }\n        }\n        return memo[key] = false;\n    }\n};",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    private Map<String, Boolean> memo = new HashMap<>();\n    public boolean isScramble(String s1, String s2) {\n        if (s1.equals(s2)) return true;\n        int n = s1.length();\n        String key = s1 + \"_\" + s2;\n        if (memo.containsKey(key)) return memo.get(key);\n        int[] count = new int[26];\n        for (int i = 0; i < n; i++) {\n            count[s1.charAt(i) - 'a']++;\n            count[s2.charAt(i) - 'a']--;\n        }\n        for (int i = 0; i < 26; i++) if (count[i] != 0) { memo.put(key, false); return false; }\n        for (int i = 1; i < n; i++) {\n            if (isScramble(s1.substring(0, i), s2.substring(0, i)) && isScramble(s1.substring(i), s2.substring(i))) {\n                memo.put(key, true); return true;\n            }\n            if (isScramble(s1.substring(0, i), s2.substring(0, i)) && isScramble(s1.substring(i), s2.substring(i))) {\n                memo.put(key, true); return true;\n            }\n        }\n        memo.put(key, false);\n        return false;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    private Map<String, Boolean> memo = new HashMap<>();\n    public boolean isScramble(String s1, String s2) {\n        if (s1.equals(s2)) return true;\n        int n = s1.length();\n        String key = s1 + \"_\" + s2;\n        if (memo.containsKey(key)) return memo.get(key);\n        int[] count = new int[26];\n        for (int i = 0; i < n; i++) {\n            count[s1.charAt(i) - 'a']++;\n            count[s2.charAt(i) - 'a']--;\n        }\n        for (int i = 0; i < 26; i++) if (count[i] != 0) { memo.put(key, false); return false; }\n        for (int i = 1; i < n; i++) {\n            if (isScramble(s1.substring(0, i), s2.substring(0, i)) && isScramble(s1.substring(i), s2.substring(i))) {\n                memo.put(key, true); return true;\n            }\n            if (isScramble(s1.substring(0, i), s2.substring(n - i)) && isScramble(s1.substring(i), s2.substring(0, n - i))) {\n                memo.put(key, true); return true;\n            }\n        }\n        memo.put(key, false);\n        return false;\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_min_cost_cut_stick",
        "title": "Minimum Cost to Cut a Stick",
        "problemStatement": "Given a wooden stick of length `n` units. The stick is labelled from `0` to `n`.\n\nGiven an integer array `cuts` where `cuts[i]` denotes a position you should perform a cut at.\n\nYou should perform the cuts in order, you can change the order of the cuts as you wish. The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut).\n\nReturn the minimum total cost of the cuts.",
        "topic": "2ddp",
        "subtopic": "interval-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Omitting the length of the current stick segment being cut from the cost transition",
        "intendedApproach": "Sort cuts and insert 0 and n as boundaries. dp[i][j] is min cost to perform cuts between index i and j. For each cut k in (i, j), cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j].",
        "explanation": "Calculating `cost = dp[i][k] + dp[k][j]` without adding `cuts[j] - cuts[i]` neglects the primary cost of making the cut itself, producing 0.",
        "constraints": [
            "2 <= n <= 10^6",
            "1 <= cuts.length <= 100",
            "1 <= cuts[i] <= n - 1",
            "All the integers in cuts are distinct.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "n = 7, cuts = [1,3,4,5]",
                "expectedOutput": "16",
                "isHidden": False,
                "explanation": "Cutting at 3 costs 7. Then cutting at 1 costs 3, cutting at 5 costs 4, and cutting at 4 costs 2. Total cost = 7 + 3 + 4 + 2 = 16.",
            },
            {
                "id": 2,
                "input": "n = 9, cuts = [5,6,1,4,2]",
                "expectedOutput": "22",
                "isHidden": False,
                "explanation": "Cutting in order [1, 3, 4, 5] yields a minimal cost of 22.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "n = 2, cuts = [1]",
                "expectedOutput": "2",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "n = 10, cuts = [1,2,3,4,5,6,7,8,9]",
                "expectedOutput": "34",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M^3)",
            "space": "O(M^2)",
        },
        "tags": [
            "2ddp",
            "interval-dp",
            "sorting",
            "hard",
        ],
        "visualData": {
            "type": "array",
            "title": "Sorted Stick Cut Points",
            "data": [
                0,
                1,
                3,
                4,
                5,
                7,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdlib.h>\n#include <limits.h>\n\nint cmp(const void* a, const void* b) {\n    return (*(int*)a - *(int*)b);\n}\n\nint minCost(int n, int* cuts, int cutsSize) {\n    int* arr = (int*)malloc((cutsSize + 2) * sizeof(int));\n    arr[0] = 0;\n    for (int i = 0; i < cutsSize; i++) arr[i + 1] = cuts[i];\n    arr[cutsSize + 1] = n;\n    int m = cutsSize + 2;\n    qsort(arr, m, sizeof(int), cmp);\n    int dp[105][105] = {0};\n    for (int len = 2; len < m; len++) {\n        for (int i = 0; i < m - len; i++) {\n            int j = i + len;\n            dp[i][j] = INT_MAX;\n            for (int k = i + 1; k < j; k++) {\n                int cost = dp[i][k] + dp[k][j];\n                if (cost < dp[i][j]) dp[i][j] = cost;\n            }\n        }\n    }\n    int res = dp[0][m - 1];\n    free(arr);\n    return res;\n}",
                "correctCode": "#include <stdlib.h>\n#include <limits.h>\n\nint cmp(const void* a, const void* b) {\n    return (*(int*)a - *(int*)b);\n}\n\nint minCost(int n, int* cuts, int cutsSize) {\n    int* arr = (int*)malloc((cutsSize + 2) * sizeof(int));\n    arr[0] = 0;\n    for (int i = 0; i < cutsSize; i++) arr[i + 1] = cuts[i];\n    arr[cutsSize + 1] = n;\n    int m = cutsSize + 2;\n    qsort(arr, m, sizeof(int), cmp);\n    int dp[105][105] = {0};\n    for (int len = 2; len < m; len++) {\n        for (int i = 0; i < m - len; i++) {\n            int j = i + len;\n            dp[i][j] = INT_MAX;\n            for (int k = i + 1; k < j; k++) {\n                int cost = (arr[j] - arr[i]) + dp[i][k] + dp[k][j];\n                if (cost < dp[i][j]) dp[i][j] = cost;\n            }\n        }\n    }\n    int res = dp[0][m - 1];\n    free(arr);\n    return res;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <algorithm>\n#include <climits>\nusing namespace std;\n\nclass Solution {\npublic:\n    int minCost(int n, vector<int>& cuts) {\n        vector<int> arr = cuts;\n        arr.push_back(0);\n        arr.push_back(n);\n        sort(arr.begin(), arr.end());\n        int m = arr.size();\n        vector<vector<int>> dp(m, vector<int>(m, 0));\n        for (int len = 2; len < m; len++) {\n            for (int i = 0; i < m - len; i++) {\n                int j = i + len;\n                dp[i][j] = INT_MAX;\n                for (int k = i + 1; k < j; k++) {\n                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);\n                }\n            }\n        }\n        return dp[0][m - 1];\n    }\n};",
                "correctCode": "#include <vector>\n#include <algorithm>\n#include <climits>\nusing namespace std;\n\nclass Solution {\npublic:\n    int minCost(int n, vector<int>& cuts) {\n        vector<int> arr = cuts;\n        arr.push_back(0);\n        arr.push_back(n);\n        sort(arr.begin(), arr.end());\n        int m = arr.size();\n        vector<vector<int>> dp(m, vector<int>(m, 0));\n        for (int len = 2; len < m; len++) {\n            for (int i = 0; i < m - len; i++) {\n                int j = i + len;\n                dp[i][j] = INT_MAX;\n                for (int k = i + 1; k < j; k++) {\n                    dp[i][j] = min(dp[i][j], (arr[j] - arr[i]) + dp[i][k] + dp[k][j]);\n                }\n            }\n        }\n        return dp[0][m - 1];\n    }\n};",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    public int minCost(int n, int[] cuts) {\n        int[] arr = new int[cuts.length + 2];\n        arr[0] = 0;\n        arr[arr.length - 1] = n;\n        System.arraycopy(cuts, 0, arr, 1, cuts.length);\n        Arrays.sort(arr);\n        int m = arr.length;\n        int[][] dp = new int[m][m];\n        for (int len = 2; len < m; len++) {\n            for (int i = 0; i < m - len; i++) {\n                int j = i + len;\n                dp[i][j] = Integer.MAX_VALUE;\n                for (int k = i + 1; k < j; k++) {\n                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j]);\n                }\n            }\n        }\n        return dp[0][m - 1];\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    public int minCost(int n, int[] cuts) {\n        int[] arr = new int[cuts.length + 2];\n        arr[0] = 0;\n        arr[arr.length - 1] = n;\n        System.arraycopy(cuts, 0, arr, 1, cuts.length);\n        Arrays.sort(arr);\n        int m = arr.length;\n        int[][] dp = new int[m][m];\n        for (int len = 2; len < m; len++) {\n            for (int i = 0; i < m - len; i++) {\n                int j = i + len;\n                dp[i][j] = Integer.MAX_VALUE;\n                for (int k = i + 1; k < j; k++) {\n                    dp[i][j] = Math.min(dp[i][j], (arr[j] - arr[i]) + dp[i][k] + dp[k][j]);\n                }\n            }\n        }\n        return dp[0][m - 1];\n    }\n}",
            },
        },
    },
    {
        "id": "q_2ddp_stone_game_iii",
        "title": "Stone Game III",
        "problemStatement": "Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array `stoneValue`.\n\nAlice and Bob take turns, with Alice starting first. On each player's turn, that player can take `1`, `2`, or `3` stones from the first remaining stones in the row.\n\nThe score of each player is the sum of values of the stones taken. The objective of each player is to end with the highest score, and both players play optimally.\n\nReturn `\"Alice\"` if Alice will win, `\"Bob\"` if Bob will win, or `\"Tie\"` if they will end the game with the same score.",
        "topic": "2ddp",
        "subtopic": "game-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Adding rather than subtracting opponent's future net advantage in minimax recurrence",
        "intendedApproach": "Let dp[i] be max relative score difference current player can achieve from index i. dp[i] = max_{k=1..3}(sum_{j=i}^{i+k-1} stone[j] - dp[i+k]). If dp[0] > 0 return \"Alice\", < 0 return \"Bob\", else \"Tie\".",
        "explanation": "Calculating `take + dp[i+k]` instead of `take - dp[i+k]` assumes both players are on the same team, failing game-theoretic adversarial play.",
        "constraints": [
            "1 <= stoneValue.length <= 5 * 10^4",
            "-1000 <= stoneValue[i] <= 1000",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "stoneValue = [1,2,3,7]",
                "expectedOutput": "\"Bob\"",
                "isHidden": False,
                "explanation": "Bob wins because he can take the remaining piles after Alice's initial choices to achieve a higher score.",
            },
            {
                "id": 2,
                "input": "stoneValue = [1,2,3,-9]",
                "expectedOutput": "\"Alice\"",
                "isHidden": False,
                "explanation": "Alice can take 3 stones [1,2,3] to secure the win with score 6 vs Bob's -9.",
            },
            {
                "id": 3,
                "input": "stoneValue = [1,2,3,6]",
                "expectedOutput": "\"Tie\"",
                "isHidden": False,
            },
        ],
        "hiddenTestCases": [
            {
                "id": 4,
                "input": "stoneValue = [-1,-2,-3]",
                "expectedOutput": "\"Tie\"",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "stoneValue = [1,2,3,0]",
                "expectedOutput": "\"Bob\"",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N)",
            "space": "O(N)",
        },
        "tags": [
            "2ddp",
            "game-dp",
            "dp",
            "hard",
        ],
        "visualData": {
            "type": "array",
            "title": "Stone Values",
            "data": [
                1,
                2,
                3,
                7,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <limits.h>\n#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nchar* stoneGameIII(int* stoneValue, int stoneValueSize) {\n    int n = stoneValueSize;\n    int dp[50005];\n    for (int i = 0; i <= n; i++) dp[i] = 0;\n    for (int i = n - 1; i >= 0; i--) {\n        dp[i] = INT_MIN;\n        int take = 0;\n        for (int k = 1; k <= 3 && i + k <= n; k++) {\n            take += stoneValue[i + k - 1];\n            dp[i] = MAX(dp[i], take + dp[i + k]);\n        }\n    }\n    if (dp[0] > 0) return \"Alice\";\n    if (dp[0] < 0) return \"Bob\";\n    return \"Tie\";\n}",
                "correctCode": "#include <limits.h>\n#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nchar* stoneGameIII(int* stoneValue, int stoneValueSize) {\n    int n = stoneValueSize;\n    int dp[50005];\n    for (int i = 0; i <= n; i++) dp[i] = 0;\n    for (int i = n - 1; i >= 0; i--) {\n        dp[i] = INT_MIN;\n        int take = 0;\n        for (int k = 1; k <= 3 && i + k <= n; k++) {\n            take += stoneValue[i + k - 1];\n            dp[i] = MAX(dp[i], take - dp[i + k]);\n        }\n    }\n    if (dp[0] > 0) return \"Alice\";\n    if (dp[0] < 0) return \"Bob\";\n    return \"Tie\";\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\n#include <climits>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    string stoneGameIII(vector<int>& stoneValue) {\n        int n = stoneValue.size();\n        vector<int> dp(n + 1, 0);\n        for (int i = n - 1; i >= 0; i--) {\n            dp[i] = INT_MIN;\n            int take = 0;\n            for (int k = 1; k <= 3 && i + k <= n; k++) {\n                take += stoneValue[i + k - 1];\n                dp[i] = max(dp[i], take + dp[i + k]);\n            }\n        }\n        if (dp[0] > 0) return \"Alice\";\n        if (dp[0] < 0) return \"Bob\";\n        return \"Tie\";\n    }\n};",
                "correctCode": "#include <string>\n#include <vector>\n#include <climits>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    string stoneGameIII(vector<int>& stoneValue) {\n        int n = stoneValue.size();\n        vector<int> dp(n + 1, 0);\n        for (int i = n - 1; i >= 0; i--) {\n            dp[i] = INT_MIN;\n            int take = 0;\n            for (int k = 1; k <= 3 && i + k <= n; k++) {\n                take += stoneValue[i + k - 1];\n                dp[i] = max(dp[i], take - dp[i + k]);\n            }\n        }\n        if (dp[0] > 0) return \"Alice\";\n        if (dp[0] < 0) return \"Bob\";\n        return \"Tie\";\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public String stoneGameIII(int[] stoneValue) {\n        int n = stoneValue.length;\n        int[] dp = new int[n + 1];\n        for (int i = n - 1; i >= 0; i--) {\n            dp[i] = Integer.MIN_VALUE;\n            int take = 0;\n            for (int k = 1; k <= 3 && i + k <= n; k++) {\n                take += stoneValue[i + k - 1];\n                dp[i] = Math.max(dp[i], take + dp[i + k]);\n            }\n        }\n        if (dp[0] > 0) return \"Alice\";\n        if (dp[0] < 0) return \"Bob\";\n        return \"Tie\";\n    }\n}",
                "correctCode": "class Solution {\n    public String stoneGameIII(int[] stoneValue) {\n        int n = stoneValue.length;\n        int[] dp = new int[n + 1];\n        for (int i = n - 1; i >= 0; i--) {\n            dp[i] = Integer.MIN_VALUE;\n            int take = 0;\n            for (int k = 1; k <= 3 && i + k <= n; k++) {\n                take += stoneValue[i + k - 1];\n                dp[i] = Math.max(dp[i], take - dp[i + k]);\n            }\n        }\n        if (dp[0] > 0) return \"Alice\";\n        if (dp[0] < 0) return \"Bob\";\n        return \"Tie\";\n    }\n}",
            },
        },
    },
]
