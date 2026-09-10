import os
import json
import ast
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# =============================================================================
# LEETCODE-STYLE DEFINITIONS FOR ALL 120 QUESTIONS
# =============================================================================

UPDATES = {
    # -------------------------------------------------------------------------
    # 1. ARRAYS (10 Questions)
    # -------------------------------------------------------------------------
    "q_arr_two_sum_sorted": {
        "problemStatement": (
            "Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, "
            "find two numbers such that they add up to a specific `target` number. Let these two numbers be "
            "`numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.\n\n"
            "Return the indices of the two numbers, `[index1, index2]`, as an integer array of length 2.\n\n"
            "The tests are generated such that there is exactly one solution. You may not use the same element twice."
        ),
        "explanations": [
            "The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].",
            "The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3. We return [1, 3]."
        ]
    },
    "q_arr_max_subarray_kadane": {
        "problemStatement": (
            "Given an integer array `nums`, find the subarray with the largest sum, and return its sum.\n\n"
            "A subarray is a contiguous non-empty sequence of elements within an array."
        ),
        "explanations": [
            "The subarray [4,-1,2,1] has the largest sum 6.",
            "The subarray [1] has the largest sum 1."
        ]
    },
    "q_arr_product_except_self": {
        "problemStatement": (
            "Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.\n\n"
            "The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.\n\n"
            "You must write an algorithm that runs in O(n) time and without using the division operation."
        ),
        "explanations": [
            "The product of all elements except nums[0] is 2*3*4 = 24. For nums[1], 1*3*4 = 12. For nums[2], 1*2*4 = 8. For nums[3], 1*2*3 = 6.",
            "The product of elements except at index 2 contains non-zero factors resulting in 0 everywhere else, and 9 at index 2."
        ]
    },
    "q_arr_trapping_rain_water": {
        "problemStatement": (
            "Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.\n\n"
            "Water can only be trapped between taller bars that bound a lower elevation area."
        ),
        "explanations": [
            "The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are trapped.",
            "The elevation bars trap 9 units of water across the troughs between heights 4 and 5."
        ]
    },
    "q_arr_merge_sorted_array": {
        "problemStatement": (
            "You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.\n\n"
            "Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.\n\n"
            "The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`."
        ),
        "explanations": [
            "The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the elements stored in nums1.",
            "The arrays we are merging are [1] and []. The result of the merge is [1]."
        ]
    },
    "q_arr_sort_colors": {
        "problemStatement": (
            "Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.\n\n"
            "We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.\n\n"
            "You must solve this problem without using the library's sort function and in-place."
        ),
        "explanations": [
            "Sorting the colors in-place results in [0,0,1,1,2,2].",
            "Sorting the colors in-place results in [0,1,2]."
        ]
    },
    "q_arr_merge_intervals": {
        "problemStatement": (
            "Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals.\n\n"
            "Return an array of the non-overlapping intervals that cover all the intervals in the input."
        ),
        "explanations": [
            "Since intervals [1,3] and [2,6] overlap, merge them into [1,6].",
            "Intervals [1,4] and [4,5] are considered overlapping because they share the endpoint 4."
        ]
    },
    "q_arr_min_size_subarray_sum": {
        "problemStatement": (
            "Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`.\n\n"
            "If there is no such subarray, return `0` instead.\n\n"
            "A subarray is a contiguous non-empty sequence of elements within an array."
        ),
        "explanations": [
            "The subarray [4,3] has the minimal length 2 with sum 7 >= 7.",
            "The subarray [4] has length 1 with sum >= 4."
        ]
    },
    "q_arr_next_permutation": {
        "problemStatement": (
            "A permutation of an array of integers is an arrangement of its members into a sequence or linear order.\n\n"
            "The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container.\n\n"
            "If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order). The replacement must be in-place."
        ),
        "explanations": [
            "The next permutation of [1,2,3] is [1,3,2].",
            "Since [3,2,1] is in descending order, it is rearranged to the lowest possible order [1,2,3]."
        ]
    },
    "q_arr_container_with_most_water": {
        "problemStatement": (
            "You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.\n\n"
            "Find two lines that together with the x-axis form a container, such that the container contains the most water.\n\n"
            "Return the maximum amount of water a container can store. Notice that you may not slant the container."
        ),
        "explanations": [
            "The vertical lines are at indices 1 and 8 with heights 8 and 7. The distance is 7, yielding a maximum area of 7 * 7 = 49.",
            "The distance between lines is 1 with height 1, yielding an area of 1."
        ]
    },

    # -------------------------------------------------------------------------
    # 2. STRINGS (8 Questions)
    # -------------------------------------------------------------------------
    "q_str_longest_unique_substring": {
        "problemStatement": (
            "Given a string `s`, find the length of the longest substring without repeating characters.\n\n"
            "A substring is a contiguous non-empty sequence of characters within a string."
        ),
        "explanations": [
            "The answer is \"abc\", with the length of 3.",
            "The answer is \"b\", with the length of 1."
        ]
    },
    "q_str_valid_anagram": {
        "problemStatement": (
            "Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.\n\n"
            "An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."
        ),
        "explanations": [
            "Both strings contain the exact same count for every character: 'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1.",
            "Character 'r', 'a', 't' in s does not match the frequency of characters in t."
        ]
    },
    "q_str_longest_palindromic_substring": {
        "problemStatement": (
            "Given a string `s`, return the longest palindromic substring in `s`.\n\n"
            "A string is palindromic if it reads the same forward and backward."
        ),
        "explanations": [
            "\"bab\" is a valid answer. \"aba\" is also a valid answer.",
            "The longest palindromic substring is \"bb\"."
        ]
    },
    "q_str_valid_palindrome_ii": {
        "problemStatement": (
            "Given a string `s`, return `true` if the `s` can be palindrome after deleting at most one character from it.\n\n"
            "A string is a palindrome if it reads the same forward and backward."
        ),
        "explanations": [
            "The string is already a palindrome without removing any character.",
            "You could delete the character 'c' to get \"aba\", which is a palindrome."
        ]
    },
    "q_str_string_compression": {
        "problemStatement": (
            "Given an array of characters `chars`, compress it using the following algorithm:\n\n"
            "Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:\n"
            "- If the group's length is `1`, append the character to `s`.\n"
            "- Otherwise, append the character followed by the group's length.\n\n"
            "The compressed string `s` should not be returned separately, but instead, be stored in the input character array `chars`. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.\n\n"
            "After you are done modifying the input array, return the new length of the array."
        ),
        "explanations": [
            "The groups are \"aa\", \"bb\", and \"ccc\". This compresses to \"a2b2c3\" with length 6.",
            "The only group is \"a\", which remains uncompressed with length 1."
        ]
    },
    "q_str_min_window_substring": {
        "problemStatement": (
            "Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window.\n\n"
            "If there is no such substring, return the empty string `\"\"`.\n\n"
            "The testcases will be generated such that the answer is unique."
        ),
        "explanations": [
            "The minimum window substring \"BANC\" includes 'A', 'B', and 'C' from string t.",
            "The entire string \"a\" is the minimum window."
        ]
    },
    "q_str_character_replacement": {
        "problemStatement": (
            "You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.\n\n"
            "Return the length of the longest substring containing the same letter you can get after performing the above operations."
        ),
        "explanations": [
            "Replace the two 'A's with two 'B's or vice versa to produce \"BBBB\" or \"AAAA\" of length 4.",
            "Replace the middle 'A' with 'B' to form \"AABBBBA\". The substring \"BBBB\" has the longest repeating letters, which is 4."
        ]
    },
    "q_str_decode_string": {
        "problemStatement": (
            "Given an encoded string, return its decoded string.\n\n"
            "The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.\n\n"
            "You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`."
        ),
        "explanations": [
            "\"a\" is repeated 3 times, followed by \"bc\" repeated 2 times, giving \"aaabcbc\".",
            "The inner \"2[c]\" becomes \"cc\", resulting in \"3[acc]\", which expands to \"accaccacc\"."
        ]
    },

    # -------------------------------------------------------------------------
    # 3. HASHMAP / HASHSET (6 Questions)
    # -------------------------------------------------------------------------
    "q_hash_two_sum": {
        "problemStatement": (
            "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.\n\n"
            "You may assume that each input would have exactly one solution, and you may not use the same element twice.\n\n"
            "You can return the answer in any order."
        ),
        "explanations": [
            "Because nums[0] + nums[1] == 9, we return [0, 1].",
            "Because nums[1] + nums[2] == 6, we return [1, 2]."
        ]
    },
    "q_hash_longest_consecutive_seq": {
        "problemStatement": (
            "Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.\n\n"
            "You must write an algorithm that runs in O(n) time."
        ),
        "explanations": [
            "The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.",
            "The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Therefore its length is 9."
        ]
    },
    "q_hash_subarray_sum_equals_k": {
        "problemStatement": (
            "Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.\n\n"
            "A subarray is a contiguous non-empty sequence of elements within an array."
        ),
        "explanations": [
            "There are two subarrays that sum to 2: [1,1] starting at index 0 and [1,1] starting at index 1.",
            "Subarrays [1,2] and [3] each sum to 3, giving a count of 2."
        ]
    },
    "q_hash_group_anagrams": {
        "problemStatement": (
            "Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.\n\n"
            "An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."
        ),
        "explanations": [
            "\"eat\", \"tea\", and \"ate\" are anagrams. \"tan\" and \"nat\" are anagrams. \"bat\" is in its own group.",
            "The single empty string forms its own anagram group [[\"\"]]."
        ]
    },
    "q_hash_first_unique_char": {
        "problemStatement": (
            "Given a string `s`, find the first non-repeating character in it and return its index.\n\n"
            "If it does not exist, return `-1`."
        ),
        "explanations": [
            "The character 'l' at index 0 is the first character that does not occur at any other index.",
            "The character 'v' at index 2 is the first non-repeating character."
        ]
    },
    "q_hash_subarray_divisible_by_k": {
        "problemStatement": (
            "Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.\n\n"
            "A subarray is a contiguous part of an array."
        ),
        "explanations": [
            "There are 7 subarrays with a sum divisible by k = 5: [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3].",
            "No non-empty subarray sums to a multiple of 9, so count is 0."
        ]
    },

    # -------------------------------------------------------------------------
    # 4. TREES & BST (10 Questions from bank_trees.py)
    # -------------------------------------------------------------------------
    "q_tree_max_depth": {
        "problemStatement": (
            "Given the root of a binary tree, return its maximum depth.\n\n"
            "A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."
        ),
        "explanations": [
            "The longest path is 3 -> 20 -> 15 (or 3 -> 20 -> 7), which has 3 nodes.",
            "The longest path is 1 -> 2, which has 2 nodes."
        ]
    },
    "q_tree_invert": {
        "problemStatement": (
            "Given the root of a binary tree, invert the tree, and return its root.\n\n"
            "Inverting a binary tree means swapping every left and right child recursively."
        ),
        "explanations": [
            "Every left subtree and right subtree is mirrored across the vertical axis.",
            "The left child 1 and right child 3 are swapped to become right child 1 and left child 3."
        ]
    },
    "q_tree_validate_bst": {
        "problemStatement": (
            "Given the root of a binary tree, determine if it is a valid binary search tree (BST).\n\n"
            "A valid BST is defined as follows:\n"
            "- The left subtree of a node contains only nodes with keys strictly less than the node's key.\n"
            "- The right subtree of a node contains only nodes with keys strictly greater than the node's key.\n"
            "- Both the left and right subtrees must also be binary search trees."
        ),
        "explanations": [
            "The root node's value is 2, with left child 1 (< 2) and right child 3 (> 2), which is a valid BST.",
            "The root node's value is 5 but its right child's value is 4, which violates the BST property."
        ]
    },
    "q_tree_lca_binary_tree": {
        "problemStatement": (
            "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.\n\n"
            "According to the definition of LCA on Wikipedia: \"The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).\""
        ),
        "explanations": [
            "The LCA of nodes 5 and 1 is 3 since 3 is the lowest node with both 5 and 1 as descendants.",
            "The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition."
        ]
    },
    "q_tree_diameter": {
        "problemStatement": (
            "Given the root of a binary tree, return the length of the diameter of the tree.\n\n"
            "The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.\n\n"
            "The length of a path between two nodes is represented by the number of edges between them."
        ),
        "explanations": [
            "3 is the length of the path [4,2,1,3] or [5,2,1,3], which has 3 edges.",
            "The path between 1 and 2 has 1 edge."
        ]
    },
    "q_tree_level_order_traversal": {
        "problemStatement": (
            "Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level)."
        ),
        "explanations": [
            "Level 0 has [3], level 1 has [9, 20], and level 2 has [15, 7].",
            "Level 0 has node [1]."
        ]
    },
    "q_tree_path_sum_ii": {
        "problemStatement": (
            "Given the root of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values in the path equals `targetSum`.\n\n"
            "Each path should be returned as a list of the node values, not node references.\n\n"
            "A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children."
        ),
        "explanations": [
            "There are two root-to-leaf paths that sum to 22: 5 -> 4 -> 11 -> 2 and 5 -> 8 -> 4 -> 5.",
            "There are no root-to-leaf paths that sum to 5."
        ]
    },
    "q_tree_kth_smallest_bst": {
        "problemStatement": (
            "Given the root of a binary search tree (BST) and an integer `k`, return the `k-th` smallest value (1-indexed) of all the values of the nodes in the tree."
        ),
        "explanations": [
            "The in-order sorted values are [1, 2, 3, 4]. The 1st smallest element is 1.",
            "The in-order sorted values are [1, 2, 3, 4, 5, 6]. The 3rd smallest element is 3."
        ]
    },
    "q_tree_symmetric_tree": {
        "problemStatement": (
            "Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)."
        ),
        "explanations": [
            "The left subtree [2, 3, 4] is a mirror reflection of the right subtree [2, 4, 3].",
            "The left subtree [2, null, 3] and right subtree [2, null, 3] are identical in shape, not mirror reflections."
        ]
    },
    "q_tree_max_path_sum": {
        "problemStatement": (
            "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.\n\nThe path sum of a path is the sum of the node's values in the path.\n\nGiven the root of a binary tree, return the maximum path sum of any non-empty path."
        ),
        "explanations": [
            "The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.",
            "The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42."
        ]
    },

    # -------------------------------------------------------------------------
    # 5. TREES EXPANDED (9 Questions from bank_trees_missing.py)
    # -------------------------------------------------------------------------
    "q_tree_preorder_traversal": {
        "problemStatement": (
            "Given the root of a binary tree, return the preorder traversal of its nodes' values.\n\n"
            "Preorder traversal visits the root node first, followed by the left subtree, and then the right subtree."
        ),
        "explanations": [
            "Preorder visits 1, then right child 2, and then 2's left child 3, yielding [1, 2, 3].",
            "The tree is empty, so the traversal is empty."
        ]
    },
    "q_tree_inorder_traversal": {
        "problemStatement": (
            "Given the root of a binary tree, return the inorder traversal of its nodes' values.\n\n"
            "Inorder traversal visits the left subtree first, followed by the root node, and then the right subtree."
        ),
        "explanations": [
            "Inorder traversal visits 1, then 3, then 2, producing [1, 3, 2].",
            "The empty tree yields an empty list []."
        ]
    },
    "q_tree_postorder_traversal": {
        "problemStatement": (
            "Given the root of a binary tree, return the postorder traversal of its nodes' values.\n\n"
            "Postorder traversal visits the left subtree first, followed by the right subtree, and then the root node."
        ),
        "explanations": [
            "Postorder traversal visits 3, then 2, then 1, yielding [3, 2, 1].",
            "The empty tree yields []."
        ]
    },
    "q_tree_same_tree": {
        "problemStatement": (
            "Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.\n\n"
            "Two binary trees are considered the same if they are structurally identical, and the nodes have the same value."
        ),
        "explanations": [
            "Both trees have root 1, left child 2, and right child 3 with identical structure and values.",
            "Tree p has left child 2 while tree q has right child 2, so their structures differ."
        ]
    },
    "q_tree_balanced_binary_tree": {
        "problemStatement": (
            "Given a binary tree, determine if it is height-balanced.\n\n"
            "A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one."
        ),
        "explanations": [
            "The height difference between left and right subtrees at every node is at most 1.",
            "The root's left subtree has depth 3 while the right subtree has depth 1. The difference is 2 > 1, so the tree is unbalanced."
        ]
    },
    "q_tree_serialize_deserialize": {
        "problemStatement": (
            "Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.\n\n"
            "Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure."
        ),
        "explanations": [
            "The binary tree is serialized into a string representation and then deserialized back into an identical tree.",
            "An empty tree is serialized and deserialized back to null."
        ]
    },
    "q_tree_vertical_order": {
        "problemStatement": (
            "Given the root of a binary tree, calculate the vertical order traversal of the binary tree.\n\n"
            "For each node at position `(row, col)`, its left and right children will be at `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.\n\n"
            "The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values."
        ),
        "explanations": [
            "Column -1 contains [9], column 0 contains [3, 15], column 1 contains [20], and column 2 contains [7].",
            "Columns from left to right are -2: [4], -1: [2], 0: [1, 5, 6], 1: [3], 2: [7]."
        ]
    },
    "q_tree_cameras": {
        "problemStatement": (
            "You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.\n\n"
            "Return the minimum number of cameras needed to monitor all nodes of the tree."
        ),
        "explanations": [
            "One camera placed at node 0 (parent of leaves) is sufficient to monitor all nodes in the tree.",
            "At least 2 cameras are needed to cover all nodes in this deeper chain."
        ]
    },
    "q_tree_recover_from_preorder": {
        "problemStatement": (
            "We run a preorder depth-first search (DFS) on the root of a binary tree.\n\n"
            "At each node in this traversal, we output `D` dashes (where `D` is the depth of this node), then we output the value of this node. If the depth of a node is `D`, the depth of its immediate child is `D + 1`. The depth of the root node is `0`.\n\n"
            "If a node has only one child, that child is guaranteed to be the left child.\n\n"
            "Given the output `traversal` of this traversal, recover the tree and return its root."
        ),
        "explanations": [
            "The string \"1-2--3--4-5--6--7\" reconstructs the binary tree with root 1, children 2 and 5, and their respective children.",
            "The dashes encode the hierarchy and depths of each node in preorder."
        ]
    },

    # -------------------------------------------------------------------------
    # 6. BST EXPANDED (13 Questions from bank_bst_missing.py)
    # -------------------------------------------------------------------------
    "q_bst_search": {
        "problemStatement": (
            "You are given the root of a binary search tree (BST) and an integer `val`.\n\n"
            "Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`."
        ),
        "explanations": [
            "The node with value 2 exists, and the subtree rooted at 2 is [2, 1, 3].",
            "Value 5 does not exist in the BST, so null is returned."
        ]
    },
    "q_bst_min_absolute_diff": {
        "problemStatement": (
            "Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree."
        ),
        "explanations": [
            "The minimum absolute difference is between node 2 and node 1 (2 - 1 = 1) or node 3 and node 2 (3 - 2 = 1).",
            "The minimum absolute difference is 1 (between 0 and 1, or 48 and 49)."
        ]
    },
    "q_bst_sorted_array_to_bst": {
        "problemStatement": (
            "Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.\n\n"
            "A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one."
        ),
        "explanations": [
            "Choosing the middle element 0 as root yields a height-balanced BST [0, -3, 9, -10, null, 5].",
            "Middle element 3 as root yields left child 1."
        ]
    },
    "q_bst_range_sum": {
        "problemStatement": (
            "Given the root node of a binary search tree and two integers `low` and `high`, return the sum of values of all nodes with a value in the inclusive range `[low, high]`."
        ),
        "explanations": [
            "Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.",
            "Nodes 6, 7, 10, and 15 are in the range [6, 10]. 6 + 7 + 10 = 23."
        ]
    },
    "q_bst_two_sum": {
        "problemStatement": (
            "Given the root of a binary search tree and an integer `k`, return `true` if there exist two elements in the BST such that their sum is equal to `k`, or `false` otherwise."
        ),
        "explanations": [
            "Nodes 5 and 4 sum to 9, so the function returns true.",
            "There are no two distinct nodes that sum to 28."
        ]
    },
    "q_bst_lca": {
        "problemStatement": (
            "Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.\n\n"
            "According to the definition of LCA on Wikipedia: \"The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).\""
        ),
        "explanations": [
            "The LCA of nodes 2 and 8 is 6 because 2 is in the left subtree and 8 is in the right subtree of 6.",
            "The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself."
        ]
    },
    "q_bst_delete_node": {
        "problemStatement": (
            "Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.\n\n"
            "Basically, the deletion can be divided into two stages:\n"
            "1. Search for a node to remove.\n"
            "2. If the node is found, delete the node."
        ),
        "explanations": [
            "Node 3 is removed. Valid replacements for 3 include 4 (its inorder successor) or 2 (its inorder predecessor).",
            "Key 0 is not found in the BST, so the tree remains unchanged."
        ]
    },
    "q_bst_insert_node": {
        "problemStatement": (
            "You are given the root node of a binary search tree (BST) and a `val` to insert into the tree. Return the root node of the BST after the insertion.\n\n"
            "It is guaranteed that the new value does not exist in the original BST.\n\n"
            "Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them."
        ),
        "explanations": [
            "Value 5 is inserted as the right child of node 4, maintaining the BST property.",
            "Value 25 is inserted as the right child of node 20."
        ]
    },
    "q_bst_recover_tree": {
        "problemStatement": (
            "You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure."
        ),
        "explanations": [
            "1 cannot be a child of 3 because 1 < 3. Swapping 1 and 3 recovers the BST.",
            "Nodes 3 and 2 were swapped. Swapping them back restores valid BST ordering."
        ]
    },
    "q_bst_iterator": {
        "problemStatement": (
            "Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST):\n\n"
            "- `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.\n"
            "- `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.\n"
            "- `int next()` Moves the pointer to the right, then returns the number at the pointer.\n\n"
            "Notice that by initializing the pointer to a non-existent smallest number, the first call to `next()` will return the smallest element in the BST."
        ),
        "explanations": [
            "Inorder traversal yields sequence 3, 7, 9, 15, 20. Calls to next() successively return these values.",
            "The iterator correctly processes elements in sorted order."
        ]
    },
    "q_bst_serialize_deserialize": {
        "problemStatement": (
            "Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.\n\n"
            "Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.\n\n"
            "The encoded string should be as compact as possible."
        ),
        "explanations": [
            "The BST is serialized into a string and deserialized back to an identical BST.",
            "An empty BST serializes and deserializes cleanly back to null."
        ]
    },
    "q_bst_count_smaller_after_self": {
        "problemStatement": (
            "Given an integer array `nums`, return an integer array `counts` where `counts[i]` is the number of smaller elements to the right of `nums[i]`."
        ),
        "explanations": [
            "To the right of 5 there are 2 smaller elements (2 and 1). To the right of 2 there is 1 (1). To the right of 6 there is 1 (1). To the right of 1 there are 0. Result: [2,1,1,0].",
            "To the right of -1 there are 0 smaller elements. To the right of -1 there are 0. Result: [0,0]."
        ]
    },
    "q_bst_balance_tree": {
        "problemStatement": (
            "Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.\n\n"
            "A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than `1`."
        ),
        "explanations": [
            "The skewed BST [1, null, 2, null, 3, null, 4] is converted into a balanced BST [2, 1, 3, null, null, null, 4].",
            "The skewed 3-node BST is rebalanced with root 2, left child 1, and right child 3."
        ]
    },

    # -------------------------------------------------------------------------
    # 7. RECURSION & BACKTRACKING (6 Questions)
    # -------------------------------------------------------------------------
    "q_rec_subsets": {
        "problemStatement": (
            "Given an integer array `nums` of unique elements, return all possible subsets (the power set).\n\n"
            "The solution set must not contain duplicate subsets. Return the solution in any order."
        ),
        "explanations": [
            "The power set contains 2^3 = 8 subsets: [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3].",
            "The single element array has subsets [] and [0]."
        ]
    },
    "q_rec_permutations": {
        "problemStatement": (
            "Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order."
        ),
        "explanations": [
            "There are 3! = 6 unique permutations: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].",
            "The two permutations are [[0,1],[1,0]]."
        ]
    },
    "q_rec_combination_sum": {
        "problemStatement": (
            "Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.\n\n"
            "The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.\n\n"
            "The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input."
        ),
        "explanations": [
            "2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is also a candidate, and 7 = 7. These are the only two combinations.",
            "2 + 2 + 2 + 2 = 8, 2 + 3 + 3 = 8, and 3 + 5 = 8 are the valid combinations summing to 8."
        ]
    },
    "q_rec_word_search": {
        "problemStatement": (
            "Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.\n\n"
            "The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once."
        ),
        "explanations": [
            "The word \"ABCCED\" can be traced along the path (0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(2,1).",
            "The word \"SEE\" can be traced along (1,3)->(2,3)->(2,2)."
        ]
    },
    "q_rec_generate_parentheses": {
        "problemStatement": (
            "Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses."
        ),
        "explanations": [
            "There are 5 valid well-formed combinations for n = 3: \"((()))\", \"(()())\", \"(())()\", \"()(())\", \"()()()\".",
            "The only well-formed combination for n = 1 is \"()\"."
        ]
    },
    "q_rec_n_queens": {
        "problemStatement": (
            "The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.\n\n"
            "Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.\n\n"
            "Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively."
        ),
        "explanations": [
            "There exist two distinct solutions to the 4-queens puzzle as shown above.",
            "There is only 1 solution for a 1x1 board: [\"Q\"]."
        ]
    },

    # -------------------------------------------------------------------------
    # 8. DYNAMIC PROGRAMMING (8 Questions from bank_dp.py)
    # -------------------------------------------------------------------------
    "q_dp_climbing_stairs": {
        "problemStatement": (
            "You are climbing a staircase. It takes `n` steps to reach the top.\n\n"
            "Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?"
        ),
        "explanations": [
            "There are two ways to climb to the top: 1 step + 1 step, or 2 steps.",
            "There are three ways to climb to the top: 1+1+1, 1+2, or 2+1."
        ]
    },
    "q_dp_coin_change": {
        "problemStatement": (
            "You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.\n\n"
            "Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.\n\n"
            "You may assume that you have an infinite number of each kind of coin."
        ),
        "explanations": [
            "11 = 5 + 5 + 1 (3 coins of minimum count).",
            "The amount of 3 cannot be made with only coins of value 2."
        ]
    },
    "q_dp_lis": {
        "problemStatement": (
            "Given an integer array `nums`, return the length of the longest strictly increasing subsequence.\n\n"
            "A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements."
        ),
        "explanations": [
            "The longest increasing subsequence is [2,3,7,101], therefore the length is 4.",
            "The longest increasing subsequence is [0,1,2,3], therefore the length is 4."
        ]
    },
    "q_dp_house_robber": {
        "problemStatement": (
            "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.\n\n"
            "Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police."
        ),
        "explanations": [
            "Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.",
            "Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1). Total amount = 2 + 9 + 1 = 12."
        ]
    },
    "q_dp_knapsack_01": {
        "problemStatement": (
            "Given `N` items, each item has a weight `wt[i]` and a profit/value `val[i]`. You are also given a knapsack with a maximum capacity `W`.\n\n"
            "Determine the maximum value that can be put in the knapsack such that the sum of the weights of the chosen items does not exceed `W`.\n\n"
            "Note that each item can either be picked or not picked (0/1 property). You cannot break items."
        ),
        "explanations": [
            "Pick the second and third items (weights 20 and 30, values 100 and 120). Total weight = 50 <= 50, total value = 220.",
            "Pick the only item with weight 4 and value 10."
        ]
    },
    "q_dp_partition_equal_subset_sum": {
        "problemStatement": (
            "Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal, or `false` otherwise."
        ),
        "explanations": [
            "The array can be partitioned as [1, 5, 5] and [11], both having sum 11.",
            "The total sum is 11, which cannot be divided into two equal integer halves."
        ]
    },
    "q_dp_word_break": {
        "problemStatement": (
            "Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.\n\n"
            "Note that the same word in the dictionary may be reused multiple times in the segmentation."
        ),
        "explanations": [
            "Return true because \"leetcode\" can be segmented as \"leet code\".",
            "Return true because \"applepenapple\" can be segmented as \"apple pen apple\". Note that you are allowed to reuse dictionary words."
        ]
    },
    "q_dp_max_product_subarray": {
        "problemStatement": (
            "Given an integer array `nums`, find a subarray that has the largest product, and return the product.\n\n"
            "The test cases are generated so that the answer will fit in a 32-bit integer.\n\n"
            "A subarray is a contiguous non-empty sequence of elements within an array."
        ),
        "explanations": [
            "[2,3] has the largest product 6.",
            "The result cannot be 2, because [-2,-1] is not a contiguous subarray."
        ]
    },

    # -------------------------------------------------------------------------
    # 9. DP EXPANDED (8 Questions from bank_dp_missing.py)
    # -------------------------------------------------------------------------
    "q_dp_min_cost_climbing_stairs": {
        "problemStatement": (
            "You are given an integer array `cost` where `cost[i]` is the cost of `i-th` step on a staircase. Once you pay the cost, you can either climb one or two steps.\n\n"
            "You can either start from the step with index `0`, or the step with index `1`.\n\n"
            "Return the minimum cost to reach the top of the floor."
        ),
        "explanations": [
            "You will start at index 1. Pay 15 and climb two steps to reach the top. Total cost is 15.",
            "Start at index 0. Pay cost[0] and step to index 2, pay cost[2] and step to index 4, pay cost[4] and step to index 6, pay cost[6] and step to index 7, pay cost[7] and step to index 9, pay cost[9] and step to top. Minimum total cost = 6."
        ]
    },
    "q_dp_fibonacci": {
        "problemStatement": (
            "The Fibonacci numbers, commonly denoted `F(n)` form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is:\n"
            "- `F(0) = 0, F(1) = 1`\n"
            "- `F(n) = F(n - 1) + F(n - 2)`, for `n > 1`.\n\n"
            "Given `n`, calculate `F(n)`."
        ),
        "explanations": [
            "F(2) = F(1) + F(0) = 1 + 0 = 1.",
            "F(3) = F(2) + F(1) = 1 + 1 = 2."
        ]
    },
    "q_dp_house_robber_ii": {
        "problemStatement": (
            "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.\n\n"
            "Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police."
        ),
        "explanations": [
            "You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses in the circle.",
            "Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4."
        ]
    },
    "q_dp_decode_ways": {
        "problemStatement": (
            "A message containing letters from A-Z can be encoded into numbers using the following mapping:\n"
            "'A' -> \"1\", 'B' -> \"2\", ..., 'Z' -> \"26\"\n\n"
            "To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).\n\n"
            "Given a string `s` containing only digits, return the number of ways to decode it."
        ),
        "explanations": [
            "\"12\" could be decoded as \"AB\" (1 2) or \"L\" (12).",
            "\"226\" could be decoded as \"BZ\" (2 26), \"VF\" (22 6), or \"BBF\" (2 2 6)."
        ]
    },
    "q_dp_distinct_subsequences": {
        "problemStatement": (
            "Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.\n\n"
            "The test cases are generated so that the answer fits on a 32-bit signed integer."
        ),
        "explanations": [
            "There are 3 ways to form \"rabbit\" from \"rabbbit\" by omitting one of the three 'b's.",
            "There are 5 ways to form \"bag\" from \"babgbag\"."
        ]
    },
    "q_dp_regex_matching": {
        "problemStatement": (
            "Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:\n"
            "- `'.'` Matches any single character.\n"
            "- `'*'` Matches zero or more of the preceding element.\n\n"
            "The matching should cover the entire input string (not partial)."
        ),
        "explanations": [
            "\"a\" does not match the entire string \"aa\".",
            "'*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes \"aa\"."
        ]
    },
    "q_dp_palindrome_partitioning_ii": {
        "problemStatement": (
            "Given a string `s`, partition `s` such that every substring of the partition is a palindrome.\n\n"
            "Return the minimum cuts needed for a palindrome partitioning of `s`."
        ),
        "explanations": [
            "The palindrome partitioning [\"aa\",\"b\"] could be produced using 1 cut.",
            "The string \"a\" is already a palindrome, so 0 cuts are needed."
        ]
    },
    "q_dp_burst_balloons": {
        "problemStatement": (
            "You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.\n\n"
            "If you burst the `i-th` balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.\n\n"
            "Return the maximum coins you can collect by bursting the balloons wisely."
        ),
        "explanations": [
            "Burst 1 -> 5 -> 3 -> 8. Coins: 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15 + 120 + 24 + 8 = 167.",
            "Burst 1 -> 5. Coins: 1*1*5 + 1*5*1 = 5 + 5 = 10."
        ]
    },

    # -------------------------------------------------------------------------
    # 10. 2D DP / MATRIX DP (6 Questions from bank_2ddp.py)
    # -------------------------------------------------------------------------
    "q_2ddp_unique_paths": {
        "problemStatement": (
            "There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.\n\n"
            "Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.\n\n"
            "The test cases are generated so that the answer will be less than or equal to `2 * 10^9`."
        ),
        "explanations": [
            "There are 28 unique paths from top-left to bottom-right in a 3x7 grid.",
            "From the top-left corner, there are a total of 3 ways to reach the bottom-right corner: 1. Right -> Down -> Down, 2. Down -> Down -> Right, 3. Down -> Right -> Down."
        ]
    },
    "q_2ddp_min_path_sum": {
        "problemStatement": (
            "Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.\n\n"
            "Note: You can only move either down or right at any point in time."
        ),
        "explanations": [
            "Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum to 7.",
            "The path 1 -> 2 -> 3 -> 6 gives minimum sum 12."
        ]
    },
    "q_2ddp_lcs": {
        "problemStatement": (
            "Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.\n\n"
            "A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.\n\n"
            "A common subsequence of two strings is a subsequence that is common to both strings."
        ),
        "explanations": [
            "The longest common subsequence is \"ace\" and its length is 3.",
            "The longest common subsequence is \"abc\" and its length is 3."
        ]
    },
    "q_2ddp_edit_distance": {
        "problemStatement": (
            "Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.\n\n"
            "You have the following three operations permitted on a word:\n"
            "- Insert a character\n"
            "- Delete a character\n"
            "- Replace a character"
        ),
        "explanations": [
            "horse -> rorse (replace 'h' with 'r'), rorse -> rose (remove 'r'), rose -> ros (remove 'e'). Total operations = 3.",
            "intention -> inention (delete 't'), inention -> enention (replace 'i' with 'e'), enention -> exention (replace 'n' with 'x'), exention -> exection (replace 'n' with 'c'), exection -> execution (insert 'u'). Total = 5."
        ]
    },
    "q_2ddp_maximal_square": {
        "problemStatement": (
            "Given an `m x n` binary matrix filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area."
        ),
        "explanations": [
            "The largest square of all 1s has side length 2, so the maximal area is 2 * 2 = 4.",
            "The largest square of all 1s has side length 1, so the area is 1."
        ]
    },
    "q_2ddp_dungeon_game": {
        "problemStatement": (
            "The demons had captured the princess and imprisoned her in the bottom-right corner of a `dungeon`. The dungeon consists of `m x n` rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.\n\n"
            "The knight has an initial health point represented by a positive integer. If at any point his health point drops to `0` or below, he dies immediately.\n\n"
            "Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).\n\n"
            "To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.\n\n"
            "Return the knight's minimum initial health so that he can rescue the princess."
        ),
        "explanations": [
            "The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT -> RIGHT -> DOWN -> DOWN.",
            "The knight needs at least 1 HP to enter a room with value 0."
        ]
    },

    # -------------------------------------------------------------------------
    # 11. 2D DP EXPANDED (8 Questions from bank_2ddp_missing.py)
    # -------------------------------------------------------------------------
    "q_2ddp_unique_paths_ii": {
        "problemStatement": (
            "You are given an `m x n` integer array `obstacleGrid`. There is a robot initially located at the top-left corner (i.e., `obstacleGrid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `obstacleGrid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.\n\n"
            "An obstacle and space are marked as `1` or `0` respectively in `obstacleGrid`. A path that the robot takes cannot include any square that is an obstacle.\n\n"
            "Return the number of possible unique paths that the robot can take to reach the bottom-right corner."
        ),
        "explanations": [
            "There is one obstacle in the middle of the 3x3 grid above. There are two paths to the bottom-right: 1. Right -> Right -> Down -> Down, 2. Down -> Down -> Right -> Right.",
            "There is an obstacle at (0,1), leaving only 1 valid path: Down -> Right."
        ]
    },
    "q_2ddp_range_sum_2d": {
        "problemStatement": (
            "Given a 2D matrix `matrix`, handle multiple queries of the following type:\n\n"
            "Calculate the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.\n\n"
            "Implement the `NumMatrix` class:\n"
            "- `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.\n"
            "- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`."
        ),
        "explanations": [
            "The region sum for rectangle (2,1) to (4,3) adds the elements inside that subgrid to 8.",
            "The region sum for rectangle (1,1) to (2,2) equals 11."
        ]
    },
    "q_2ddp_target_sum": {
        "problemStatement": (
            "You are given an integer array `nums` and an integer `target`.\n\n"
            "You want to build an expression out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.\n\n"
            "For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `\"+2-1\"`.\n\n"
            "Return the number of different expressions that you can build, which evaluates to `target`."
        ),
        "explanations": [
            "There are 5 ways to assign symbols to make the sum of nums be target 3: -1+1+1+1+1 = 3, +1-1+1+1+1 = 3, +1+1-1+1+1 = 3, +1+1+1-1+1 = 3, +1+1+1+1-1 = 3.",
            "Only +1 yields sum 1."
        ]
    },
    "q_2ddp_longest_palindromic_subseq": {
        "problemStatement": (
            "Given a string `s`, find the longest palindromic subsequence's length in `s`.\n\n"
            "A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements."
        ),
        "explanations": [
            "One possible longest palindromic subsequence is \"bbbb\".",
            "One possible longest palindromic subsequence is \"bb\"."
        ]
    },
    "q_2ddp_interleaving_string": {
        "problemStatement": (
            "Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.\n\n"
            "An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:\n"
            "- `s = s_1 + s_2 + ... + s_n`\n"
            "- `t = t_1 + t_2 + ... + t_m`\n"
            "- `|n - m| <= 1`\n"
            "- The interleaving is `s_1 + t_1 + s_2 + t_2 + ...` or `t_1 + s_1 + t_2 + s_2 + ...`"
        ),
        "explanations": [
            "s1 = \"aabcc\", s2 = \"dbbca\", s3 = \"aadbbcbcac\". Split s1 = \"aa\" + \"bc\" + \"c\", s2 = \"dbbc\" + \"a\". Interleaving gives \"aadbbcbcac\".",
            "It is impossible to interleave s1 and s2 to obtain s3 because character counts or relative orderings do not match."
        ]
    },
    "q_2ddp_scramble_string": {
        "problemStatement": (
            "We can scramble a string s to get a string t using the following algorithm:\n"
            "1. If the length of the string is 1, stop.\n"
            "2. If the length of the string is > 1, do the following:\n"
            "   - Split the string into two non-empty substrings at a random index.\n"
            "   - Randomly decide whether to swap the two substrings or to keep them in their original order.\n"
            "   - Apply step 1 recursively on each of the two substrings.\n\n"
            "Given two strings `s1` and `s2` of the same length, return `true` if `s2` is a scrambled string of `s1`, otherwise, return `false`."
        ),
        "explanations": [
            "\"great\" can be split into \"gr\" and \"eat\", then swapped and recursively partitioned to form \"rgeat\".",
            "\"abcde\" cannot be scrambled into \"caebd\" through valid binary splits."
        ]
    },
    "q_2ddp_min_cost_cut_stick": {
        "problemStatement": (
            "Given a wooden stick of length `n` units. The stick is labelled from `0` to `n`.\n\n"
            "Given an integer array `cuts` where `cuts[i]` denotes a position you should perform a cut at.\n\n"
            "You should perform the cuts in order, you can change the order of the cuts as you wish. The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut).\n\n"
            "Return the minimum total cost of the cuts."
        ),
        "explanations": [
            "Cutting at 3 costs 7. Then cutting at 1 costs 3, cutting at 5 costs 4, and cutting at 4 costs 2. Total cost = 7 + 3 + 4 + 2 = 16.",
            "Cutting in order [1, 3, 4, 5] yields a minimal cost of 22."
        ]
    },
    "q_2ddp_stone_game_iii": {
        "problemStatement": (
            "Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array `stoneValue`.\n\n"
            "Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take `1`, `2`, or `3` stones from the first remaining stones in the row.\n\n"
            "The score of each player is the sum of values of the stones taken. The objective of each player is to end with the highest score, and both players play optimally.\n\n"
            "Return `\"Alice\"` if Alice will win, `\"Bob\"` if Bob will win, or `\"Tie\"` if they will end the game with the same score."
        ),
        "explanations": [
            "Bob wins because he can take the remaining piles after Alice's initial choices to achieve a higher score.",
            "Alice can take 3 stones [1,2,3] to secure the win with score 6 vs Bob's -9."
        ]
    },

    # -------------------------------------------------------------------------
    # 12. GRAPHS (10 Questions from bank_graphs.py)
    # -------------------------------------------------------------------------
    "q_graph_number_of_islands": {
        "problemStatement": (
            "Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.\n\n"
            "An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water."
        ),
        "explanations": [
            "All '1's are connected horizontally or vertically into a single island.",
            "There are 3 separate connected components of '1's representing 3 islands."
        ]
    },
    "q_graph_course_schedule": {
        "problemStatement": (
            "There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.\n\n"
            "For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.\n\n"
            "Return `true` if you can finish all courses. Otherwise, return `false`."
        ),
        "explanations": [
            "There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.",
            "To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible due to a cycle."
        ]
    },
    "q_graph_rotting_oranges": {
        "problemStatement": (
            "You are given an `m x n` `grid` where each cell can have one of three values:\n"
            "- `0` representing an empty cell,\n"
            "- `1` representing a fresh orange, or\n"
            "- `2` representing a rotten orange.\n\n"
            "Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.\n\n"
            "Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`."
        ),
        "explanations": [
            "After 4 minutes, all fresh oranges become rotten through adjacent spread.",
            "The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally."
        ]
    },
    "q_graph_network_delay_dijkstra": {
        "problemStatement": (
            "You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u_i, v_i, w_i)`, where `u_i` is the source node, `v_i` is the target node, and `w_i` is the time it takes for a signal to travel from source to target.\n\n"
            "We will send a signal from a given node `k`. Return the minimum time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`."
        ),
        "explanations": [
            "The signal sent from node 2 reaches node 1 in 1 unit of time, node 3 in 1 unit of time, and node 4 in 2 units of time (via node 3). Maximum time = 2.",
            "Node 2 cannot reach node 1 because the edge is directed from 1 to 2."
        ]
    },
    "q_graph_redundant_connection": {
        "problemStatement": (
            "In this problem, a tree is an undirected graph that is connected and has no cycles.\n\n"
            "You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the graph.\n\n"
            "Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input."
        ),
        "explanations": [
            "Removing edge [2,3] leaves a connected tree connecting all nodes 1, 2, and 3.",
            "The edge [1,4] creates a redundant cycle and occurs last in the input."
        ]
    },
    "q_graph_pacific_atlantic": {
        "problemStatement": (
            "There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.\n\n"
            "The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.\n\n"
            "The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.\n\n"
            "Return a 2D list of grid coordinates `result` where `result[i] = [r_i, c_i]` denotes that rain water can flow from cell `(r_i, c_i)` to both the Pacific and Atlantic oceans."
        ),
        "explanations": [
            "Water from cells [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]] can flow to both Pacific (top/left) and Atlantic (bottom/right) oceans.",
            "The only cell in the grid connects to both oceans."
        ]
    },
    "q_graph_word_ladder": {
        "problemStatement": (
            "A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:\n"
            "- Every adjacent pair of words differs by a single letter.\n"
            "- Every `s_i` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.\n"
            "- `s_k == endWord`\n\n"
            "Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists."
        ),
        "explanations": [
            "One shortest transformation sequence is \"hit\" -> \"hot\" -> \"dot\" -> \"dog\" -> \"cog\", which is 5 words long.",
            "The endWord \"cog\" is not in wordList, therefore there is no valid transformation sequence."
        ]
    },
    "q_graph_valid_tree": {
        "problemStatement": (
            "You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [a_i, b_i]` indicates that there is an undirected edge between nodes `a_i` and `b_i` in the graph.\n\n"
            "Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise.\n\n"
            "A valid tree is an undirected graph that is fully connected and contains no cycles."
        ),
        "explanations": [
            "The graph contains 5 nodes and 4 edges with no cycles and connects all nodes, which forms a valid tree.",
            "The edges [1,2], [2,3], [1,3] form a cycle, so the graph is not a tree."
        ]
    },
    "q_graph_is_bipartite": {
        "problemStatement": (
            "There is an undirected graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to.\n\n"
            "A graph is bipartite if the nodes can be partitioned into two independent sets `A` and `B` such that every edge in the graph connects a node in set `A` and a node in set `B`.\n\n"
            "Return `true` if and only if it is bipartite."
        ),
        "explanations": [
            "We can divide the vertices into two groups: {0, 3} and {1, 2}. Every edge connects a vertex from the first group to the second.",
            "We cannot divide the vertices into two independent sets because nodes 0, 1, 2 form an odd-length cycle of 3 edges."
        ]
    },
    "q_graph_min_spanning_tree": {
        "problemStatement": (
            "Given a weighted, undirected, and connected graph of `V` vertices and `E` edges, find the sum of weights of the edges of the Minimum Spanning Tree (MST).\n\n"
            "A minimum spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight."
        ),
        "explanations": [
            "The edges in the MST are (0,1) with weight 5 and (1,2) with weight 10. Total weight = 15.",
            "The MST contains edges with weights 1, 2, and 2, giving total weight 5."
        ]
    },

    # -------------------------------------------------------------------------
    # 13. GRAPHS EXPANDED (10 Questions from bank_graphs_missing.py)
    # -------------------------------------------------------------------------
    "q_graph_center_star": {
        "problemStatement": (
            "There is an undirected star graph consisting of `n` nodes labeled from `1` to `n`. A star graph is a graph where there is one center node and exactly `n - 1` edges that connect the center node with every other node.\n\n"
            "You are given a 2D integer array `edges` where each `edges[i] = [u_i, v_i]` indicates that there is an edge between the nodes `u_i` and `v_i`.\n\n"
            "Return the center of the given star graph."
        ),
        "explanations": [
            "Node 2 is connected to every other node (1, 3, 4), so 2 is the center.",
            "Node 1 is present in every edge, so 1 is the center."
        ]
    },
    "q_graph_path_exists": {
        "problemStatement": (
            "There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (inclusive). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [u_i, v_i]` denotes a bi-directional edge between vertex `u_i` and vertex `v_i`. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.\n\n"
            "You want to determine if there is a valid path that exists from vertex `source` to vertex `destination`.\n\n"
            "Given `edges` and the integers `n`, `source`, and `destination`, return `true` if there is a valid path from `source` to `destination`, or `false` otherwise."
        ),
        "explanations": [
            "There are two paths from vertex 0 to vertex 2: 0 -> 1 -> 2, and 0 -> 2.",
            "There is no path from vertex 0 to vertex 5."
        ]
    },
    "q_graph_number_of_provinces": {
        "problemStatement": (
            "There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.\n\n"
            "A province is a group of directly or indirectly connected cities and no other cities outside of the group.\n\n"
            "You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i-th` city and the `j-th` city are directly connected, and `isConnected[i][j] = 0` otherwise.\n\n"
            "Return the total number of provinces."
        ),
        "explanations": [
            "Cities 0 and 1 are connected, and city 2 is separate, forming 2 provinces.",
            "No cities are connected to each other, forming 3 separate provinces."
        ]
    },
    "q_graph_flood_fill": {
        "problemStatement": (
            "An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image.\n\n"
            "You are also given three integers `sr`, `sc`, and `color`. You should perform a flood fill on the image starting from the pixel `image[sr][sc]`.\n\n"
            "To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `color`.\n\n"
            "Return the modified image after performing the flood fill."
        ),
        "explanations": [
            "From the center of the image at coordinate (1, 1), all connected pixels with the same color are colored with 2.",
            "The starting pixel is already of color 2 and has no neighboring pixels of the same old color, so no changes are made."
        ]
    },
    "q_graph_find_town_judge": {
        "problemStatement": (
            "In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.\n\n"
            "If the town judge exists, then:\n"
            "1. The town judge trusts nobody.\n"
            "2. Everybody (except for the town judge) trusts the town judge.\n"
            "3. There is exactly one person that satisfies properties 1 and 2.\n\n"
            "You are given an array `trust` where `trust[i] = [a_i, b_i]` representing that the person labeled `a_i` trusts the person labeled `b_i`.\n\n"
            "Return the label of the town judge if the town judge exists and can be identified, or return `-1` otherwise."
        ),
        "explanations": [
            "Person 1 trusts person 2, and person 2 trusts nobody. Person 2 is trusted by n-1 people.",
            "Person 1 and 2 trust person 3, and person 3 trusts nobody. Person 3 is the judge."
        ]
    },
    "q_graph_clone_graph": {
        "problemStatement": (
            "Given a reference of a node in a connected undirected graph.\n\n"
            "Return a deep copy (clone) of the graph.\n\n"
            "Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors."
        ),
        "explanations": [
            "The cloned graph has 4 nodes with identical values and adjacency topology as the original graph.",
            "A single isolated node is cloned with the same value 1 and empty neighbor list."
        ]
    },
    "q_graph_course_schedule_ii": {
        "problemStatement": (
            "There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must take course `b_i` first if you want to take course `a_i`.\n\n"
            "For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.\n\n"
            "Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array."
        ),
        "explanations": [
            "There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].",
            "Both [0,1,2,3] and [0,2,1,3] are valid topological orderings."
        ]
    },
    "q_graph_cheapest_flights_k_stops": {
        "problemStatement": (
            "There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.\n\n"
            "You are also given three integers `src`, `dst`, and `k`, return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`."
        ),
        "explanations": [
            "The optimal path with at most 1 stop from city 0 to 3 is 0 -> 1 -> 3 with cost 100 + 600 = 700.",
            "The direct path 0 -> 2 has price 500, but taking 0 -> 1 -> 2 has price 100 + 100 = 200 with at most 1 stop."
        ]
    },
    "q_graph_alien_dictionary": {
        "problemStatement": (
            "There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.\n\n"
            "You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are sorted lexicographically by the rules of this new language.\n\n"
            "Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return `\"\"`. If there are multiple solutions, return any of them."
        ),
        "explanations": [
            "From \"wrt\" and \"wrf\", 't' < 'f'. From \"wrt\" and \"er\", 'w' < 'e'. From \"er\" and \"ett\", 'r' < 't'. From \"ett\" and \"rftt\", 'e' < 'r'. The order is \"wertf\".",
            "From \"z\" and \"x\", 'z' < 'x'. The order is \"zx\"."
        ]
    },
    "q_graph_critical_connections": {
        "problemStatement": (
            "There are `n` servers numbered from `0` to `n - 1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a_i, b_i]` represents a connection between servers `a_i` and `b_i`. Any server can reach other servers directly or indirectly through the network.\n\n"
            "A critical connection is a connection that, if removed, will make some servers unable to reach some other server.\n\n"
            "Return all critical connections in the network in any order."
        ),
        "explanations": [
            "Removing connection [1,3] disconnects server 3 from the rest of the network, making it a critical bridge connection.",
            "Removing [0,1] disconnects server 0 and server 1."
        ]
    },

    # -------------------------------------------------------------------------
    # 14. ADVANCED DSA (8 Questions from bank_advanced.py)
    # -------------------------------------------------------------------------
    "q_list_reverse_linked_list": {
        "problemStatement": (
            "Given the `head` of a singly linked list, reverse the list, and return the reversed list."
        ),
        "explanations": [
            "The linked list 1 -> 2 -> 3 -> 4 -> 5 is reversed to 5 -> 4 -> 3 -> 2 -> 1.",
            "The list 1 -> 2 is reversed to 2 -> 1."
        ]
    },
    "q_list_merge_two_sorted_lists": {
        "problemStatement": (
            "You are given the heads of two sorted linked lists `list1` and `list2`.\n\n"
            "Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.\n\n"
            "Return the head of the merged linked list."
        ),
        "explanations": [
            "The merged list combines [1,2,4] and [1,3,4] into [1,1,2,3,4,4].",
            "Merging two empty lists results in an empty list."
        ]
    },
    "q_stack_daily_temperatures": {
        "problemStatement": (
            "Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature.\n\n"
            "If there is no future day for which this is possible, keep `answer[i] == 0` instead."
        ),
        "explanations": [
            "For day 0 (73), day 1 (74) is warmer (1 day wait). For day 2 (75), day 6 (76) is warmer (4 days wait).",
            "Day 0 (30) waits 1 day for 40, day 1 (40) waits 1 day for 50, day 2 (50) has no warmer day (0)."
        ]
    },
    "q_bs_search_rotated_array": {
        "problemStatement": (
            "There is an integer array `nums` sorted in ascending order (with distinct values).\n\n"
            "Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed).\n\n"
            "Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.\n\n"
            "You must write an algorithm with O(log n) runtime complexity."
        ),
        "explanations": [
            "Target 0 is found at index 4 in the rotated array [4,5,6,7,0,1,2].",
            "Target 3 is not present in nums, so -1 is returned."
        ]
    },
    "q_bs_find_min_rotated_array": {
        "problemStatement": (
            "Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times.\n\n"
            "Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.\n\n"
            "You must write an algorithm that runs in O(log n) time."
        ),
        "explanations": [
            "The original array was [1,2,3,4,5] rotated 3 times. The minimum value is 1.",
            "The minimum element in [4,5,6,7,0,1,2] is 0."
        ]
    },
    "q_heap_kth_largest_element": {
        "problemStatement": (
            "Given an integer array `nums` and an integer `k`, return the `k-th` largest element in the array.\n\n"
            "Note that it is the `k-th` largest element in the sorted order, not the `k-th` distinct element.\n\n"
            "Can you solve it without sorting?"
        ),
        "explanations": [
            "The sorted array in descending order is [6, 5, 4, 3, 2, 1]. The 2nd largest element is 5.",
            "The 4th largest element in [3,2,3,1,2,4,5,5,6] is 4."
        ]
    },
    "q_stack_min_stack": {
        "problemStatement": (
            "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.\n\n"
            "Implement the `MinStack` class:\n"
            "- `MinStack()` initializes the stack object.\n"
            "- `void push(int val)` pushes the element `val` onto the stack.\n"
            "- `void pop()` removes the element on the top of the stack.\n"
            "- `int top()` gets the top element of the stack.\n"
            "- `int getMin()` retrieves the minimum element in the stack.\n\n"
            "You must implement a solution with `O(1)` time complexity for each function."
        ),
        "explanations": [
            "MinStack operations return -3 for getMin(), 0 for top(), and -2 for getMin() after popping 0.",
            "The stack maintains minimum element tracking in constant time."
        ]
    },
    "q_bs_median_two_sorted_arrays": {
        "problemStatement": (
            "Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.\n\n"
            "The overall run time complexity should be O(log (m+n))."
        ),
        "explanations": [
            "merged array = [1,2,3] and median is 2.00000.",
            "merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.50000."
        ]
    }
}

