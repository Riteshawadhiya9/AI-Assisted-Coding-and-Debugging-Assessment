# Recursion & Backtracking Debugging Problems (6 Questions: C, C++, Java)

RECURSION_QUESTIONS = [
    {
        "id": "q_rec_subsets",
        "title": "Subsets (Power Set Generation)",
        "problemStatement": "Given an integer array `nums` of unique elements, return all possible subsets (the power set).\n\nThe solution set must not contain duplicate subsets. Return the solution in any order.",
        "topic": "recursion",
        "subtopic": "backtracking",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect recursion",
        "bugConcept": "Missing backtracking pop step (removing current element after recursive call), causing all subsets to accumulate all elements monotonically",
        "intendedApproach": "At each index `start`, add a copy of the current subset to results. For `i` from `start` to `n-1`: add nums[i] to subset, recurse with `i + 1`, then pop nums[i] from subset.",
        "explanation": "Backtracking requires restoring the state of the accumulator list after returning from a recursive branch. Without `subset.pop()`, elements from previous branches stay in the accumulator for subsequent branches.",
        "constraints": [
            "1 <= nums.length <= 10",
            "-10 <= nums[i] <= 10",
            "All the numbers of nums are unique.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "nums = [1,2,3]",
                "expectedOutput": "[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]",
                "isHidden": False,
                "explanation": "The power set contains 2^3 = 8 subsets: [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3].",
            },
            {
                "id": 2,
                "input": "nums = [0]",
                "expectedOutput": "[[],[0]]",
                "isHidden": False,
                "explanation": "The single element array has subsets [] and [0].",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "nums = [1,2]",
                "expectedOutput": "[[],[1],[2],[1,2]]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "nums = [4,5,6,7]",
                "expectedOutput": "[[],[4],[5],[6],[7],[4,5],[4,6],[4,7],[5,6],[5,7],[6,7],[4,5,6],[4,5,7],[4,6,7],[5,6,7],[4,5,6,7]]",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "nums = [9]",
                "expectedOutput": "[[],[9]]",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N * 2^N)",
            "space": "O(N)",
        },
        "tags": [
            "recursion",
            "backtracking",
            "subsets",
            "medium",
        ],
        "visualData": {
            "type": "array",
            "title": "Subsets Decision Tree: [1, 2, 3]",
            "data": [
                1,
                2,
                3,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "void backtrack(int* nums, int n, int start, int* current, int curSize) {\n    // record current subset\n    for (int i = start; i < n; i++) {\n        current[curSize] = nums[i];\n        backtrack(nums, n, i + 1, current, curSize);\n    }\n}",
                "correctCode": "void backtrack(int* nums, int n, int start, int* current, int curSize) {\n    // record current subset\n    for (int i = start; i < n; i++) {\n        current[curSize] = nums[i];\n        backtrack(nums, n, i + 1, current, curSize + 1);\n    }\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nvoid backtrack(const vector<int>& nums, int start, vector<int>& curr, vector<vector<int>>& res) {\n    res.push_back(curr);\n    for (size_t i = start; i < nums.size(); i++) {\n        curr.push_back(nums[i]);\n        backtrack(nums, i + 1, curr, res);\n    }\n}\n\nvector<vector<int>> subsets(vector<int>& nums) {\n    vector<vector<int>> res;\n    vector<int> curr;\n    backtrack(nums, 0, curr, res);\n    return res;\n}",
                "correctCode": "#include <vector>\nusing namespace std;\n\nvoid backtrack(const vector<int>& nums, int start, vector<int>& curr, vector<vector<int>>& res) {\n    res.push_back(curr);\n    for (size_t i = start; i < nums.size(); i++) {\n        curr.push_back(nums[i]);\n        backtrack(nums, i + 1, curr, res);\n        curr.pop_back();\n    }\n}\n\nvector<vector<int>> subsets(vector<int>& nums) {\n    vector<vector<int>> res;\n    vector<int> curr;\n    backtrack(nums, 0, curr, res);\n    return res;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    private void backtrack(int[] nums, int start, List<Integer> curr, List<List<Integer>> res) {\n        res.add(new ArrayList<>(curr));\n        for (int i = start; i < nums.length; i++) {\n            curr.add(nums[i]);\n            backtrack(nums, i + 1, curr, res);\n        }\n    }\n    public List<List<Integer>> subsets(int[] nums) {\n        List<List<Integer>> res = new ArrayList<>();\n        backtrack(nums, 0, new ArrayList<>(), res);\n        return res;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    private void backtrack(int[] nums, int start, List<Integer> curr, List<List<Integer>> res) {\n        res.add(new ArrayList<>(curr));\n        for (int i = start; i < nums.length; i++) {\n            curr.add(nums[i]);\n            backtrack(nums, i + 1, curr, res);\n            curr.remove(curr.size() - 1);\n        }\n    }\n    public List<List<Integer>> subsets(int[] nums) {\n        List<List<Integer>> res = new ArrayList<>();\n        backtrack(nums, 0, new ArrayList<>(), res);\n        return res;\n    }\n}",
            },
        },
    },
    {
        "id": "q_rec_permutations",
        "title": "Permutations (All Orderings)",
        "problemStatement": "Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.",
        "topic": "recursion",
        "subtopic": "backtracking",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect recursion",
        "bugConcept": "Failure to reset visited/used boolean flag upon returning from recursive branch",
        "intendedApproach": "Track used elements using a boolean array `used`. If path length equals nums.length, add path to results. Otherwise loop through 0..n-1: if !used[i], set used[i]=true, recurse, and backtrack set used[i]=false and pop path.",
        "explanation": "If `used[i]` is not reset to `false` during backtracking, future recursive branches cannot reuse that element, preventing subsequent permutations from being generated.",
        "constraints": [
            "1 <= nums.length <= 6",
            "-10 <= nums[i] <= 10",
            "All the integers of nums are unique.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "nums = [1,2,3]",
                "expectedOutput": "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]",
                "isHidden": False,
                "explanation": "There are 3! = 6 unique permutations: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].",
            },
            {
                "id": 2,
                "input": "nums = [0,1]",
                "expectedOutput": "[[0,1],[1,0]]",
                "isHidden": False,
                "explanation": "The two permutations are [[0,1],[1,0]].",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "nums = [1]",
                "expectedOutput": "[[1]]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "nums = [5,6,7]",
                "expectedOutput": "[[5,6,7],[5,7,6],[6,5,7],[6,7,5],[7,5,6],[7,6,5]]",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "nums = [1,2,3,4]",
                "expectedOutput": "24 permutations",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N * N!)",
            "space": "O(N)",
        },
        "tags": [
            "recursion",
            "backtracking",
            "permutations",
            "medium",
        ],
        "visualData": {
            "type": "array",
            "title": "Permutation Tree: [1, 2, 3]",
            "data": [
                1,
                2,
                3,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n\nvoid permuteHelper(int* nums, int n, int* curr, int curLen, bool* used) {\n    if (curLen == n) {\n        // record permutation\n        return;\n    }\n    for (int i = 0; i < n; i++) {\n        if (!used[i]) {\n            used[i] = true;\n            curr[curLen] = nums[i];\n            permuteHelper(nums, n, curr, curLen + 1, used);\n        }\n    }\n}",
                "correctCode": "#include <stdbool.h>\n\nvoid permuteHelper(int* nums, int n, int* curr, int curLen, bool* used) {\n    if (curLen == n) {\n        // record permutation\n        return;\n    }\n    for (int i = 0; i < n; i++) {\n        if (!used[i]) {\n            used[i] = true;\n            curr[curLen] = nums[i];\n            permuteHelper(nums, n, curr, curLen + 1, used);\n            used[i] = false;\n        }\n    }\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nvoid backtrack(const vector<int>& nums, vector<int>& curr, vector<bool>& used, vector<vector<int>>& res) {\n    if (curr.size() == nums.size()) {\n        res.push_back(curr);\n        return;\n    }\n    for (size_t i = 0; i < nums.size(); i++) {\n        if (!used[i]) {\n            used[i] = true;\n            curr.push_back(nums[i]);\n            backtrack(nums, curr, used, res);\n            curr.pop_back();\n        }\n    }\n}\n\nvector<vector<int>> permute(vector<int>& nums) {\n    vector<vector<int>> res;\n    vector<int> curr;\n    vector<bool> used(nums.size(), false);\n    backtrack(nums, curr, used, res);\n    return res;\n}",
                "correctCode": "#include <vector>\nusing namespace std;\n\nvoid backtrack(const vector<int>& nums, vector<int>& curr, vector<bool>& used, vector<vector<int>>& res) {\n    if (curr.size() == nums.size()) {\n        res.push_back(curr);\n        return;\n    }\n    for (size_t i = 0; i < nums.size(); i++) {\n        if (!used[i]) {\n            used[i] = true;\n            curr.push_back(nums[i]);\n            backtrack(nums, curr, used, res);\n            curr.pop_back();\n            used[i] = false;\n        }\n    }\n}\n\nvector<vector<int>> permute(vector<int>& nums) {\n    vector<vector<int>> res;\n    vector<int> curr;\n    vector<bool> used(nums.size(), false);\n    backtrack(nums, curr, used, res);\n    return res;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    private void backtrack(int[] nums, List<Integer> curr, boolean[] used, List<List<Integer>> res) {\n        if (curr.size() == nums.length) {\n            res.add(new ArrayList<>(curr));\n            return;\n        }\n        for (int i = 0; i < nums.length; i++) {\n            if (!used[i]) {\n                used[i] = true;\n                curr.add(nums[i]);\n                backtrack(nums, curr, used, res);\n                curr.remove(curr.size() - 1);\n            }\n        }\n    }\n    public List<List<Integer>> permute(int[] nums) {\n        List<List<Integer>> res = new ArrayList<>();\n        backtrack(nums, new ArrayList<>(), new boolean[nums.length], res);\n        return res;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    private void backtrack(int[] nums, List<Integer> curr, boolean[] used, List<List<Integer>> res) {\n        if (curr.size() == nums.length) {\n            res.add(new ArrayList<>(curr));\n            return;\n        }\n        for (int i = 0; i < nums.length; i++) {\n            if (!used[i]) {\n                used[i] = true;\n                curr.add(nums[i]);\n                backtrack(nums, curr, used, res);\n                curr.remove(curr.size() - 1);\n                used[i] = false;\n            }\n        }\n    }\n    public List<List<Integer>> permute(int[] nums) {\n        List<List<Integer>> res = new ArrayList<>();\n        backtrack(nums, new ArrayList<>(), new boolean[nums.length], res);\n        return res;\n    }\n}",
            },
        },
    },
    {
        "id": "q_rec_combination_sum",
        "title": "Combination Sum (Unbounded Re-use)",
        "problemStatement": "Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.\n\nThe same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.\n\nThe test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.",
        "topic": "recursion",
        "subtopic": "backtracking",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect recursion",
        "bugConcept": "Advancing start index to i+1 instead of i on recursive call, preventing numbers from being reused",
        "intendedApproach": "Backtrack from index `start`. Since elements can be reused, recurse with same index `i` (not `i + 1`) when `target - candidates[i] >= 0`.",
        "explanation": "Because candidates can be reused unlimited times, recursing with `i + 1` disallows repeating the current candidate (e.g. 2 + 2 + 3 = 7 for target 7 with candidate 2 becomes impossible).",
        "constraints": [
            "1 <= candidates.length <= 30",
            "2 <= candidates[i] <= 40",
            "All elements of candidates are distinct.",
            "1 <= target <= 40",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "candidates = [2,3,6,7], target = 7",
                "expectedOutput": "[[2,2,3],[7]]",
                "isHidden": False,
                "explanation": "2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is also a candidate, and 7 = 7. These are the only two combinations.",
            },
            {
                "id": 2,
                "input": "candidates = [2,3,5], target = 8",
                "expectedOutput": "[[2,2,2,2],[2,3,3],[3,5]]",
                "isHidden": False,
                "explanation": "2 + 2 + 2 + 2 = 8, 2 + 3 + 3 = 8, and 3 + 5 = 8 are the valid combinations summing to 8.",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "candidates = [2], target = 1",
                "expectedOutput": "[]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "candidates = [1], target = 2",
                "expectedOutput": "[[1,1]]",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "candidates = [3,4,5], target = 9",
                "expectedOutput": "[[3,3,3],[4,5]]",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N^(T/M))",
            "space": "O(T/M)",
        },
        "tags": [
            "recursion",
            "backtracking",
            "medium",
        ],
        "visualData": {
            "type": "array",
            "title": "Candidates Array",
            "data": [
                2,
                3,
                6,
                7,
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "void backtrack(int* cand, int n, int target, int start, int* curr, int curLen) {\n    if (target == 0) { /* record */ return; }\n    if (target < 0) return;\n    for (int i = start; i < n; i++) {\n        curr[curLen] = cand[i];\n        backtrack(cand, n, target - cand[i], i + 1, curr, curLen + 1);\n    }\n}",
                "correctCode": "void backtrack(int* cand, int n, int target, int start, int* curr, int curLen) {\n    if (target == 0) { /* record */ return; }\n    if (target < 0) return;\n    for (int i = start; i < n; i++) {\n        curr[curLen] = cand[i];\n        backtrack(cand, n, target - cand[i], i, curr, curLen + 1);\n    }\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\nusing namespace std;\n\nvoid backtrack(const vector<int>& cand, int target, int start, vector<int>& curr, vector<vector<int>>& res) {\n    if (target == 0) {\n        res.push_back(curr);\n        return;\n    }\n    if (target < 0) return;\n    for (size_t i = start; i < cand.size(); i++) {\n        curr.push_back(cand[i]);\n        backtrack(cand, target - cand[i], i + 1, curr, res);\n        curr.pop_back();\n    }\n}\n\nvector<vector<int>> combinationSum(vector<int>& candidates, int target) {\n    vector<vector<int>> res;\n    vector<int> curr;\n    backtrack(candidates, target, 0, curr, res);\n    return res;\n}",
                "correctCode": "#include <vector>\nusing namespace std;\n\nvoid backtrack(const vector<int>& cand, int target, int start, vector<int>& curr, vector<vector<int>>& res) {\n    if (target == 0) {\n        res.push_back(curr);\n        return;\n    }\n    if (target < 0) return;\n    for (size_t i = start; i < cand.size(); i++) {\n        curr.push_back(cand[i]);\n        backtrack(cand, target - cand[i], i, curr, res);\n        curr.pop_back();\n    }\n}\n\nvector<vector<int>> combinationSum(vector<int>& candidates, int target) {\n    vector<vector<int>> res;\n    vector<int> curr;\n    backtrack(candidates, target, 0, curr, res);\n    return res;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    private void backtrack(int[] cand, int target, int start, List<Integer> curr, List<List<Integer>> res) {\n        if (target == 0) {\n            res.add(new ArrayList<>(curr));\n            return;\n        }\n        if (target < 0) return;\n        for (int i = start; i < cand.length; i++) {\n            curr.add(cand[i]);\n            backtrack(cand, target - cand[i], i + 1, curr, res);\n            curr.remove(curr.size() - 1);\n        }\n    }\n    public List<List<Integer>> combinationSum(int[] candidates, int target) {\n        List<List<Integer>> res = new ArrayList<>();\n        backtrack(candidates, target, 0, new ArrayList<>(), res);\n        return res;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    private void backtrack(int[] cand, int target, int start, List<Integer> curr, List<List<Integer>> res) {\n        if (target == 0) {\n            res.add(new ArrayList<>(curr));\n            return;\n        }\n        if (target < 0) return;\n        for (int i = start; i < cand.length; i++) {\n            curr.add(cand[i]);\n            backtrack(cand, target - cand[i], i, curr, res);\n            curr.remove(curr.size() - 1);\n        }\n    }\n    public List<List<Integer>> combinationSum(int[] candidates, int target) {\n        List<List<Integer>> res = new ArrayList<>();\n        backtrack(candidates, target, 0, new ArrayList<>(), res);\n        return res;\n    }\n}",
            },
        },
    },
    {
        "id": "q_rec_word_search",
        "title": "Word Search (2D Board Backtracking)",
        "problemStatement": "Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.\n\nThe word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.",
        "topic": "recursion",
        "subtopic": "backtracking",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "incorrect recursion",
        "bugConcept": "Failure to unmark visited board cell upon backtrack return, causing false negatives in subsequent searches",
        "intendedApproach": "For each cell (r, c), start DFS. If board[r][c] != word[k], return false. Temporarily mark board[r][c] = '#'. Search all 4 neighbors for k+1. Restore board[r][c] = originalChar and return result.",
        "explanation": "If `board[r][c]` is changed to `#` to mark it visited but not restored when the path fails, future alternative search paths originating from other directions cannot use this cell.",
        "constraints": [
            "m == board.length",
            "n = board[i].length",
            "1 <= m, n <= 6",
            "1 <= word.length <= 15",
            "board and word consist of only lowercase and uppercase English letters.",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCCED\"",
                "expectedOutput": "true",
                "isHidden": False,
                "explanation": "The word \"ABCCED\" can be traced along the path (0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(2,1).",
            },
            {
                "id": 2,
                "input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"SEE\"",
                "expectedOutput": "true",
                "isHidden": False,
                "explanation": "The word \"SEE\" can be traced along (1,3)->(2,3)->(2,2).",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCB\"",
                "expectedOutput": "false",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "board = [[\"a\"]], word = \"a\"",
                "expectedOutput": "true",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "board = [[\"a\",\"b\"],[\"c\",\"d\"]], word = \"acdb\"",
                "expectedOutput": "true",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(M * N * 3^L)",
            "space": "O(L)",
        },
        "tags": [
            "recursion",
            "backtracking",
            "matrix",
            "medium",
        ],
        "visualData": {
            "type": "matrix",
            "title": "Grid Board: 3x4",
            "data": [
                [
                    "A",
                    "B",
                    "C",
                    "E",
                ],
                [
                    "S",
                    "F",
                    "C",
                    "S",
                ],
                [
                    "A",
                    "D",
                    "E",
                    "E",
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n#include <string.h>\n\nbool dfs(char** board, int m, int n, int r, int c, char* word, int k) {\n    if (word[k] == '\\0') return true;\n    if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != word[k]) return false;\n    char temp = board[r][c];\n    board[r][c] = '#';\n    bool found = dfs(board, m, n, r + 1, c, word, k + 1) ||\n                 dfs(board, m, n, r - 1, c, word, k + 1) ||\n                 dfs(board, m, n, r, c + 1, word, k + 1) ||\n                 dfs(board, m, n, r, c - 1, word, k + 1);\n    return found;\n}",
                "correctCode": "#include <stdbool.h>\n#include <string.h>\n\nbool dfs(char** board, int m, int n, int r, int c, char* word, int k) {\n    if (word[k] == '\\0') return true;\n    if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != word[k]) return false;\n    char temp = board[r][c];\n    board[r][c] = '#';\n    bool found = dfs(board, m, n, r + 1, c, word, k + 1) ||\n                 dfs(board, m, n, r - 1, c, word, k + 1) ||\n                 dfs(board, m, n, r, c + 1, word, k + 1) ||\n                 dfs(board, m, n, r, c - 1, word, k + 1);\n    board[r][c] = temp;\n    return found;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <string>\nusing namespace std;\n\nbool dfs(vector<vector<char>>& board, int r, int c, const string& word, int k) {\n    if (k == (int)word.length()) return true;\n    if (r < 0 || r >= (int)board.size() || c < 0 || c >= (int)board[0].size() || board[r][c] != word[k]) {\n        return false;\n    }\n    char temp = board[r][c];\n    board[r][c] = '#';\n    bool found = dfs(board, r + 1, c, word, k + 1) ||\n                 dfs(board, r - 1, c, word, k + 1) ||\n                 dfs(board, r, c + 1, word, k + 1) ||\n                 dfs(board, r, c - 1, word, k + 1);\n    return found;\n}",
                "correctCode": "#include <vector>\n#include <string>\nusing namespace std;\n\nbool dfs(vector<vector<char>>& board, int r, int c, const string& word, int k) {\n    if (k == (int)word.length()) return true;\n    if (r < 0 || r >= (int)board.size() || c < 0 || c >= (int)board[0].size() || board[r][c] != word[k]) {\n        return false;\n    }\n    char temp = board[r][c];\n    board[r][c] = '#';\n    bool found = dfs(board, r + 1, c, word, k + 1) ||\n                 dfs(board, r - 1, c, word, k + 1) ||\n                 dfs(board, r, c + 1, word, k + 1) ||\n                 dfs(board, r, c - 1, word, k + 1);\n    board[r][c] = temp;\n    return found;\n}",
            },
            "java": {
                "buggyCode": "class Solution {\n    private boolean dfs(char[][] board, int r, int c, String word, int k) {\n        if (k == word.length()) return true;\n        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(k)) {\n            return false;\n        }\n        char temp = board[r][c];\n        board[r][c] = '#';\n        boolean found = dfs(board, r + 1, c, word, k + 1) ||\n                        dfs(board, r - 1, c, word, k + 1) ||\n                        dfs(board, r, c + 1, word, k + 1) ||\n                        dfs(board, r, c - 1, word, k + 1);\n        return found;\n    }\n    public boolean exist(char[][] board, String word) {\n        for (int r = 0; r < board.length; r++) {\n            for (int c = 0; c < board[0].length; c++) {\n                if (dfs(board, r, c, word, 0)) return true;\n            }\n        }\n        return false;\n    }\n}",
                "correctCode": "class Solution {\n    private boolean dfs(char[][] board, int r, int c, String word, int k) {\n        if (k == word.length()) return true;\n        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(k)) {\n            return false;\n        }\n        char temp = board[r][c];\n        board[r][c] = '#';\n        boolean found = dfs(board, r + 1, c, word, k + 1) ||\n                        dfs(board, r - 1, c, word, k + 1) ||\n                        dfs(board, r, c + 1, word, k + 1) ||\n                        dfs(board, r, c - 1, word, k + 1);\n        board[r][c] = temp;\n        return found;\n    }\n    public boolean exist(char[][] board, String word) {\n        for (int r = 0; r < board.length; r++) {\n            for (int c = 0; c < board[0].length; c++) {\n                if (dfs(board, r, c, word, 0)) return true;\n            }\n        }\n        return false;\n    }\n}",
            },
        },
    },
    {
        "id": "q_rec_generate_parentheses",
        "title": "Generate Parentheses",
        "problemStatement": "Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.",
        "topic": "recursion",
        "subtopic": "backtracking",
        "difficulty": "medium",
        "estimatedTime": 20,
        "primaryBugType": "boundary",
        "bugConcept": "Wrong condition for placing closing parenthesis (close < n instead of close < open)",
        "intendedApproach": "Maintain open and close counts. Can add '(' if open < n. Can add ')' ONLY if close < open. When open == n && close == n, record combination.",
        "explanation": "If closing parenthesis condition is `close < n`, it allows adding closing parentheses before corresponding opening ones (e.g. producing \")(\"), creating ill-formed sequences.",
        "constraints": [
            "1 <= n <= 8",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "n = 3",
                "expectedOutput": "[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]",
                "isHidden": False,
                "explanation": "There are 5 valid well-formed combinations for n = 3: \"((()))\", \"(()())\", \"(())()\", \"()(())\", \"()()()\".",
            },
            {
                "id": 2,
                "input": "n = 1",
                "expectedOutput": "[\"()\"]",
                "isHidden": False,
                "explanation": "The only well-formed combination for n = 1 is \"()\".",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "n = 2",
                "expectedOutput": "[\"(())\",\"()()\"]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "n = 4",
                "expectedOutput": "14 combinations",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(4^N / sqrt(N))",
            "space": "O(N)",
        },
        "tags": [
            "recursion",
            "backtracking",
            "strings",
            "medium",
        ],
        "visualData": {
            "type": "array",
            "title": "Parentheses Balance State",
            "data": [
                "(",
                "(",
                "(",
                ")",
                ")",
                ")",
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "void backtrack(int n, int open, int close, char* curr, int len) {\n    if (open == n && close == n) {\n        curr[len] = '\\0';\n        // record\n        return;\n    }\n    if (open < n) {\n        curr[len] = '(';\n        backtrack(n, open + 1, close, curr, len + 1);\n    }\n    if (close < n) {\n        curr[len] = ')';\n        backtrack(n, open, close + 1, curr, len + 1);\n    }\n}",
                "correctCode": "void backtrack(int n, int open, int close, char* curr, int len) {\n    if (open == n && close == n) {\n        curr[len] = '\\0';\n        // record\n        return;\n    }\n    if (open < n) {\n        curr[len] = '(';\n        backtrack(n, open + 1, close, curr, len + 1);\n    }\n    if (close < open) {\n        curr[len] = ')';\n        backtrack(n, open, close + 1, curr, len + 1);\n    }\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <string>\nusing namespace std;\n\nvoid backtrack(int n, int open, int close, string curr, vector<string>& res) {\n    if (open == n && close == n) {\n        res.push_back(curr);\n        return;\n    }\n    if (open < n) {\n        backtrack(n, open + 1, close, curr + '(', res);\n    }\n    if (close < n) {\n        backtrack(n, open, close + 1, curr + ')', res);\n    }\n}\n\nvector<string> generateParenthesis(int n) {\n    vector<string> res;\n    backtrack(n, 0, 0, \"\", res);\n    return res;\n}",
                "correctCode": "#include <vector>\n#include <string>\nusing namespace std;\n\nvoid backtrack(int n, int open, int close, string curr, vector<string>& res) {\n    if (open == n && close == n) {\n        res.push_back(curr);\n        return;\n    }\n    if (open < n) {\n        backtrack(n, open + 1, close, curr + '(', res);\n    }\n    if (close < open) {\n        backtrack(n, open, close + 1, curr + ')', res);\n    }\n}\n\nvector<string> generateParenthesis(int n) {\n    vector<string> res;\n    backtrack(n, 0, 0, \"\", res);\n    return res;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    private void backtrack(int n, int open, int close, StringBuilder curr, List<String> res) {\n        if (open == n && close == n) {\n            res.add(curr.toString());\n            return;\n        }\n        if (open < n) {\n            curr.append('(');\n            backtrack(n, open + 1, close, curr, res);\n            curr.deleteCharAt(curr.length() - 1);\n        }\n        if (close < n) {\n            curr.append(')');\n            backtrack(n, open, close + 1, curr, res);\n            curr.deleteCharAt(curr.length() - 1);\n        }\n    }\n    public List<String> generateParenthesis(int n) {\n        List<String> res = new ArrayList<>();\n        backtrack(n, 0, 0, new StringBuilder(), res);\n        return res;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    private void backtrack(int n, int open, int close, StringBuilder curr, List<String> res) {\n        if (open == n && close == n) {\n            res.add(curr.toString());\n            return;\n        }\n        if (open < n) {\n            curr.append('(');\n            backtrack(n, open + 1, close, curr, res);\n            curr.deleteCharAt(curr.length() - 1);\n        }\n        if (close < open) {\n            curr.append(')');\n            backtrack(n, open, close + 1, curr, res);\n            curr.deleteCharAt(curr.length() - 1);\n        }\n    }\n    public List<String> generateParenthesis(int n) {\n        List<String> res = new ArrayList<>();\n        backtrack(n, 0, 0, new StringBuilder(), res);\n        return res;\n    }\n}",
            },
        },
    },
    {
        "id": "q_rec_n_queens",
        "title": "N-Queens (Distinct Board Solutions)",
        "problemStatement": "The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.\n\nGiven an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.\n\nEach solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.",
        "topic": "recursion",
        "subtopic": "backtracking",
        "difficulty": "hard",
        "estimatedTime": 25,
        "primaryBugType": "boundary",
        "bugConcept": "Wrong diagonal index calculation formula for anti-diagonal (row + col vs row - col + n)",
        "intendedApproach": "Place row by row. Track occupied columns, main diagonals `row - col + n`, and anti-diagonals `row + col`. If all are free, place Queen, mark sets, and recurse to `row + 1`.",
        "explanation": "Main diagonals have constant `row - col` (offset by n to avoid negative indices), while anti-diagonals have constant `row + col`. Confusing the two formulas allows conflicting diagonal queen attacks.",
        "constraints": [
            "1 <= n <= 9",
        ],
        "visibleTestCases": [
            {
                "id": 1,
                "input": "n = 4",
                "expectedOutput": "[[\\\".Q..\\\",\\\"...Q\\\",\\\"Q...\\\",\\\"..Q.\\\"],[\\\"..Q.\\\",\\\"Q...\\\",\\\"...Q\\\",\\\".Q..\\\"]]",
                "isHidden": False,
                "explanation": "There exist two distinct solutions to the 4-queens puzzle as shown above.",
            },
            {
                "id": 2,
                "input": "n = 1",
                "expectedOutput": "[[\\\"Q\\\"]]",
                "isHidden": False,
                "explanation": "There is only 1 solution for a 1x1 board: [\"Q\"].",
            },
        ],
        "hiddenTestCases": [
            {
                "id": 3,
                "input": "n = 2",
                "expectedOutput": "[]",
                "isHidden": True,
            },
            {
                "id": 4,
                "input": "n = 3",
                "expectedOutput": "[]",
                "isHidden": True,
            },
            {
                "id": 5,
                "input": "n = 5",
                "expectedOutput": "10 solutions",
                "isHidden": True,
            },
        ],
        "expectedComplexity": {
            "time": "O(N!)",
            "space": "O(N^2)",
        },
        "tags": [
            "recursion",
            "backtracking",
            "matrix",
            "hard",
        ],
        "visualData": {
            "type": "matrix",
            "title": "4x4 N-Queens Board Placement",
            "data": [
                [
                    ".",
                    "Q",
                    ".",
                    ".",
                ],
                [
                    ".",
                    ".",
                    ".",
                    "Q",
                ],
                [
                    "Q",
                    ".",
                    ".",
                    ".",
                ],
                [
                    ".",
                    ".",
                    "Q",
                    ".",
                ],
            ],
        },
        "implementations": {
            "c": {
                "buggyCode": "#include <stdbool.h>\n#include <string.h>\n\nbool isSafe(int* queens, int row, int col) {\n    for (int r = 0; r < row; r++) {\n        int c = queens[r];\n        if (c == col) return false;\n        if (row - r == col - c) return false;\n    }\n    return true;\n}",
                "correctCode": "#include <stdbool.h>\n#include <stdlib.h>\n\nbool isSafe(int* queens, int row, int col) {\n    for (int r = 0; r < row; r++) {\n        int c = queens[r];\n        if (c == col) return false;\n        if (abs(row - r) == abs(col - c)) return false;\n    }\n    return true;\n}",
            },
            "cpp": {
                "buggyCode": "#include <vector>\n#include <string>\n#include <cmath>\nusing namespace std;\n\nbool isSafe(const vector<int>& queens, int row, int col) {\n    for (int r = 0; r < row; r++) {\n        int c = queens[r];\n        if (c == col) return false;\n        if (row - r == col - c) return false;\n    }\n    return true;\n}",
                "correctCode": "#include <vector>\n#include <string>\n#include <cmath>\nusing namespace std;\n\nbool isSafe(const vector<int>& queens, int row, int col) {\n    for (int r = 0; r < row; r++) {\n        int c = queens[r];\n        if (c == col) return false;\n        if (abs(row - r) == abs(col - c)) return false;\n    }\n    return true;\n}",
            },
            "java": {
                "buggyCode": "import java.util.*;\n\nclass Solution {\n    private boolean isSafe(int[] queens, int row, int col) {\n        for (int r = 0; r < row; r++) {\n            int c = queens[r];\n            if (c == col) return false;\n            if (row - r == col - c) return false;\n        }\n        return true;\n    }\n}",
                "correctCode": "import java.util.*;\n\nclass Solution {\n    private boolean isSafe(int[] queens, int row, int col) {\n        for (int r = 0; r < row; r++) {\n            int c = queens[r];\n            if (c == col) return false;\n            if (Math.abs(row - r) == Math.abs(col - c)) return false;\n        }\n        return true;\n    }\n}",
            },
        },
    },
]
