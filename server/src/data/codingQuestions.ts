/**
 * ============================================================================
 * CODING QUESTION BANK — AI-ASSISTED CODING SECTION
 * ============================================================================
 * 50 LeetCode-style DSA problems across 20 topics.
 * Each problem has:  title, difficulty, topic, problem statement,
 * examples, constraints, function signatures, starter code, solution code,
 * test cases, tags, and estimated time.
 *
 * Languages supported: C, C++, Java, Python, JavaScript
 * ============================================================================
 */

import { CodingQuestion } from '../types/codingTypes';

const codingQuestions: CodingQuestion[] = [
  // ═══════════════════════════════════════════════════════════════════════════
  // ARRAYS (3 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_arr_two_sum',
    title: 'Two Sum',
    difficulty: 'easy',
    topic: 'arrays',
    problemStatement: `Given an array of integers \`nums\` and an integer \`target\`, return the indices of the two numbers that add up to \`target\`.\n\nYou may assume that each input has exactly one solution, and you may not use the same element twice.\n\nReturn the answer in any order.`,
    examples: [
      { input: 'nums = [2,7,11,15], target = 9', output: '[0,1]', explanation: 'nums[0] + nums[1] = 2 + 7 = 9.' },
      { input: 'nums = [3,2,4], target = 6', output: '[1,2]', explanation: 'nums[1] + nums[2] = 2 + 4 = 6.' },
    ],
    constraints: ['2 <= nums.length <= 10^4', '-10^9 <= nums[i] <= 10^9', '-10^9 <= target <= 10^9', 'Only one valid answer exists.'],
    functionSignature: {
      python: 'def twoSum(nums: List[int], target: int) -> List[int]:',
      javascript: 'function twoSum(nums, target)',
      cpp: 'vector<int> twoSum(vector<int>& nums, int target)',
      java: 'public int[] twoSum(int[] nums, int target)',
      c: 'int* twoSum(int* nums, int numsSize, int target, int* returnSize)',
    },
    starterCode: {
      python: `def twoSum(nums, target):\n    # Write your solution here\n    pass`,
      javascript: `function twoSum(nums, target) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<int> twoSum(vector<int>& nums, int target) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public int[] twoSum(int[] nums, int target) {\n        // Write your solution here\n        return new int[]{};\n    }\n}`,
    },
    solutionCode: {
      python: `def twoSum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n    return []`,
      javascript: `function twoSum(nums, target) {\n    const map = new Map();\n    for (let i = 0; i < nums.length; i++) {\n        const complement = target - nums[i];\n        if (map.has(complement)) return [map.get(complement), i];\n        map.set(nums[i], i);\n    }\n    return [];\n}`,
    },
    testCases: [
      { id: 1, input: 'nums = [2,7,11,15], target = 9', expectedOutput: '[0,1]', isHidden: false },
      { id: 2, input: 'nums = [3,2,4], target = 6', expectedOutput: '[1,2]', isHidden: false },
      { id: 3, input: 'nums = [3,3], target = 6', expectedOutput: '[0,1]', isHidden: true },
    ],
    tags: ['array', 'hash-table'],
    estimatedTime: 10,
  },
  {
    id: 'cq_arr_max_subarray',
    title: 'Maximum Subarray',
    difficulty: 'medium',
    topic: 'arrays',
    problemStatement: `Given an integer array \`nums\`, find the subarray with the largest sum, and return its sum.\n\nA subarray is a contiguous non-empty sequence of elements within an array.`,
    examples: [
      { input: 'nums = [-2,1,-3,4,-1,2,1,-5,4]', output: '6', explanation: 'The subarray [4,-1,2,1] has the largest sum 6.' },
      { input: 'nums = [1]', output: '1', explanation: 'The subarray [1] has the largest sum 1.' },
    ],
    constraints: ['1 <= nums.length <= 10^5', '-10^4 <= nums[i] <= 10^4'],
    functionSignature: {
      python: 'def maxSubArray(nums: List[int]) -> int:',
      javascript: 'function maxSubArray(nums)',
      cpp: 'int maxSubArray(vector<int>& nums)',
      java: 'public int maxSubArray(int[] nums)',
    },
    starterCode: {
      python: `def maxSubArray(nums):\n    # Write your solution here\n    pass`,
      javascript: `function maxSubArray(nums) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint maxSubArray(vector<int>& nums) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int maxSubArray(int[] nums) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def maxSubArray(nums):\n    max_sum = nums[0]\n    current = nums[0]\n    for i in range(1, len(nums)):\n        current = max(nums[i], current + nums[i])\n        max_sum = max(max_sum, current)\n    return max_sum`,
      javascript: `function maxSubArray(nums) {\n    let maxSum = nums[0], current = nums[0];\n    for (let i = 1; i < nums.length; i++) {\n        current = Math.max(nums[i], current + nums[i]);\n        maxSum = Math.max(maxSum, current);\n    }\n    return maxSum;\n}`,
    },
    testCases: [
      { id: 1, input: 'nums = [-2,1,-3,4,-1,2,1,-5,4]', expectedOutput: '6', isHidden: false },
      { id: 2, input: 'nums = [1]', expectedOutput: '1', isHidden: false },
      { id: 3, input: 'nums = [5,4,-1,7,8]', expectedOutput: '23', isHidden: true },
      { id: 4, input: 'nums = [-1]', expectedOutput: '-1', isHidden: true },
    ],
    tags: ['array', 'dynamic-programming', 'kadane'],
    estimatedTime: 15,
  },
  {
    id: 'cq_arr_prod_except_self',
    title: 'Product of Array Except Self',
    difficulty: 'medium',
    topic: 'arrays',
    problemStatement: `Given an integer array \`nums\`, return an array \`answer\` such that \`answer[i]\` is equal to the product of all the elements of \`nums\` except \`nums[i]\`.\n\nThe product of any prefix or suffix of \`nums\` is guaranteed to fit in a 32-bit integer.\n\nYou must write an algorithm that runs in O(n) time and without using the division operation.`,
    examples: [
      { input: 'nums = [1,2,3,4]', output: '[24,12,8,6]', explanation: 'For index 0: 2*3*4=24; index 1: 1*3*4=12; index 2: 1*2*4=8; index 3: 1*2*3=6.' },
      { input: 'nums = [-1,1,0,-3,3]', output: '[0,0,9,0,0]', explanation: 'Zero makes all products zero except the one at the zero position.' },
    ],
    constraints: ['2 <= nums.length <= 10^5', '-30 <= nums[i] <= 30', 'Product of any prefix/suffix fits in a 32-bit integer'],
    functionSignature: {
      python: 'def productExceptSelf(nums: List[int]) -> List[int]:',
      javascript: 'function productExceptSelf(nums)',
      cpp: 'vector<int> productExceptSelf(vector<int>& nums)',
      java: 'public int[] productExceptSelf(int[] nums)',
    },
    starterCode: {
      python: `def productExceptSelf(nums):\n    # Write your solution here\n    pass`,
      javascript: `function productExceptSelf(nums) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<int> productExceptSelf(vector<int>& nums) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public int[] productExceptSelf(int[] nums) {\n        // Write your solution here\n        return new int[]{};\n    }\n}`,
    },
    solutionCode: {
      python: `def productExceptSelf(nums):\n    n = len(nums)\n    result = [1] * n\n    prefix = 1\n    for i in range(n):\n        result[i] = prefix\n        prefix *= nums[i]\n    suffix = 1\n    for i in range(n - 1, -1, -1):\n        result[i] *= suffix\n        suffix *= nums[i]\n    return result`,
    },
    testCases: [
      { id: 1, input: 'nums = [1,2,3,4]', expectedOutput: '[24,12,8,6]', isHidden: false },
      { id: 2, input: 'nums = [-1,1,0,-3,3]', expectedOutput: '[0,0,9,0,0]', isHidden: false },
      { id: 3, input: 'nums = [2,3]', expectedOutput: '[3,2]', isHidden: true },
    ],
    tags: ['array', 'prefix-product'],
    estimatedTime: 20,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // STRINGS (3 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_str_valid_anagram',
    title: 'Valid Anagram',
    difficulty: 'easy',
    topic: 'strings',
    problemStatement: `Given two strings \`s\` and \`t\`, return \`true\` if \`t\` is an anagram of \`s\`, and \`false\` otherwise.\n\nAn anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.`,
    examples: [
      { input: 's = "anagram", t = "nagaram"', output: 'true', explanation: 'Both strings contain the same characters with the same frequencies.' },
      { input: 's = "rat", t = "car"', output: 'false', explanation: '"rat" and "car" do not contain the same characters.' },
    ],
    constraints: ['1 <= s.length, t.length <= 5 * 10^4', 's and t consist of lowercase English letters'],
    functionSignature: {
      python: 'def isAnagram(s: str, t: str) -> bool:',
      javascript: 'function isAnagram(s, t)',
      cpp: 'bool isAnagram(string s, string t)',
      java: 'public boolean isAnagram(String s, String t)',
    },
    starterCode: {
      python: `def isAnagram(s, t):\n    # Write your solution here\n    pass`,
      javascript: `function isAnagram(s, t) {\n    // Write your solution here\n}`,
      cpp: `#include <string>\nusing namespace std;\n\nbool isAnagram(string s, string t) {\n    // Write your solution here\n    return false;\n}`,
      java: `class Solution {\n    public boolean isAnagram(String s, String t) {\n        // Write your solution here\n        return false;\n    }\n}`,
    },
    solutionCode: {
      python: `def isAnagram(s, t):\n    if len(s) != len(t):\n        return False\n    count = {}\n    for c in s:\n        count[c] = count.get(c, 0) + 1\n    for c in t:\n        count[c] = count.get(c, 0) - 1\n        if count[c] < 0:\n            return False\n    return True`,
    },
    testCases: [
      { id: 1, input: 's = "anagram", t = "nagaram"', expectedOutput: 'true', isHidden: false },
      { id: 2, input: 's = "rat", t = "car"', expectedOutput: 'false', isHidden: false },
      { id: 3, input: 's = "a", t = "a"', expectedOutput: 'true', isHidden: true },
    ],
    tags: ['string', 'hash-table', 'sorting'],
    estimatedTime: 10,
  },
  {
    id: 'cq_str_longest_no_repeat',
    title: 'Longest Substring Without Repeating Characters',
    difficulty: 'medium',
    topic: 'strings',
    problemStatement: `Given a string \`s\`, find the length of the longest substring without repeating characters.`,
    examples: [
      { input: 's = "abcabcbb"', output: '3', explanation: 'The answer is "abc", with length 3.' },
      { input: 's = "bbbbb"', output: '1', explanation: 'The answer is "b", with length 1.' },
      { input: 's = "pwwkew"', output: '3', explanation: 'The answer is "wke", with length 3.' },
    ],
    constraints: ['0 <= s.length <= 5 * 10^4', 's consists of English letters, digits, symbols and spaces'],
    functionSignature: {
      python: 'def lengthOfLongestSubstring(s: str) -> int:',
      javascript: 'function lengthOfLongestSubstring(s)',
      cpp: 'int lengthOfLongestSubstring(string s)',
      java: 'public int lengthOfLongestSubstring(String s)',
    },
    starterCode: {
      python: `def lengthOfLongestSubstring(s):\n    # Write your solution here\n    pass`,
      javascript: `function lengthOfLongestSubstring(s) {\n    // Write your solution here\n}`,
      cpp: `#include <string>\nusing namespace std;\n\nint lengthOfLongestSubstring(string s) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int lengthOfLongestSubstring(String s) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def lengthOfLongestSubstring(s):\n    char_index = {}\n    left = 0\n    max_len = 0\n    for right, c in enumerate(s):\n        if c in char_index and char_index[c] >= left:\n            left = char_index[c] + 1\n        char_index[c] = right\n        max_len = max(max_len, right - left + 1)\n    return max_len`,
    },
    testCases: [
      { id: 1, input: 's = "abcabcbb"', expectedOutput: '3', isHidden: false },
      { id: 2, input: 's = "bbbbb"', expectedOutput: '1', isHidden: false },
      { id: 3, input: 's = "pwwkew"', expectedOutput: '3', isHidden: false },
      { id: 4, input: 's = ""', expectedOutput: '0', isHidden: true },
    ],
    tags: ['string', 'sliding-window', 'hash-table'],
    estimatedTime: 15,
  },
  {
    id: 'cq_str_min_window',
    title: 'Minimum Window Substring',
    difficulty: 'hard',
    topic: 'strings',
    problemStatement: `Given two strings \`s\` and \`t\` of lengths \`m\` and \`n\` respectively, return the minimum window substring of \`s\` such that every character in \`t\` (including duplicates) is included in the window.\n\nIf there is no such substring, return the empty string \`""\`.\n\nThe answer is guaranteed to be unique.`,
    examples: [
      { input: 's = "ADOBECODEBANC", t = "ABC"', output: '"BANC"', explanation: 'The minimum window substring "BANC" contains A, B, and C from string t.' },
      { input: 's = "a", t = "a"', output: '"a"', explanation: 'The entire string s is the minimum window.' },
    ],
    constraints: ['m == s.length', 'n == t.length', '1 <= m, n <= 10^5', 's and t consist of uppercase and lowercase English letters'],
    functionSignature: {
      python: 'def minWindow(s: str, t: str) -> str:',
      javascript: 'function minWindow(s, t)',
      cpp: 'string minWindow(string s, string t)',
      java: 'public String minWindow(String s, String t)',
    },
    starterCode: {
      python: `def minWindow(s, t):\n    # Write your solution here\n    pass`,
      javascript: `function minWindow(s, t) {\n    // Write your solution here\n}`,
      cpp: `#include <string>\nusing namespace std;\n\nstring minWindow(string s, string t) {\n    // Write your solution here\n    return "";\n}`,
      java: `class Solution {\n    public String minWindow(String s, String t) {\n        // Write your solution here\n        return "";\n    }\n}`,
    },
    solutionCode: {
      python: `def minWindow(s, t):\n    from collections import Counter\n    need = Counter(t)\n    missing = len(t)\n    left = start = end = 0\n    for right, c in enumerate(s, 1):\n        if need[c] > 0:\n            missing -= 1\n        need[c] -= 1\n        if missing == 0:\n            while need[s[left]] < 0:\n                need[s[left]] += 1\n                left += 1\n            if not end or right - left <= end - start:\n                start, end = left, right\n            need[s[left]] += 1\n            missing += 1\n            left += 1\n    return s[start:end]`,
    },
    testCases: [
      { id: 1, input: 's = "ADOBECODEBANC", t = "ABC"', expectedOutput: '"BANC"', isHidden: false },
      { id: 2, input: 's = "a", t = "a"', expectedOutput: '"a"', isHidden: false },
      { id: 3, input: 's = "a", t = "aa"', expectedOutput: '""', isHidden: true },
    ],
    tags: ['string', 'sliding-window', 'hash-table'],
    estimatedTime: 30,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // HASHMAP / HASHSET (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_hash_group_anagrams',
    title: 'Group Anagrams',
    difficulty: 'medium',
    topic: 'hashmap',
    problemStatement: `Given an array of strings \`strs\`, group the anagrams together. You can return the answer in any order.\n\nAn anagram is a word formed by rearranging the letters of another word, using all original letters exactly once.`,
    examples: [
      { input: 'strs = ["eat","tea","tan","ate","nat","bat"]', output: '[["bat"],["nat","tan"],["ate","eat","tea"]]', explanation: 'Words are grouped by their sorted character composition.' },
      { input: 'strs = [""]', output: '[[""]]', explanation: 'Single empty string forms its own group.' },
    ],
    constraints: ['1 <= strs.length <= 10^4', '0 <= strs[i].length <= 100', 'strs[i] consists of lowercase English letters'],
    functionSignature: {
      python: 'def groupAnagrams(strs: List[str]) -> List[List[str]]:',
      javascript: 'function groupAnagrams(strs)',
    },
    starterCode: {
      python: `def groupAnagrams(strs):\n    # Write your solution here\n    pass`,
      javascript: `function groupAnagrams(strs) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\n#include <string>\nusing namespace std;\n\nvector<vector<string>> groupAnagrams(vector<string>& strs) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        // Write your solution here\n        return new ArrayList<>();\n    }\n}`,
    },
    solutionCode: {
      python: `def groupAnagrams(strs):\n    groups = {}\n    for s in strs:\n        key = ''.join(sorted(s))\n        groups.setdefault(key, []).append(s)\n    return list(groups.values())`,
    },
    testCases: [
      { id: 1, input: 'strs = ["eat","tea","tan","ate","nat","bat"]', expectedOutput: '[["eat","tea","ate"],["tan","nat"],["bat"]]', isHidden: false },
      { id: 2, input: 'strs = [""]', expectedOutput: '[[""]]', isHidden: false },
      { id: 3, input: 'strs = ["a"]', expectedOutput: '[["a"]]', isHidden: true },
    ],
    tags: ['hash-table', 'string', 'sorting'],
    estimatedTime: 15,
  },
  {
    id: 'cq_hash_top_k_frequent',
    title: 'Top K Frequent Elements',
    difficulty: 'medium',
    topic: 'hashmap',
    problemStatement: `Given an integer array \`nums\` and an integer \`k\`, return the \`k\` most frequent elements. You may return the answer in any order.`,
    examples: [
      { input: 'nums = [1,1,1,2,2,3], k = 2', output: '[1,2]', explanation: '1 appears 3 times, 2 appears 2 times. These are the 2 most frequent.' },
      { input: 'nums = [1], k = 1', output: '[1]', explanation: 'Only one element.' },
    ],
    constraints: ['1 <= nums.length <= 10^5', '-10^4 <= nums[i] <= 10^4', 'k is in range [1, number of unique elements]', 'Answer is guaranteed unique'],
    functionSignature: {
      python: 'def topKFrequent(nums: List[int], k: int) -> List[int]:',
      javascript: 'function topKFrequent(nums, k)',
    },
    starterCode: {
      python: `def topKFrequent(nums, k):\n    # Write your solution here\n    pass`,
      javascript: `function topKFrequent(nums, k) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<int> topKFrequent(vector<int>& nums, int k) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public int[] topKFrequent(int[] nums, int k) {\n        // Write your solution here\n        return new int[]{};\n    }\n}`,
    },
    solutionCode: {
      python: `def topKFrequent(nums, k):\n    from collections import Counter\n    return [x for x, _ in Counter(nums).most_common(k)]`,
    },
    testCases: [
      { id: 1, input: 'nums = [1,1,1,2,2,3], k = 2', expectedOutput: '[1,2]', isHidden: false },
      { id: 2, input: 'nums = [1], k = 1', expectedOutput: '[1]', isHidden: false },
      { id: 3, input: 'nums = [4,4,4,1,1,2,2,2,3], k = 2', expectedOutput: '[4,2]', isHidden: true },
    ],
    tags: ['hash-table', 'heap', 'bucket-sort'],
    estimatedTime: 15,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // LINKED LIST (3 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_ll_reverse',
    title: 'Reverse Linked List',
    difficulty: 'easy',
    topic: 'linked-list',
    problemStatement: `Given the head of a singly linked list, reverse the list, and return the reversed list.`,
    examples: [
      { input: 'head = [1,2,3,4,5]', output: '[5,4,3,2,1]', explanation: 'Reverse all the links.' },
      { input: 'head = [1,2]', output: '[2,1]', explanation: 'Swap the two nodes.' },
    ],
    constraints: ['The number of nodes is in range [0, 5000]', '-5000 <= Node.val <= 5000'],
    functionSignature: {
      python: 'def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:',
      javascript: 'function reverseList(head)',
    },
    starterCode: {
      python: `# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\n\ndef reverseList(head):\n    # Write your solution here\n    pass`,
      javascript: `// function ListNode(val, next) { this.val = val; this.next = next || null; }\n\nfunction reverseList(head) {\n    // Write your solution here\n}`,
      cpp: `struct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(nullptr) {}\n};\n\nListNode* reverseList(ListNode* head) {\n    // Write your solution here\n    return nullptr;\n}`,
      java: `class Solution {\n    public ListNode reverseList(ListNode head) {\n        // Write your solution here\n        return null;\n    }\n}`,
    },
    solutionCode: {
      python: `def reverseList(head):\n    prev = None\n    curr = head\n    while curr:\n        nxt = curr.next\n        curr.next = prev\n        prev = curr\n        curr = nxt\n    return prev`,
    },
    testCases: [
      { id: 1, input: 'head = [1,2,3,4,5]', expectedOutput: '[5,4,3,2,1]', isHidden: false },
      { id: 2, input: 'head = [1,2]', expectedOutput: '[2,1]', isHidden: false },
      { id: 3, input: 'head = []', expectedOutput: '[]', isHidden: true },
    ],
    tags: ['linked-list', 'recursion'],
    estimatedTime: 10,
  },
  {
    id: 'cq_ll_merge_two',
    title: 'Merge Two Sorted Lists',
    difficulty: 'easy',
    topic: 'linked-list',
    problemStatement: `Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.`,
    examples: [
      { input: 'list1 = [1,2,4], list2 = [1,3,4]', output: '[1,1,2,3,4,4]', explanation: 'Merge the two lists node by node in sorted order.' },
      { input: 'list1 = [], list2 = []', output: '[]', explanation: 'Both lists are empty.' },
    ],
    constraints: ['Number of nodes in both lists is in [0, 50]', '-100 <= Node.val <= 100', 'Both lists are sorted in non-decreasing order'],
    functionSignature: {
      python: 'def mergeTwoLists(list1, list2) -> Optional[ListNode]:',
      javascript: 'function mergeTwoLists(list1, list2)',
    },
    starterCode: {
      python: `def mergeTwoLists(list1, list2):\n    # Write your solution here\n    pass`,
      javascript: `function mergeTwoLists(list1, list2) {\n    // Write your solution here\n}`,
      cpp: `ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {\n    // Write your solution here\n    return nullptr;\n}`,
      java: `class Solution {\n    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {\n        // Write your solution here\n        return null;\n    }\n}`,
    },
    solutionCode: {
      python: `def mergeTwoLists(list1, list2):\n    dummy = ListNode(0)\n    curr = dummy\n    while list1 and list2:\n        if list1.val <= list2.val:\n            curr.next = list1\n            list1 = list1.next\n        else:\n            curr.next = list2\n            list2 = list2.next\n        curr = curr.next\n    curr.next = list1 or list2\n    return dummy.next`,
    },
    testCases: [
      { id: 1, input: 'list1 = [1,2,4], list2 = [1,3,4]', expectedOutput: '[1,1,2,3,4,4]', isHidden: false },
      { id: 2, input: 'list1 = [], list2 = []', expectedOutput: '[]', isHidden: false },
      { id: 3, input: 'list1 = [], list2 = [0]', expectedOutput: '[0]', isHidden: true },
    ],
    tags: ['linked-list', 'recursion'],
    estimatedTime: 10,
  },
  {
    id: 'cq_ll_detect_cycle',
    title: 'Linked List Cycle',
    difficulty: 'easy',
    topic: 'linked-list',
    problemStatement: `Given \`head\`, the head of a linked list, determine if the linked list has a cycle in it.\n\nThere is a cycle if some node in the list can be reached again by continuously following the \`next\` pointer.\n\nReturn \`true\` if there is a cycle, otherwise return \`false\`.`,
    examples: [
      { input: 'head = [3,2,0,-4], pos = 1', output: 'true', explanation: 'There is a cycle where tail connects to node index 1.' },
      { input: 'head = [1], pos = -1', output: 'false', explanation: 'No cycle in the linked list.' },
    ],
    constraints: ['Number of nodes is in [0, 10^4]', '-10^5 <= Node.val <= 10^5', 'pos is -1 or a valid index'],
    functionSignature: {
      python: 'def hasCycle(head: Optional[ListNode]) -> bool:',
      javascript: 'function hasCycle(head)',
    },
    starterCode: {
      python: `def hasCycle(head):\n    # Write your solution here\n    pass`,
      javascript: `function hasCycle(head) {\n    // Write your solution here\n}`,
      cpp: `bool hasCycle(ListNode *head) {\n    // Write your solution here\n    return false;\n}`,
      java: `class Solution {\n    public boolean hasCycle(ListNode head) {\n        // Write your solution here\n        return false;\n    }\n}`,
    },
    solutionCode: {
      python: `def hasCycle(head):\n    slow = fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n        if slow == fast:\n            return True\n    return False`,
    },
    testCases: [
      { id: 1, input: 'head = [3,2,0,-4], pos = 1', expectedOutput: 'true', isHidden: false },
      { id: 2, input: 'head = [1,2], pos = 0', expectedOutput: 'true', isHidden: false },
      { id: 3, input: 'head = [1], pos = -1', expectedOutput: 'false', isHidden: true },
    ],
    tags: ['linked-list', 'two-pointers'],
    estimatedTime: 10,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // STACK (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_stack_valid_parens',
    title: 'Valid Parentheses',
    difficulty: 'easy',
    topic: 'stack',
    problemStatement: `Given a string \`s\` containing just the characters \`'('\`, \`')'\`, \`'{'\`, \`'}'\`, \`'['\` and \`']'\`, determine if the input string is valid.\n\nAn input string is valid if:\n1. Open brackets must be closed by the same type of brackets.\n2. Open brackets must be closed in the correct order.\n3. Every close bracket has a corresponding open bracket of the same type.`,
    examples: [
      { input: 's = "()"', output: 'true', explanation: 'Simple matched parentheses.' },
      { input: 's = "()[]{}"', output: 'true', explanation: 'All bracket types match.' },
      { input: 's = "(]"', output: 'false', explanation: 'Mismatched bracket types.' },
    ],
    constraints: ['1 <= s.length <= 10^4', 's consists of parentheses only: ()[]{}'],
    functionSignature: {
      python: 'def isValid(s: str) -> bool:',
      javascript: 'function isValid(s)',
    },
    starterCode: {
      python: `def isValid(s):\n    # Write your solution here\n    pass`,
      javascript: `function isValid(s) {\n    // Write your solution here\n}`,
      cpp: `#include <string>\nusing namespace std;\n\nbool isValid(string s) {\n    // Write your solution here\n    return false;\n}`,
      java: `class Solution {\n    public boolean isValid(String s) {\n        // Write your solution here\n        return false;\n    }\n}`,
    },
    solutionCode: {
      python: `def isValid(s):\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for c in s:\n        if c in mapping:\n            if not stack or stack[-1] != mapping[c]:\n                return False\n            stack.pop()\n        else:\n            stack.append(c)\n    return len(stack) == 0`,
    },
    testCases: [
      { id: 1, input: 's = "()"', expectedOutput: 'true', isHidden: false },
      { id: 2, input: 's = "()[]{}"', expectedOutput: 'true', isHidden: false },
      { id: 3, input: 's = "(]"', expectedOutput: 'false', isHidden: false },
      { id: 4, input: 's = "([)]"', expectedOutput: 'false', isHidden: true },
    ],
    tags: ['stack', 'string'],
    estimatedTime: 10,
  },
  {
    id: 'cq_stack_daily_temps',
    title: 'Daily Temperatures',
    difficulty: 'medium',
    topic: 'stack',
    problemStatement: `Given an array of integers \`temperatures\` representing daily temperatures, return an array \`answer\` such that \`answer[i]\` is the number of days you have to wait after the \`i\`th day to get a warmer temperature.\n\nIf there is no future day that is warmer, set \`answer[i] = 0\`.`,
    examples: [
      { input: 'temperatures = [73,74,75,71,69,72,76,73]', output: '[1,1,4,2,1,1,0,0]', explanation: 'For day 0 (73), the next warmer day is day 1 (74), so answer[0]=1.' },
      { input: 'temperatures = [30,40,50,60]', output: '[1,1,1,0]', explanation: 'Each day has the next day as warmer, except the last.' },
    ],
    constraints: ['1 <= temperatures.length <= 10^5', '30 <= temperatures[i] <= 100'],
    functionSignature: {
      python: 'def dailyTemperatures(temperatures: List[int]) -> List[int]:',
      javascript: 'function dailyTemperatures(temperatures)',
    },
    starterCode: {
      python: `def dailyTemperatures(temperatures):\n    # Write your solution here\n    pass`,
      javascript: `function dailyTemperatures(temperatures) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<int> dailyTemperatures(vector<int>& temperatures) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public int[] dailyTemperatures(int[] temperatures) {\n        // Write your solution here\n        return new int[]{};\n    }\n}`,
    },
    solutionCode: {
      python: `def dailyTemperatures(temperatures):\n    n = len(temperatures)\n    result = [0] * n\n    stack = []\n    for i in range(n):\n        while stack and temperatures[i] > temperatures[stack[-1]]:\n            idx = stack.pop()\n            result[idx] = i - idx\n        stack.append(i)\n    return result`,
    },
    testCases: [
      { id: 1, input: 'temperatures = [73,74,75,71,69,72,76,73]', expectedOutput: '[1,1,4,2,1,1,0,0]', isHidden: false },
      { id: 2, input: 'temperatures = [30,40,50,60]', expectedOutput: '[1,1,1,0]', isHidden: false },
      { id: 3, input: 'temperatures = [30,60,90]', expectedOutput: '[1,1,0]', isHidden: true },
    ],
    tags: ['stack', 'monotonic-stack', 'array'],
    estimatedTime: 15,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // QUEUE (1 question)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_queue_sliding_window_max',
    title: 'Sliding Window Maximum',
    difficulty: 'hard',
    topic: 'queue',
    problemStatement: `You are given an array of integers \`nums\` and a sliding window of size \`k\` that moves from the very left to the very right. You can only see the \`k\` numbers in the window.\n\nReturn the maximum value in the sliding window at each position.`,
    examples: [
      { input: 'nums = [1,3,-1,-3,5,3,6,7], k = 3', output: '[3,3,5,5,6,7]', explanation: 'Window positions: [1,3,-1]→3, [3,-1,-3]→3, [-1,-3,5]→5, [-3,5,3]→5, [5,3,6]→6, [3,6,7]→7.' },
    ],
    constraints: ['1 <= nums.length <= 10^5', '-10^4 <= nums[i] <= 10^4', '1 <= k <= nums.length'],
    functionSignature: {
      python: 'def maxSlidingWindow(nums: List[int], k: int) -> List[int]:',
      javascript: 'function maxSlidingWindow(nums, k)',
    },
    starterCode: {
      python: `def maxSlidingWindow(nums, k):\n    # Write your solution here\n    pass`,
      javascript: `function maxSlidingWindow(nums, k) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<int> maxSlidingWindow(vector<int>& nums, int k) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public int[] maxSlidingWindow(int[] nums, int k) {\n        // Write your solution here\n        return new int[]{};\n    }\n}`,
    },
    solutionCode: {
      python: `def maxSlidingWindow(nums, k):\n    from collections import deque\n    dq = deque()\n    result = []\n    for i, num in enumerate(nums):\n        while dq and dq[0] < i - k + 1:\n            dq.popleft()\n        while dq and nums[dq[-1]] < num:\n            dq.pop()\n        dq.append(i)\n        if i >= k - 1:\n            result.append(nums[dq[0]])\n    return result`,
    },
    testCases: [
      { id: 1, input: 'nums = [1,3,-1,-3,5,3,6,7], k = 3', expectedOutput: '[3,3,5,5,6,7]', isHidden: false },
      { id: 2, input: 'nums = [1], k = 1', expectedOutput: '[1]', isHidden: false },
      { id: 3, input: 'nums = [1,-1], k = 1', expectedOutput: '[1,-1]', isHidden: true },
    ],
    tags: ['queue', 'deque', 'sliding-window', 'monotonic-queue'],
    estimatedTime: 25,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // RECURSION (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_rec_pow',
    title: 'Pow(x, n)',
    difficulty: 'medium',
    topic: 'recursion',
    problemStatement: `Implement \`pow(x, n)\`, which calculates \`x\` raised to the power \`n\` (i.e., \`x^n\`).`,
    examples: [
      { input: 'x = 2.00000, n = 10', output: '1024.00000', explanation: '2^10 = 1024.' },
      { input: 'x = 2.10000, n = 3', output: '9.26100', explanation: '2.1^3 = 9.261.' },
      { input: 'x = 2.00000, n = -2', output: '0.25000', explanation: '2^(-2) = 1/4 = 0.25.' },
    ],
    constraints: ['-100.0 < x < 100.0', '-2^31 <= n <= 2^31-1', 'n is an integer', 'x is not zero when n < 0'],
    functionSignature: {
      python: 'def myPow(x: float, n: int) -> float:',
      javascript: 'function myPow(x, n)',
    },
    starterCode: {
      python: `def myPow(x, n):\n    # Write your solution here\n    pass`,
      javascript: `function myPow(x, n) {\n    // Write your solution here\n}`,
      cpp: `double myPow(double x, int n) {\n    // Write your solution here\n    return 0.0;\n}`,
      java: `class Solution {\n    public double myPow(double x, int n) {\n        // Write your solution here\n        return 0.0;\n    }\n}`,
    },
    solutionCode: {
      python: `def myPow(x, n):\n    if n == 0:\n        return 1\n    if n < 0:\n        x = 1 / x\n        n = -n\n    if n % 2 == 0:\n        return myPow(x * x, n // 2)\n    return x * myPow(x * x, (n - 1) // 2)`,
    },
    testCases: [
      { id: 1, input: 'x = 2.00000, n = 10', expectedOutput: '1024.00000', isHidden: false },
      { id: 2, input: 'x = 2.10000, n = 3', expectedOutput: '9.26100', isHidden: false },
      { id: 3, input: 'x = 2.00000, n = -2', expectedOutput: '0.25000', isHidden: true },
    ],
    tags: ['recursion', 'math', 'binary-exponentiation'],
    estimatedTime: 15,
  },
  {
    id: 'cq_rec_subsets',
    title: 'Subsets',
    difficulty: 'medium',
    topic: 'recursion',
    problemStatement: `Given an integer array \`nums\` of unique elements, return all possible subsets (the power set).\n\nThe solution set must not contain duplicate subsets. Return the solution in any order.`,
    examples: [
      { input: 'nums = [1,2,3]', output: '[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]', explanation: 'All possible subsets of the set {1,2,3}.' },
      { input: 'nums = [0]', output: '[[],[0]]', explanation: 'Two subsets: empty set and {0}.' },
    ],
    constraints: ['1 <= nums.length <= 10', '-10 <= nums[i] <= 10', 'All elements are unique'],
    functionSignature: {
      python: 'def subsets(nums: List[int]) -> List[List[int]]:',
      javascript: 'function subsets(nums)',
    },
    starterCode: {
      python: `def subsets(nums):\n    # Write your solution here\n    pass`,
      javascript: `function subsets(nums) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<vector<int>> subsets(vector<int>& nums) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public List<List<Integer>> subsets(int[] nums) {\n        // Write your solution here\n        return new ArrayList<>();\n    }\n}`,
    },
    solutionCode: {
      python: `def subsets(nums):\n    result = []\n    def backtrack(start, current):\n        result.append(current[:])\n        for i in range(start, len(nums)):\n            current.append(nums[i])\n            backtrack(i + 1, current)\n            current.pop()\n    backtrack(0, [])\n    return result`,
    },
    testCases: [
      { id: 1, input: 'nums = [1,2,3]', expectedOutput: '[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]', isHidden: false },
      { id: 2, input: 'nums = [0]', expectedOutput: '[[],[0]]', isHidden: false },
      { id: 3, input: 'nums = [1,2]', expectedOutput: '[[],[1],[2],[1,2]]', isHidden: true },
    ],
    tags: ['recursion', 'backtracking', 'bit-manipulation'],
    estimatedTime: 15,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // BINARY SEARCH (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_bs_search_rotated',
    title: 'Search in Rotated Sorted Array',
    difficulty: 'medium',
    topic: 'binary-search',
    problemStatement: `There is an integer array \`nums\` sorted in ascending order (with distinct values). Before being passed to your function, \`nums\` is possibly rotated at an unknown pivot index.\n\nGiven the array \`nums\` after the possible rotation and an integer \`target\`, return the index of \`target\` if it is in \`nums\`, or \`-1\` if it is not.`,
    examples: [
      { input: 'nums = [4,5,6,7,0,1,2], target = 0', output: '4', explanation: '0 is found at index 4.' },
      { input: 'nums = [4,5,6,7,0,1,2], target = 3', output: '-1', explanation: '3 is not in the array.' },
    ],
    constraints: ['1 <= nums.length <= 5000', '-10^4 <= nums[i] <= 10^4', 'All values are unique', 'nums is an ascending array possibly rotated'],
    functionSignature: {
      python: 'def search(nums: List[int], target: int) -> int:',
      javascript: 'function search(nums, target)',
    },
    starterCode: {
      python: `def search(nums, target):\n    # Write your solution here\n    pass`,
      javascript: `function search(nums, target) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint search(vector<int>& nums, int target) {\n    // Write your solution here\n    return -1;\n}`,
      java: `class Solution {\n    public int search(int[] nums, int target) {\n        // Write your solution here\n        return -1;\n    }\n}`,
    },
    solutionCode: {
      python: `def search(nums, target):\n    lo, hi = 0, len(nums) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if nums[mid] == target:\n            return mid\n        if nums[lo] <= nums[mid]:\n            if nums[lo] <= target < nums[mid]:\n                hi = mid - 1\n            else:\n                lo = mid + 1\n        else:\n            if nums[mid] < target <= nums[hi]:\n                lo = mid + 1\n            else:\n                hi = mid - 1\n    return -1`,
    },
    testCases: [
      { id: 1, input: 'nums = [4,5,6,7,0,1,2], target = 0', expectedOutput: '4', isHidden: false },
      { id: 2, input: 'nums = [4,5,6,7,0,1,2], target = 3', expectedOutput: '-1', isHidden: false },
      { id: 3, input: 'nums = [1], target = 0', expectedOutput: '-1', isHidden: true },
    ],
    tags: ['binary-search', 'array'],
    estimatedTime: 20,
  },
  {
    id: 'cq_bs_find_min_rotated',
    title: 'Find Minimum in Rotated Sorted Array',
    difficulty: 'medium',
    topic: 'binary-search',
    problemStatement: `Suppose an array of length \`n\` sorted in ascending order is rotated between \`1\` and \`n\` times. Given the sorted rotated array \`nums\` of unique elements, return the minimum element of this array.\n\nYou must write an algorithm that runs in O(log n) time.`,
    examples: [
      { input: 'nums = [3,4,5,1,2]', output: '1', explanation: 'The original array was [1,2,3,4,5] rotated 3 times.' },
      { input: 'nums = [4,5,6,7,0,1,2]', output: '0', explanation: 'The original array was [0,1,2,4,5,6,7] rotated 4 times.' },
    ],
    constraints: ['n == nums.length', '1 <= n <= 5000', '-5000 <= nums[i] <= 5000', 'All integers are unique'],
    functionSignature: {
      python: 'def findMin(nums: List[int]) -> int:',
      javascript: 'function findMin(nums)',
    },
    starterCode: {
      python: `def findMin(nums):\n    # Write your solution here\n    pass`,
      javascript: `function findMin(nums) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint findMin(vector<int>& nums) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int findMin(int[] nums) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def findMin(nums):\n    lo, hi = 0, len(nums) - 1\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if nums[mid] > nums[hi]:\n            lo = mid + 1\n        else:\n            hi = mid\n    return nums[lo]`,
    },
    testCases: [
      { id: 1, input: 'nums = [3,4,5,1,2]', expectedOutput: '1', isHidden: false },
      { id: 2, input: 'nums = [4,5,6,7,0,1,2]', expectedOutput: '0', isHidden: false },
      { id: 3, input: 'nums = [11,13,15,17]', expectedOutput: '11', isHidden: true },
    ],
    tags: ['binary-search', 'array'],
    estimatedTime: 15,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // TREES (3 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_tree_max_depth',
    title: 'Maximum Depth of Binary Tree',
    difficulty: 'easy',
    topic: 'trees',
    problemStatement: `Given the \`root\` of a binary tree, return its maximum depth.\n\nA binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.`,
    examples: [
      { input: 'root = [3,9,20,null,null,15,7]', output: '3', explanation: 'The longest path is root→20→15 (or root→20→7), giving depth 3.' },
      { input: 'root = [1,null,2]', output: '2', explanation: 'The longest path is root→2, giving depth 2.' },
    ],
    constraints: ['Number of nodes is in [0, 10^4]', '-100 <= Node.val <= 100'],
    functionSignature: { python: 'def maxDepth(root: Optional[TreeNode]) -> int:', javascript: 'function maxDepth(root)' },
    starterCode: {
      python: `def maxDepth(root):\n    # Write your solution here\n    pass`,
      javascript: `function maxDepth(root) {\n    // Write your solution here\n}`,
      cpp: `struct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nint maxDepth(TreeNode* root) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int maxDepth(TreeNode root) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def maxDepth(root):\n    if not root:\n        return 0\n    return 1 + max(maxDepth(root.left), maxDepth(root.right))`,
    },
    testCases: [
      { id: 1, input: 'root = [3,9,20,null,null,15,7]', expectedOutput: '3', isHidden: false },
      { id: 2, input: 'root = [1,null,2]', expectedOutput: '2', isHidden: false },
      { id: 3, input: 'root = []', expectedOutput: '0', isHidden: true },
    ],
    tags: ['tree', 'dfs', 'recursion'],
    estimatedTime: 10,
  },
  {
    id: 'cq_tree_level_order',
    title: 'Binary Tree Level Order Traversal',
    difficulty: 'medium',
    topic: 'trees',
    problemStatement: `Given the \`root\` of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).`,
    examples: [
      { input: 'root = [3,9,20,null,null,15,7]', output: '[[3],[9,20],[15,7]]', explanation: 'Three levels: root, second level, leaves.' },
      { input: 'root = [1]', output: '[[1]]', explanation: 'Single node at level 0.' },
    ],
    constraints: ['Number of nodes is in [0, 2000]', '-1000 <= Node.val <= 1000'],
    functionSignature: { python: 'def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:', javascript: 'function levelOrder(root)' },
    starterCode: {
      python: `def levelOrder(root):\n    # Write your solution here\n    pass`,
      javascript: `function levelOrder(root) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<vector<int>> levelOrder(TreeNode* root) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public List<List<Integer>> levelOrder(TreeNode root) {\n        // Write your solution here\n        return new ArrayList<>();\n    }\n}`,
    },
    solutionCode: {
      python: `def levelOrder(root):\n    if not root:\n        return []\n    result = []\n    queue = [root]\n    while queue:\n        level = []\n        next_queue = []\n        for node in queue:\n            level.append(node.val)\n            if node.left:\n                next_queue.append(node.left)\n            if node.right:\n                next_queue.append(node.right)\n        result.append(level)\n        queue = next_queue\n    return result`,
    },
    testCases: [
      { id: 1, input: 'root = [3,9,20,null,null,15,7]', expectedOutput: '[[3],[9,20],[15,7]]', isHidden: false },
      { id: 2, input: 'root = [1]', expectedOutput: '[[1]]', isHidden: false },
      { id: 3, input: 'root = []', expectedOutput: '[]', isHidden: true },
    ],
    tags: ['tree', 'bfs', 'queue'],
    estimatedTime: 15,
  },
  {
    id: 'cq_tree_max_path_sum',
    title: 'Binary Tree Maximum Path Sum',
    difficulty: 'hard',
    topic: 'trees',
    problemStatement: `A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can only appear in the sequence at most once. The path does not need to pass through the root.\n\nGiven the \`root\` of a binary tree, return the maximum path sum of any non-empty path.`,
    examples: [
      { input: 'root = [1,2,3]', output: '6', explanation: 'The optimal path is 2→1→3 with sum 6.' },
      { input: 'root = [-10,9,20,null,null,15,7]', output: '42', explanation: 'The optimal path is 15→20→7 with sum 42.' },
    ],
    constraints: ['Number of nodes is in [1, 3 * 10^4]', '-1000 <= Node.val <= 1000'],
    functionSignature: { python: 'def maxPathSum(root: Optional[TreeNode]) -> int:', javascript: 'function maxPathSum(root)' },
    starterCode: {
      python: `def maxPathSum(root):\n    # Write your solution here\n    pass`,
      javascript: `function maxPathSum(root) {\n    // Write your solution here\n}`,
      cpp: `int maxPathSum(TreeNode* root) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int maxPathSum(TreeNode root) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def maxPathSum(root):\n    max_sum = [float('-inf')]\n    def dfs(node):\n        if not node:\n            return 0\n        left = max(dfs(node.left), 0)\n        right = max(dfs(node.right), 0)\n        max_sum[0] = max(max_sum[0], node.val + left + right)\n        return node.val + max(left, right)\n    dfs(root)\n    return max_sum[0]`,
    },
    testCases: [
      { id: 1, input: 'root = [1,2,3]', expectedOutput: '6', isHidden: false },
      { id: 2, input: 'root = [-10,9,20,null,null,15,7]', expectedOutput: '42', isHidden: false },
      { id: 3, input: 'root = [-3]', expectedOutput: '-3', isHidden: true },
    ],
    tags: ['tree', 'dfs', 'dynamic-programming'],
    estimatedTime: 25,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // BST (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_bst_validate',
    title: 'Validate Binary Search Tree',
    difficulty: 'medium',
    topic: 'bst',
    problemStatement: `Given the \`root\` of a binary tree, determine if it is a valid binary search tree (BST).\n\nA valid BST is defined as follows:\n- The left subtree of a node contains only nodes with keys less than the node's key.\n- The right subtree of a node contains only nodes with keys greater than the node's key.\n- Both the left and right subtrees must also be binary search trees.`,
    examples: [
      { input: 'root = [2,1,3]', output: 'true', explanation: 'Left child 1 < root 2 < right child 3.' },
      { input: 'root = [5,1,4,null,null,3,6]', output: 'false', explanation: 'Node 4 is in the right subtree of 5 but is less than 5.' },
    ],
    constraints: ['Number of nodes is in [1, 10^4]', '-2^31 <= Node.val <= 2^31-1'],
    functionSignature: { python: 'def isValidBST(root: Optional[TreeNode]) -> bool:', javascript: 'function isValidBST(root)' },
    starterCode: {
      python: `def isValidBST(root):\n    # Write your solution here\n    pass`,
      javascript: `function isValidBST(root) {\n    // Write your solution here\n}`,
      cpp: `bool isValidBST(TreeNode* root) {\n    // Write your solution here\n    return false;\n}`,
      java: `class Solution {\n    public boolean isValidBST(TreeNode root) {\n        // Write your solution here\n        return false;\n    }\n}`,
    },
    solutionCode: {
      python: `def isValidBST(root):\n    def helper(node, lo, hi):\n        if not node:\n            return True\n        if node.val <= lo or node.val >= hi:\n            return False\n        return helper(node.left, lo, node.val) and helper(node.right, node.val, hi)\n    return helper(root, float('-inf'), float('inf'))`,
    },
    testCases: [
      { id: 1, input: 'root = [2,1,3]', expectedOutput: 'true', isHidden: false },
      { id: 2, input: 'root = [5,1,4,null,null,3,6]', expectedOutput: 'false', isHidden: false },
      { id: 3, input: 'root = [1]', expectedOutput: 'true', isHidden: true },
    ],
    tags: ['tree', 'bst', 'dfs'],
    estimatedTime: 15,
  },
  {
    id: 'cq_bst_kth_smallest',
    title: 'Kth Smallest Element in a BST',
    difficulty: 'medium',
    topic: 'bst',
    problemStatement: `Given the \`root\` of a binary search tree, and an integer \`k\`, return the \`k\`th smallest value (1-indexed) of all the values of the nodes in the tree.`,
    examples: [
      { input: 'root = [3,1,4,null,2], k = 1', output: '1', explanation: 'Inorder traversal gives [1,2,3,4]. The 1st smallest is 1.' },
      { input: 'root = [5,3,6,2,4,null,null,1], k = 3', output: '3', explanation: 'Inorder traversal gives [1,2,3,4,5,6]. The 3rd smallest is 3.' },
    ],
    constraints: ['Number of nodes is in [1, 10^4]', '0 <= Node.val <= 10^4', '1 <= k <= n'],
    functionSignature: { python: 'def kthSmallest(root: Optional[TreeNode], k: int) -> int:', javascript: 'function kthSmallest(root, k)' },
    starterCode: {
      python: `def kthSmallest(root, k):\n    # Write your solution here\n    pass`,
      javascript: `function kthSmallest(root, k) {\n    // Write your solution here\n}`,
      cpp: `int kthSmallest(TreeNode* root, int k) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int kthSmallest(TreeNode root, int k) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def kthSmallest(root, k):\n    stack = []\n    curr = root\n    count = 0\n    while curr or stack:\n        while curr:\n            stack.append(curr)\n            curr = curr.left\n        curr = stack.pop()\n        count += 1\n        if count == k:\n            return curr.val\n        curr = curr.right\n    return -1`,
    },
    testCases: [
      { id: 1, input: 'root = [3,1,4,null,2], k = 1', expectedOutput: '1', isHidden: false },
      { id: 2, input: 'root = [5,3,6,2,4,null,null,1], k = 3', expectedOutput: '3', isHidden: false },
      { id: 3, input: 'root = [1], k = 1', expectedOutput: '1', isHidden: true },
    ],
    tags: ['tree', 'bst', 'inorder'],
    estimatedTime: 15,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // HEAP (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_heap_kth_largest',
    title: 'Kth Largest Element in an Array',
    difficulty: 'medium',
    topic: 'heap',
    problemStatement: `Given an integer array \`nums\` and an integer \`k\`, return the \`k\`th largest element in the array.\n\nNote that it is the \`k\`th largest element in the sorted order, not the \`k\`th distinct element.\n\nCan you solve it without sorting?`,
    examples: [
      { input: 'nums = [3,2,1,5,6,4], k = 2', output: '5', explanation: 'The sorted array is [1,2,3,4,5,6]. The 2nd largest is 5.' },
      { input: 'nums = [3,2,3,1,2,4,5,5,6], k = 4', output: '4', explanation: 'The sorted array is [1,2,2,3,3,4,5,5,6]. The 4th largest is 4.' },
    ],
    constraints: ['1 <= k <= nums.length <= 10^5', '-10^4 <= nums[i] <= 10^4'],
    functionSignature: { python: 'def findKthLargest(nums: List[int], k: int) -> int:', javascript: 'function findKthLargest(nums, k)' },
    starterCode: {
      python: `def findKthLargest(nums, k):\n    # Write your solution here\n    pass`,
      javascript: `function findKthLargest(nums, k) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint findKthLargest(vector<int>& nums, int k) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int findKthLargest(int[] nums, int k) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def findKthLargest(nums, k):\n    import heapq\n    return heapq.nlargest(k, nums)[-1]`,
    },
    testCases: [
      { id: 1, input: 'nums = [3,2,1,5,6,4], k = 2', expectedOutput: '5', isHidden: false },
      { id: 2, input: 'nums = [3,2,3,1,2,4,5,5,6], k = 4', expectedOutput: '4', isHidden: false },
      { id: 3, input: 'nums = [1], k = 1', expectedOutput: '1', isHidden: true },
    ],
    tags: ['heap', 'quickselect', 'sorting'],
    estimatedTime: 15,
  },
  {
    id: 'cq_heap_merge_k_lists',
    title: 'Merge k Sorted Lists',
    difficulty: 'hard',
    topic: 'heap',
    problemStatement: `You are given an array of \`k\` linked-lists \`lists\`, each linked-list is sorted in ascending order.\n\nMerge all the linked-lists into one sorted linked-list and return it.`,
    examples: [
      { input: 'lists = [[1,4,5],[1,3,4],[2,6]]', output: '[1,1,2,3,4,4,5,6]', explanation: 'Merge all three sorted lists into one sorted list.' },
      { input: 'lists = []', output: '[]', explanation: 'No lists to merge.' },
    ],
    constraints: ['k == lists.length', '0 <= k <= 10^4', '0 <= lists[i].length <= 500', '-10^4 <= lists[i][j] <= 10^4', 'Each list is sorted in ascending order'],
    functionSignature: { python: 'def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:', javascript: 'function mergeKLists(lists)' },
    starterCode: {
      python: `def mergeKLists(lists):\n    # Write your solution here\n    pass`,
      javascript: `function mergeKLists(lists) {\n    // Write your solution here\n}`,
      cpp: `ListNode* mergeKLists(vector<ListNode*>& lists) {\n    // Write your solution here\n    return nullptr;\n}`,
      java: `class Solution {\n    public ListNode mergeKLists(ListNode[] lists) {\n        // Write your solution here\n        return null;\n    }\n}`,
    },
    solutionCode: {
      python: `def mergeKLists(lists):\n    import heapq\n    heap = []\n    for i, l in enumerate(lists):\n        if l:\n            heapq.heappush(heap, (l.val, i, l))\n    dummy = ListNode(0)\n    curr = dummy\n    while heap:\n        val, i, node = heapq.heappop(heap)\n        curr.next = node\n        curr = curr.next\n        if node.next:\n            heapq.heappush(heap, (node.next.val, i, node.next))\n    return dummy.next`,
    },
    testCases: [
      { id: 1, input: 'lists = [[1,4,5],[1,3,4],[2,6]]', expectedOutput: '[1,1,2,3,4,4,5,6]', isHidden: false },
      { id: 2, input: 'lists = []', expectedOutput: '[]', isHidden: false },
      { id: 3, input: 'lists = [[]]', expectedOutput: '[]', isHidden: true },
    ],
    tags: ['heap', 'linked-list', 'divide-and-conquer'],
    estimatedTime: 25,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // GRAPHS (3 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_graph_num_islands',
    title: 'Number of Islands',
    difficulty: 'medium',
    topic: 'graphs',
    problemStatement: `Given an \`m x n\` 2D binary grid \`grid\` which represents a map of \`'1'\`s (land) and \`'0'\`s (water), return the number of islands.\n\nAn island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.`,
    examples: [
      { input: 'grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]', output: '1', explanation: 'All 1s are connected, forming one island.' },
      { input: 'grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]', output: '3', explanation: 'Three separate groups of connected 1s.' },
    ],
    constraints: ['m == grid.length', 'n == grid[i].length', '1 <= m, n <= 300', 'grid[i][j] is "0" or "1"'],
    functionSignature: { python: 'def numIslands(grid: List[List[str]]) -> int:', javascript: 'function numIslands(grid)' },
    starterCode: {
      python: `def numIslands(grid):\n    # Write your solution here\n    pass`,
      javascript: `function numIslands(grid) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint numIslands(vector<vector<char>>& grid) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int numIslands(char[][] grid) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def numIslands(grid):\n    if not grid:\n        return 0\n    count = 0\n    for i in range(len(grid)):\n        for j in range(len(grid[0])):\n            if grid[i][j] == '1':\n                dfs(grid, i, j)\n                count += 1\n    return count\n\ndef dfs(grid, i, j):\n    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':\n        return\n    grid[i][j] = '0'\n    dfs(grid, i+1, j)\n    dfs(grid, i-1, j)\n    dfs(grid, i, j+1)\n    dfs(grid, i, j-1)`,
    },
    testCases: [
      { id: 1, input: 'grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]', expectedOutput: '1', isHidden: false },
      { id: 2, input: 'grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]', expectedOutput: '3', isHidden: false },
      { id: 3, input: 'grid = [["1"]]', expectedOutput: '1', isHidden: true },
    ],
    tags: ['graph', 'dfs', 'bfs', 'matrix'],
    estimatedTime: 20,
  },
  {
    id: 'cq_graph_course_schedule',
    title: 'Course Schedule',
    difficulty: 'medium',
    topic: 'graphs',
    problemStatement: `There are a total of \`numCourses\` courses you have to take, labeled from \`0\` to \`numCourses - 1\`. You are given an array \`prerequisites\` where \`prerequisites[i] = [a, b]\` indicates you must take course \`b\` before course \`a\`.\n\nReturn \`true\` if you can finish all courses, otherwise return \`false\`.`,
    examples: [
      { input: 'numCourses = 2, prerequisites = [[1,0]]', output: 'true', explanation: 'Take course 0, then course 1. No cycle.' },
      { input: 'numCourses = 2, prerequisites = [[1,0],[0,1]]', output: 'false', explanation: 'Course 0 requires 1 and course 1 requires 0. Cycle detected.' },
    ],
    constraints: ['1 <= numCourses <= 2000', '0 <= prerequisites.length <= 5000', 'prerequisites[i].length == 2', '0 <= a, b < numCourses', 'All pairs are unique'],
    functionSignature: { python: 'def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:', javascript: 'function canFinish(numCourses, prerequisites)' },
    starterCode: {
      python: `def canFinish(numCourses, prerequisites):\n    # Write your solution here\n    pass`,
      javascript: `function canFinish(numCourses, prerequisites) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nbool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n    // Write your solution here\n    return false;\n}`,
      java: `class Solution {\n    public boolean canFinish(int numCourses, int[][] prerequisites) {\n        // Write your solution here\n        return false;\n    }\n}`,
    },
    solutionCode: {
      python: `def canFinish(numCourses, prerequisites):\n    adj = [[] for _ in range(numCourses)]\n    for a, b in prerequisites:\n        adj[a].append(b)\n    visited = [0] * numCourses  # 0: unvisited, 1: visiting, 2: done\n    def dfs(node):\n        if visited[node] == 1:\n            return False\n        if visited[node] == 2:\n            return True\n        visited[node] = 1\n        for nei in adj[node]:\n            if not dfs(nei):\n                return False\n        visited[node] = 2\n        return True\n    return all(dfs(i) for i in range(numCourses))`,
    },
    testCases: [
      { id: 1, input: 'numCourses = 2, prerequisites = [[1,0]]', expectedOutput: 'true', isHidden: false },
      { id: 2, input: 'numCourses = 2, prerequisites = [[1,0],[0,1]]', expectedOutput: 'false', isHidden: false },
      { id: 3, input: 'numCourses = 1, prerequisites = []', expectedOutput: 'true', isHidden: true },
    ],
    tags: ['graph', 'topological-sort', 'dfs', 'cycle-detection'],
    estimatedTime: 20,
  },
  {
    id: 'cq_graph_word_ladder',
    title: 'Word Ladder',
    difficulty: 'hard',
    topic: 'graphs',
    problemStatement: `Given two words, \`beginWord\` and \`endWord\`, and a dictionary \`wordList\`, return the number of words in the shortest transformation sequence from \`beginWord\` to \`endWord\`, or \`0\` if no such sequence exists.\n\nEach adjacent pair of words differs by exactly one letter. Every transformed word must exist in \`wordList\`. Note that \`beginWord\` does not need to be in \`wordList\`.`,
    examples: [
      { input: 'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]', output: '5', explanation: 'hit → hot → dot → dog → cog (5 words).' },
      { input: 'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]', output: '0', explanation: 'endWord "cog" is not in wordList.' },
    ],
    constraints: ['1 <= beginWord.length <= 10', 'endWord.length == beginWord.length', '1 <= wordList.length <= 5000', 'All words have the same length', 'All words consist of lowercase English letters'],
    functionSignature: { python: 'def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:', javascript: 'function ladderLength(beginWord, endWord, wordList)' },
    starterCode: {
      python: `def ladderLength(beginWord, endWord, wordList):\n    # Write your solution here\n    pass`,
      javascript: `function ladderLength(beginWord, endWord, wordList) {\n    // Write your solution here\n}`,
      cpp: `#include <string>\n#include <vector>\nusing namespace std;\n\nint ladderLength(string beginWord, string endWord, vector<string>& wordList) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int ladderLength(String beginWord, String endWord, List<String> wordList) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def ladderLength(beginWord, endWord, wordList):\n    from collections import deque\n    word_set = set(wordList)\n    if endWord not in word_set:\n        return 0\n    queue = deque([(beginWord, 1)])\n    visited = {beginWord}\n    while queue:\n        word, depth = queue.popleft()\n        for i in range(len(word)):\n            for c in 'abcdefghijklmnopqrstuvwxyz':\n                next_word = word[:i] + c + word[i+1:]\n                if next_word == endWord:\n                    return depth + 1\n                if next_word in word_set and next_word not in visited:\n                    visited.add(next_word)\n                    queue.append((next_word, depth + 1))\n    return 0`,
    },
    testCases: [
      { id: 1, input: 'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]', expectedOutput: '5', isHidden: false },
      { id: 2, input: 'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]', expectedOutput: '0', isHidden: false },
      { id: 3, input: 'beginWord = "a", endWord = "c", wordList = ["a","b","c"]', expectedOutput: '2', isHidden: true },
    ],
    tags: ['graph', 'bfs', 'string'],
    estimatedTime: 30,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // GREEDY (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_greedy_jump_game',
    title: 'Jump Game',
    difficulty: 'medium',
    topic: 'greedy',
    problemStatement: `You are given an integer array \`nums\`. You are initially positioned at the array's first index, and each element represents your maximum jump length at that position.\n\nReturn \`true\` if you can reach the last index, or \`false\` otherwise.`,
    examples: [
      { input: 'nums = [2,3,1,1,4]', output: 'true', explanation: 'Jump 1 step from 0 to 1, then 3 steps to the last index.' },
      { input: 'nums = [3,2,1,0,4]', output: 'false', explanation: 'You always end up at index 3 which has 0 jump length.' },
    ],
    constraints: ['1 <= nums.length <= 10^4', '0 <= nums[i] <= 10^5'],
    functionSignature: { python: 'def canJump(nums: List[int]) -> bool:', javascript: 'function canJump(nums)' },
    starterCode: {
      python: `def canJump(nums):\n    # Write your solution here\n    pass`,
      javascript: `function canJump(nums) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nbool canJump(vector<int>& nums) {\n    // Write your solution here\n    return false;\n}`,
      java: `class Solution {\n    public boolean canJump(int[] nums) {\n        // Write your solution here\n        return false;\n    }\n}`,
    },
    solutionCode: {
      python: `def canJump(nums):\n    farthest = 0\n    for i in range(len(nums)):\n        if i > farthest:\n            return False\n        farthest = max(farthest, i + nums[i])\n    return True`,
    },
    testCases: [
      { id: 1, input: 'nums = [2,3,1,1,4]', expectedOutput: 'true', isHidden: false },
      { id: 2, input: 'nums = [3,2,1,0,4]', expectedOutput: 'false', isHidden: false },
      { id: 3, input: 'nums = [0]', expectedOutput: 'true', isHidden: true },
    ],
    tags: ['greedy', 'array'],
    estimatedTime: 15,
  },
  {
    id: 'cq_greedy_merge_intervals',
    title: 'Merge Intervals',
    difficulty: 'medium',
    topic: 'greedy',
    problemStatement: `Given an array of \`intervals\` where \`intervals[i] = [start_i, end_i]\`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.`,
    examples: [
      { input: 'intervals = [[1,3],[2,6],[8,10],[15,18]]', output: '[[1,6],[8,10],[15,18]]', explanation: 'Intervals [1,3] and [2,6] overlap, merging to [1,6].' },
      { input: 'intervals = [[1,4],[4,5]]', output: '[[1,5]]', explanation: 'Intervals [1,4] and [4,5] are considered overlapping.' },
    ],
    constraints: ['1 <= intervals.length <= 10^4', 'intervals[i].length == 2', '0 <= start_i <= end_i <= 10^4'],
    functionSignature: { python: 'def merge(intervals: List[List[int]]) -> List[List[int]]:', javascript: 'function merge(intervals)' },
    starterCode: {
      python: `def merge(intervals):\n    # Write your solution here\n    pass`,
      javascript: `function merge(intervals) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<vector<int>> merge(vector<vector<int>>& intervals) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public int[][] merge(int[][] intervals) {\n        // Write your solution here\n        return new int[][]{};\n    }\n}`,
    },
    solutionCode: {
      python: `def merge(intervals):\n    intervals.sort(key=lambda x: x[0])\n    merged = [intervals[0]]\n    for start, end in intervals[1:]:\n        if start <= merged[-1][1]:\n            merged[-1][1] = max(merged[-1][1], end)\n        else:\n            merged.append([start, end])\n    return merged`,
    },
    testCases: [
      { id: 1, input: 'intervals = [[1,3],[2,6],[8,10],[15,18]]', expectedOutput: '[[1,6],[8,10],[15,18]]', isHidden: false },
      { id: 2, input: 'intervals = [[1,4],[4,5]]', expectedOutput: '[[1,5]]', isHidden: false },
      { id: 3, input: 'intervals = [[1,4],[0,0]]', expectedOutput: '[[0,0],[1,4]]', isHidden: true },
    ],
    tags: ['greedy', 'sorting', 'array'],
    estimatedTime: 15,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // BACKTRACKING (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_bt_combination_sum',
    title: 'Combination Sum',
    difficulty: 'medium',
    topic: 'backtracking',
    problemStatement: `Given an array of distinct integers \`candidates\` and a target integer \`target\`, return a list of all unique combinations of \`candidates\` where the chosen numbers sum to \`target\`. You may return the combinations in any order.\n\nThe same number may be chosen from \`candidates\` an unlimited number of times.`,
    examples: [
      { input: 'candidates = [2,3,6,7], target = 7', output: '[[2,2,3],[7]]', explanation: '2+2+3=7 and 7=7.' },
      { input: 'candidates = [2,3,5], target = 8', output: '[[2,2,2,2],[2,3,3],[3,5]]', explanation: 'Three combinations that sum to 8.' },
    ],
    constraints: ['1 <= candidates.length <= 30', '2 <= candidates[i] <= 40', 'All elements are distinct', '1 <= target <= 40'],
    functionSignature: { python: 'def combinationSum(candidates: List[int], target: int) -> List[List[int]]:', javascript: 'function combinationSum(candidates, target)' },
    starterCode: {
      python: `def combinationSum(candidates, target):\n    # Write your solution here\n    pass`,
      javascript: `function combinationSum(candidates, target) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<vector<int>> combinationSum(vector<int>& candidates, int target) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public List<List<Integer>> combinationSum(int[] candidates, int target) {\n        // Write your solution here\n        return new ArrayList<>();\n    }\n}`,
    },
    solutionCode: {
      python: `def combinationSum(candidates, target):\n    result = []\n    def backtrack(start, current, remaining):\n        if remaining == 0:\n            result.append(current[:])\n            return\n        for i in range(start, len(candidates)):\n            if candidates[i] > remaining:\n                continue\n            current.append(candidates[i])\n            backtrack(i, current, remaining - candidates[i])\n            current.pop()\n    backtrack(0, [], target)\n    return result`,
    },
    testCases: [
      { id: 1, input: 'candidates = [2,3,6,7], target = 7', expectedOutput: '[[2,2,3],[7]]', isHidden: false },
      { id: 2, input: 'candidates = [2,3,5], target = 8', expectedOutput: '[[2,2,2,2],[2,3,3],[3,5]]', isHidden: false },
      { id: 3, input: 'candidates = [2], target = 1', expectedOutput: '[]', isHidden: true },
    ],
    tags: ['backtracking', 'array'],
    estimatedTime: 20,
  },
  {
    id: 'cq_bt_n_queens',
    title: 'N-Queens',
    difficulty: 'hard',
    topic: 'backtracking',
    problemStatement: `The n-queens puzzle is the problem of placing \`n\` queens on an \`n x n\` chessboard such that no two queens attack each other.\n\nGiven an integer \`n\`, return all distinct solutions. Each solution contains a distinct board configuration with \`'Q'\` and \`'.'\`.`,
    examples: [
      { input: 'n = 4', output: '[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]', explanation: 'Two distinct solutions for placing 4 queens.' },
      { input: 'n = 1', output: '[["Q"]]', explanation: 'Only one way to place a single queen.' },
    ],
    constraints: ['1 <= n <= 9'],
    functionSignature: { python: 'def solveNQueens(n: int) -> List[List[str]]:', javascript: 'function solveNQueens(n)' },
    starterCode: {
      python: `def solveNQueens(n):\n    # Write your solution here\n    pass`,
      javascript: `function solveNQueens(n) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\n#include <string>\nusing namespace std;\n\nvector<vector<string>> solveNQueens(int n) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public List<List<String>> solveNQueens(int n) {\n        // Write your solution here\n        return new ArrayList<>();\n    }\n}`,
    },
    solutionCode: {
      python: `def solveNQueens(n):\n    result = []\n    cols = set()\n    diag1 = set()\n    diag2 = set()\n    board = [['.' ] * n for _ in range(n)]\n    def backtrack(row):\n        if row == n:\n            result.append([''.join(r) for r in board])\n            return\n        for col in range(n):\n            if col in cols or (row - col) in diag1 or (row + col) in diag2:\n                continue\n            cols.add(col)\n            diag1.add(row - col)\n            diag2.add(row + col)\n            board[row][col] = 'Q'\n            backtrack(row + 1)\n            board[row][col] = '.'\n            cols.discard(col)\n            diag1.discard(row - col)\n            diag2.discard(row + col)\n    backtrack(0)\n    return result`,
    },
    testCases: [
      { id: 1, input: 'n = 4', expectedOutput: '2 solutions', isHidden: false },
      { id: 2, input: 'n = 1', expectedOutput: '[["Q"]]', isHidden: false },
      { id: 3, input: 'n = 5', expectedOutput: '10 solutions', isHidden: true },
    ],
    tags: ['backtracking', 'recursion'],
    estimatedTime: 30,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // DYNAMIC PROGRAMMING (4 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_dp_climbing_stairs',
    title: 'Climbing Stairs',
    difficulty: 'easy',
    topic: 'dp',
    problemStatement: `You are climbing a staircase. It takes \`n\` steps to reach the top.\n\nEach time you can either climb \`1\` or \`2\` steps. In how many distinct ways can you climb to the top?`,
    examples: [
      { input: 'n = 2', output: '2', explanation: 'Two ways: 1+1 or 2.' },
      { input: 'n = 3', output: '3', explanation: 'Three ways: 1+1+1, 1+2, 2+1.' },
    ],
    constraints: ['1 <= n <= 45'],
    functionSignature: { python: 'def climbStairs(n: int) -> int:', javascript: 'function climbStairs(n)' },
    starterCode: {
      python: `def climbStairs(n):\n    # Write your solution here\n    pass`,
      javascript: `function climbStairs(n) {\n    // Write your solution here\n}`,
      cpp: `int climbStairs(int n) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int climbStairs(int n) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def climbStairs(n):\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b`,
    },
    testCases: [
      { id: 1, input: 'n = 2', expectedOutput: '2', isHidden: false },
      { id: 2, input: 'n = 3', expectedOutput: '3', isHidden: false },
      { id: 3, input: 'n = 5', expectedOutput: '8', isHidden: true },
    ],
    tags: ['dynamic-programming', 'math'],
    estimatedTime: 10,
  },
  {
    id: 'cq_dp_house_robber',
    title: 'House Robber',
    difficulty: 'medium',
    topic: 'dp',
    problemStatement: `You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, and adjacent houses have security systems that will contact the police if two adjacent houses are broken into on the same night.\n\nGiven an integer array \`nums\` representing the amount of money at each house, return the maximum amount of money you can rob tonight without alerting the police.`,
    examples: [
      { input: 'nums = [1,2,3,1]', output: '4', explanation: 'Rob house 1 (1) and house 3 (3) = 4.' },
      { input: 'nums = [2,7,9,3,1]', output: '12', explanation: 'Rob house 1 (2), house 3 (9) and house 5 (1) = 12.' },
    ],
    constraints: ['1 <= nums.length <= 100', '0 <= nums[i] <= 400'],
    functionSignature: { python: 'def rob(nums: List[int]) -> int:', javascript: 'function rob(nums)' },
    starterCode: {
      python: `def rob(nums):\n    # Write your solution here\n    pass`,
      javascript: `function rob(nums) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint rob(vector<int>& nums) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int rob(int[] nums) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def rob(nums):\n    if not nums:\n        return 0\n    if len(nums) == 1:\n        return nums[0]\n    prev2, prev1 = 0, 0\n    for num in nums:\n        prev2, prev1 = prev1, max(prev1, prev2 + num)\n    return prev1`,
    },
    testCases: [
      { id: 1, input: 'nums = [1,2,3,1]', expectedOutput: '4', isHidden: false },
      { id: 2, input: 'nums = [2,7,9,3,1]', expectedOutput: '12', isHidden: false },
      { id: 3, input: 'nums = [0]', expectedOutput: '0', isHidden: true },
    ],
    tags: ['dynamic-programming', 'array'],
    estimatedTime: 15,
  },
  {
    id: 'cq_dp_coin_change',
    title: 'Coin Change',
    difficulty: 'medium',
    topic: 'dp',
    problemStatement: `You are given an integer array \`coins\` representing coins of different denominations and an integer \`amount\` representing a total amount of money.\n\nReturn the fewest number of coins needed to make up that amount. If it cannot be made up by any combination, return \`-1\`.\n\nYou may assume you have an infinite number of each kind of coin.`,
    examples: [
      { input: 'coins = [1,5,10], amount = 12', output: '3', explanation: '12 = 10 + 1 + 1.' },
      { input: 'coins = [2], amount = 3', output: '-1', explanation: '3 cannot be made from coins of denomination 2.' },
    ],
    constraints: ['1 <= coins.length <= 12', '1 <= coins[i] <= 2^31-1', '0 <= amount <= 10^4'],
    functionSignature: { python: 'def coinChange(coins: List[int], amount: int) -> int:', javascript: 'function coinChange(coins, amount)' },
    starterCode: {
      python: `def coinChange(coins, amount):\n    # Write your solution here\n    pass`,
      javascript: `function coinChange(coins, amount) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint coinChange(vector<int>& coins, int amount) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int coinChange(int[] coins, int amount) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def coinChange(coins, amount):\n    dp = [float('inf')] * (amount + 1)\n    dp[0] = 0\n    for i in range(1, amount + 1):\n        for coin in coins:\n            if coin <= i:\n                dp[i] = min(dp[i], dp[i - coin] + 1)\n    return dp[amount] if dp[amount] != float('inf') else -1`,
    },
    testCases: [
      { id: 1, input: 'coins = [1,5,10], amount = 12', expectedOutput: '3', isHidden: false },
      { id: 2, input: 'coins = [2], amount = 3', expectedOutput: '-1', isHidden: false },
      { id: 3, input: 'coins = [1], amount = 0', expectedOutput: '0', isHidden: true },
    ],
    tags: ['dynamic-programming', 'bfs'],
    estimatedTime: 20,
  },
  {
    id: 'cq_dp_longest_increasing_subseq',
    title: 'Longest Increasing Subsequence',
    difficulty: 'medium',
    topic: 'dp',
    problemStatement: `Given an integer array \`nums\`, return the length of the longest strictly increasing subsequence.`,
    examples: [
      { input: 'nums = [10,9,2,5,3,7,101,18]', output: '4', explanation: 'The longest increasing subsequence is [2,3,7,101], length 4.' },
      { input: 'nums = [0,1,0,3,2,3]', output: '4', explanation: 'The longest increasing subsequence is [0,1,2,3], length 4.' },
    ],
    constraints: ['1 <= nums.length <= 2500', '-10^4 <= nums[i] <= 10^4'],
    functionSignature: { python: 'def lengthOfLIS(nums: List[int]) -> int:', javascript: 'function lengthOfLIS(nums)' },
    starterCode: {
      python: `def lengthOfLIS(nums):\n    # Write your solution here\n    pass`,
      javascript: `function lengthOfLIS(nums) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint lengthOfLIS(vector<int>& nums) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int lengthOfLIS(int[] nums) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def lengthOfLIS(nums):\n    from bisect import bisect_left\n    tails = []\n    for num in nums:\n        pos = bisect_left(tails, num)\n        if pos == len(tails):\n            tails.append(num)\n        else:\n            tails[pos] = num\n    return len(tails)`,
    },
    testCases: [
      { id: 1, input: 'nums = [10,9,2,5,3,7,101,18]', expectedOutput: '4', isHidden: false },
      { id: 2, input: 'nums = [0,1,0,3,2,3]', expectedOutput: '4', isHidden: false },
      { id: 3, input: 'nums = [7,7,7,7]', expectedOutput: '1', isHidden: true },
    ],
    tags: ['dynamic-programming', 'binary-search'],
    estimatedTime: 20,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // 2D DP (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_2ddp_unique_paths',
    title: 'Unique Paths',
    difficulty: 'medium',
    topic: '2d-dp',
    problemStatement: `A robot is located at the top-left corner of an \`m x n\` grid. The robot can only move either down or right at any point.\n\nThe robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?`,
    examples: [
      { input: 'm = 3, n = 7', output: '28', explanation: 'There are 28 unique paths from top-left to bottom-right.' },
      { input: 'm = 3, n = 2', output: '3', explanation: 'Three paths: Right-Down-Down, Down-Right-Down, Down-Down-Right.' },
    ],
    constraints: ['1 <= m, n <= 100'],
    functionSignature: { python: 'def uniquePaths(m: int, n: int) -> int:', javascript: 'function uniquePaths(m, n)' },
    starterCode: {
      python: `def uniquePaths(m, n):\n    # Write your solution here\n    pass`,
      javascript: `function uniquePaths(m, n) {\n    // Write your solution here\n}`,
      cpp: `int uniquePaths(int m, int n) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int uniquePaths(int m, int n) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def uniquePaths(m, n):\n    dp = [[1] * n for _ in range(m)]\n    for i in range(1, m):\n        for j in range(1, n):\n            dp[i][j] = dp[i-1][j] + dp[i][j-1]\n    return dp[m-1][n-1]`,
    },
    testCases: [
      { id: 1, input: 'm = 3, n = 7', expectedOutput: '28', isHidden: false },
      { id: 2, input: 'm = 3, n = 2', expectedOutput: '3', isHidden: false },
      { id: 3, input: 'm = 1, n = 1', expectedOutput: '1', isHidden: true },
    ],
    tags: ['dynamic-programming', '2d-dp', 'math'],
    estimatedTime: 15,
  },
  {
    id: 'cq_2ddp_longest_common_subseq',
    title: 'Longest Common Subsequence',
    difficulty: 'medium',
    topic: '2d-dp',
    problemStatement: `Given two strings \`text1\` and \`text2\`, return the length of their longest common subsequence. If there is no common subsequence, return \`0\`.\n\nA subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.`,
    examples: [
      { input: 'text1 = "abcde", text2 = "ace"', output: '3', explanation: 'The LCS is "ace", length 3.' },
      { input: 'text1 = "abc", text2 = "abc"', output: '3', explanation: 'The LCS is "abc", length 3.' },
      { input: 'text1 = "abc", text2 = "def"', output: '0', explanation: 'No common subsequence.' },
    ],
    constraints: ['1 <= text1.length, text2.length <= 1000', 'text1 and text2 consist of lowercase English letters only'],
    functionSignature: { python: 'def longestCommonSubsequence(text1: str, text2: str) -> int:', javascript: 'function longestCommonSubsequence(text1, text2)' },
    starterCode: {
      python: `def longestCommonSubsequence(text1, text2):\n    # Write your solution here\n    pass`,
      javascript: `function longestCommonSubsequence(text1, text2) {\n    // Write your solution here\n}`,
      cpp: `#include <string>\nusing namespace std;\n\nint longestCommonSubsequence(string text1, string text2) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int longestCommonSubsequence(String text1, String text2) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def longestCommonSubsequence(text1, text2):\n    m, n = len(text1), len(text2)\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    for i in range(1, m + 1):\n        for j in range(1, n + 1):\n            if text1[i-1] == text2[j-1]:\n                dp[i][j] = dp[i-1][j-1] + 1\n            else:\n                dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n    return dp[m][n]`,
    },
    testCases: [
      { id: 1, input: 'text1 = "abcde", text2 = "ace"', expectedOutput: '3', isHidden: false },
      { id: 2, input: 'text1 = "abc", text2 = "abc"', expectedOutput: '3', isHidden: false },
      { id: 3, input: 'text1 = "abc", text2 = "def"', expectedOutput: '0', isHidden: true },
    ],
    tags: ['dynamic-programming', '2d-dp', 'lcs'],
    estimatedTime: 20,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // KNAPSACK (1 question)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_dp_01_knapsack',
    title: 'Partition Equal Subset Sum',
    difficulty: 'medium',
    topic: 'dp',
    problemStatement: `Given an integer array \`nums\`, return \`true\` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal, or \`false\` otherwise.\n\nThis is equivalent to the 0/1 Knapsack problem where the target sum is half of the total array sum.`,
    examples: [
      { input: 'nums = [1,5,11,5]', output: 'true', explanation: 'The array can be partitioned as [1,5,5] and [11].' },
      { input: 'nums = [1,2,3,5]', output: 'false', explanation: 'No way to partition into equal sum subsets.' },
    ],
    constraints: ['1 <= nums.length <= 200', '1 <= nums[i] <= 100'],
    functionSignature: { python: 'def canPartition(nums: List[int]) -> bool:', javascript: 'function canPartition(nums)' },
    starterCode: {
      python: `def canPartition(nums):\n    # Write your solution here\n    pass`,
      javascript: `function canPartition(nums) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nbool canPartition(vector<int>& nums) {\n    // Write your solution here\n    return false;\n}`,
      java: `class Solution {\n    public boolean canPartition(int[] nums) {\n        // Write your solution here\n        return false;\n    }\n}`,
    },
    solutionCode: {
      python: `def canPartition(nums):\n    total = sum(nums)\n    if total % 2 != 0:\n        return False\n    target = total // 2\n    dp = [False] * (target + 1)\n    dp[0] = True\n    for num in nums:\n        for j in range(target, num - 1, -1):\n            dp[j] = dp[j] or dp[j - num]\n    return dp[target]`,
    },
    testCases: [
      { id: 1, input: 'nums = [1,5,11,5]', expectedOutput: 'true', isHidden: false },
      { id: 2, input: 'nums = [1,2,3,5]', expectedOutput: 'false', isHidden: false },
      { id: 3, input: 'nums = [1,1]', expectedOutput: 'true', isHidden: true },
    ],
    tags: ['dynamic-programming', 'knapsack'],
    estimatedTime: 20,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // TWO POINTERS (2 questions)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_tp_container_water',
    title: 'Container With Most Water',
    difficulty: 'medium',
    topic: 'two-pointers',
    problemStatement: `You are given an integer array \`height\` of length \`n\`. There are \`n\` vertical lines drawn such that the two endpoints of the \`i\`th line are \`(i, 0)\` and \`(i, height[i])\`.\n\nFind two lines that together with the x-axis form a container, such that the container contains the most water.\n\nReturn the maximum amount of water a container can store.`,
    examples: [
      { input: 'height = [1,8,6,2,5,4,8,3,7]', output: '49', explanation: 'Lines at index 1 (height 8) and index 8 (height 7) form a container with area 7*7=49.' },
      { input: 'height = [1,1]', output: '1', explanation: 'The only container has area 1.' },
    ],
    constraints: ['n == height.length', '2 <= n <= 10^5', '0 <= height[i] <= 10^4'],
    functionSignature: { python: 'def maxArea(height: List[int]) -> int:', javascript: 'function maxArea(height)' },
    starterCode: {
      python: `def maxArea(height):\n    # Write your solution here\n    pass`,
      javascript: `function maxArea(height) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint maxArea(vector<int>& height) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int maxArea(int[] height) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def maxArea(height):\n    left, right = 0, len(height) - 1\n    max_water = 0\n    while left < right:\n        w = right - left\n        h = min(height[left], height[right])\n        max_water = max(max_water, w * h)\n        if height[left] < height[right]:\n            left += 1\n        else:\n            right -= 1\n    return max_water`,
    },
    testCases: [
      { id: 1, input: 'height = [1,8,6,2,5,4,8,3,7]', expectedOutput: '49', isHidden: false },
      { id: 2, input: 'height = [1,1]', expectedOutput: '1', isHidden: false },
      { id: 3, input: 'height = [4,3,2,1,4]', expectedOutput: '16', isHidden: true },
    ],
    tags: ['two-pointers', 'greedy', 'array'],
    estimatedTime: 15,
  },
  {
    id: 'cq_tp_three_sum',
    title: '3Sum',
    difficulty: 'medium',
    topic: 'two-pointers',
    problemStatement: `Given an integer array \`nums\`, return all the triplets \`[nums[i], nums[j], nums[k]]\` such that \`i != j\`, \`i != k\`, and \`j != k\`, and \`nums[i] + nums[j] + nums[k] == 0\`.\n\nThe solution set must not contain duplicate triplets.`,
    examples: [
      { input: 'nums = [-1,0,1,2,-1,-4]', output: '[[-1,-1,2],[-1,0,1]]', explanation: 'The distinct triplets that sum to 0.' },
      { input: 'nums = [0,1,1]', output: '[]', explanation: 'No triplet sums to 0.' },
    ],
    constraints: ['3 <= nums.length <= 3000', '-10^5 <= nums[i] <= 10^5'],
    functionSignature: { python: 'def threeSum(nums: List[int]) -> List[List[int]]:', javascript: 'function threeSum(nums)' },
    starterCode: {
      python: `def threeSum(nums):\n    # Write your solution here\n    pass`,
      javascript: `function threeSum(nums) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvector<vector<int>> threeSum(vector<int>& nums) {\n    // Write your solution here\n    return {};\n}`,
      java: `class Solution {\n    public List<List<Integer>> threeSum(int[] nums) {\n        // Write your solution here\n        return new ArrayList<>();\n    }\n}`,
    },
    solutionCode: {
      python: `def threeSum(nums):\n    nums.sort()\n    result = []\n    for i in range(len(nums) - 2):\n        if i > 0 and nums[i] == nums[i-1]:\n            continue\n        left, right = i + 1, len(nums) - 1\n        while left < right:\n            total = nums[i] + nums[left] + nums[right]\n            if total < 0:\n                left += 1\n            elif total > 0:\n                right -= 1\n            else:\n                result.append([nums[i], nums[left], nums[right]])\n                while left < right and nums[left] == nums[left+1]:\n                    left += 1\n                while left < right and nums[right] == nums[right-1]:\n                    right -= 1\n                left += 1\n                right -= 1\n    return result`,
    },
    testCases: [
      { id: 1, input: 'nums = [-1,0,1,2,-1,-4]', expectedOutput: '[[-1,-1,2],[-1,0,1]]', isHidden: false },
      { id: 2, input: 'nums = [0,1,1]', expectedOutput: '[]', isHidden: false },
      { id: 3, input: 'nums = [0,0,0]', expectedOutput: '[[0,0,0]]', isHidden: true },
    ],
    tags: ['two-pointers', 'sorting', 'array'],
    estimatedTime: 20,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // SLIDING WINDOW (1 question)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_sw_max_profit',
    title: 'Best Time to Buy and Sell Stock',
    difficulty: 'easy',
    topic: 'sliding-window',
    problemStatement: `You are given an array \`prices\` where \`prices[i]\` is the price of a given stock on the \`i\`th day.\n\nYou want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.\n\nReturn the maximum profit you can achieve. If you cannot achieve any profit, return \`0\`.`,
    examples: [
      { input: 'prices = [7,1,5,3,6,4]', output: '5', explanation: 'Buy on day 2 (price=1) and sell on day 5 (price=6), profit=5.' },
      { input: 'prices = [7,6,4,3,1]', output: '0', explanation: 'Prices are decreasing, no profit possible.' },
    ],
    constraints: ['1 <= prices.length <= 10^5', '0 <= prices[i] <= 10^4'],
    functionSignature: { python: 'def maxProfit(prices: List[int]) -> int:', javascript: 'function maxProfit(prices)' },
    starterCode: {
      python: `def maxProfit(prices):\n    # Write your solution here\n    pass`,
      javascript: `function maxProfit(prices) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint maxProfit(vector<int>& prices) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int maxProfit(int[] prices) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def maxProfit(prices):\n    min_price = float('inf')\n    max_profit = 0\n    for price in prices:\n        min_price = min(min_price, price)\n        max_profit = max(max_profit, price - min_price)\n    return max_profit`,
    },
    testCases: [
      { id: 1, input: 'prices = [7,1,5,3,6,4]', expectedOutput: '5', isHidden: false },
      { id: 2, input: 'prices = [7,6,4,3,1]', expectedOutput: '0', isHidden: false },
      { id: 3, input: 'prices = [1,2]', expectedOutput: '1', isHidden: true },
    ],
    tags: ['sliding-window', 'array', 'greedy'],
    estimatedTime: 10,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // PREFIX SUM (1 question)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_prefix_subarray_sum_k',
    title: 'Subarray Sum Equals K',
    difficulty: 'medium',
    topic: 'prefix-sum',
    problemStatement: `Given an array of integers \`nums\` and an integer \`k\`, return the total number of subarrays whose sum equals to \`k\`.\n\nA subarray is a contiguous non-empty sequence of elements within an array.`,
    examples: [
      { input: 'nums = [1,1,1], k = 2', output: '2', explanation: 'Two subarrays [1,1] starting at index 0 and 1.' },
      { input: 'nums = [1,2,3], k = 3', output: '2', explanation: 'Subarrays [1,2] and [3] both sum to 3.' },
    ],
    constraints: ['1 <= nums.length <= 2 * 10^4', '-1000 <= nums[i] <= 1000', '-10^7 <= k <= 10^7'],
    functionSignature: { python: 'def subarraySum(nums: List[int], k: int) -> int:', javascript: 'function subarraySum(nums, k)' },
    starterCode: {
      python: `def subarraySum(nums, k):\n    # Write your solution here\n    pass`,
      javascript: `function subarraySum(nums, k) {\n    // Write your solution here\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nint subarraySum(vector<int>& nums, int k) {\n    // Write your solution here\n    return 0;\n}`,
      java: `class Solution {\n    public int subarraySum(int[] nums, int k) {\n        // Write your solution here\n        return 0;\n    }\n}`,
    },
    solutionCode: {
      python: `def subarraySum(nums, k):\n    count = 0\n    prefix = 0\n    prefix_counts = {0: 1}\n    for num in nums:\n        prefix += num\n        count += prefix_counts.get(prefix - k, 0)\n        prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1\n    return count`,
    },
    testCases: [
      { id: 1, input: 'nums = [1,1,1], k = 2', expectedOutput: '2', isHidden: false },
      { id: 2, input: 'nums = [1,2,3], k = 3', expectedOutput: '2', isHidden: false },
      { id: 3, input: 'nums = [1,-1,0], k = 0', expectedOutput: '3', isHidden: true },
    ],
    tags: ['prefix-sum', 'hash-table', 'array'],
    estimatedTime: 15,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // MATRIX / 2D GRID (1 question)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_matrix_rotate',
    title: 'Rotate Image',
    difficulty: 'medium',
    topic: 'arrays',
    problemStatement: `You are given an \`n x n\` 2D matrix representing an image, rotate the image by 90 degrees clockwise.\n\nYou have to rotate the image in-place, which means you have to modify the input matrix directly. Do NOT allocate another 2D matrix.`,
    examples: [
      { input: 'matrix = [[1,2,3],[4,5,6],[7,8,9]]', output: '[[7,4,1],[8,5,2],[9,6,3]]', explanation: 'Rotate the 3x3 matrix 90 degrees clockwise.' },
      { input: 'matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]', output: '[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]', explanation: 'Rotate the 4x4 matrix 90 degrees clockwise.' },
    ],
    constraints: ['n == matrix.length == matrix[i].length', '1 <= n <= 20', '-1000 <= matrix[i][j] <= 1000'],
    functionSignature: { python: 'def rotate(matrix: List[List[int]]) -> None:', javascript: 'function rotate(matrix)' },
    starterCode: {
      python: `def rotate(matrix):\n    # Write your solution here (modify in-place)\n    pass`,
      javascript: `function rotate(matrix) {\n    // Write your solution here (modify in-place)\n}`,
      cpp: `#include <vector>\nusing namespace std;\n\nvoid rotate(vector<vector<int>>& matrix) {\n    // Write your solution here\n}`,
      java: `class Solution {\n    public void rotate(int[][] matrix) {\n        // Write your solution here\n    }\n}`,
    },
    solutionCode: {
      python: `def rotate(matrix):\n    n = len(matrix)\n    # Transpose\n    for i in range(n):\n        for j in range(i + 1, n):\n            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n    # Reverse each row\n    for row in matrix:\n        row.reverse()`,
    },
    testCases: [
      { id: 1, input: 'matrix = [[1,2,3],[4,5,6],[7,8,9]]', expectedOutput: '[[7,4,1],[8,5,2],[9,6,3]]', isHidden: false },
      { id: 2, input: 'matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]', expectedOutput: '[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]', isHidden: false },
      { id: 3, input: 'matrix = [[1]]', expectedOutput: '[[1]]', isHidden: true },
    ],
    tags: ['matrix', 'array', 'math'],
    estimatedTime: 15,
  },

  // ═══════════════════════════════════════════════════════════════════════════
  // TRIE (1 question)
  // ═══════════════════════════════════════════════════════════════════════════
  {
    id: 'cq_trie_implement',
    title: 'Implement Trie (Prefix Tree)',
    difficulty: 'medium',
    topic: 'advanced-dsa',
    problemStatement: `Implement a trie with \`insert\`, \`search\`, and \`startsWith\` methods.\n\n- \`insert(word)\`: Inserts the string \`word\` into the trie.\n- \`search(word)\`: Returns \`true\` if the string \`word\` is in the trie, and \`false\` otherwise.\n- \`startsWith(prefix)\`: Returns \`true\` if there is a previously inserted string that has the prefix \`prefix\`, and \`false\` otherwise.`,
    examples: [
      { input: '["Trie","insert","search","search","startsWith","insert","search"]\n[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]', output: '[null,null,true,false,true,null,true]', explanation: 'Insert "apple", search for it (found), search "app" (not a complete word), startsWith "app" (true), insert "app", search "app" (now found).' },
    ],
    constraints: ['1 <= word.length, prefix.length <= 2000', 'word and prefix consist only of lowercase English letters', 'At most 3 * 10^4 calls to insert, search, and startsWith'],
    functionSignature: { python: 'class Trie:', javascript: 'class Trie' },
    starterCode: {
      python: `class Trie:\n    def __init__(self):\n        # Initialize your data structure here\n        pass\n\n    def insert(self, word):\n        # Write your solution here\n        pass\n\n    def search(self, word):\n        # Write your solution here\n        pass\n\n    def startsWith(self, prefix):\n        # Write your solution here\n        pass`,
      javascript: `class Trie {\n    constructor() {\n        // Initialize your data structure here\n    }\n\n    insert(word) {\n        // Write your solution here\n    }\n\n    search(word) {\n        // Write your solution here\n    }\n\n    startsWith(prefix) {\n        // Write your solution here\n    }\n}`,
      cpp: `class Trie {\npublic:\n    Trie() {\n        // Initialize your data structure here\n    }\n\n    void insert(string word) {\n        // Write your solution here\n    }\n\n    bool search(string word) {\n        // Write your solution here\n        return false;\n    }\n\n    bool startsWith(string prefix) {\n        // Write your solution here\n        return false;\n    }\n};`,
      java: `class Trie {\n    public Trie() {\n        // Initialize your data structure here\n    }\n\n    public void insert(String word) {\n        // Write your solution here\n    }\n\n    public boolean search(String word) {\n        // Write your solution here\n        return false;\n    }\n\n    public boolean startsWith(String prefix) {\n        // Write your solution here\n        return false;\n    }\n}`,
    },
    solutionCode: {
      python: `class Trie:\n    def __init__(self):\n        self.children = {}\n        self.is_end = False\n\n    def insert(self, word):\n        node = self\n        for c in word:\n            if c not in node.children:\n                node.children[c] = Trie()\n            node = node.children[c]\n        node.is_end = True\n\n    def search(self, word):\n        node = self._find(word)\n        return node is not None and node.is_end\n\n    def startsWith(self, prefix):\n        return self._find(prefix) is not None\n\n    def _find(self, prefix):\n        node = self\n        for c in prefix:\n            if c not in node.children:\n                return None\n            node = node.children[c]\n        return node`,
    },
    testCases: [
      { id: 1, input: 'insert("apple"), search("apple")', expectedOutput: 'true', isHidden: false },
      { id: 2, input: 'insert("apple"), search("app")', expectedOutput: 'false', isHidden: false },
      { id: 3, input: 'insert("apple"), startsWith("app")', expectedOutput: 'true', isHidden: true },
    ],
    tags: ['trie', 'design', 'string'],
    estimatedTime: 20,
  },
];

export default codingQuestions;