def to_py(val, indent=0):
    ind = ' ' * indent
    if isinstance(val, dict):
        if not val:
            return '{}'
        lines = ['{\n']
        for k, v in val.items():
            lines.append(f'{ind}    {json.dumps(k)}: {to_py(v, indent + 4)},\n')
        lines.append(f'{ind}}}')
        return ''.join(lines)
    elif isinstance(val, list):
        if not val:
            return '[]'
        lines = ['[\n']
        for item in val:
            lines.append(f'{ind}    {to_py(item, indent + 4)},\n')
        lines.append(f'{ind}]')
        return ''.join(lines)
    elif val is True:
        return 'True'
    elif val is False:
        return 'False'
    elif val is None:
        return 'None'
    elif isinstance(val, (int, float)):
        return str(val)
    elif isinstance(val, str):
        return json.dumps(val, ensure_ascii=False)
    else:
        return repr(val)

MODULES = [
    ("bank_arrays.py", "ARRAY_QUESTIONS", "# Array Debugging Problems (10 Questions: C, C++, Java)\n\n"),
    ("bank_strings.py", "STRING_QUESTIONS", "# String Debugging Problems (8 Questions: C, C++, Java)\n\n"),
    ("bank_hashmap.py", "HASHMAP_QUESTIONS", "# HashMap & HashSet Debugging Problems (6 Questions: C, C++, Java)\n\n"),
    ("bank_trees.py", "TREE_QUESTIONS", "# Trees & BST Debugging Problems (10 Questions: C, C++, Java)\n\n"),
    ("bank_trees_missing.py", "MISSING_TREE_QUESTIONS", "# Additional Binary Tree Questions (9 Questions)\n\n"),
    ("bank_bst_missing.py", "MISSING_BST_QUESTIONS", "# Additional BST Questions (13 Questions)\n\n"),
    ("bank_recursion.py", "RECURSION_QUESTIONS", "# Recursion & Backtracking Debugging Problems (6 Questions: C, C++, Java)\n\n"),
    ("bank_dp.py", "DP_QUESTIONS", "# Dynamic Programming 1D Debugging Problems (8 Questions: C, C++, Java)\n\n"),
    ("bank_dp_missing.py", "MISSING_DP_QUESTIONS", "# Missing 1D DP Questions (8 Questions)\n\n"),
    ("bank_2ddp.py", "DP2D_QUESTIONS", "# 2D Dynamic Programming & Matrix DP Problems (6 Questions: C, C++, Java)\n\n"),
    ("bank_2ddp_missing.py", "MISSING_2DDP_QUESTIONS", "# Missing 2D DP Questions (8 Questions)\n\n"),
    ("bank_graphs.py", "GRAPH_QUESTIONS", "# Graph Debugging Problems (10 Questions: C, C++, Java)\n\n"),
    ("bank_graphs_missing.py", "MISSING_GRAPH_QUESTIONS", "# Missing Graph Questions (10 Questions)\n\n"),
    ("bank_advanced.py", "ADVANCED_QUESTIONS", "# Advanced DSA Problems (8 Questions: C, C++, Java)\n\n"),
]

