# Missing 1D DP Questions (8 Questions)

MISSING_DP_QUESTIONS = [
    {
        "id": "q_dp_min_cost_climbing_stairs",
        "title": "Min Cost Climbing Stairs",
        "problemStatement": "You are given an integer array `cost` where `cost[i]` is the cost of `i-th` step on a staircase. Once you pay the cost, you can either climb one or two steps.\n\nYou can either start from the step with index `0`, or the step with index `1`.\n\nReturn the minimum cost to reach the top of the floor.",
        "topic": "dp",
        "subtopic": "sequence-dp",
        "difficulty": "easy",
        "estimatedTime": 15,
        "primaryBugType": "off-by-one",
        "bugConcept": "Stopping DP computation at n - 1, calculating cost to stand on last step instead of reaching top floor",
        "intendedApproach": "Let dp[i] be the min cost to reach step i. dp[0] = 0, dp[1] = 0. For i from 2 to n: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]). Return dp[n].",
        "explanation": "Stopping at `i < n` and returning `min(dp[n-1], dp[n-2])` without adding the step cost to reach the top floor results in an off-by-one stair calculation.",
        "constraints": [
            "2 <= cost.length <= 1000",
            "0 <= cost[i] <= 999",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "cost = [10,15,20]",
                "expectedOutput": "15",
                "isHidden": False,
                "explanation": "You will start at index 1. Pay 15 and climb two steps to reach the top. Total cost is 15.",
            },
            {
                "id": 2,
                "input": "cost = [1,100,1,1,1,100,1,1,100,1]",
                "expectedOutput": "6",
                "isHidden": False,
                "explanation": "Start at index 0. Pay cost[0] and step to index 2, pay cost[2] and step to index 4, pay cost[4] and step to index 6, pay cost[6] and step to index 7, pay cost[7] and step to index 9, pay cost[9] and step to top. Minimum total cost = 6.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "cost = [0,0]",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "cost = [10,15]",
                "expectedOutput": "10",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N)",
            "space": "O(1)",
        },
        "tags": [
            "dp",
            "array",
            "easy",
        ],
        "visualData": {
            "type": "array",
            "title": "Staircase Step Costs",
            "data": [
                10,
                15,
                20,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#define MIN(a, b) ((a) < (b) ? (a) : (b))\n\nint minCostClimbingStairs(int* cost, int costSize) {\n    int prev2 = cost[0];\n    int prev1 = cost[1];\n    for (int i = 2; i < costSize - 1; i++) {\n        int cur = cost[i] + MIN(prev1, prev2);\n        prev2 = prev1;\n        prev1 = cur;\n    }\n    return MIN(prev1, prev2);\n}",
                "correctCode": "#define MIN(a, b) ((a) < (b) ? (a) : (b))\n\nint minCostClimbingStairs(int* cost, int costSize) {\n    int prev2 = 0;\n    int prev1 = 0;\n    for (int i = 2; i <= costSize; i++) {\n        int cur = MIN(prev1 + cost[i - 1], prev2 + cost[i - 2]);\n        prev2 = prev1;\n        prev1 = cur;\n    }\n    return prev1;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int minCostClimbingStairs(vector<int>& cost) {\n        int n = cost.size();\n        int prev2 = cost[0];\n        int prev1 = cost[1];\n        for (int i = 2; i < n - 1; i++) {\n            int cur = cost[i] + min(prev1, prev2);\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return min(prev1, prev2);\n    }\n};",
                "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int minCostClimbingStairs(vector<int>& cost) {\n        int n = cost.size();\n        int prev2 = 0;\n        int prev1 = 0;\n        for (int i = 2; i <= n; i++) {\n            int cur = min(prev1 + cost[i - 1], prev2 + cost[i - 2]);\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int minCostClimbingStairs(int[] cost) {\n        int n = cost.length;\n        int prev2 = cost[0];\n        int prev1 = cost[1];\n        for (int i = 2; i < n - 1; i++) {\n            int cur = cost[i] + Math.min(prev1, prev2);\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return Math.min(prev1, prev2);\n    }\n}",
                "correctCode": "class Solution {\n    public int minCostClimbingStairs(int[] cost) {\n        int n = cost.length;\n        int prev2 = 0;\n        int prev1 = 0;\n        for (int i = 2; i <= n; i++) {\n            int cur = Math.min(prev1 + cost[i - 1], prev2 + cost[i - 2]);\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\n}",
            },
        },
    },
    {
        "id": "q_dp_fibonacci",
        "title": "Fibonacci Number",
        "problemStatement": "The Fibonacci numbers, commonly denoted `F(n)` form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is:\n- `F(0) = 0, F(1) = 1`\n- `F(n) = F(n - 1) + F(n - 2)`, for `n > 1`.\n\nGiven `n`, calculate `F(n)`.",
        "topic": "dp",
        "subtopic": "fibonacci",
        "difficulty": "easy",
        "estimatedTime": 10,
        "primaryBugType": "incorrect initialization",
        "bugConcept": "Initializing F(0) to 1 instead of 0, shifting entire sequence value",
        "intendedApproach": "Base cases: if n <= 1 return n. Maintain prev2 = 0, prev1 = 1. Iteratively calculate cur = prev1 + prev2.",
        "explanation": "Initializing both prev1 and prev2 to 1 computes F(0)=1, F(1)=1, F(2)=2, producing incorrect values for F(0) and subsequent Fibonacci terms.",
        "constraints": [
            "0 <= n <= 30",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "n = 2",
                "expectedOutput": "1",
                "isHidden": False,
                "explanation": "F(2) = F(1) + F(0) = 1 + 0 = 1.",
            },
            {
                "id": 2,
                "input": "n = 3",
                "expectedOutput": "2",
                "isHidden": False,
                "explanation": "F(3) = F(2) + F(1) = 1 + 1 = 2.",
            },
            {
                "id": 3,
                "input": "n = 4",
                "expectedOutput": "3",
                "isHidden": False,
            },
        ],
        "hiddenTestCases": [
            {
                "id": 4,
                "input": "n = 0",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "n = 1",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 6,
                "input": "n = 10",
                "expectedOutput": "55",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N)",
            "space": "O(1)",
        },
        "tags": [
            "dp",
            "math",
            "recursion",
            "easy",
        ],
        "visualData": {
            "type": "array",
            "title": "Fibonacci Sequence",
            "data": [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "int fib(int n) {\n    if (n <= 1) return n;\n    int prev2 = 1, prev1 = 1;\n    for (int i = 2; i <= n; i++) {\n        int cur = prev1 + prev2;\n        prev2 = prev1;\n        prev1 = cur;\n    }\n    return prev1;\n}",
                "correctCode": "int fib(int n) {\n    if (n <= 1) return n;\n    int prev2 = 0, prev1 = 1;\n    for (int i = 2; i <= n; i++) {\n        int cur = prev1 + prev2;\n        prev2 = prev1;\n        prev1 = cur;\n    }\n    return prev1;\n}",
            },
            "cpp": {
                "buggyCode": "class Solution {\npublic:\n    int fib(int n) {\n        if (n <= 1) return n;\n        int prev2 = 1, prev1 = 1;\n        for (int i = 2; i <= n; i++) {\n            int cur = prev1 + prev2;\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\n};",
                "correctCode": "class Solution {\npublic:\n    int fib(int n) {\n        if (n <= 1) return n;\n        int prev2 = 0, prev1 = 1;\n        for (int i = 2; i <= n; i++) {\n            int cur = prev1 + prev2;\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int fib(int n) {\n        if (n <= 1) return n;\n        int prev2 = 1, prev1 = 1;\n        for (int i = 2; i <= n; i++) {\n            int cur = prev1 + prev2;\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\n}",
                "correctCode": "class Solution {\n    public int fib(int n) {\n        if (n <= 1) return n;\n        int prev2 = 0, prev1 = 1;\n        for (int i = 2; i <= n; i++) {\n            int cur = prev1 + prev2;\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\n}",
            },
        },
    },
    {
        "id": "q_dp_house_robber_ii",
        "title": "House Robber II",
        "problemStatement": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.\n\nGiven an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.",
        "topic": "dp",
        "subtopic": "circular-dp",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "boundary",
        "bugConcept": "Robbing both first and last house by improperly setting circular DP subranges",
        "intendedApproach": "If n == 1 return nums[0]. Otherwise max between linear rob on houses [0, n - 2] (excluding last) and houses [1, n - 1] (excluding first).",
        "explanation": "Evaluating `rob(nums, 0, n - 1)` includes both the first and last houses together, violating the circular adjacency constraint.",
        "constraints": [
            "1 <= nums.length <= 100",
            "0 <= nums[i] <= 1000",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "nums = [2,3,2]",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses in the circle.",
            },
            {
                "id": 2,
                "input": "nums = [1,2,3,1]",
                "expectedOutput": "4",
                "isHidden": False,
                "explanation": "Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.",
            },
            {
                "id": 3,
                "input": "nums = [1,2,3]",
                "expectedOutput": "3",
                "isHidden": False,
            },
        ],
        "hiddenTestCases": [
            {
                "id": 4,
                "input": "nums = [0]",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "nums = [200,3,140,20,10]",
                "expectedOutput": "340",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N)",
            "space": "O(1)",
        },
        "tags": [
            "dp",
            "array",
            "medium",
        ],
        "visualData": {
            "type": "array",
            "title": "Circular House Values",
            "data": [
                2,
                3,
                2,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nint robLinear(int* nums, int start, int end) {\n    int prev2 = 0, prev1 = 0;\n    for (int i = start; i <= end; i++) {\n        int cur = MAX(prev1, prev2 + nums[i]);\n        prev2 = prev1;\n        prev1 = cur;\n    }\n    return prev1;\n}\n\nint rob(int* nums, int numsSize) {\n    if (numsSize == 1) return nums[0];\n    return MAX(robLinear(nums, 0, numsSize - 1), robLinear(nums, 1, numsSize - 1));\n}",
                "correctCode": "#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nint robLinear(int* nums, int start, int end) {\n    int prev2 = 0, prev1 = 0;\n    for (int i = start; i <= end; i++) {\n        int cur = MAX(prev1, prev2 + nums[i]);\n        prev2 = prev1;\n        prev1 = cur;\n    }\n    return prev1;\n}\n\nint rob(int* nums, int numsSize) {\n    if (numsSize == 1) return nums[0];\n    return MAX(robLinear(nums, 0, numsSize - 2), robLinear(nums, 1, numsSize - 1));\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\n    int robLinear(vector<int>& nums, int start, int end) {\n        int prev2 = 0, prev1 = 0;\n        for (int i = start; i <= end; i++) {\n            int cur = max(prev1, prev2 + nums[i]);\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\npublic:\n    int rob(vector<int>& nums) {\n        int n = nums.size();\n        if (n == 1) return nums[0];\n        return max(robLinear(nums, 0, n - 1), robLinear(nums, 1, n - 1));\n    }\n};",
                "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\n    int robLinear(vector<int>& nums, int start, int end) {\n        int prev2 = 0, prev1 = 0;\n        for (int i = start; i <= end; i++) {\n            int cur = max(prev1, prev2 + nums[i]);\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\npublic:\n    int rob(vector<int>& nums) {\n        int n = nums.size();\n        if (n == 1) return nums[0];\n        return max(robLinear(nums, 0, n - 2), robLinear(nums, 1, n - 1));\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    private int robLinear(int[] nums, int start, int end) {\n        int prev2 = 0, prev1 = 0;\n        for (int i = start; i <= end; i++) {\n            int cur = Math.max(prev1, prev2 + nums[i]);\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\n    public int rob(int[] nums) {\n        int n = nums.length;\n        if (n == 1) return nums[0];\n        return Math.max(robLinear(nums, 0, n - 1), robLinear(nums, 1, n - 1));\n    }\n}",
                "correctCode": "class Solution {\n    private int robLinear(int[] nums, int start, int end) {\n        int prev2 = 0, prev1 = 0;\n        for (int i = start; i <= end; i++) {\n            int cur = Math.max(prev1, prev2 + nums[i]);\n            prev2 = prev1;\n            prev1 = cur;\n        }\n        return prev1;\n    }\n    public int rob(int[] nums) {\n        int n = nums.length;\n        if (n == 1) return nums[0];\n        return Math.max(robLinear(nums, 0, n - 2), robLinear(nums, 1, n - 1));\n    }\n}",
            },
        },
    },
    {
        "id": "q_dp_decode_ways",
        "title": "Decode Ways",
        "problemStatement": "A message containing letters from A-Z can be encoded into numbers using the following mapping:\n'A' -> \"1\", 'B' -> \"2\", ..., 'Z' -> \"26\"\n\nTo decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).\n\nGiven a string `s` containing only digits, return the number of ways to decode it.",
        "topic": "dp",
        "subtopic": "string-dp",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect condition",
        "bugConcept": "Allowing invalid 2-digit numbers up to 27 instead of capping at 26",
        "intendedApproach": "dp[i] stores ways to decode prefix s[0..i-1]. If s[i-1] != '0', dp[i] += dp[i-1]. If two digits s[i-2..i-1] are between 10 and 26, dp[i] += dp[i-2].",
        "explanation": "Condition `num >= 10 && num <= 27` allows '27' to be treated as a single letter, whereas valid alphabetic encodings only extend through 26 ('Z').",
        "constraints": [
            "1 <= s.length <= 100",
            "s contains only digits and may contain leading zero(s).",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "s = \"12\"",
                "expectedOutput": "2",
                "isHidden": False,
                "explanation": "\"12\" could be decoded as \"AB\" (1 2) or \"L\" (12).",
            },
            {
                "id": 2,
                "input": "s = \"226\"",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "\"226\" could be decoded as \"BZ\" (2 26), \"VF\" (22 6), or \"BBF\" (2 2 6).",
            },
            {
                "id": 3,
                "input": "s = \"06\"",
                "expectedOutput": "0",
                "isHidden": False,
            },
        ],
        "hiddenTestCases": [
            {
                "id": 4,
                "input": "s = \"27\"",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "s = \"10\"",
                "expectedOutput": "1",
                "isHidden": True,
            },
            {
                "id": 6,
                "input": "s = \"2101\"",
                "expectedOutput": "1",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N)",
            "space": "O(N)",
        },
        "tags": [
            "dp",
            "strings",
            "medium",
        ],
        "visualData": {
            "type": "array",
            "title": "Decoded Ways DP Transitions",
            "data": [
                1,
                2,
                3,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <string.h>\n#include <stdlib.h>\n\nint numDecodings(char* s) {\n    int n = strlen(s);\n    if (n == 0 || s[0] == '0') return 0;\n    int* dp = (int*)calloc(n + 1, sizeof(int));\n    dp[0] = 1;\n    dp[1] = 1;\n    for (int i = 2; i <= n; i++) {\n        if (s[i - 1] != '0') dp[i] += dp[i - 1];\n        int twoDigit = (s[i - 2] - '0') * 10 + (s[i - 1] - '0');\n        if (twoDigit >= 10 && twoDigit <= 27) {\n            dp[i] += dp[i - 2];\n        }\n    }\n    int res = dp[n];\n    free(dp);\n    return res;\n}",
                "correctCode": "#include <string.h>\n#include <stdlib.h>\n\nint numDecodings(char* s) {\n    int n = strlen(s);\n    if (n == 0 || s[0] == '0') return 0;\n    int* dp = (int*)calloc(n + 1, sizeof(int));\n    dp[0] = 1;\n    dp[1] = 1;\n    for (int i = 2; i <= n; i++) {\n        if (s[i - 1] != '0') dp[i] += dp[i - 1];\n        int twoDigit = (s[i - 2] - '0') * 10 + (s[i - 1] - '0');\n        if (twoDigit >= 10 && twoDigit <= 26) {\n            dp[i] += dp[i - 2];\n        }\n    }\n    int res = dp[n];\n    free(dp);\n    return res;\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int numDecodings(string s) {\n        int n = s.size();\n        if (n == 0 || s[0] == '0') return 0;\n        vector<int> dp(n + 1, 0);\n        dp[0] = 1;\n        dp[1] = 1;\n        for (int i = 2; i <= n; i++) {\n            if (s[i - 1] != '0') dp[i] += dp[i - 1];\n            int twoDigit = stoi(s.substr(i - 2, 2));\n            if (twoDigit >= 10 && twoDigit <= 27) {\n                dp[i] += dp[i - 2];\n            }\n        }\n        return dp[n];\n    }\n};",
                "correctCode": "#include <string>\n#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int numDecodings(string s) {\n        int n = s.size();\n        if (n == 0 || s[0] == '0') return 0;\n        vector<int> dp(n + 1, 0);\n        dp[0] = 1;\n        dp[1] = 1;\n        for (int i = 2; i <= n; i++) {\n            if (s[i - 1] != '0') dp[i] += dp[i - 1];\n            int twoDigit = stoi(s.substr(i - 2, 2));\n            if (twoDigit >= 10 && twoDigit <= 26) {\n                dp[i] += dp[i - 2];\n            }\n        }\n        return dp[n];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int numDecodings(String s) {\n        int n = s.length();\n        if (n == 0 || s.charAt(0) == '0') return 0;\n        int[] dp = new int[n + 1];\n        dp[0] = 1;\n        dp[1] = 1;\n        for (int i = 2; i <= n; i++) {\n            if (s.charAt(i - 1) != '0') dp[i] += dp[i - 1];\n            int twoDigit = Integer.parseInt(s.substring(i - 2, i));\n            if (twoDigit >= 10 && twoDigit <= 27) {\n                dp[i] += dp[i - 2];\n            }\n        }\n        return dp[n];\n    }\n}",
                "correctCode": "class Solution {\n    public int numDecodings(String s) {\n        int n = s.length();\n        if (n == 0 || s.charAt(0) == '0') return 0;\n        int[] dp = new int[n + 1];\n        dp[0] = 1;\n        dp[1] = 1;\n        for (int i = 2; i <= n; i++) {\n            if (s.charAt(i - 1) != '0') dp[i] += dp[i - 1];\n            int twoDigit = Integer.parseInt(s.substring(i - 2, i));\n            if (twoDigit >= 10 && twoDigit <= 26) {\n                dp[i] += dp[i - 2];\n            }\n        }\n        return dp[n];\n    }\n}",
            },
        },
    },
    {
        "id": "q_dp_distinct_subsequences",
        "title": "Distinct Subsequences",
        "problemStatement": "Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.\n\nThe test cases are generated so that the answer fits on a 32-bit signed integer.",
        "topic": "dp",
        "subtopic": "string-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Omitting the branch that skips matching characters in s when s[i-1] == t[j-1]",
        "intendedApproach": "Let dp[i][j] be distinct subsequences of s[0..i-1] matching t[0..j-1]. Always dp[i][j] = dp[i-1][j] (skip s[i-1]). If s[i-1] == t[j-1], also add dp[i-1][j-1].",
        "explanation": "When `s[i-1] == t[j-1]`, setting `dp[i][j] = dp[i-1][j-1]` without adding `dp[i-1][j]` ignores all ways to form t without using character s[i-1].",
        "constraints": [
            "1 <= s.length, t.length <= 1000",
            "s and t consist of English letters.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "s = \"rabbbit\", t = \"rabbit\"",
                "expectedOutput": "3",
                "isHidden": False,
                "explanation": "There are 3 ways to form \"rabbit\" from \"rabbbit\" by omitting one of the three 'b's.",
            },
            {
                "id": 2,
                "input": "s = \"babgbag\", t = \"bag\"",
                "expectedOutput": "5",
                "isHidden": False,
                "explanation": "There are 5 ways to form \"bag\" from \"babgbag\".",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "s = \"a\", t = \"b\"",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "s = \"aaa\", t = \"a\"",
                "expectedOutput": "3",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(N)",
        },
        "tags": [
            "dp",
            "strings",
            "hard",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Subsequence Alignment Grid",
            "data": [
                [
                    1,
                    0,
                    0,
                ],
                [
                    1,
                    1,
                    0,
                ],
                [
                    1,
                    2,
                    1,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <string.h>\n#include <stdlib.h>\n\nint numDistinct(char* s, char* t) {\n    int m = strlen(s), n = strlen(t);\n    unsigned long long dp[1005] = {0};\n    dp[0] = 1;\n    for (int i = 1; i <= m; i++) {\n        for (int j = n; j >= 1; j--) {\n            if (s[i - 1] == t[j - 1]) {\n                dp[j] = dp[j - 1];\n            }\n        }\n    }\n    return (int)dp[n];\n}",
                "correctCode": "#include <string.h>\n#include <stdlib.h>\n\nint numDistinct(char* s, char* t) {\n    int m = strlen(s), n = strlen(t);\n    unsigned long long dp[1005] = {0};\n    dp[0] = 1;\n    for (int i = 1; i <= m; i++) {\n        for (int j = n; j >= 1; j--) {\n            if (s[i - 1] == t[j - 1]) {\n                dp[j] += dp[j - 1];\n            }\n        }\n    }\n    return (int)dp[n];\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int numDistinct(string s, string t) {\n        int m = s.size(), n = t.size();\n        vector<unsigned long long> dp(n + 1, 0);\n        dp[0] = 1;\n        for (int i = 1; i <= m; i++) {\n            for (int j = n; j >= 1; j--) {\n                if (s[i - 1] == t[j - 1]) {\n                    dp[j] = dp[j - 1];\n                }\n            }\n        }\n        return dp[n];\n    }\n};",
                "correctCode": "#include <string>\n#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    int numDistinct(string s, string t) {\n        int m = s.size(), n = t.size();\n        vector<unsigned long long> dp(n + 1, 0);\n        dp[0] = 1;\n        for (int i = 1; i <= m; i++) {\n            for (int j = n; j >= 1; j--) {\n                if (s[i - 1] == t[j - 1]) {\n                    dp[j] += dp[j - 1];\n                }\n            }\n        }\n        return dp[n];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int numDistinct(String s, String t) {\n        int m = s.length(), n = t.length();\n        int[] dp = new int[n + 1];\n        dp[0] = 1;\n        for (int i = 1; i <= m; i++) {\n            for (int j = n; j >= 1; j--) {\n                if (s.charAt(i - 1) == t.charAt(j - 1)) {\n                    dp[j] = dp[j - 1];\n                }\n            }\n        }\n        return dp[n];\n    }\n}",
                "correctCode": "class Solution {\n    public int numDistinct(String s, String t) {\n        int m = s.length(), n = t.length();\n        int[] dp = new int[n + 1];\n        dp[0] = 1;\n        for (int i = 1; i <= m; i++) {\n            for (int j = n; j >= 1; j--) {\n                if (s.charAt(i - 1) == t.charAt(j - 1)) {\n                    dp[j] += dp[j - 1];\n                }\n            }\n        }\n        return dp[n];\n    }\n}",
            },
        },
    },
    {
        "id": "q_dp_regex_matching",
        "title": "Regular Expression Matching",
        "problemStatement": "Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:\n- `'.'` Matches any single character.\n- `'*'` Matches zero or more of the preceding element.\n\nThe matching should cover the entire input string (not partial).",
        "topic": "dp",
        "subtopic": "string-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Missing the 0-occurrence transition for asterisk wildcard pattern",
        "intendedApproach": "Let dp[i][j] represent whether s[0..i-1] matches p[0..j-1]. If p[j-1] == '*', it can match 0 of preceding (dp[i][j-2]) or 1+ of preceding (dp[i-1][j] if s[i-1] matches p[j-2]).",
        "explanation": "Setting `dp[i][j] = dp[i-1][j]` only handles repetition of 1 or more characters, completely failing patterns like \"a*b\" matching \"b\" where 0 occurrences are taken.",
        "constraints": [
            "1 <= s.length <= 20",
            "1 <= p.length <= 20",
            "s contains only lowercase English letters.",
            "p contains only lowercase English letters, '.', and '*'.",
            "It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "s = \"aa\", p = \"a\"",
                "expectedOutput": "false",
                "isHidden": False,
                "explanation": "\"a\" does not match the entire string \"aa\".",
            },
            {
                "id": 2,
                "input": "s = \"aa\", p = \"a*\"",
                "expectedOutput": "true",
                "isHidden": False,
                "explanation": "'*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes \"aa\".",
            },
            {
                "id": 3,
                "input": "s = \"ab\", p = \".*\"",
                "expectedOutput": "true",
                "isHidden": False,
            },
        ],
        "hiddenTestCases": [
            {
                "id": 4,
                "input": "s = \"aab\", p = \"c*a*b\"",
                "expectedOutput": "true",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "s = \"mississippi\", p = \"mis*is*p*.\"",
                "expectedOutput": "false",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N)",
            "space": "O(M * N)",
        },
        "tags": [
            "dp",
            "strings",
            "recursion",
            "hard",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Regex DP Matching Grid",
            "data": [
                [
                    True,
                    False,
                    False,
                ],
                [
                    False,
                    True,
                    True,
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n#include <string.h>\n\nbool isMatch(char* s, char* p) {\n    int m = strlen(s), n = strlen(p);\n    bool dp[25][25] = {false};\n    dp[0][0] = true;\n    for (int j = 2; j <= n; j++) {\n        if (p[j - 1] == '*') dp[0][j] = dp[0][j - 2];\n    }\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else if (p[j - 1] == '*') {\n                if (p[j - 2] == '.' || p[j - 2] == s[i - 1]) {\n                    dp[i][j] = dp[i - 1][j];\n                }\n            }\n        }\n    }\n    return dp[m][n];\n}",
                "correctCode": "#include <stdbool.h>\n#include <string.h>\n\nbool isMatch(char* s, char* p) {\n    int m = strlen(s), n = strlen(p);\n    bool dp[25][25] = {false};\n    dp[0][0] = true;\n    for (int j = 2; j <= n; j++) {\n        if (p[j - 1] == '*') dp[0][j] = dp[0][j - 2];\n    }\n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else if (p[j - 1] == '*') {\n                dp[i][j] = dp[i][j - 2];\n                if (p[j - 2] == '.' || p[j - 2] == s[i - 1]) {\n                    dp[i][j] = dp[i][j] || dp[i - 1][j];\n                }\n            }\n        }\n    }\n    return dp[m][n];\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    bool isMatch(string s, string p) {\n        int m = s.size(), n = p.size();\n        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));\n        dp[0][0] = true;\n        for (int j = 2; j <= n; j++) {\n            if (p[j - 1] == '*') dp[0][j] = dp[0][j - 2];\n        }\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else if (p[j - 1] == '*') {\n                    if (p[j - 2] == '.' || p[j - 2] == s[i - 1]) {\n                        dp[i][j] = dp[i - 1][j];\n                    }\n                }\n            }\n        }\n        return dp[m][n];\n    }\n};",
                "correctCode": "#include <string>\n#include <vector>\nusing namespace std;\n\nclass Solution {\npublic:\n    bool isMatch(string s, string p) {\n        int m = s.size(), n = p.size();\n        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));\n        dp[0][0] = true;\n        for (int j = 2; j <= n; j++) {\n            if (p[j - 1] == '*') dp[0][j] = dp[0][j - 2];\n        }\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else if (p[j - 1] == '*') {\n                    dp[i][j] = dp[i][j - 2];\n                    if (p[j - 2] == '.' || p[j - 2] == s[i - 1]) {\n                        dp[i][j] = dp[i][j] || dp[i - 1][j];\n                    }\n                }\n            }\n        }\n        return dp[m][n];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public boolean isMatch(String s, String p) {\n        int m = s.length(), n = p.length();\n        boolean[][] dp = new boolean[m + 1][n + 1];\n        dp[0][0] = true;\n        for (int j = 2; j <= n; j++) {\n            if (p.charAt(j - 1) == '*') dp[0][j] = dp[0][j - 2];\n        }\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (p.charAt(j - 1) == '.' || p.charAt(j - 1) == s.charAt(i - 1)) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else if (p.charAt(j - 1) == '*') {\n                    if (p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1)) {\n                        dp[i][j] = dp[i - 1][j];\n                    }\n                }\n            }\n        }\n        return dp[m][n];\n    }\n}",
                "correctCode": "class Solution {\n    public boolean isMatch(String s, String p) {\n        int m = s.length(), n = p.length();\n        boolean[][] dp = new boolean[m + 1][n + 1];\n        dp[0][0] = true;\n        for (int j = 2; j <= n; j++) {\n            if (p.charAt(j - 1) == '*') dp[0][j] = dp[0][j - 2];\n        }\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (p.charAt(j - 1) == '.' || p.charAt(j - 1) == s.charAt(i - 1)) {\n                    dp[i][j] = dp[i - 1][j - 1];\n                } else if (p.charAt(j - 1) == '*') {\n                    dp[i][j] = dp[i][j - 2];\n                    if (p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1)) {\n                        dp[i][j] = dp[i][j] || dp[i - 1][j];\n                    }\n                }\n            }\n        }\n        return dp[m][n];\n    }\n}",
            },
        },
    },
    {
        "id": "q_dp_palindrome_partitioning_ii",
        "title": "Palindrome Partitioning II",
        "problemStatement": "Given a string `s`, partition `s` such that every substring of the partition is a palindrome.\n\nReturn the minimum cuts needed for a palindrome partitioning of `s`.",
        "topic": "dp",
        "subtopic": "interval-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "off-by-one",
        "bugConcept": "Counting cuts as total substrings instead of cuts (cuts = substrings - 1)",
        "intendedApproach": "Precompute isPal[j][i] for all pairs. dp[i] is min cuts for prefix s[0..i]. If isPal[0][i] is true, dp[i] = 0 (0 cuts). Else dp[i] = min(dp[i], dp[j - 1] + 1) for all j such that isPal[j][i] is true.",
        "explanation": "When prefix s[0..i] is a palindrome, 0 cuts are needed. Initializing `dp[i] = 1` counts parts instead of cuts.",
        "constraints": [
            "1 <= s.length <= 2000",
            "s consists of lowercase English letters only.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "s = \"aab\"",
                "expectedOutput": "1",
                "isHidden": False,
                "explanation": "The palindrome partitioning [\"aa\",\"b\"] could be produced using 1 cut.",
            },
            {
                "id": 2,
                "input": "s = \"a\"",
                "expectedOutput": "0",
                "isHidden": False,
                "explanation": "The string \"a\" is already a palindrome, so 0 cuts are needed.",
            },
            {
                "id": 3,
                "input": "s = \"ab\"",
                "expectedOutput": "1",
                "isHidden": False,
            },
        ],
        "hiddenTestCases": [
            {
                "id": 4,
                "input": "s = \"racecar\"",
                "expectedOutput": "0",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "s = \"ababbbabbababa\"",
                "expectedOutput": "3",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N^2)",
            "space": "O(N^2)",
        },
        "tags": [
            "dp",
            "strings",
            "interval-dp",
            "hard",
        ],
        "visualData": {
            "type": "array",
            "title": "Min Cuts Prefix Array",
            "data": [
                0,
                0,
                1,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <string.h>\n#include <stdbool.h>\n#include <stdlib.h>\n#define MIN(a, b) ((a) < (b) ? (a) : (b))\n\nint minCut(char* s) {\n    int n = strlen(s);\n    bool isPal[2005][2005] = {false};\n    int dp[2005];\n    for (int i = 0; i < n; i++) {\n        dp[i] = i;\n        for (int j = 0; j <= i; j++) {\n            if (s[j] == s[i] && (i - j <= 2 || isPal[j + 1][i - 1])) {\n                isPal[j][i] = true;\n                dp[i] = (j == 0) ? 1 : MIN(dp[i], dp[j - 1] + 1);\n            }\n        }\n    }\n    return dp[n - 1];\n}",
                "correctCode": "#include <string.h>\n#include <stdbool.h>\n#include <stdlib.h>\n#define MIN(a, b) ((a) < (b) ? (a) : (b))\n\nint minCut(char* s) {\n    int n = strlen(s);\n    bool isPal[2005][2005] = {false};\n    int dp[2005];\n    for (int i = 0; i < n; i++) {\n        dp[i] = i;\n        for (int j = 0; j <= i; j++) {\n            if (s[j] == s[i] && (i - j <= 2 || isPal[j + 1][i - 1])) {\n                isPal[j][i] = true;\n                dp[i] = (j == 0) ? 0 : MIN(dp[i], dp[j - 1] + 1);\n            }\n        }\n    }\n    return dp[n - 1];\n}",
            },
            "cpp": {
                "buggyCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int minCut(string s) {\n        int n = s.size();\n        vector<vector<bool>> isPal(n, vector<bool>(n, false));\n        vector<int> dp(n);\n        for (int i = 0; i < n; i++) {\n            dp[i] = i;\n            for (int j = 0; j <= i; j++) {\n                if (s[j] == s[i] && (i - j <= 2 || isPal[j + 1][i - 1])) {\n                    isPal[j][i] = true;\n                    dp[i] = (j == 0) ? 1 : min(dp[i], dp[j - 1] + 1);\n                }\n            }\n        }\n        return dp[n - 1];\n    }\n};",
                "correctCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int minCut(string s) {\n        int n = s.size();\n        vector<vector<bool>> isPal(n, vector<bool>(n, false));\n        vector<int> dp(n);\n        for (int i = 0; i < n; i++) {\n            dp[i] = i;\n            for (int j = 0; j <= i; j++) {\n                if (s[j] == s[i] && (i - j <= 2 || isPal[j + 1][i - 1])) {\n                    isPal[j][i] = true;\n                    dp[i] = (j == 0) ? 0 : min(dp[i], dp[j - 1] + 1);\n                }\n            }\n        }\n        return dp[n - 1];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int minCut(String s) {\n        int n = s.length();\n        boolean[][] isPal = new boolean[n][n];\n        int[] dp = new int[n];\n        for (int i = 0; i < n; i++) {\n            dp[i] = i;\n            for (int j = 0; j <= i; j++) {\n                if (s.charAt(j) == s.charAt(i) && (i - j <= 2 || isPal[j + 1][i - 1])) {\n                    isPal[j][i] = true;\n                    dp[i] = (j == 0) ? 1 : Math.min(dp[i], dp[j - 1] + 1);\n                }\n            }\n        }\n        return dp[n - 1];\n    }\n}",
                "correctCode": "class Solution {\n    public int minCut(String s) {\n        int n = s.length();\n        boolean[][] isPal = new boolean[n][n];\n        int[] dp = new int[n];\n        for (int i = 0; i < n; i++) {\n            dp[i] = i;\n            for (int j = 0; j <= i; j++) {\n                if (s.charAt(j) == s.charAt(i) && (i - j <= 2 || isPal[j + 1][i - 1])) {\n                    isPal[j][i] = true;\n                    dp[i] = (j == 0) ? 0 : Math.min(dp[i], dp[j - 1] + 1);\n                }\n            }\n        }\n        return dp[n - 1];\n    }\n}",
            },
        },
    },
    {
        "id": "q_dp_burst_balloons",
        "title": "Burst Balloons",
        "problemStatement": "You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.\n\nIf you burst the `i-th` balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.\n\nReturn the maximum coins you can collect by bursting the balloons wisely.",
        "topic": "dp",
        "subtopic": "interval-dp",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "incorrect state transition",
        "bugConcept": "Multiplying by immediate adjacent indices instead of interval outer boundary values",
        "intendedApproach": "Pad nums with 1 at both ends. In interval DP dp[l][r], consider balloon k burst LAST in (l, r). Coins gained = arr[l] * arr[k] * arr[r] + dp[l][k] + dp[k][r].",
        "explanation": "Because balloon k is assumed to burst last among (l, r), all other balloons in (l, r) are already gone. Its immediate neighbors are arr[l] and arr[r], not arr[k-1] and arr[k+1].",
        "constraints": [
            "n == nums.length",
            "1 <= n <= 300",
            "0 <= nums[i] <= 100",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "nums = [3,1,5,8]",
                "expectedOutput": "167",
                "isHidden": False,
                "explanation": "Burst 1 -> 5 -> 3 -> 8. Coins: 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15 + 120 + 24 + 8 = 167.",
            },
            {
                "id": 2,
                "input": "nums = [1,5]",
                "expectedOutput": "10",
                "isHidden": False,
                "explanation": "Burst 1 -> 5. Coins: 1*1*5 + 1*5*1 = 5 + 5 = 10.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "nums = [7]",
                "expectedOutput": "7",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "nums = [9,76,64]",
                "expectedOutput": "44296",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N^3)",
            "space": "O(N^2)",
        },
        "tags": [
            "dp",
            "interval-dp",
            "hard",
        ],
        "visualData": {
            "type": "array",
            "title": "Balloon Coins",
            "data": [
                3,
                1,
                5,
                8,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <string.h>\n#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nint maxCoins(int* nums, int numsSize) {\n    int arr[305];\n    arr[0] = 1;\n    for (int i = 0; i < numsSize; i++) arr[i + 1] = nums[i];\n    arr[numsSize + 1] = 1;\n    int n = numsSize + 2;\n    int dp[305][305] = {0};\n    for (int len = 2; len < n; len++) {\n        for (int l = 0; l < n - len; l++) {\n            int r = l + len;\n            for (int k = l + 1; k < r; k++) {\n                int coins = arr[k - 1] * arr[k] * arr[k + 1] + dp[l][k] + dp[k][r];\n                dp[l][r] = MAX(dp[l][r], coins);\n            }\n        }\n    }\n    return dp[0][n - 1];\n}",
                "correctCode": "#include <string.h>\n#define MAX(a, b) ((a) > (b) ? (a) : (b))\n\nint maxCoins(int* nums, int numsSize) {\n    int arr[305];\n    arr[0] = 1;\n    for (int i = 0; i < numsSize; i++) arr[i + 1] = nums[i];\n    arr[numsSize + 1] = 1;\n    int n = numsSize + 2;\n    int dp[305][305] = {0};\n    for (int len = 2; len < n; len++) {\n        for (int l = 0; l < n - len; l++) {\n            int r = l + len;\n            for (int k = l + 1; k < r; k++) {\n                int coins = arr[l] * arr[k] * arr[r] + dp[l][k] + dp[k][r];\n                dp[l][r] = MAX(dp[l][r], coins);\n            }\n        }\n    }\n    return dp[0][n - 1];\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int maxCoins(vector<int>& nums) {\n        int n = nums.size();\n        vector<int> arr(n + 2, 1);\n        for (int i = 0; i < n; i++) arr[i + 1] = nums[i];\n        int m = n + 2;\n        vector<vector<int>> dp(m, vector<int>(m, 0));\n        for (int len = 2; len < m; len++) {\n            for (int l = 0; l < m - len; l++) {\n                int r = l + len;\n                for (int k = l + 1; k < r; k++) {\n                    int coins = arr[k - 1] * arr[k] * arr[k + 1] + dp[l][k] + dp[k][r];\n                    dp[l][r] = max(dp[l][r], coins);\n                }\n            }\n        }\n        return dp[0][m - 1];\n    }\n};",
                "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int maxCoins(vector<int>& nums) {\n        int n = nums.size();\n        vector<int> arr(n + 2, 1);\n        for (int i = 0; i < n; i++) arr[i + 1] = nums[i];\n        int m = n + 2;\n        vector<vector<int>> dp(m, vector<int>(m, 0));\n        for (int len = 2; len < m; len++) {\n            for (int l = 0; l < m - len; l++) {\n                int r = l + len;\n                for (int k = l + 1; k < r; k++) {\n                    int coins = arr[l] * arr[k] * arr[r] + dp[l][k] + dp[k][r];\n                    dp[l][r] = max(dp[l][r], coins);\n                }\n            }\n        }\n        return dp[0][m - 1];\n    }\n};",
            },
            "java": {
                "buggyCode": "class Solution {\n    public int maxCoins(int[] nums) {\n        int n = nums.length;\n        int[] arr = new int[n + 2];\n        arr[0] = 1;\n        arr[n + 1] = 1;\n        System.arraycopy(nums, 0, arr, 1, n);\n        int m = n + 2;\n        int[][] dp = new int[m][m];\n        for (int len = 2; len < m; len++) {\n            for (int l = 0; l < m - len; l++) {\n                int r = l + len;\n                for (int k = l + 1; k < r; k++) {\n                    int coins = arr[k - 1] * arr[k] * arr[k + 1] + dp[l][k] + dp[k][r];\n                    dp[l][r] = Math.max(dp[l][r], coins);\n                }\n            }\n        }\n        return dp[0][m - 1];\n    }\n}",
                "correctCode": "class Solution {\n    public int maxCoins(int[] nums) {\n        int n = nums.length;\n        int[] arr = new int[n + 2];\n        arr[0] = 1;\n        arr[n + 1] = 1;\n        System.arraycopy(nums, 0, arr, 1, n);\n        int m = n + 2;\n        int[][] dp = new int[m][m];\n        for (int len = 2; len < m; len++) {\n            for (int l = 0; l < m - len; l++) {\n                int r = l + len;\n                for (int k = l + 1; k < r; k++) {\n                    int coins = arr[l] * arr[k] * arr[r] + dp[l][k] + dp[k][r];\n                    dp[l][r] = Math.max(dp[l][r], coins);\n                }\n            }\n        }\n        return dp[0][m - 1];\n    }\n}",
            },
        },
    },
]