def apply_updates():
    data_dir = os.path.dirname(__file__)
    total_updated = 0

    for filename, var_name, header in MODULES:
        filepath = os.path.join(data_dir, filename)
        module_name = filename.replace('.py', '')
        
        # Import dynamically
        mod = __import__(module_name)
        q_list = getattr(mod, var_name)
        
        for q in q_list:
            qid = q["id"]
            if qid not in UPDATES:
                raise ValueError(f"Missing update for question ID: {qid}")
            
            # Apply LeetCode problemStatement
            q["problemStatement"] = UPDATES[qid]["problemStatement"]
            
            # Apply visible test case explanations
            explanations = UPDATES[qid].get("explanations", [])
            for idx, tc in enumerate(q.get("visibleTestCases", [])):
                if idx < len(explanations):
                    tc["explanation"] = explanations[idx]
            
            total_updated += 1

        # Format and save
        py_code = header + f"{var_name} = " + to_py(q_list) + "\n"
        
        # Validate AST before writing
        ast.parse(py_code)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(py_code)
        print(f"Successfully updated {len(q_list)} questions in {filename}")

    print(f"\n==================================================")
    print(f"TOTAL QUESTIONS UPDATED: {total_updated}")
    print(f"==================================================")

if __name__ == "__main__":
    apply_updates()
