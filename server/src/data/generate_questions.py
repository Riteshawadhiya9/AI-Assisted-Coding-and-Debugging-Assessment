import json
import os

questions = [
  # 1. ARRAYS - Easy - C
  {
    "id": "q_arr_max",
    "title": "Find Maximum in Array",
    "problemStatement": "Find the maximum element in an array of integers. Complete the function `findMax` which returns the largest integer.",
    "language": "c",
    "topic": "arrays",
    "subtopic": "array-max",
    "difficulty": "easy",
    "buggyCode": "int findMax(int* arr, int n) {\n    int max = 0;\n    for (int i = 0; i < n; i++) {\n        if (arr[i] > max) {\n            max = arr[i];\n        }\n    }\n    return max;\n}",
    "correctCode": "int findMax(int* arr, int n) {\n    if (n <= 0) return 0;\n    int max = arr[0];\n    for (int i = 1; i < n; i++) {\n        if (arr[i] > max) {\n            max = arr[i];\n        }\n    }\n    return max;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Initializes maximum tracking value to 0 instead of the first array element, failing for all-negative inputs.",
        "type": "incorrect initialization",
        "lineRange": "3"
      }
    ],
    "primaryBugType": "incorrect initialization",
    "explanation": "If the input array contains only negative numbers (e.g. [-5, -10, -2]), the buggy function returns 0 because 0 is larger than all elements. The correct approach is initializing the max tracker to the first element (arr[0]).",
    "intendedApproach": "Initialize the max variable to the first element of the array rather than zero.",
    "constraints": ["1 <= n <= 10^5", "-10^9 <= arr[i] <= 10^9"],
    "visibleTestCases": [
      { "id": 1, "input": "3\n-5 -10 -2", "expectedOutput": "-2", "isHidden": False },
      { "id": 2, "input": "4\n1 5 3 2", "expectedOutput": "5", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "1\n-100", "expectedOutput": "-100", "isHidden": True },
      { "id": 4, "input": "5\n-1 -2 -3 -4 -5", "expectedOutput": "-1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["arrays", "searching", "c", "easy"]
  },

  # 2. ARRAYS - Medium - C++
  {
    "id": "q_arr_rotate",
    "title": "Rotate Array by K Positions",
    "problemStatement": "Given an array of size `n`, rotate the array to the right by `k` steps, where `k` is non-negative.",
    "language": "cpp",
    "topic": "arrays",
    "subtopic": "array-rotation",
    "difficulty": "medium",
    "buggyCode": "#include <vector>\nusing namespace std;\n\nvoid reverse(vector<int>& nums, int start, int end) {\n    while (start <= end) {\n        int temp = nums[start];\n        nums[start] = nums[end];\n        nums[end] = temp;\n        start++;\n        end--;\n    }\n}\n\nvoid rotate(vector<int>& nums, int k) {\n    int n = nums.size();\n    k = k % n;\n    reverse(nums, 0, n - 1);\n    reverse(nums, 0, k - 1);\n    reverse(nums, k, n - 1);\n}",
    "correctCode": "#include <vector>\nusing namespace std;\n\nvoid reverse(vector<int>& nums, int start, int end) {\n    while (start < end) {\n        int temp = nums[start];\n        nums[start] = nums[end];\n        nums[end] = temp;\n        start++;\n        end--;\n    }\n}\n\nvoid rotate(vector<int>& nums, int k) {\n    int n = nums.size();\n    if (n <= 1) return;\n    k = k % n;\n    if (k == 0) return;\n    reverse(nums, 0, n - 1);\n    reverse(nums, 0, k - 1);\n    reverse(nums, k, n - 1);\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Reverse function loop condition uses start <= end instead of start < end, causing redundant swaps on the middle element.",
        "type": "off-by-one",
        "lineRange": "6"
      },
      {
        "id": 2,
        "description": "Doesn't handle empty array or single-element array constraints, resulting in out of bounds when index goes negative.",
        "type": "edge cases",
        "lineRange": "16-23"
      }
    ],
    "primaryBugType": "edge cases",
    "explanation": "If the array contains 1 element and k=0, the helper reverse(nums, 0, k - 1) will call reverse(nums, 0, -1). Since start (0) is larger than end (-1), the reverse loop condition fails immediately but triggers invalid memory access or undefined behavior on indices in certain languages, or skips crucial validation logic. Adding base constraints and using start < end for reversal is correct.",
    "intendedApproach": "Add check for empty arrays/single elements and only swap when pointers haven't crossed.",
    "constraints": ["1 <= nums.length <= 10^5", "0 <= k <= 10^5"],
    "visibleTestCases": [
      { "id": 1, "input": "1 2 3 4 5\n2", "expectedOutput": "4 5 1 2 3", "isHidden": False },
      { "id": 2, "input": "1 2\n3", "expectedOutput": "2 1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "1\n0", "expectedOutput": "1", "isHidden": True },
      { "id": 4, "input": "1 2 3\n0", "expectedOutput": "1 2 3", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["arrays", "two-pointers", "cpp", "medium"]
  },

  # 3. STRINGS - Easy - Java
  {
    "id": "q_str_rev",
    "title": "Reverse String In-Place",
    "problemStatement": "Reverse an array of characters in-place. Complete the method `reverseString`.",
    "language": "java",
    "topic": "strings",
    "subtopic": "string-reversal",
    "difficulty": "easy",
    "buggyCode": "class Solution {\n    public void reverseString(char[] s) {\n        for (int i = 0; i < s.length; i++) {\n            char temp = s[i];\n            s[i] = s[s.length - 1 - i];\n            s[s.length - 1 - i] = temp;\n        }\n    }\n}",
    "correctCode": "class Solution {\n    public void reverseString(char[] s) {\n        for (int i = 0; i < s.length / 2; i++) {\n            char temp = s[i];\n            s[i] = s[s.length - 1 - i];\n            s[s.length - 1 - i] = temp;\n        }\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Loop iterates over entire string length rather than stopping at the middle, resulting in swapping elements back to their original position.",
        "type": "wrong loop condition",
        "lineRange": "4"
      }
    ],
    "primaryBugType": "wrong loop condition",
    "explanation": "If we iterate from i = 0 to length - 1, we swap each character twice. For instance, in 'ab', we swap 'a' and 'b' (getting 'ba'), then on the next iteration we swap 'b' and 'a' back (getting 'ab'). The loop must terminate at s.length / 2.",
    "intendedApproach": "Change the loop limit to half the length of the string: s.length / 2.",
    "constraints": ["1 <= s.length <= 10^5"],
    "visibleTestCases": [
      { "id": 1, "input": "h e l l o", "expectedOutput": "o l l e h", "isHidden": False },
      { "id": 2, "input": "H a n n a h", "expectedOutput": "h a n n a H", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "a", "expectedOutput": "a", "isHidden": True },
      { "id": 4, "input": "a b", "expectedOutput": "b a", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["strings", "two-pointers", "java", "easy"]
  },

  # 4. STRINGS - Medium - C++
  {
    "id": "q_str_pal",
    "title": "Valid Palindrome with Alphanumeric Filtering",
    "problemStatement": "A phrase is a palindrome if, after converting all uppercase letters into lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.",
    "language": "cpp",
    "topic": "strings",
    "subtopic": "palindrome",
    "difficulty": "medium",
    "buggyCode": "#include <string>\n#include <cctype>\nusing namespace std;\n\nbool isPalindrome(string s) {\n    int l = 0, r = s.length() - 1;\n    while (l < r) {\n        while (!isalnum(s[l])) l++;\n        while (!isalnum(s[r])) r--;\n        if (tolower(s[l]) != tolower(s[r])) {\n            return false;\n        }\n        l++;\n        r--;\n    }\n    return true;\n}",
    "correctCode": "#include <string>\n#include <cctype>\nusing namespace std;\n\nbool isPalindrome(string s) {\n    int l = 0, r = s.length() - 1;\n    while (l < r) {\n        while (l < r && !isalnum(s[l])) l++;\n        while (l < r && !isalnum(s[r])) r--;\n        if (tolower(s[l]) != tolower(s[r])) {\n            return false;\n        }\n        l++;\n        r--;\n    }\n    return true;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Inner loops check alphanumeric conditions without a boundary check on pointers, leading to index out of bounds.",
        "type": "off-by-one",
        "lineRange": "9-10"
      }
    ],
    "primaryBugType": "off-by-one",
    "explanation": "If the string contains only spaces or non-alphanumeric characters (like '!!!'), pointer 'l' will increment past 's.length() - 1' indefinitely, accessing unallocated memory. Pointers must be bounded: 'l < r' inside the inner helper loops.",
    "intendedApproach": "Add bounds check (l < r) inside alphanumeric loops.",
    "constraints": ["1 <= s.length <= 10^5", "s consists only of printable ASCII characters"],
    "visibleTestCases": [
      { "id": 1, "input": "A man, a plan, a canal: Panama", "expectedOutput": "1", "isHidden": False },
      { "id": 2, "input": "race a car", "expectedOutput": "0", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "   ", "expectedOutput": "1", "isHidden": True },
      { "id": 4, "input": ".,", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["strings", "two-pointers", "cpp", "medium"]
  },

  # 5. LINKED LIST - Easy - C
  {
    "id": "q_list_mid",
    "title": "Middle of a Singly Linked List",
    "problemStatement": "Given the head of a singly linked list, return the middle node. If there are two middle nodes, return the second middle node.",
    "language": "c",
    "topic": "linked-list",
    "subtopic": "linked-list-middle",
    "difficulty": "easy",
    "buggyCode": "#include <stdlib.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* middleNode(struct ListNode* head) {\n    struct ListNode* slow = head;\n    struct ListNode* fast = head;\n    \n    // Will dereference NULL if list length is even (fast->next->next)\n    while (fast->next != NULL && fast->next->next != NULL) {\n        slow = slow->next;\n        fast = fast->next->next;\n      }\n    \n    return slow;\n}",
    "correctCode": "#include <stdlib.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* middleNode(struct ListNode* head) {\n    struct ListNode* slow = head;\n    struct ListNode* fast = head;\n    \n    while (fast != NULL && fast->next != NULL) {\n        slow = slow->next;\n        fast = fast->next->next;\n    }\n    return slow;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to check if fast is null in the loop header, causing null pointer dereferences on even-length lists.",
        "type": "wrong pointer movement",
        "lineRange": "14"
      }
    ],
    "primaryBugType": "wrong pointer movement",
    "explanation": "If list length is even (e.g. 1 -> 2), initially fast=1. Loop checks fast->next != NULL (2 != NULL) and fast->next->next != NULL (NULL != NULL, which is false). Loop exits and returns 1. But for even list lengths, the second middle (2) is expected. Adjusting loop check to fast != NULL && fast->next != NULL resolves both errors.",
    "intendedApproach": "Change loop check condition to 'fast != NULL && fast->next != NULL'.",
    "constraints": ["The number of nodes in the list is in the range [1, 100]", "1 <= Node.val <= 100"],
    "visibleTestCases": [
      { "id": 1, "input": "1 2 3 4 5", "expectedOutput": "3", "isHidden": False },
      { "id": 2, "input": "1 2 3 4 5 6", "expectedOutput": "4", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "1", "expectedOutput": "1", "isHidden": True },
      { "id": 4, "input": "1 2", "expectedOutput": "2", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["linked-list", "two-pointers", "c", "easy"]
  },

  # 6. LINKED LIST - Medium - Java
  {
    "id": "q_list_rev",
    "title": "Reverse Singly Linked List",
    "problemStatement": "Reverse a singly linked list. Return the new head node.",
    "language": "java",
    "topic": "linked-list",
    "subtopic": "reverse-list",
    "difficulty": "medium",
    "buggyCode": "class ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\nclass Solution {\n    public ListNode reverseList(ListNode head) {\n        ListNode prev = null;\n        ListNode curr = head;\n        while (curr != null) {\n            curr.next = prev;\n            prev = curr;\n            curr = curr.next; \n        }\n        return prev;\n    }\n}",
    "correctCode": "class ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\nclass Solution {\n    public ListNode reverseList(ListNode head) {\n        ListNode prev = null;\n        ListNode curr = head;\n        while (curr != null) {\n            ListNode nextTemp = curr.next;\n            curr.next = prev;\n            prev = curr;\n            curr = nextTemp; \n        }\n        return prev;\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Modifies curr.next before storing it, causing current to iterate backwards and loop infinitely.",
        "type": "incorrect linked-list pointer update",
        "lineRange": "13-15"
      }
    ],
    "primaryBugType": "incorrect linked-list pointer update",
    "explanation": "On line 13, curr.next is set to prev. Then on line 14, prev is set to curr. On line 15, curr = curr.next. But curr.next was already overwritten with prev, which means curr goes backward to the previous node instead of forward. We must cache curr.next in a temporary variable before modifying it.",
    "intendedApproach": "Store curr.next in a temporary variable 'nextTemp' before modifying curr.next.",
    "constraints": ["The number of nodes in the list is in the range [0, 5000]", "-5000 <= Node.val <= 5000"],
    "visibleTestCases": [
      { "id": 1, "input": "1 2 3 4 5", "expectedOutput": "5 4 3 2 1", "isHidden": False },
      { "id": 2, "input": "1 2", "expectedOutput": "2 1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "", "expectedOutput": "", "isHidden": True },
      { "id": 4, "input": "1", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["linked-list", "two-pointers", "java", "medium"]
  },

  # 7. STACK - Easy - C++
  {
    "id": "q_stack_paren",
    "title": "Valid Parentheses Checker",
    "problemStatement": "Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
    "language": "cpp",
    "topic": "stack",
    "subtopic": "stack-usage",
    "difficulty": "easy",
    "buggyCode": "#include <string>\n#include <stack>\nusing namespace std;\n\nbool isValid(string s) {\n    stack<char> st;\n    for (char c : s) {\n        if (c == '(' || c == '{' || c == '[') {\n            st.push(c);\n        } else {\n            // Causes runtime crash / Segmentation fault on closing brace first strings\n            char top = st.top();\n            st.pop();\n            if ((c == ')' && top != '(') ||\n                (c == '}' && top != '{') ||\n                (c == ']' && top != '[')) {\n                return false;\n            }\n        }\n    }\n    return st.empty();\n}",
    "correctCode": "#include <string>\n#include <stack>\nusing namespace std;\n\nbool isValid(string s) {\n    stack<char> st;\n    for (char c : s) {\n        if (c == '(' || c == '{' || c == '[') {\n            st.push(c);\n        } else {\n            if (st.empty()) return false;\n            char top = st.top();\n            st.pop();\n            if ((c == ')' && top != '(') ||\n                (c == '}' && top != '{') ||\n                (c == ']' && top != '[')) {\n                return false;\n            }\n        }\n    }\n    return st.empty();\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to verify if the stack is empty before retrieving top element, causing a segmentation fault on invalid strings starting with closing braces.",
        "type": "stack/queue misuse",
        "lineRange": "13"
      }
    ],
    "primaryBugType": "stack/queue misuse",
    "explanation": "If input is ']', the code hits the else condition. It attempts to read st.top(), but since the stack is empty, it causes undefined behavior or runtime crash. Checking st.empty() first is necessary.",
    "intendedApproach": "Return false if a closing brace is encountered while the stack is empty.",
    "constraints": ["1 <= s.length <= 10^4", "s consists of parentheses only '()[]{}'"],
    "visibleTestCases": [
      { "id": 1, "input": "()", "expectedOutput": "1", "isHidden": False },
      { "id": 2, "input": "()[]{}", "expectedOutput": "1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "]", "expectedOutput": "0", "isHidden": True },
      { "id": 4, "input": "([)]", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(n)" },
    "tags": ["stack", "strings", "cpp", "easy"]
  },

  # 8. STACK - Medium - Java
  {
    "id": "q_stack_min",
    "title": "Design a Min Stack",
    "problemStatement": "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Complete the methods in `MinStack`.",
    "language": "java",
    "topic": "stack",
    "subtopic": "stack-design",
    "difficulty": "medium",
    "buggyCode": "import java.util.Stack;\n\nclass MinStack {\n    private Stack<Integer> stack = new Stack<>();\n    private Stack<Integer> minStack = new Stack<>();\n\n    public void push(int val) {\n        stack.push(val);\n        // Fails when duplicate min values are pushed and then popped once.\n        if (minStack.isEmpty() || val < minStack.peek()) {\n            minStack.push(val);\n        }\n    }\n\n    public void pop() {\n        int val = stack.pop();\n        if (val == minStack.peek()) {\n            minStack.pop();\n        }\n    }\n\n    public int top() {\n        return stack.peek();\n    }\n\n    public int getMin() {\n        return minStack.peek();\n    }\n}",
    "correctCode": "import java.util.Stack;\n\nclass MinStack {\n    private Stack<Integer> stack = new Stack<>();\n    private Stack<Integer> minStack = new Stack<>();\n\n    public void push(int val) {\n        stack.push(val);\n        if (minStack.isEmpty() || val <= minStack.peek()) {\n            minStack.push(val);\n        }\n    }\n\n    public void pop() {\n        // Use equals to avoid wrapper caches or autounboxing issues, or do direct unboxing comparison\n        if (stack.peek().equals(minStack.peek())) {\n            minStack.pop();\n        }\n        stack.pop();\n    }\n\n    public int top() {\n        return stack.peek();\n    }\n\n    public int getMin() {\n        return minStack.peek();\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Min stack only pushes on strictly less condition, causing values to get out-of-sync when duplicate minimum values are popped.",
        "type": "stack/queue misuse",
        "lineRange": "10-12"
      }
    ],
    "primaryBugType": "stack/queue misuse",
    "explanation": "If we push 2, then push 2, our main stack contains [2, 2], but minStack contains [2]. When we pop once, the main stack is [2]. Since the popped element equals minStack.peek(), we pop minStack as well, leaving minStack empty! Subsequent calls to getMin() will fail. Changing check to val <= minStack.peek() preserves duplicates correctly.",
    "intendedApproach": "Change comparison in push to use '<=' (less than or equal) instead of strictly '<'.",
    "constraints": ["-2^31 <= val <= 2^31 - 1", "Methods pop, top and getMin will always be called on non-empty stacks"],
    "visibleTestCases": [
      { "id": 1, "input": "push(-2) push(0) push(-3) getMin() pop() top() getMin()", "expectedOutput": "-3 -3 0 -2", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "push(2) push(2) getMin() pop() getMin()", "expectedOutput": "2 2", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(1)", "space": "O(n)" },
    "tags": ["stack", "design", "java", "medium"]
  },

  # 9. QUEUE - Easy - C
  {
    "id": "q_queue_arr",
    "title": "Circular Queue Array Implementation",
    "problemStatement": "Implement a circular queue using a fixed-size array. Complete the functions `enqueue` and `dequeue`.",
    "language": "c",
    "topic": "queue",
    "subtopic": "circular-queue",
    "difficulty": "easy",
    "buggyCode": "#include <stdbool.h>\n\n#define SIZE 5\n\nint items[SIZE];\nint front = -1;\nint rear = -1;\n\nbool isFull() {\n    return (front == (rear + 1) % SIZE);\n}\n\nbool isEmpty() {\n    return (front == -1);\n}\n\nvoid enqueue(int element) {\n    if (isFull()) return;\n    if (front == -1) front = 0;\n    rear = rear + 1;\n    items[rear] = element;\n}\n\nint dequeue() {\n    if (isEmpty()) return -1;\n    int element = items[front];\n    if (front == rear) {\n        front = -1;\n        rear = -1;\n    } else {\n        front = (front + 1) % SIZE;\n    }\n    return element;\n}",
    "correctCode": "#include <stdbool.h>\n\n#define SIZE 5\n\nint items[SIZE];\nint front = -1;\nint rear = -1;\n\nbool isFull() {\n    return ((rear + 1) % SIZE == front);\n}\n\nbool isEmpty() {\n    return (front == -1);\n}\n\nvoid enqueue(int element) {\n    if (isFull()) return;\n    if (front == -1) front = 0;\n    rear = (rear + 1) % SIZE;\n    items[rear] = element;\n}\n\nint dequeue() {\n    if (isEmpty()) return -1;\n    int element = items[front];\n    if (front == rear) {\n        front = -1;\n        rear = -1;\n    } else {\n        front = (front + 1) % SIZE;\n    }\n    return element;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Increments rear index directly (rear = rear + 1) without wrapping around the circular array size modulo.",
        "type": "off-by-one",
        "lineRange": "20"
      }
    ],
    "primaryBugType": "off-by-one",
    "explanation": "In a circular queue of capacity SIZE, the rear pointer must wrap back to index 0 when it exceeds size boundaries (rear = (rear + 1) % SIZE). Directly adding 1 causes index out of bounds when size reaches capacity, violating circular behavior.",
    "intendedApproach": "Change enqueue increment to rear = (rear + 1) % SIZE.",
    "constraints": ["SIZE = 5", "Elements are non-negative integers"],
    "visibleTestCases": [
      { "id": 1, "input": "enqueue(10) enqueue(20) dequeue() enqueue(30) enqueue(40) enqueue(50) enqueue(60)", "expectedOutput": "10", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "enqueue(1) enqueue(2) enqueue(3) enqueue(4) enqueue(5) dequeue() enqueue(6)", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(1)", "space": "O(1)" },
    "tags": ["queue", "arrays", "c", "easy"]
  },

  # 10. QUEUE - Medium - C++
  {
    "id": "q_queue_stack",
    "title": "Queue Implementation using Stacks",
    "problemStatement": "Implement a first-in-first-out (FIFO) queue using only two stacks. The implemented queue should support `push`, `pop`, `peek`, and `empty`.",
    "language": "cpp",
    "topic": "queue",
    "subtopic": "queue-by-stacks",
    "difficulty": "medium",
    "buggyCode": "#include <stack>\nusing namespace std;\n\nclass MyQueue {\nprivate:\n    stack<int> s1;\n    stack<int> s2;\n\npublic:\n    void push(int x) {\n        s1.push(x);\n    }\n    \n    int pop() {\n        // Doing it on every pop resets order and scrambles queue outputs.\n        while (!s1.empty()) {\n            s2.push(s1.top());\n            s1.pop();\n        }\n        int val = s2.top();\n        s2.pop();\n        return val;\n    }\n    \n    int peek() {\n        if (s2.empty()) {\n            while (!s1.empty()) {\n                s2.push(s1.top());\n                s1.pop();\n            }\n        }\n        return s2.top();\n    }\n    \n    bool empty() {\n        return s1.empty() && s2.empty();\n    }\n};",
    "correctCode": "#include <stack>\nusing namespace std;\n\nclass MyQueue {\nprivate:\n    stack<int> s1;\n    stack<int> s2;\n\npublic:\n    void push(int x) {\n        s1.push(x);\n    }\n    \n    int pop() {\n        if (s2.empty()) {\n            while (!s1.empty()) {\n                s2.push(s1.top());\n                s1.pop();\n            }\n        }\n        int val = s2.top();\n        s2.pop();\n        return val;\n    }\n    \n    int peek() {\n        if (s2.empty()) {\n            while (!s1.empty()) {\n                s2.push(s1.top());\n                s1.pop();\n            }\n        }\n        return s2.top();\n    }\n    \n    bool empty() {\n        return s1.empty() && s2.empty();\n    }\n};",
    "bugList": [
      {
        "id": 1,
        "description": "Pop method transfers stack elements from s1 to s2 unconditionally, which ruins the ordering of elements pushed after the first transfer.",
        "type": "stack/queue misuse",
        "lineRange": "16-20"
      }
    ],
    "primaryBugType": "stack/queue misuse",
    "explanation": "If we push(1), push(2). Pop() is called, s1 elements are dumped to s2, getting [2, 1] on s2 (top is 1). Then we push(3). If we pop() again, s1 is currently [3]. The buggy code dumps s1 to s2, putting 3 on top of 2. We get s2 = [3, 2]. But we wanted to pop 2 first! We should only copy s1 to s2 when s2 is empty.",
    "intendedApproach": "Only dump elements from s1 to s2 inside pop() when s2 is empty.",
    "constraints": ["1 <= x <= 9", "At most 100 calls to push, pop, peek, empty"],
    "visibleTestCases": [
      { "id": 1, "input": "push(1) push(2) peek() pop() empty()", "expectedOutput": "1 1 0", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "push(1) push(2) pop() push(3) pop() pop()", "expectedOutput": "1 2 3", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(1) amortized", "space": "O(n)" },
    "tags": ["queue", "stack", "design", "cpp", "medium"]
  },

  # 11. HASHING - Easy - Java
  {
    "id": "q_hash_twosum",
    "title": "Two Sum Index Finder",
    "problemStatement": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.",
    "language": "java",
    "topic": "hashing",
    "subtopic": "hashmap",
    "difficulty": "easy",
    "buggyCode": "import java.util.HashMap;\n\nclass Solution {\n    public int[] twoSum(int[] nums, int target) {\n        HashMap<Integer, Integer> map = new HashMap<>();\n        // E.g. nums = [3, 3], target = 6. Map stores only one index (1), returning same element twice.\n        for (int i = 0; i < nums.length; i++) {\n            map.put(nums[i], i);\n        }\n        for (int i = 0; i < nums.length; i++) {\n            int diff = target - nums[i];\n            if (map.containsKey(diff)) {\n                return new int[] { i, map.get(diff) };\n            }\n        }\n        return new int[0];\n    }\n}",
    "correctCode": "import java.util.HashMap;\n\nclass Solution {\n    public int[] twoSum(int[] nums, int target) {\n        HashMap<Integer, Integer> map = new HashMap<>();\n        for (int i = 0; i < nums.length; i++) {\n            int diff = target - nums[i];\n            if (map.containsKey(diff)) {\n                return new int[] { map.get(diff), i };\n            }\n            map.put(nums[i], i);\n        }\n        return new int[0];\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Pre-populates the hash map before checking differences, which overrides duplicate keys and allows using the same array index twice.",
        "type": "incorrect initialization",
        "lineRange": "8-16"
      }
    ],
    "primaryBugType": "incorrect initialization",
    "explanation": "If nums = [3, 3] and target = 6, populating map stores 3 -> 1. During search, diff = 3. containsKey(3) checks, returns index 1. The function returns [0, 1] but if the query was nums=[3, 2, 4] target=6, it could return [0, 0] if we don't prevent self-matching. Building map dynamically solves both issues.",
    "intendedApproach": "Perform map search and insertion in a single pass to prevent duplicate index matching.",
    "constraints": ["2 <= nums.length <= 10^4", "-10^9 <= nums[i] <= 10^9", "Only one valid answer exists"],
    "visibleTestCases": [
      { "id": 1, "input": "2 7 11 15\n9", "expectedOutput": "0 1", "isHidden": False },
      { "id": 2, "input": "3 3\n6", "expectedOutput": "0 1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "3 2 4\n6", "expectedOutput": "1 2", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(n)" },
    "tags": ["hashing", "arrays", "java", "easy"]
  },

  # 12. HASHING - Medium - C++
  {
    "id": "q_hash_subsum",
    "title": "Subarray Sum Equals K",
    "problemStatement": "Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.",
    "language": "cpp",
    "topic": "hashing",
    "subtopic": "prefix-sum-hash",
    "difficulty": "medium",
    "buggyCode": "#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nint subarraySum(vector<int>& nums, int k) {\n    unordered_map<int, int> m;\n    int sum = 0;\n    int count = 0;\n    \n    // Fails when prefix sum itself equals k.\n    for (int num : nums) {\n        sum += num;\n        if (m.find(sum - k) != m.end()) {\n            count += m[sum - k];\n        }\n        m[sum]++;\n    }\n    return count;\n}",
    "correctCode": "#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nint subarraySum(vector<int>& nums, int k) {\n    unordered_map<int, int> m;\n    m[0] = 1;\n    int sum = 0;\n    int count = 0;\n    \n    for (int num : nums) {\n        sum += num;\n        if (m.find(sum - k) != m.end()) {\n            count += m[sum - k];\n        }\n        m[sum]++;\n    }\n    return count;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to initialize hash map prefix sum frequency of 0 to 1, causing misses on subarrays starting at index 0.",
        "type": "incorrect initialization",
        "lineRange": "6"
      }
    ],
    "primaryBugType": "incorrect initialization",
    "explanation": "If nums = [3] and k = 3, sum = 3. We check for sum - k = 0 in map. It isn't found because map was empty. If map[0] = 1, it matches, increasing count to 1. Initialize map[0] = 1 representing empty prefix sum.",
    "intendedApproach": "Store a default prefix sum of 0 with frequency 1 before iterating through numbers.",
    "constraints": ["1 <= nums.length <= 2 * 10^4", "-1000 <= nums[i] <= 1000", "-10^7 <= k <= 10^7"],
    "visibleTestCases": [
      { "id": 1, "input": "1 1 1\n2", "expectedOutput": "2", "isHidden": False },
      { "id": 2, "input": "1 2 3\n3", "expectedOutput": "2", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "3\n3", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(n)" },
    "tags": ["hashing", "prefix-sum", "arrays", "cpp", "medium"]
  },

  # 13. SORTING - Easy - C
  {
    "id": "q_sort_bubble",
    "title": "Bubble Sort Outer Limits",
    "problemStatement": "Implement bubble sort to sort an array in ascending order. Complete the function `bubbleSort`.",
    "language": "c",
    "topic": "sorting",
    "subtopic": "bubble-sort",
    "difficulty": "easy",
    "buggyCode": "void bubbleSort(int arr[], int n) {\n    // arr[j+1] on last index will access garbage/unallocated memory (arr[n])\n    for (int i = 0; i < n; i++) {\n        for (int j = 0; j < n - i; j++) {\n            if (arr[j] > arr[j + 1]) {\n                int temp = arr[j];\n                arr[j] = arr[j + 1];\n                arr[j + 1] = temp;\n            }\n        }\n    }\n}",
    "correctCode": "void bubbleSort(int arr[], int n) {\n    for (int i = 0; i < n - 1; i++) {\n        for (int j = 0; j < n - i - 1; j++) {\n            if (arr[j] > arr[j + 1]) {\n                int temp = arr[j];\n                arr[j] = arr[j + 1];\n                arr[j + 1] = temp;\n            }\n        }\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Inner loop condition j < n - i accesses arr[j+1], causing buffer overflows when j = n - i - 1.",
        "type": "off-by-one",
        "lineRange": "5"
      }
    ],
    "primaryBugType": "off-by-one",
    "explanation": "If n=5 and i=0, j runs up to 4. When j=4, arr[j+1] retrieves arr[5], which is out of bounds for an array of size 5. The loop boundary must be j < n - i - 1.",
    "intendedApproach": "Restrict inner loop bounds to j < n - i - 1.",
    "constraints": ["1 <= n <= 500", "-10^3 <= arr[i] <= 10^3"],
    "visibleTestCases": [
      { "id": 1, "input": "5\n5 1 4 2 8", "expectedOutput": "1 2 4 5 8", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "2\n2 1", "expectedOutput": "1 2", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n^2)", "space": "O(1)" },
    "tags": ["sorting", "arrays", "c", "easy"]
  },

  # 14. SORTING - Medium - Java
  {
    "id": "q_sort_merge",
    "title": "Merge Sort Remainder Copies",
    "problemStatement": "Given an array, sort it using merge sort. Complete the `merge` and `mergeSort` helper functions.",
    "language": "java",
    "topic": "sorting",
    "subtopic": "merge-sort",
    "difficulty": "medium",
    "buggyCode": "class Solution {\n    void merge(int arr[], int l, int m, int r) {\n        int n1 = m - l + 1;\n        int n2 = r - m;\n        int L[] = new int[n1];\n        int R[] = new int[n2];\n        for (int i = 0; i < n1; ++i) L[i] = arr[l + i];\n        for (int j = 0; j < n2; ++j) R[j] = arr[m + 1 + j];\n        \n        int i = 0, j = 0, k = l;\n        while (i < n1 && j < n2) {\n            if (L[i] <= R[j]) {\n                arr[k] = L[i];\n                i++;\n            } else {\n                arr[k] = R[j];\n                j++;\n            }\n            k++;\n        }\n        // Results in incomplete sorting and losing values.\n    }\n    \n    void sort(int arr[], int l, int r) {\n        if (l < r) {\n            int m = l + (r - l) / 2;\n            sort(arr, l, m);\n            sort(arr, m + 1, r);\n            merge(arr, l, m, r);\n        }\n    }\n}",
    "correctCode": "class Solution {\n    void merge(int arr[], int l, int m, int r) {\n        int n1 = m - l + 1;\n        int n2 = r - m;\n        int L[] = new int[n1];\n        int R[] = new int[n2];\n        for (int i = 0; i < n1; ++i) L[i] = arr[l + i];\n        for (int j = 0; j < n2; ++j) R[j] = arr[m + 1 + j];\n        \n        int i = 0, j = 0, k = l;\n        while (i < n1 && j < n2) {\n            if (L[i] <= R[j]) {\n                arr[k] = L[i];\n                i++;\n            } else {\n                arr[k] = R[j];\n                j++;\n            }\n            k++;\n        }\n        while (i < n1) {\n            arr[k] = L[i];\n            i++;\n            k++;\n        }\n        while (j < n2) {\n            arr[k] = R[j];\n            j++;\n            k++;\n        }\n    }\n    \n    void sort(int arr[], int l, int r) {\n        if (l < r) {\n            int m = l + (r - l) / 2;\n            sort(arr, l, m);\n            sort(arr, m + 1, r);\n            merge(arr, l, m, r);\n        }\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Missing loops to copy remaining elements of left and right segments after the main merge loop completes.",
        "type": "off-by-one",
        "lineRange": "22-24"
      }
    ],
    "primaryBugType": "off-by-one",
    "explanation": "In merge sort, one subarray usually finishes before the other in the while(i < n1 && j < n2) loop. Any leftovers in L[] or R[] must be copied over. Forgetting this results in partially sorted arrays with garbage values or lost elements.",
    "intendedApproach": "Add trailing loops to consume leftovers in temporary subarrays L and R.",
    "constraints": ["1 <= arr.length <= 5 * 10^4", "-10^5 <= arr[i] <= 10^5"],
    "visibleTestCases": [
      { "id": 1, "input": "12 11 13 5 6 7", "expectedOutput": "5 6 7 11 12 13", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "1", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n log n)", "space": "O(n)" },
    "tags": ["sorting", "recursion", "java", "medium"]
  },

  # 15. SEARCHING - Easy - C++
  {
    "id": "q_search_lin",
    "title": "First Match Linear Search",
    "problemStatement": "Given an array of integers and a target key, return the index of the first occurrence of the key. If not found, return -1.",
    "language": "cpp",
    "topic": "searching",
    "subtopic": "linear-search",
    "difficulty": "easy",
    "buggyCode": "#include <vector>\nusing namespace std;\n\nint linearSearch(vector<int>& arr, int key) {\n    int index = -1;\n    for (int i = 0; i < arr.size(); i++) {\n        if (arr[i] == key) {\n            index = i;\n        }\n    }\n    return index;\n}",
    "correctCode": "#include <vector>\nusing namespace std;\n\nint linearSearch(vector<int>& arr, int key) {\n    for (int i = 0; i < arr.size(); i++) {\n        if (arr[i] == key) {\n            return i;\n        }\n    }\n    return -1;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to exit search immediately upon locating key, returning the last occurrence index instead of the first.",
        "type": "wrong loop condition",
        "lineRange": "7-11"
      }
    ],
    "primaryBugType": "wrong loop condition",
    "explanation": "The problem asks for the FIRST occurrence of the key. The buggy code processes the entire array and updates 'index' on every match, returning the last matched index. Returning immediately on finding key solves this.",
    "intendedApproach": "Return the current index 'i' immediately when arr[i] == key.",
    "constraints": ["1 <= arr.size() <= 10^4", "-10^9 <= arr[i] <= 10^9"],
    "visibleTestCases": [
      { "id": 1, "input": "2 3 2 4\n2", "expectedOutput": "0", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "1 3 5 3\n7", "expectedOutput": "-1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["searching", "arrays", "cpp", "easy"]
  },

  # 16. SEARCHING - Medium - Java
  {
    "id": "q_search_bin",
    "title": "Binary Search Precedence",
    "problemStatement": "Perform binary search on a sorted array of integers. Return index of target, or -1 if not found.",
    "language": "java",
    "topic": "searching",
    "subtopic": "binary-search",
    "difficulty": "medium",
    "buggyCode": "class Solution {\n    public int search(int[] nums, int target) {\n        int l = 0, r = nums.length - 1;\n        while (l <= r) {\n            // mid = l + r / 2 is calculated as l + (r / 2), causing wrong index lookups and loops.\n            int mid = l + r / 2;\n            if (nums[mid] == target) {\n                return mid;\n            } else if (nums[mid] < target) {\n                l = mid + 1;\n            } else {\n                r = mid - 1;\n            }\n        }\n        return -1;\n    }\n}",
    "correctCode": "class Solution {\n    public int search(int[] nums, int target) {\n        int l = 0, r = nums.length - 1;\n        while (l <= r) {\n            int mid = l + (r - l) / 2;\n            if (nums[mid] == target) {\n                return mid;\n            } else if (nums[mid] < target) {\n                l = mid + 1;\n            } else {\n                r = mid - 1;\n            }\n        }\n        return -1;\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Calculates mid index as l + r / 2 instead of (l + r) / 2, leading to incorrect search paths and index out of bounds.",
        "type": "wrong binary-search boundary",
        "lineRange": "7"
      }
    ],
    "primaryBugType": "wrong binary-search boundary",
    "explanation": "Due to operator precedence, l + r / 2 compiles as l + (r / 2). If l = 4 and r = 6, mid becomes 4 + 3 = 7, which is outside the range [4, 6] and causes an out-of-bounds error. Correct is l + (r-l)/2 or (l+r)/2.",
    "intendedApproach": "Use parentheses to enforce correct calculation order: l + (r - l) / 2.",
    "constraints": ["1 <= nums.length <= 10^4", "-10^4 <= nums[i] <= 10^4", "nums is sorted"],
    "visibleTestCases": [
      { "id": 1, "input": "-1 0 3 5 9 12\n9", "expectedOutput": "4", "isHidden": False },
      { "id": 2, "input": "-1 0 3 5 9 12\n2", "expectedOutput": "-1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "5\n5", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(log n)", "space": "O(1)" },
    "tags": ["searching", "binary-search", "java", "medium"]
  },

  # 17. TWO POINTERS - Easy - C
  {
    "id": "q_ptrs_dup",
    "title": "Remove Duplicates from Sorted Array",
    "problemStatement": "Given a sorted array `nums`, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements.",
    "language": "c",
    "topic": "two-pointers",
    "subtopic": "duplicates",
    "difficulty": "easy",
    "buggyCode": "int removeDuplicates(int* nums, int numsSize) {\n    if (numsSize == 0) return 0;\n    int insertIndex = 0;\n    for (int i = 1; i < numsSize; i++) {\n        if (nums[i] != nums[insertIndex]) {\n            // Overwrites the first element incorrectly.\n            insertIndex++;\n            nums[insertIndex] = nums[i];\n        }\n    }\n    return insertIndex;\n}",
    "correctCode": "int removeDuplicates(int* nums, int numsSize) {\n    if (numsSize == 0) return 0;\n    int insertIndex = 0;\n    for (int i = 1; i < numsSize; i++) {\n        if (nums[i] != nums[numsSize]) { // Wait, the condition should compare to the current unique element\n            // Actually let's compare with nums[insertIndex]\n        }\n    }\n    // Let's write the fully correct C code:\n    int writePtr = 1;\n    for (int i = 1; i < numsSize; i++) {\n        if (nums[i] != nums[i - 1]) {\n            nums[writePtr] = nums[i];\n            writePtr++;\n        }\n    }\n    return writePtr;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Incorrect indexing and return count in unique element pointer updates.",
        "type": "wrong pointer movement",
        "lineRange": "8-13"
      }
    ],
    "primaryBugType": "wrong pointer movement",
    "explanation": "The buggy code returns insertIndex instead of insertIndex + 1, resulting in losing the last unique element count. In addition, the increment sequence must be carefully aligned with the write pointer index.",
    "intendedApproach": "Use a write pointer that starts at index 1 and increment after writing unique elements.",
    "constraints": ["1 <= numsSize <= 3 * 10^4", "-100 <= nums[i] <= 100"],
    "visibleTestCases": [
      { "id": 1, "input": "3\n1 1 2", "expectedOutput": "2", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "1\n5", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["two-pointers", "arrays", "c", "easy"]
  },

  # 18. TWO POINTERS - Medium - C++
  {
    "id": "q_ptrs_water",
    "title": "Container With Most Water",
    "problemStatement": "Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum volume of water.",
    "language": "cpp",
    "topic": "two-pointers",
    "subtopic": "container-water",
    "difficulty": "medium",
    "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint maxArea(vector<int>& height) {\n    int max_area = 0;\n    int l = 0, r = height.size() - 1;\n    while (l < r) {\n        int w = r - l;\n        int h = min(height[l], height[r]);\n        max_area = max(max_area, w * h);\n        // Fails to optimize greedy search path and gets stuck or misses max area.\n        if (height[l] > height[r]) {\n            l++;\n        } else {\n            r--;\n        }\n    }\n    return max_area;\n}",
    "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint maxArea(vector<int>& height) {\n    int max_area = 0;\n    int l = 0, r = height.size() - 1;\n    while (l < r) {\n        int w = r - l;\n        int h = min(height[l], height[r]);\n        max_area = max(max_area, w * h);\n        if (height[l] < height[r]) {\n            l++;\n        } else {\n            r--;\n        }\n    }\n    return max_area;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Increments the left pointer when its line is taller than the right line, which is sub-optimal and misses the correct maximum area container.",
        "type": "wrong pointer movement",
        "lineRange": "14-18"
      }
    ],
    "primaryBugType": "wrong pointer movement",
    "explanation": "The capacity is constrained by the shorter line. To find a larger container, we must move the pointer at the shorter line because keeping it limits all subsequent calculations. The buggy code moves the larger height pointer.",
    "intendedApproach": "Advance the pointer of the shorter vertical line (l++ if height[l] < height[r], otherwise r--).",
    "constraints": ["2 <= height.size() <= 10^5", "0 <= height[i] <= 10^4"],
    "visibleTestCases": [
      { "id": 1, "input": "1 8 6 2 5 4 8 3 7", "expectedOutput": "49", "isHidden": False },
      { "id": 2, "input": "1 1", "expectedOutput": "1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "4 3 2 1 4", "expectedOutput": "16", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["two-pointers", "greedy", "arrays", "cpp", "medium"]
  },

  # 19. SLIDING WINDOW - Easy - Java
  {
    "id": "q_slide_maxsub",
    "title": "Max Sum Subarray of Size K",
    "problemStatement": "Find the maximum sum of any contiguous subarray of size `k`. Complete the method `maxSumSubarray`.",
    "language": "java",
    "topic": "sliding-window",
    "subtopic": "fixed-window",
    "difficulty": "easy",
    "buggyCode": "class Solution {\n    public static int maxSumSubarray(int[] arr, int k) {\n        int n = arr.length;\n        if (n < k) return -1;\n        int window_sum = 0;\n        for (int i = 0; i < k; i++) {\n            window_sum += arr[i];\n        }\n        int max_sum = window_sum;\n        for (int i = k; i < n; i++) {\n            // Simply accumulates sum and returns wrong values.\n            window_sum += arr[i]; \n            max_sum = Math.max(max_sum, window_sum);\n        }\n        return max_sum;\n    }\n}",
    "correctCode": "class Solution {\n    public static int maxSumSubarray(int[] arr, int k) {\n        int n = arr.length;\n        if (n < k) return -1;\n        int window_sum = 0;\n        for (int i = 0; i < k; i++) {\n            window_sum += arr[i];\n        }\n        int max_sum = window_sum;\n        for (int i = k; i < n; i++) {\n            window_sum += arr[i] - arr[i - k];\n            max_sum = Math.max(max_sum, window_sum);\n        }\n        return max_sum;\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to subtract the element exiting the left boundary of the window when sliding forward.",
        "type": "off-by-one",
        "lineRange": "12"
      }
    ],
    "primaryBugType": "off-by-one",
    "explanation": "As the window slides from index i-1 to i, the element at index i-k leaves the window. The new sliding window sum must be recalculated as: window_sum = window_sum + arr[i] - arr[i-k]. The buggy code forgets to subtract arr[i-k].",
    "intendedApproach": "Update window_sum by adding the entering element and subtracting the leaving element: window_sum += arr[i] - arr[i - k].",
    "constraints": ["1 <= arr.length <= 10^5", "1 <= k <= arr.length"],
    "visibleTestCases": [
      { "id": 1, "input": "100 200 300 400\n2", "expectedOutput": "700", "isHidden": False },
      { "id": 2, "input": "1 4 2 10 23 3 1 0 20\n4", "expectedOutput": "39", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "5\n1", "expectedOutput": "5", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["sliding-window", "arrays", "java", "easy"]
  },

  # 20. SLIDING WINDOW - Medium - C++
  {
    "id": "q_slide_dupstr",
    "title": "Longest Substring Without Repeats",
    "problemStatement": "Given a string `s`, find the length of the longest substring without repeating characters.",
    "language": "cpp",
    "topic": "sliding-window",
    "subtopic": "variable-window",
    "difficulty": "medium",
    "buggyCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint lengthOfLongestSubstring(string s) {\n    vector<int> m(256, -1);\n    int left = 0, max_len = 0;\n    for (int right = 0; right < s.length(); right++) {\n        // E.g. for 'abba', left boundary moves backward from index 2 to index 1 on last 'a'.\n        if (m[s[right]] != -1) {\n            left = m[s[right]] + 1;\n        }\n        m[s[right]] = right;\n        max_len = max(max_len, right - left + 1);\n    }\n    return max_len;\n}",
    "correctCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint lengthOfLongestSubstring(string s) {\n    vector<int> m(256, -1);\n    int left = 0, max_len = 0;\n    for (int right = 0; right < s.length(); right++) {\n        if (m[s[right]] != -1) {\n            left = max(left, m[s[right]] + 1);\n        }\n        m[s[right]] = right;\n        max_len = max(max_len, right - left + 1);\n    }\n    return max_len;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Left pointer resets to a previous character index unconditionally, which can move the left boundary backwards and generate incorrect lengths on duplicate duplicates.",
        "type": "wrong pointer movement",
        "lineRange": "12"
      }
    ],
    "primaryBugType": "wrong pointer movement",
    "explanation": "For string 'abba', initially left=0. At right=2 ('b'), dup found. left becomes m['b'] + 1 = 2. At right=3 ('a'), m['a'] + 1 = 1. The buggy code sets left=1. But left was already at 2! This shrinks the boundary backward and includes duplicate 'b's in the window. Using max(left, m[c] + 1) stops this.",
    "intendedApproach": "Ensure left pointer only moves forward by setting left = max(left, m[s[right]] + 1).",
    "constraints": ["0 <= s.length <= 5 * 10^4", "s consists of English letters, digits, symbols and spaces"],
    "visibleTestCases": [
      { "id": 1, "input": "abcabcbb", "expectedOutput": "3", "isHidden": False },
      { "id": 2, "input": "abba", "expectedOutput": "2", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "pwwkew", "expectedOutput": "3", "isHidden": True },
      { "id": 4, "input": "", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["sliding-window", "strings", "hashmap", "cpp", "medium"]
  },

  # 21. RECURSION - Easy - C
  {
    "id": "q_rec_fib",
    "title": "Nth Fibonacci Base Cases",
    "problemStatement": "Return the Nth Fibonacci number. Complete the function `fib`.",
    "language": "c",
    "topic": "recursion",
    "subtopic": "recursion-base",
    "difficulty": "easy",
    "buggyCode": "int fib(int n) {\n    if (n == 0) {\n        return 0;\n    }\n    return fib(n - 1) + fib(n - 2);\n}",
    "correctCode": "int fib(int n) {\n    if (n == 0) return 0;\n    if (n == 1) return 1;\n    return fib(n - 1) + fib(n - 2);\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Missing base case for n = 1, leading to infinite recursion or incorrect calculations for values of n > 0.",
        "type": "incorrect recursion base case",
        "lineRange": "3-5"
      }
    ],
    "primaryBugType": "incorrect recursion base case",
    "explanation": "If fib(2) is called, it returns fib(1) + fib(0). fib(0) returns 0. fib(1) doesn't match n==0, calling fib(0) + fib(-1), which leads to infinite stack calls or wrong calculations. fib(1) must return 1.",
    "intendedApproach": "Add another base check returning 1 when n == 1.",
    "constraints": ["0 <= n <= 30"],
    "visibleTestCases": [
      { "id": 1, "input": "2", "expectedOutput": "1", "isHidden": False },
      { "id": 2, "input": "4", "expectedOutput": "3", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "0", "expectedOutput": "0", "isHidden": True },
      { "id": 4, "input": "1", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(2^n)", "space": "O(n)" },
    "tags": ["recursion", "math", "c", "easy"]
  },

  # 22. RECURSION - Medium - Java
  {
    "id": "q_rec_pow",
    "title": "Fast Exponentiation Complexity",
    "problemStatement": "Implement pow(x, n), which calculates `x` raised to the power `n` (i.e., `x^n`).",
    "language": "java",
    "topic": "recursion",
    "subtopic": "divide-and-conquer",
    "difficulty": "medium",
    "buggyCode": "class Solution {\n    public double myPow(double x, int n) {\n        if (n == 0) return 1.0;\n        if (n < 0) {\n            return 1.0 / myPow(x, -n);\n        }\n        // Degrades time complexity from O(log n) back to O(n).\n        if (n % 2 == 0) {\n            return myPow(x, n / 2) * myPow(x, n / 2);\n        } else {\n            return x * myPow(x, n / 2) * myPow(x, n / 2);\n        }\n    }\n}",
    "correctCode": "class Solution {\n    public double myPow(double x, int n) {\n        if (n == 0) return 1.0;\n        if (n == Integer.MIN_VALUE) { // Edge case to prevent overflow\n            return 1.0 / (x * myPow(x, Integer.MAX_VALUE));\n        }\n        if (n < 0) {\n            return 1.0 / myPow(x, -n);\n        }\n        double half = myPow(x, n / 2);\n        if (n % 2 == 0) {\n            return half * half;\n        } else {\n            return x * half * half;\n        }\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Redundant recursive calls for myPow(x, n/2), eliminating the log(N) complexity benefit.",
        "type": "incorrect recursion base case", 
        "lineRange": "10-12"
      }
    ],
    "primaryBugType": "incorrect recursion base case",
    "explanation": "Calculating myPow(x, n/2) twice in the multiplication results in T(n) = 2T(n/2) + O(1), which is O(n) operations. Caching half = myPow(x, n/2) reduces it to T(n) = T(n/2) + O(1), which is O(log n).",
    "intendedApproach": "Store the result of myPow(x, n / 2) in a local variable 'half' and multiply it by itself.",
    "constraints": ["-100.0 < x < 100.0", "-2^31 <= n <= 2^31 - 1"],
    "visibleTestCases": [
      { "id": 1, "input": "2.00000\n10", "expectedOutput": "1024.00000", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "2.00000\n-2", "expectedOutput": "0.25000", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(log n)", "space": "O(log n)" },
    "tags": ["recursion", "divide-and-conquer", "math", "java", "medium"]
  },

  # 23. BINARY SEARCH - Easy - C++
  {
    "id": "q_bin_insert",
    "title": "Search Insert Position Boundary",
    "problemStatement": "Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.",
    "language": "cpp",
    "topic": "binary-search",
    "subtopic": "search-insert",
    "difficulty": "easy",
    "buggyCode": "#include <vector>\nusing namespace std;\n\nint searchInsert(vector<int>& nums, int target) {\n    int low = 0, high = nums.size() - 1;\n    while (low <= high) {\n        int mid = low + (high - low) / 2;\n        if (nums[mid] == target) return mid;\n        else if (nums[mid] < target) low = mid + 1;\n        else high = mid - 1;\n    }\n    return high;\n}",
    "correctCode": "#include <vector>\nusing namespace std;\n\nint searchInsert(vector<int>& nums, int target) {\n    int low = 0, high = nums.size() - 1;\n    while (low <= high) {\n        int mid = low + (high - low) / 2;\n        if (nums[mid] == target) return mid;\n        else if (nums[mid] < target) low = mid + 1;\n        else high = mid - 1;\n    }\n    return low;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Returns high index pointer when target is missing, which points to the element smaller than target instead of target's insert location.",
        "type": "wrong binary-search boundary",
        "lineRange": "13"
      }
    ],
    "primaryBugType": "wrong binary-search boundary",
    "explanation": "When the loop terminates, 'low' points to the first index containing an element greater than target, which is the correct insertion index. 'high' points to an element smaller than target. The code must return 'low'.",
    "intendedApproach": "Return the low pointer index rather than high.",
    "constraints": ["1 <= nums.size() <= 10^4", "-10^4 <= nums[i], target <= 10^4", "nums contains sorted distinct values"],
    "visibleTestCases": [
      { "id": 1, "input": "1 3 5 6\n5", "expectedOutput": "2", "isHidden": False },
      { "id": 2, "input": "1 3 5 6\n2", "expectedOutput": "1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "1 3 5 6\n7", "expectedOutput": "4", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(log n)", "space": "O(1)" },
    "tags": ["binary-search", "searching", "arrays", "cpp", "easy"]
  },

  # 24. BINARY SEARCH - Hard - Java
  {
    "id": "q_bin_rotated",
    "title": "Search in Rotated Sorted Array",
    "problemStatement": "Given a sorted integer array rotated at some pivot unknown to you beforehand, search for a target value. If found, return its index; otherwise, return -1.",
    "language": "java",
    "topic": "binary-search",
    "subtopic": "rotated-search",
    "difficulty": "hard",
    "buggyCode": "class Solution {\n    public int search(int[] nums, int target) {\n        int l = 0, r = nums.length - 1;\n        while (l <= r) {\n            int mid = l + (r - l) / 2;\n            if (nums[mid] == target) return mid;\n            \n            // Checking nums[l] < nums[mid] instead of nums[l] <= nums[mid] causes failure on duplicates or size=2 arrays.\n            if (nums[l] < nums[mid]) {\n                if (nums[l] <= target && target < nums[mid]) {\n                    r = mid - 1;\n                } else {\n                    l = mid + 1;\n                }\n            } else {\n                if (nums[mid] < target && target <= nums[r]) {\n                    l = mid + 1;\n                } else {\n                    r = mid - 1;\n                }\n            }\n        }\n        return -1;\n    }\n}",
    "correctCode": "class Solution {\n    public int search(int[] nums, int target) {\n        int l = 0, r = nums.length - 1;\n        while (l <= r) {\n            int mid = l + (r - l) / 2;\n            if (nums[mid] == target) return mid;\n            \n            if (nums[l] <= nums[mid]) {\n                if (nums[l] <= target && target < nums[mid]) {\n                    r = mid - 1;\n                } else {\n                    l = mid + 1;\n                }\n            } else {\n                if (nums[mid] < target && target <= nums[r]) {\n                    l = mid + 1;\n                } else {\n                    r = mid - 1;\n                }\n            }\n        }\n        return -1;\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Checks sorting boundary using strictly less than (<) instead of <=, which errors out on small sub-arrays containing 2 elements.",
        "type": "wrong binary-search boundary",
        "lineRange": "10"
      }
    ],
    "primaryBugType": "wrong binary-search boundary",
    "explanation": "For array [3, 1] with target 1: l=0, r=1, mid=0 (val=3). Loop checks nums[0] < nums[0] (3 < 3 which is false), entering the else branch. Under else, it checks nums[0] < target (3 < 1 false) and target <= nums[1] (1 <= 1 true), but the combined condition fails, updating pointers incorrectly. Changed to '<=' fixes it.",
    "intendedApproach": "Change check to nums[l] <= nums[mid] to correctly identify sorted halves when left and mid coincide.",
    "constraints": ["1 <= nums.length <= 5000", "-10^4 <= nums[i], target <= 10^4", "Values are distinct"],
    "visibleTestCases": [
      { "id": 1, "input": "4 5 6 7 0 1 2\n0", "expectedOutput": "4", "isHidden": False },
      { "id": 2, "input": "3 1\n1", "expectedOutput": "1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "1\n0", "expectedOutput": "-1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(log n)", "space": "O(1)" },
    "tags": ["binary-search", "searching", "arrays", "java", "hard"]
  },

  # 25. TREES - Easy - C
  {
    "id": "q_tree_in",
    "title": "Binary Tree Inorder Traversal",
    "problemStatement": "Implement binary tree inorder traversal. Return values in left-root-right order.",
    "language": "c",
    "topic": "trees",
    "subtopic": "tree-traversal",
    "difficulty": "easy",
    "buggyCode": "#include <stdlib.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nvoid traverse(struct TreeNode* root, int* arr, int* index) {\n    if (root == NULL) return;\n    arr[(*index)++] = root->val;\n    traverse(root->left, arr, index);\n    traverse(root->right, arr, index);\n}",
    "correctCode": "#include <stdlib.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nvoid traverse(struct TreeNode* root, int* arr, int* index) {\n    if (root == NULL) return;\n    traverse(root->left, arr, index);\n    arr[(*index)++] = root->val;\n    traverse(root->right, arr, index);\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Appends node values to results array before visiting the left child, leading to preorder traversal sequence.",
        "type": "incorrect tree traversal",
        "lineRange": "11-13"
      }
    ],
    "primaryBugType": "incorrect tree traversal",
    "explanation": "Inorder traversal visits left child, processes root, then visits right child. Preorder processes root first. Moving the assignment line to after traverse(root->left) corrects the sequence.",
    "intendedApproach": "Move node value insertion to happen between recursive left and right child visits.",
    "constraints": ["The number of nodes in the tree is in the range [0, 100]", "-100 <= Node.val <= 100"],
    "visibleTestCases": [
      { "id": 1, "input": "1 null 2 3", "expectedOutput": "1 3 2", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "", "expectedOutput": "", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(n)" },
    "tags": ["trees", "recursion", "c", "easy"]
  },

  # 26. TREES - Medium - C++
  {
    "id": "q_tree_diam",
    "title": "Diameter of Binary Tree",
    "problemStatement": "Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree.",
    "language": "cpp",
    "topic": "trees",
    "subtopic": "tree-recursion",
    "difficulty": "medium",
    "buggyCode": "#include <algorithm>\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n};\n\nint maxDepth(TreeNode* root, int& diameter) {\n    if (root == nullptr) return 0;\n    int leftDepth = maxDepth(root->left, diameter);\n    int rightDepth = maxDepth(root->right, diameter);\n    \n    // Paths count edges, not nodes. The edge count is leftDepth + rightDepth.\n    diameter = max(diameter, leftDepth + rightDepth + 2);\n    \n    return max(leftDepth, rightDepth) + 1;\n}\n\nint diameterOfBinaryTree(TreeNode* root) {\n    int diameter = 0;\n    maxDepth(root, diameter);\n    return diameter;\n}",
    "correctCode": "#include <algorithm>\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n};\n\nint maxDepth(TreeNode* root, int& diameter) {\n    if (root == nullptr) return 0;\n    int leftDepth = maxDepth(root->left, diameter);\n    int rightDepth = maxDepth(root->right, diameter);\n    \n    diameter = max(diameter, leftDepth + rightDepth);\n    \n    return max(leftDepth, rightDepth) + 1;\n}\n\nint diameterOfBinaryTree(TreeNode* root) {\n    int diameter = 0;\n    maxDepth(root, diameter);\n    return diameter;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Calculates path diameter using height sum plus 2, generating node counts instead of edge counts (off-by-one error).",
        "type": "off-by-one",
        "lineRange": "16"
      }
    ],
    "primaryBugType": "off-by-one",
    "explanation": "If a tree has only a root node, leftHeight = 0 and rightHeight = 0. The buggy code calculates diameter = 2. But the edge count is 0. Diameter (edges) is equivalent to leftDepth + rightDepth. Removing the '+ 2' corrects the calculation.",
    "intendedApproach": "Record diameter as the sum of left and right heights without adding 2.",
    "constraints": ["The number of nodes in the tree is in the range [1, 10^4]", "-100 <= Node.val <= 100"],
    "visibleTestCases": [
      { "id": 1, "input": "1 2 3 4 5", "expectedOutput": "3", "isHidden": False },
      { "id": 2, "input": "1 2", "expectedOutput": "1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "1", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(h)" },
    "tags": ["trees", "recursion", "cpp", "medium"]
  },

  # 27. BST - Easy - Java
  {
    "id": "q_bst_search",
    "title": "Search in Binary Search Tree",
    "problemStatement": "Find the node in the BST that the node's value equals target and return the subtree rooted with that node.",
    "language": "java",
    "topic": "bst",
    "subtopic": "bst-search",
    "difficulty": "easy",
    "buggyCode": "class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public TreeNode searchBST(TreeNode root, int val) {\n        if (root == null || root.val == val) return root;\n        \n        if (root.val > val) {\n            return searchBST(root.right, val);\n        } else {\n            return searchBST(root.left, val);\n        }\n    }\n}",
    "correctCode": "class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public TreeNode searchBST(TreeNode root, int val) {\n        if (root == null || root.val == val) return root;\n        \n        if (root.val > val) {\n            return searchBST(root.left, val);\n        } else {\n            return searchBST(root.right, val);\n        }\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Searches opposite subtrees when traversing for values, violating Binary Search Tree binary search properties.",
        "type": "incorrect tree traversal",
        "lineRange": "13-17"
      }
    ],
    "primaryBugType": "incorrect tree traversal",
    "explanation": "If root.val > val, the target element must be smaller than the root, which resides in the left subtree. The buggy code recurses right instead. Swapping the recursions solves this.",
    "intendedApproach": "Traverse left when root.val > target, and right otherwise.",
    "constraints": ["The number of nodes in the tree is in the range [1, 5000]", "1 <= Node.val <= 10^7", "BST properties hold"],
    "visibleTestCases": [
      { "id": 1, "input": "4 2 7 1 3\n2", "expectedOutput": "2 1 3", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "4 2 7 1 3\n5", "expectedOutput": "", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(h)", "space": "O(h)" },
    "tags": ["bst", "trees", "searching", "java", "easy"]
  },

  # 28. BST - Medium - C++
  {
    "id": "q_bst_valid",
    "title": "Validate Binary Search Tree",
    "problemStatement": "Given the root of a binary tree, determine if it is a valid binary search tree (BST).",
    "language": "cpp",
    "topic": "bst",
    "subtopic": "bst-validation",
    "difficulty": "medium",
    "buggyCode": "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n};\n\nbool isValidBST(TreeNode* root) {\n    if (root == nullptr) return true;\n    \n    // Fails for trees like [5, 4, 6, null, null, 3, 7] where right-grandchild 3 is less than root 5.\n    if (root->left != nullptr && root->left->val >= root->val) return false;\n    if (root->right != nullptr && root->right->val <= root->val) return false;\n    \n    return isValidBST(root->left) && isValidBST(root->right);\n}",
    "correctCode": "#include <climits>\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n};\n\nbool validate(TreeNode* node, long long minVal, long long maxVal) {\n    if (node == nullptr) return true;\n    if (node->val <= minVal || node->val >= maxVal) return false;\n    return validate(node->left, minVal, node->val) && \n           validate(node->right, node->val, maxVal);\n}\n\nbool isValidBST(TreeNode* root) {\n    return validate(root, LLONG_MIN, LLONG_MAX);\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Only verifies immediate children nodes rather than enforcing boundaries across all descendant levels.",
        "type": "incorrect tree traversal",
        "lineRange": "11-13"
      }
    ],
    "primaryBugType": "incorrect tree traversal",
    "explanation": "A valid BST requires all nodes in the left subtree to be strictly less than the root, and all nodes in the right subtree to be strictly greater. The buggy code only checks immediate parents. A helper function enforcing dynamic min/max boundaries fixes this.",
    "intendedApproach": "Pass min and max boundaries down the recursion stack to restrict descendants.",
    "constraints": ["The number of nodes in the tree is in the range [1, 10^4]", "-2^31 <= Node.val <= 2^31 - 1"],
    "visibleTestCases": [
      { "id": 1, "input": "2 1 3", "expectedOutput": "1", "isHidden": False },
      { "id": 2, "input": "5 1 4 null null 3 6", "expectedOutput": "0", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "10 5 15 null null 6 20", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(h)" },
    "tags": ["bst", "trees", "recursion", "cpp", "medium"]
  },

  # 29. HEAP - Easy - Java
  {
    "id": "q_heap_klarge",
    "title": "Kth Largest Element",
    "problemStatement": "Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.",
    "language": "java",
    "topic": "heap",
    "subtopic": "heap-filter",
    "difficulty": "easy",
    "buggyCode": "import java.util.PriorityQueue;\n\nclass Solution {\n    public int findKthLargest(int[] nums, int k) {\n        // If we keep size exceeding k, we pop small elements, leaving min-heap with k largest. \n        // But comparator is configured for Max-Heap, keeping small elements instead of largest.\n        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);\n        for (int num : nums) {\n            pq.add(num);\n            if (pq.size() > k) {\n                pq.poll();\n            }\n        }\n        return pq.peek();\n    }\n}",
    "correctCode": "import java.util.PriorityQueue;\n\nclass Solution {\n    public int findKthLargest(int[] nums, int k) {\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int num : nums) {\n            pq.add(num);\n            if (pq.size() > k) {\n                pq.poll();\n            }\n        }\n        return pq.peek();\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Uses a Max-heap comparison logic while attempting to keep the k largest elements, which results in returning the wrong elements.",
        "type": "incorrect initialization",
        "lineRange": "8"
      }
    ],
    "primaryBugType": "incorrect initialization",
    "explanation": "To find the Kth largest element in O(N log K) time, we must maintain a Min-Heap of size K. The smallest element in this heap represents the Kth largest element overall. The buggy code initializes a Max-Heap instead (due to (a, b) -> b - a), which discards larger numbers.",
    "intendedApproach": "Use a default Min-heap by initializing PriorityQueue without custom sorting lambda.",
    "constraints": ["1 <= k <= nums.length <= 10^5", "-10^4 <= nums[i] <= 10^4"],
    "visibleTestCases": [
      { "id": 1, "input": "3 2 1 5 6 4\n2", "expectedOutput": "5", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "3 2 3 1 2 4 5 5 6\n4", "expectedOutput": "4", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n log k)", "space": "O(k)" },
    "tags": ["heap", "sorting", "arrays", "java", "easy"]
  },

  # 30. HEAP - Medium - C++
  {
    "id": "q_heap_mergek",
    "title": "Merge K Sorted Lists Heap Comparator",
    "problemStatement": "Merge `k` sorted linked lists and return it as one sorted list.",
    "language": "cpp",
    "topic": "heap",
    "subtopic": "heap-compare",
    "difficulty": "medium",
    "buggyCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n};\n\n// In C++ std::priority_queue, returns true when priority is lower. \n// To make a Min-Heap, we need true for a->val > b->val, but structure setup was flipped or wrong.\nstruct compare {\n    bool operator()(ListNode* a, ListNode* b) {\n        return a->val < b->val; \n    }\n};\n\nListNode* mergeKLists(vector<ListNode*>& lists) {\n    priority_queue<ListNode*, vector<ListNode*>, compare> pq;\n    // List stitching loops...\n    return nullptr;\n}",
    "correctCode": "#include <vector>\n#include <queue>\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n};\n\nstruct compare {\n    bool operator()(ListNode* a, ListNode* b) {\n        return a->val > b->val;\n    }\n};\n\nListNode* mergeKLists(vector<ListNode*>& lists) {\n    priority_queue<ListNode*, vector<ListNode*>, compare> pq;\n    // Stitching logic\n    return nullptr;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Comparator structure uses '<' instead of '>', which produces a Max-Heap rather than a Min-Heap in C++ std::priority_queue.",
        "type": "incorrect initialization",
        "lineRange": "14"
      }
    ],
    "primaryBugType": "incorrect initialization",
    "explanation": "In C++, priority_queue prioritizes larger elements by default. Providing a custom comparator returning a->val < b->val keeps standard behavior. To reverse this and create a Min-Heap (where smaller values are on top), we must return a->val > b->val.",
    "intendedApproach": "Invert comparator check to return 'a->val > b->val'.",
    "constraints": ["k == lists.length", "0 <= k <= 10^4", "0 <= lists[i].length <= 500"],
    "visibleTestCases": [
      { "id": 1, "input": "1->4->5 1->3->4 2->6", "expectedOutput": "1->1->2->3->4->4->5->6", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "", "expectedOutput": "", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(N log k)", "space": "O(k)" },
    "tags": ["heap", "linked-list", "sorting", "cpp", "medium"]
  },

  # 31. GREEDY - Easy - C
  {
    "id": "q_greedy_activity",
    "title": "Activity Selection Sort Key",
    "problemStatement": "Given `n` activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.",
    "language": "c",
    "topic": "greedy",
    "subtopic": "scheduling",
    "difficulty": "easy",
    "buggyCode": "#include <stdlib.h>\n\nstruct Activity {\n    int start, finish;\n};\n\n// Greedy optimal scheduling requires sorting by earliest FINISH time.\nint compare(const void* a, const void* b) {\n    return ((struct Activity*)a)->start - ((struct Activity*)b)->start;\n}\n\nint maxActivities(struct Activity arr[], int n) {\n    qsort(arr, n, sizeof(struct Activity), compare);\n    int count = 1;\n    int lastFinish = arr[0].finish;\n    for (int i = 1; i < n; i++) {\n        if (arr[i].start >= lastFinish) {\n            count++;\n            lastFinish = arr[i].finish;\n        }\n    }\n    return count;\n}",
    "correctCode": "#include <stdlib.h>\n\nstruct Activity {\n    int start, finish;\n};\n\nint compare(const void* a, const void* b) {\n    return ((struct Activity*)a)->finish - ((struct Activity*)b)->finish;\n}\n\nint maxActivities(struct Activity arr[], int n) {\n    if (n == 0) return 0;\n    qsort(arr, n, sizeof(struct Activity), compare);\n    int count = 1;\n    int lastFinish = arr[0].finish;\n    for (int i = 1; i < n; i++) {\n        if (arr[i].start >= lastFinish) {\n            count++;\n            lastFinish = arr[i].finish;\n        }\n    }\n    return count;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Sorts activity list by start times rather than finish times, causing greedy heuristic calculations to fail.",
        "type": "incorrect initialization", 
        "lineRange": "10"
      }
    ],
    "primaryBugType": "incorrect initialization",
    "explanation": "Greedy activity selection works by choosing the activity that finishes first, leaving the maximum room for subsequent tasks. Sorting by start time fails (e.g. an activity starting at 0 and finishing at 100 blocks everything, even if smaller items start at 1 and finish at 2).",
    "intendedApproach": "Sort activities by finish time in the custom comparator.",
    "constraints": ["1 <= n <= 1000", "0 <= start[i] < finish[i] <= 10^5"],
    "visibleTestCases": [
      { "id": 1, "input": "3\n1 2\n3 4\n0 6", "expectedOutput": "2", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "3\n5 9\n1 2\n3 4", "expectedOutput": "3", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n log n)", "space": "O(1)" },
    "tags": ["greedy", "sorting", "math", "c", "easy"]
  },

  # 32. GREEDY - Medium - Java
  {
    "id": "q_greedy_jump",
    "title": "Jump Game Unreachable Index",
    "problemStatement": "You are given an integer array `nums`. You are initially positioned at the array's first index, and each element represents your maximum jump length at that position. Return `true` if you can reach the last index.",
    "language": "java",
    "topic": "greedy",
    "subtopic": "jump-game",
    "difficulty": "medium",
    "buggyCode": "class Solution {\n    public boolean canJump(int[] nums) {\n        int maxReach = 0;\n        for (int i = 0; i < nums.length; i++) {\n            // If maxReach is stuck at 0 but we continue loop, maxReach gets updated on unreachable cells.\n            // E.g. [3, 2, 1, 0, 4] -> at index 4, i=4. maxReach was 3. But we do max(3, 4+4) = 8, returning true.\n            maxReach = Math.max(maxReach, i + nums[i]);\n        }\n        return maxReach >= nums.length - 1;\n    }\n}",
    "correctCode": "class Solution {\n    public boolean canJump(int[] nums) {\n        int maxReach = 0;\n        for (int i = 0; i < nums.length; i++) {\n            if (i > maxReach) return false;\n            maxReach = Math.max(maxReach, i + nums[i]);\n        }\n        return maxReach >= nums.length - 1;\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to exit loop when the current index exceeds the maximum reach limit, allowing unreachable jumps to count.",
        "type": "wrong loop condition",
        "lineRange": "5"
      }
    ],
    "primaryBugType": "wrong loop condition",
    "explanation": "If we get stuck at a zero value where we cannot move forward, any index beyond that point is unreachable. If we continue the loop, we might evaluate a cell that could jump to the end, but we have no way of reaching it. Adding 'if (i > maxReach) return false' halts the loop correctly.",
    "intendedApproach": "Add check to return false if current index 'i' is larger than 'maxReach'.",
    "constraints": ["1 <= nums.length <= 10^4", "0 <= nums[i] <= 10^5"],
    "visibleTestCases": [
      { "id": 1, "input": "2 3 1 1 4", "expectedOutput": "1", "isHidden": False },
      { "id": 2, "input": "3 2 1 0 4", "expectedOutput": "0", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "0", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(1)" },
    "tags": ["greedy", "arrays", "java", "medium"]
  },

  # 33. BACKTRACKING - Medium - C++
  {
    "id": "q_back_sub",
    "title": "Subsets Backtracking POP",
    "problemStatement": "Given an integer array of unique elements, return all possible subsets. Complete the function `subsets`.",
    "language": "cpp",
    "topic": "backtracking",
    "subtopic": "subsets",
    "difficulty": "medium",
    "buggyCode": "#include <vector>\nusing namespace std;\n\nvoid backtrack(vector<int>& nums, int start, vector<int>& path, vector<vector<int>>& res) {\n    res.push_back(path);\n    for (int i = start; i < nums.size(); i++) {\n        path.push_back(nums[i]);\n        backtrack(nums, i + 1, path, res);\n        // Accumulates path endlessly and fails backtracking step.\n    }\n}\n\nvector<vector<int>> subsets(vector<int>& nums) {\n    vector<vector<int>> res;\n    vector<int> path;\n    backtrack(nums, 0, path, res);\n    return res;\n}",
    "correctCode": "#include <vector>\nusing namespace std;\n\nvoid backtrack(vector<int>& nums, int start, vector<int>& path, vector<vector<int>>& res) {\n    res.push_back(path);\n    for (int i = start; i < nums.size(); i++) {\n        path.push_back(nums[i]);\n        backtrack(nums, i + 1, path, res);\n        path.pop_back();\n    }\n}\n\nvector<vector<int>> subsets(vector<int>& nums) {\n    vector<vector<int>> res;\n    vector<int> path;\n    backtrack(nums, 0, path, res);\n    return res;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to pop the last element from path vector before moving to the next candidate, which leaves junk in backtracking states.",
        "type": "incorrect recursion base case", 
        "lineRange": "9-11"
      }
    ],
    "primaryBugType": "incorrect recursion base case",
    "explanation": "Backtracking relies on traversing down a branch and returning the working state back to original. Forgetting path.pop_back() doesn't clear the element, resulting in paths containing all elements aggregated from previous runs.",
    "intendedApproach": "Call path.pop_back() after returning from recursive call to backtrack.",
    "constraints": ["1 <= nums.size() <= 10", "All elements are unique"],
    "visibleTestCases": [
      { "id": 1, "input": "1 2", "expectedOutput": "[] [1] [1,2] [2]", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "0", "expectedOutput": "[] [0]", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n * 2^n)", "space": "O(n)" },
    "tags": ["backtracking", "recursion", "arrays", "cpp", "medium"]
  },

  # 34. BACKTRACKING - Hard - Java
  {
    "id": "q_back_nqueens",
    "title": "N-Queens Conflict Checker",
    "problemStatement": "Place `n` queens on an `n x n` chessboard such that no two queens attack each other. Return the number of distinct solutions.",
    "language": "java",
    "topic": "backtracking",
    "subtopic": "n-queens",
    "difficulty": "hard",
    "buggyCode": "class Solution {\n    private int count = 0;\n\n    private boolean isSafe(int row, int col, int[] queens) {\n        for (int i = 0; i < row; i++) {\n            // Checks only vertical column overlaps, allowing diagonal attacks.\n            if (queens[i] == col) {\n                return false;\n            }\n        }\n        return true;\n    }\n\n    private void solve(int row, int n, int[] queens) {\n        if (row == n) {\n            count++;\n            return;\n        }\n        for (int col = 0; col < n; col++) {\n            if (isSafe(row, col, queens)) {\n                queens[row] = col;\n                solve(row + 1, n, queens);\n            }\n        }\n    }\n\n    public int totalNQueens(int n) {\n        solve(0, n, new int[n]);\n        return count;\n    }\n}",
    "correctCode": "class Solution {\n    private int count = 0;\n\n    private boolean isSafe(int row, int col, int[] queens) {\n        for (int i = 0; i < row; i++) {\n            if (queens[i] == col) {\n                return false;\n            }\n            if (Math.abs(queens[i] - col) == Math.abs(i - row)) {\n                return false;\n            }\n        }\n        return true;\n    }\n\n    private void solve(int row, int n, int[] queens) {\n        if (row == n) {\n            count++;\n            return;\n        }\n        for (int col = 0; col < n; col++) {\n            if (isSafe(row, col, queens)) {\n                queens[row] = col;\n                solve(row + 1, n, queens);\n            }\n        }\n    }\n\n    public int totalNQueens(int n) {\n        solve(0, n, new int[n]);\n        return count;\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "isSafe method checks only column overlaps and ignores diagonal threats between queens.",
        "type": "edge cases",
        "lineRange": "5-11"
      }
    ],
    "primaryBugType": "edge cases",
    "explanation": "Two queens are in conflict if they share column coordinates or fall on the same diagonals. Diagonal collision is defined as Math.abs(queens[i] - col) == Math.abs(i - row). The buggy code only checks for column overlaps.",
    "intendedApproach": "Add checks for row-column differences match to catch diagonal attacks.",
    "constraints": ["1 <= n <= 9"],
    "visibleTestCases": [
      { "id": 1, "input": "4", "expectedOutput": "2", "isHidden": False },
      { "id": 2, "input": "1", "expectedOutput": "1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "3", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n!)", "space": "O(n)" },
    "tags": ["backtracking", "recursion", "java", "hard"]
  },

  # 35. PREFIX SUM - Easy - C
  {
    "id": "q_prefix_range",
    "title": "Range Sum Query 1-Indexed",
    "problemStatement": "Given an integer array `nums`, handle multiple queries of the sum of elements of `nums` between indices `left` and `right` inclusive. Complete the functions `createPrefix` and `sumRange`.",
    "language": "c",
    "topic": "prefix-sum",
    "subtopic": "prefix-range",
    "difficulty": "easy",
    "buggyCode": "#include <stdlib.h>\n\nint* prefixSums;\n\nvoid createPrefix(int* nums, int numsSize) {\n    prefixSums = (int*)malloc((numsSize + 1) * sizeof(int));\n    prefixSums[0] = 0;\n    for (int i = 0; i < numsSize; i++) {\n        prefixSums[i + 1] = prefixSums[i] + nums[i];\n    }\n}\n\nint sumRange(int left, int right) {\n    // Calls prefixSums[right] - prefixSums[left] instead of prefixSums[right + 1] - prefixSums[left].\n    return prefixSums[right] - prefixSums[left];\n}",
    "correctCode": "#include <stdlib.h>\n\nint* prefixSums;\n\nvoid createPrefix(int* nums, int numsSize) {\n    prefixSums = (int*)malloc((numsSize + 1) * sizeof(int));\n    prefixSums[0] = 0;\n    for (int i = 0; i < numsSize; i++) {\n        prefixSums[i + 1] = prefixSums[i] + nums[i];\n    }\n}\n\nint sumRange(int left, int right) {\n    return prefixSums[right + 1] - prefixSums[left];\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Calculates range sum as prefixSums[right] - prefixSums[left], missing the element at index 'right' due to 1-based indexing offsets.",
        "type": "off-by-one",
        "lineRange": "16"
      }
    ],
    "primaryBugType": "off-by-one",
    "explanation": "Because prefixSums uses size n+1 (where index i represents sum up to i-1), the sum of range [left, right] is cumulative sum up to 'right' (stored in prefixSums[right + 1]) minus cumulative sum up to 'left - 1' (stored in prefixSums[left]). The buggy code uses prefixSums[right] which leaves out nums[right].",
    "intendedApproach": "Adjust index offsets to: prefixSums[right + 1] - prefixSums[left].",
    "constraints": ["1 <= numsSize <= 10^4", "0 <= left <= right < numsSize"],
    "visibleTestCases": [
      { "id": 1, "input": "-2 0 3 -5 2 -1\n2 5", "expectedOutput": "-1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "1 2 3\n0 2", "expectedOutput": "6", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(1)", "space": "O(n)" },
    "tags": ["prefix-sum", "arrays", "c", "easy"]
  },

  # 36. PREFIX SUM - Medium - C++
  {
    "id": "q_prefix_divk",
    "title": "Subarray Sums Divisible by K",
    "problemStatement": "Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.",
    "language": "cpp",
    "topic": "prefix-sum",
    "subtopic": "prefix-modulo",
    "difficulty": "medium",
    "buggyCode": "#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nint subarraysDivByK(vector<int>& nums, int k) {\n    unordered_map<int, int> m;\n    m[0] = 1;\n    int sum = 0;\n    int count = 0;\n    for (int num : nums) {\n        sum += num;\n        // sum % k can be negative in C++, making lookup fail for matching positive remainders.\n        int rem = sum % k;\n        if (m.find(rem) != m.end()) {\n            count += m[rem];\n        }\n        m[rem]++;\n    }\n    return count;\n}",
    "correctCode": "#include <vector>\n#include <unordered_map>\nusing namespace std;\n\nint subarraysDivByK(vector<int>& nums, int k) {\n    unordered_map<int, int> m;\n    m[0] = 1;\n    int sum = 0;\n    int count = 0;\n    for (int num : nums) {\n        sum += num;\n        int rem = sum % k;\n        if (rem < 0) rem += k;\n        if (m.find(rem) != m.end()) {\n            count += m[rem];\n        }\n        m[rem]++;\n    }\n    return count;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to normalize negative modulo remainders, resulting in missed division matches in C++ modulo behavior.",
        "type": "edge cases",
        "lineRange": "13-17"
      }
    ],
    "primaryBugType": "edge cases",
    "explanation": "In C++, modulo of negative numbers returns negative remainders (e.g. -2 % 5 = -2). However, in modular arithmetic, remainders -2 and 3 are equivalent. We must add k to negative remainders to map them onto the range [0, k-1].",
    "intendedApproach": "If remainder is negative, add k to normalize: if (rem < 0) rem += k.",
    "constraints": ["1 <= nums.size() <= 3 * 10^4", "-10^4 <= nums[i] <= 10^4", "2 <= k <= 10^4"],
    "visibleTestCases": [
      { "id": 1, "input": "4 5 0 -2 -3 1\n5", "expectedOutput": "7", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "-5\n5", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n)", "space": "O(k)" },
    "tags": ["prefix-sum", "hashing", "math", "cpp", "medium"]
  },

  # 37. GRAPHS - Medium - Java
  {
    "id": "q_graph_bfs",
    "title": "Breadth First Search Redundant Push",
    "problemStatement": "Implement breadth first search (BFS) on an adjacency list. Return the nodes in traversal order.",
    "language": "java",
    "topic": "graphs",
    "subtopic": "bfs",
    "difficulty": "medium",
    "buggyCode": "import java.util.*;\n\nclass Solution {\n    public List<Integer> bfs(int V, List<List<Integer>> adj) {\n        List<Integer> res = new ArrayList<>();\n        boolean[] visited = new boolean[V];\n        Queue<Integer> q = new LinkedList<>();\n        \n        q.add(0);\n        // Causes same nodes to get added to the queue multiple times from different parents, degrading speed and creating memory leaks.\n        while (!q.isEmpty()) {\n            int curr = q.poll();\n            visited[curr] = true;\n            res.add(curr);\n            \n            for (int neighbor : adj.get(curr)) {\n                if (!visited[neighbor]) {\n                    q.add(neighbor);\n                }\n            }\n        }\n        return res;\n    }\n}",
    "correctCode": "import java.util.*;\n\nclass Solution {\n    public List<Integer> bfs(int V, List<List<Integer>> adj) {\n        List<Integer> res = new ArrayList<>();\n        boolean[] visited = new boolean[V];\n        Queue<Integer> q = new LinkedList<>();\n        \n        q.add(0);\n        visited[0] = true;\n        while (!q.isEmpty()) {\n            int curr = q.poll();\n            res.add(curr);\n            \n            for (int neighbor : adj.get(curr)) {\n                if (!visited[neighbor]) {\n                    visited[neighbor] = true;\n                    q.add(neighbor);\n                }\n            }\n        }\n        return res;\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Marks nodes as visited when popped from queue instead of when pushed, leading to redundant entries and exponential queue size growth.",
        "type": "incorrect visited handling",
        "lineRange": "13-20"
      }
    ],
    "primaryBugType": "incorrect visited handling",
    "explanation": "If node A and B both connect to C, and we pop A, we add C to the queue since C is not visited. If we pop B before popping C, we check if C is visited. Since C hasn't been popped yet, visited[C] is still false, so we add C to the queue again! Nodes must be flagged visited immediately upon insertion to queue.",
    "intendedApproach": "Set visited[node] = true immediately when adding a node to the queue.",
    "constraints": ["1 <= V <= 10^4", "0 <= E <= 10^4"],
    "visibleTestCases": [
      { "id": 1, "input": "5\n0 1\n0 2\n1 3\n2 4", "expectedOutput": "0 1 2 3 4", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "1\n", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(V + E)", "space": "O(V)" },
    "tags": ["graphs", "queue", "bfs", "java", "medium"]
  },

  # 38. GRAPHS - Hard - C++
  {
    "id": "q_graph_safe",
    "title": "Eventual Safe States",
    "problemStatement": "A node is a safe node if all possible paths starting from that node lead to a terminal node. Find all safe nodes in a directed graph. Return indices in sorted order.",
    "language": "cpp",
    "topic": "graphs",
    "subtopic": "cycle-detection",
    "difficulty": "hard",
    "buggyCode": "#include <vector>\nusing namespace std;\n\nbool dfs(int u, vector<vector<int>>& graph, vector<int>& state) {\n    if (state[u] > 0) return state[u] == 2;\n    \n    state[u] = 1; \n    for (int v : graph[u]) {\n        // If dfs returns true (safe), it returns false (unsafe) incorrectly because of logical inversion.\n        if (!dfs(v, graph, state)) {\n            return false;\n        }\n    }\n    state[u] = 2;\n    return true;\n}\n\nvector<int> eventualSafeNodes(vector<vector<int>>& graph) {\n    int n = graph.size();\n    vector<int> state(n, 0); \n    vector<int> res;\n    for (int i = 0; i < n; i++) {\n        if (dfs(i, graph, state)) {\n            res.push_back(i);\n        }\n    }\n    return res;\n}",
    "correctCode": "#include <vector>\nusing namespace std;\n\nbool dfs(int u, vector<vector<int>>& graph, vector<int>& state) {\n    if (state[u] > 0) return state[u] == 2;\n    \n    state[u] = 1; \n    for (int v : graph[u]) {\n        if (state[v] == 1) return false; // Cycle detected\n        if (!dfs(v, graph, state)) {\n            return false;\n        }\n    }\n    state[u] = 2;\n    return true;\n}\n\nvector<int> eventualSafeNodes(vector<vector<int>>& graph) {\n    int n = graph.size();\n    vector<int> state(n, 0); \n    vector<int> res;\n    for (int i = 0; i < n; i++) {\n        if (dfs(i, graph, state)) {\n            res.push_back(i);\n        }\n    }\n    return res;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to identify self-loops or cycles when dfs evaluates a neighbor state of 1 (currently visiting).",
        "type": "wrong graph traversal",
        "lineRange": "8-13"
      }
    ],
    "primaryBugType": "wrong graph traversal",
    "explanation": "If a graph has a self-loop (e.g. 0 -> 0), dfs(0) calls dfs(0). Since state[0] = 1, it checks state[u] > 0 on line 5. It returns 'state[0] == 2' which is false. The code returns false, which happens to be correct. However, if neighbor v has state 1 (active in stack), we must explicitly reject it. Otherwise, cyclic components bypass checks.",
    "intendedApproach": "Explicitly identify cycles by checking state[v] == 1 inside loops.",
    "constraints": ["1 <= graph.length <= 10^4", "0 <= graph[i].length <= graph.length"],
    "visibleTestCases": [
      { "id": 1, "input": "1 2\n2 3\n5\n0\n5\n\n\n", "expectedOutput": "2 4 5 6", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "0\n", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(V + E)", "space": "O(V)" },
    "tags": ["graphs", "dfs", "cycle-detection", "cpp", "hard"]
  },

  # 39. 2D DP - Medium - Java
  {
    "id": "q_dp_paths",
    "title": "Unique Paths Grid Bounds",
    "problemStatement": "A robot is located at the top-left corner of a `m x n` grid. The robot can only move either down or right at any point. Find the number of unique paths to the bottom-right corner.",
    "language": "java",
    "topic": "2ddp",
    "subtopic": "grid-paths",
    "difficulty": "medium",
    "buggyCode": "class Solution {\n    public int uniquePaths(int m, int n) {\n        int[][] dp = new int[m][n];\n        // Will overwrite boundary or skip elements if loops are out of alignment.\n        for (int i = 0; i < m; i++) dp[i][0] = 1;\n        for (int j = 0; j < n; j++) dp[0][j] = 1;\n        \n        for (int i = 1; i < m; i++) {\n            for (int j = 1; j < n; j++) {\n                dp[i][j] = dp[i-1][j] + dp[i][j-1];\n            }\n        }\n        return dp[m-1][n-1];\n    }\n}",
    "correctCode": "class Solution {\n    public int uniquePaths(int m, int n) {\n        int[][] dp = new int[m][n];\n        for (int i = 0; i < m; i++) dp[i][0] = 1;\n        for (int j = 1; j < n; j++) dp[0][j] = 1;\n        \n        for (int i = 1; i < m; i++) {\n            for (int j = 1; j < n; j++) {\n                dp[i][j] = dp[i-1][j] + dp[i][j-1];\n            }\n        }\n        return dp[m-1][n-1];\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Initializes row 0 starting at index 0 (dp[0][0] = 1), which is redundant but correct, except the loops can cause bounds anomalies on 1D grid shapes.",
        "type": "incorrect DP state/transition",
        "lineRange": "8"
      }
    ],
    "primaryBugType": "incorrect DP state/transition",
    "explanation": "If m = 1 or n = 1, setting boundaries is fine, but loop boundaries must start at 1 to prevent self-overwrites or redundant operations. For circular or small dimensions, initialization index overrides are common errors.",
    "intendedApproach": "Initialize boundary loops to start at index 1 for columns.",
    "constraints": ["1 <= m, n <= 100"],
    "visibleTestCases": [
      { "id": 1, "input": "3 7", "expectedOutput": "28", "isHidden": False },
      { "id": 2, "input": "3 2", "expectedOutput": "3", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "1 1", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(m * n)", "space": "O(m * n)" },
    "tags": ["2ddp", "matrix", "java", "medium"]
  },

  # 40. 2D DP - Hard - C++
  {
    "id": "q_dp_minpath",
    "title": "Minimum Path Sum DP Cell",
    "problemStatement": "Find the minimum path sum in a grid from top-left to bottom-right.",
    "language": "cpp",
    "topic": "2ddp",
    "subtopic": "grid-paths",
    "difficulty": "hard",
    "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint minPathSum(vector<vector<int>>& grid) {\n    int m = grid.size();\n    int n = grid[0].size();\n    vector<vector<int>> dp(m, vector<int>(n, 0));\n    \n    dp[0][0] = grid[0][0];\n    for (int i = 1; i < m; i++) dp[i][0] = dp[i-1][0] + grid[i][0];\n    for (int j = 1; j < n; j++) dp[0][j] = dp[0][j-1] + grid[0][j];\n    \n    for (int i = 1; i < m; i++) {\n        for (int j = 1; j < n; j++) {\n            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i-1][j-1]);\n        }\n    }\n    return dp[m-1][n-1];\n}",
    "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint minPathSum(vector<vector<int>>& grid) {\n    int m = grid.size();\n    int n = grid[0].size();\n    vector<vector<int>> dp(m, vector<int>(n, 0));\n    \n    dp[0][0] = grid[0][0];\n    for (int i = 1; i < m; i++) dp[i][0] = dp[i-1][0] + grid[i][0];\n    for (int j = 1; j < n; j++) dp[0][j] = dp[0][j-1] + grid[0][j];\n    \n    for (int i = 1; i < m; i++) {\n        for (int j = 1; j < n; j++) {\n            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);\n        }\n    }\n    return dp[m-1][n-1];\n}",
    "bugList": [
      {
        "id": 1,
        "description": "State transition uses diagonal cell dp[i-1][j-1] instead of left cell dp[i][j-1], violating movement constraints.",
        "type": "incorrect DP state/transition",
        "lineRange": "16"
      }
    ],
    "primaryBugType": "incorrect DP state/transition",
    "explanation": "You can only move either down or right. This means you can only reach cell (i, j) from (i-1, j) [downward move] or (i, j-1) [rightward move]. The transition should be min(dp[i-1][j], dp[i][j-1]). The buggy code uses diagonal lookup dp[i-1][j-1].",
    "intendedApproach": "Correct the DP lookup index to use the left cell dp[i][j - 1].",
    "constraints": ["1 <= grid.length <= 200", "0 <= grid[i][j] <= 100"],
    "visibleTestCases": [
      { "id": 1, "input": "1 3 1\n1 5 1\n4 2 1", "expectedOutput": "7", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "1 2\n5 6", "expectedOutput": "12", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(m * n)", "space": "O(m * n)" },
    "tags": ["2ddp", "matrix", "cpp", "hard"]
  },

  # 41. 0/1 KNAPSACK - Medium - C
  {
    "id": "q_knap_01",
    "title": "0/1 Knapsack Space Optimization",
    "problemStatement": "Given weights and values of `n` items, put these items in a knapsack of capacity `W` to get the maximum total value. Complete the function `knapSack`.",
    "language": "c",
    "topic": "knapsack-01",
    "subtopic": "knapsack",
    "difficulty": "medium",
    "buggyCode": "#include <stdlib.h>\n#include <string.h>\n\nint max(int a, int b) { return (a > b) ? a : b; }\n\nint knapSack(int W, int wt[], int val[], int n) {\n    int* dp = (int*)calloc(W + 1, sizeof(int));\n    for (int i = 0; i < n; i++) {\n        // Allows picking the same item multiple times (acting as Unbounded Knapsack instead of 0/1 Knapsack).\n        for (int w = wt[i]; w <= W; w++) {\n            dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);\n        }\n    }\n    int result = dp[W];\n    free(dp);\n    return result;\n}",
    "correctCode": "#include <stdlib.h>\n#include <string.h>\n\nint max(int a, int b) { return (a > b) ? a : b; }\n\nint knapSack(int W, int wt[], int val[], int n) {\n    int* dp = (int*)calloc(W + 1, sizeof(int));\n    for (int i = 0; i < n; i++) {\n        for (int w = W; w >= wt[i]; w--) {\n            dp[w] = max(dp[w], val[i] + dp[w - wt[i]]);\n        }\n    }\n    int result = dp[W];\n    free(dp);\n    return result;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Iterates capacity loop forward from wt[i] to W, which allows picking an item multiple times in 1D array DP space optimization.",
        "type": "wrong knapsack transition",
        "lineRange": "11"
      }
    ],
    "primaryBugType": "wrong knapsack transition",
    "explanation": "When optimizing knapsack space to a 1D array, we must loop backwards from W to wt[i]. If we loop forward, dp[w - wt[i]] contains the state where item i has already been added in the current iteration, leading to multiple item additions. Looing backward ensures we use results from the previous items only.",
    "intendedApproach": "Invert inner loop direction to run backwards from W down to wt[i].",
    "constraints": ["1 <= n <= 1000", "1 <= W <= 1000", "0 <= wt[i], val[i] <= 1000"],
    "visibleTestCases": [
      { "id": 1, "input": "4\n1 2 3\n10 15 40\n6", "expectedOutput": "55", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "3\n10 20 30\n60 100 120\n50", "expectedOutput": "220", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n * W)", "space": "O(W)" },
    "tags": ["knapsack-01", "dynamic-programming", "c", "medium"]
  },

  # 42. 0/1 KNAPSACK - Hard - Java
  {
    "id": "q_knap_partition",
    "title": "Partition Equal Subset Sum",
    "problemStatement": "Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal.",
    "language": "java",
    "topic": "knapsack-01",
    "subtopic": "knapsack-partition",
    "difficulty": "hard",
    "buggyCode": "class Solution {\n    public boolean canPartition(int[] nums) {\n        int sum = 0;\n        for (int num : nums) sum += num;\n        if (sum % 2 != 0) return false;\n        int target = sum / 2;\n        \n        boolean[] dp = new boolean[target + 1];\n        // dp[0] should be true since sum of 0 is always achievable with empty subset.\n        dp[0] = false; \n        \n        for (int num : nums) {\n            for (int j = target; j >= num; j--) {\n                dp[j] = dp[j] || dp[j - num];\n            }\n        }\n        return dp[target];\n    }\n}",
    "correctCode": "class Solution {\n    public boolean canPartition(int[] nums) {\n        int sum = 0;\n        for (int num : nums) sum += num;\n        if (sum % 2 != 0) return false;\n        int target = sum / 2;\n        \n        boolean[] dp = new boolean[target + 1];\n        dp[0] = true;\n        \n        for (int num : nums) {\n            for (int j = target; j >= num; j--) {\n                dp[j] = dp[j] || dp[j - num];\n            }\n        }\n        return dp[target];\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Initializes subset sum base case dp[0] to false instead of true, preventing subsets from matching target sums.",
        "type": "incorrect DP state/transition",
        "lineRange": "11"
      }
    ],
    "primaryBugType": "incorrect DP state/transition",
    "explanation": "dp[j] tracks if a subset sum of j is possible. The base case dp[0] represents achieving a sum of 0, which is always possible by choosing no elements (empty subset). If dp[0] is false, all transitions dp[j] = dp[j] || dp[j - num] fail, resulting in returning false for all targets.",
    "intendedApproach": "Initialize the base case dp[0] = true.",
    "constraints": ["1 <= nums.length <= 200", "1 <= nums[i] <= 100"],
    "visibleTestCases": [
      { "id": 1, "input": "1 5 11 5", "expectedOutput": "1", "isHidden": False },
      { "id": 2, "input": "1 2 3 5", "expectedOutput": "0", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "3 3", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n * target)", "space": "O(target)" },
    "tags": ["knapsack-01", "dynamic-programming", "java", "hard"]
  },

  # 43. UNBOUNDED KNAPSACK - Medium - C++
  {
    "id": "q_knap_coins",
    "title": "Coin Change 2 Combinations",
    "problemStatement": "Given an integer array `coins` and an integer `amount`, return the number of combinations that make up that amount. You have an infinite number of each coin.",
    "language": "cpp",
    "topic": "knapsack-unbounded",
    "subtopic": "coin-change",
    "difficulty": "medium",
    "buggyCode": "#include <vector>\nusing namespace std;\n\nint change(int amount, vector<int>& coins) {\n    vector<int> dp(amount + 1, 0);\n    dp[0] = 1;\n    \n    // Calculates permutations instead of combinations (e.g. counts [1, 2] and [2, 1] separately).\n    for (int i = 1; i <= amount; i++) {\n        for (int coin : coins) {\n            if (i >= coin) {\n                dp[i] += dp[i - coin];\n            }\n        }\n    }\n    return dp[amount];\n}",
    "correctCode": "#include <vector>\nusing namespace std;\n\nint change(int amount, vector<int>& coins) {\n    vector<int> dp(amount + 1, 0);\n    dp[0] = 1;\n    \n    for (int coin : coins) {\n        for (int i = coin; i <= amount; i++) {\n            dp[i] += dp[i - coin];\n        }\n    }\n    return dp[amount];\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Loops nested incorrectly. Iterating amount in outer loop generates coin arrangement permutations rather than unique coin combinations.",
        "type": "wrong knapsack transition",
        "lineRange": "10-16"
      }
    ],
    "primaryBugType": "wrong knapsack transition",
    "explanation": "If amount = 3, coins = [1, 2]. By looping coins on outer block, we process all combinations using 1s first, then add combinations using 2s. This prevents duplicate orderings like {1, 2} and {2, 1}. The buggy code loops amount first, generating permutations.",
    "intendedApproach": "Swap loop nesting to iterate coins in outer loop and amount in inner loop.",
    "constraints": ["1 <= coins.length <= 300", "1 <= coins[i] <= 5000", "0 <= amount <= 5000"],
    "visibleTestCases": [
      { "id": 1, "input": "5\n1 2 5", "expectedOutput": "4", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "3\n2", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(amount * n)", "space": "O(amount)" },
    "tags": ["knapsack-unbounded", "dynamic-programming", "cpp", "medium"]
  },

  # 44. UNBOUNDED KNAPSACK - Hard - Java
  {
    "id": "q_knap_rod",
    "title": "Rod Cutting DP Index",
    "problemStatement": "Given a rod of length `n` and an array of prices that contains prices of all pieces of size smaller than `n`, determine the maximum value obtainable by cutting up the rod and selling the pieces.",
    "language": "java",
    "topic": "knapsack-unbounded",
    "subtopic": "rod-cutting",
    "difficulty": "hard",
    "buggyCode": "class Solution {\n    public int cutRod(int price[], int n) {\n        int[] dp = new int[n + 1];\n        dp[0] = 0;\n        for (int i = 1; i <= n; i++) {\n            int max_val = Integer.MIN_VALUE;\n            for (int j = 0; j < i; j++) {\n                // Subtracts j instead of j + 1 from dp, causing incorrect subproblem lookup.\n                max_val = Math.max(max_val, price[j] + dp[i - j]); \n            }\n            dp[i] = max_val;\n        }\n        return dp[n];\n    }\n}",
    "correctCode": "class Solution {\n    public int cutRod(int price[], int n) {\n        int[] dp = new int[n + 1];\n        dp[0] = 0;\n        for (int i = 1; i <= n; i++) {\n            int max_val = Integer.MIN_VALUE;\n            for (int j = 0; j < i; j++) {\n                max_val = Math.max(max_val, price[j] + dp[i - (j + 1)]);\n            }\n            dp[i] = max_val;\n        }\n        return dp[n];\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Subtracts index j instead of j + 1 when evaluating remaining rod lengths from dp state array.",
        "type": "incorrect DP state/transition",
        "lineRange": "9"
      }
    ],
    "primaryBugType": "incorrect DP state/transition",
    "explanation": "j represents 0-based iteration index. The piece length being cut is j + 1 (since piece price at price[0] corresponds to length 1). The remaining rod length must be i - (j + 1). Subtracting j checks dp[i - j], which represents cutting a piece of size j, matching incorrect prices.",
    "intendedApproach": "Change index subtraction to `dp[i - (j + 1)]`.",
    "constraints": ["1 <= n <= 1000", "1 <= price[i] <= 10^5"],
    "visibleTestCases": [
      { "id": 1, "input": "8\n1 5 8 9 10 17 17 20", "expectedOutput": "22", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "8\n3 5 8 9 10 17 17 20", "expectedOutput": "24", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n^2)", "space": "O(n)" },
    "tags": ["knapsack-unbounded", "dynamic-programming", "java", "hard"]
  },

  # 45. LCS - Medium - C
  {
    "id": "q_lcs_length",
    "title": "Longest Common Subsequence DP Bounds",
    "problemStatement": "Find the length of the longest common subsequence between two strings `text1` and `text2`.",
    "language": "c",
    "topic": "lcs",
    "subtopic": "lcs",
    "difficulty": "medium",
    "buggyCode": "#include <string.h>\n#include <stdlib.h>\n\nint max(int a, int b) { return (a > b) ? a : b; }\n\nint longestCommonSubsequence(char* text1, char* text2) {\n    int m = strlen(text1);\n    int n = strlen(text2);\n    int dp[m + 1][n + 1];\n    \n    // Contains garbage values and corrupts DP transitions.\n    \n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (text1[i - 1] == text2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1] + 1;\n            } else {\n                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[m][n];\n}",
    "correctCode": "#include <string.h>\n#include <stdlib.h>\n\nint max(int a, int b) { return (a > b) ? a : b; }\n\nint longestCommonSubsequence(char* text1, char* text2) {\n    int m = strlen(text1);\n    int n = strlen(text2);\n    int dp[m + 1][n + 1];\n    \n    for (int i = 0; i <= m; i++) dp[i][0] = 0;\n    for (int j = 0; j <= n; j++) dp[0][j] = 0;\n    \n    for (int i = 1; i <= m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (text1[i - 1] == text2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1] + 1;\n            } else {\n                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[m][n];\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Fails to initialize DP array boundaries (first row and first column) to zero, leading to corruption from garbage memory values.",
        "type": "incorrect DP state/transition",
        "lineRange": "10-12"
      }
    ],
    "primaryBugType": "incorrect DP state/transition",
    "explanation": "In C, multidimensional array allocations on stack (like dp[m+1][n+1]) contain garbage values. Since DP starts filling from index 1, cells like dp[1][1] access dp[0][0], dp[0][1], and dp[1][0] which are uninitialized. Initializing them to 0 is required.",
    "intendedApproach": "Explicitly loop to initialize the first row and column of the DP table to zero.",
    "constraints": ["1 <= text1.length, text2.length <= 1000", "s consist of lowercase English characters"],
    "visibleTestCases": [
      { "id": 1, "input": "abcde\nace", "expectedOutput": "3", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "abc\ndef", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(m * n)", "space": "O(m * n)" },
    "tags": ["lcs", "dynamic-programming", "c", "medium"]
  },

  # 46. LCS - Hard - C++
  {
    "id": "q_lcs_pal",
    "title": "Longest Palindromic Subsequence",
    "problemStatement": "Given a string `s`, find the longest palindromic subsequence's length in `s`.",
    "language": "cpp",
    "topic": "lcs",
    "subtopic": "lcs-palindrome",
    "difficulty": "hard",
    "buggyCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint longestPalindromeSubseq(string s) {\n    int n = s.length();\n    vector<vector<int>> dp(n, vector<int>(n, 0));\n    \n    // dp[i][j] requires dp[i+1][j-1] which hasn't been computed yet because i+1 is larger than i. \n    // Computes incorrect lengths or zeroes.\n    for (int i = 0; i < n; i++) {\n        dp[i][i] = 1;\n        for (int j = i + 1; j < n; j++) {\n            if (s[i] == s[j]) {\n                dp[i][j] = dp[i + 1][j - 1] + 2;\n            } else {\n                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[0][n - 1];\n}",
    "correctCode": "#include <string>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint longestPalindromeSubseq(string s) {\n    int n = s.length();\n    vector<vector<int>> dp(n, vector<int>(n, 0));\n    \n    for (int i = n - 1; i >= 0; i--) {\n        dp[i][i] = 1;\n        for (int j = i + 1; j < n; j++) {\n            if (s[i] == s[j]) {\n                dp[i][j] = dp[i + 1][j - 1] + 2;\n            } else {\n                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    return dp[0][n - 1];\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Iterates outer loop i from 0 upwards instead of n-1 downwards, which uses uncalculated DP states from subproblems.",
        "type": "incorrect DP state/transition",
        "lineRange": "13-15"
      }
    ],
    "primaryBugType": "incorrect DP state/transition",
    "explanation": "To solve dp[i][j], we need dp[i+1][j-1] (the inner substring). If outer loop i runs forward (0, 1, 2...), when computing dp[0][2], we access dp[1][1] (which is calculated), but if we needed dp[i+1][j] (e.g. dp[1][2]), it was not yet computed. Looping i backwards ensures subproblems with larger i (shorter substrings) are calculated first.",
    "intendedApproach": "Reverse outer loop to run from n-1 down to 0.",
    "constraints": ["1 <= s.length() <= 1000", "s consists only of lowercase English letters"],
    "visibleTestCases": [
      { "id": 1, "input": "bbbab", "expectedOutput": "4", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "cbbd", "expectedOutput": "2", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n^2)", "space": "O(n^2)" },
    "tags": ["lcs", "dynamic-programming", "cpp", "hard"]
  },

  # 47. LIS - Medium - Java
  {
    "id": "q_lis_length",
    "title": "Longest Increasing Subsequence Base",
    "problemStatement": "Given an integer array `nums`, return the length of the longest strictly increasing subsequence.",
    "language": "java",
    "topic": "lis",
    "subtopic": "lis",
    "difficulty": "medium",
    "buggyCode": "import java.util.Arrays;\n\nclass Solution {\n    public int lengthOfLIS(int[] nums) {\n        if (nums == null || nums.length == 0) return 0;\n        int[] dp = new int[nums.length];\n        // Subsequence of single character has length 1. Defaulting to 0 yields off-by-one errors.\n        \n        int maxLIS = 0;\n        for (int i = 0; i < nums.length; i++) {\n            for (int j = 0; j < i; j++) {\n                if (nums[i] > nums[j]) {\n                    dp[i] = Math.max(dp[i], dp[j] + 1);\n                }\n            }\n            maxLIS = Math.max(maxLIS, dp[i]);\n        }\n        return maxLIS;\n    }\n}",
    "correctCode": "import java.util.Arrays;\n\nclass Solution {\n    public int lengthOfLIS(int[] nums) {\n        if (nums == null || nums.length == 0) return 0;\n        int[] dp = new int[nums.length];\n        Arrays.fill(dp, 1);\n        \n        int maxLIS = 1;\n        for (int i = 0; i < nums.length; i++) {\n            for (int j = 0; j < i; j++) {\n                if (nums[i] > nums[j]) {\n                    dp[i] = Math.max(dp[i], dp[j] + 1);\n                }\n            }\n            maxLIS = Math.max(maxLIS, dp[i]);\n        }\n        return maxLIS;\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Doesn't initialize DP values to 1, causing the sequence length calculations to be off-by-one.",
        "type": "incorrect DP state/transition",
        "lineRange": "6"
      }
    ],
    "primaryBugType": "incorrect DP state/transition",
    "explanation": "Each individual element is a valid increasing subsequence of length 1. If we don't initialize dp[i] = 1, then for an array where no element is greater than another (e.g. [5, 4, 3]), dp remains all 0s, and maxLIS returns 0 instead of 1. Initializing dp to 1 resolves this.",
    "intendedApproach": "Initialize the entire dp array with 1 using Arrays.fill().",
    "constraints": ["1 <= nums.length <= 2500", "-10^4 <= nums[i] <= 10^4"],
    "visibleTestCases": [
      { "id": 1, "input": "10 9 2 5 3 7 101 18", "expectedOutput": "4", "isHidden": False },
      { "id": 2, "input": "7 7 7 7 7", "expectedOutput": "1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "1", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n^2)", "space": "O(n)" },
    "tags": ["lis", "dynamic-programming", "java", "medium"]
  },

  # 48. LIS - Hard - C++
  {
    "id": "q_lis_envelope",
    "title": "Russian Doll Envelopes Sorting",
    "problemStatement": "You are given a 2D array of integers `envelopes` where `envelopes[i] = [wi, hi]` represents the width and height of an envelope. One envelope can fit into another if and only if both the width and height of one envelope are strictly greater than the other. Return the maximum number of envelopes you can Russian doll.",
    "language": "cpp",
    "topic": "lis",
    "subtopic": "lis-sort",
    "difficulty": "hard",
    "buggyCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int maxEnvelopes(vector<vector<int>>& envelopes) {\n        // Allows envelopes with same width to count in LIS height check, violating strict size checks.\n        // Correct sort must sort height in DESCENDING order when widths match.\n        sort(envelopes.begin(), envelopes.end(), [](const vector<int>& a, const vector<int>& b) {\n            if (a[0] == b[0]) return a[1] < b[1]; \n            return a[0] < b[0];\n        });\n        \n        vector<int> dp;\n        for (auto& env : envelopes) {\n            int h = env[1];\n            auto it = lower_bound(dp.begin(), dp.end(), h);\n            if (it == dp.end()) dp.push_back(h);\n            else *it = h;\n        }\n        return dp.size();\n    }\n};",
    "correctCode": "#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int maxEnvelopes(vector<vector<int>>& envelopes) {\n        sort(envelopes.begin(), envelopes.end(), [](const vector<int>& a, const vector<int>& b) {\n            if (a[0] == b[0]) return a[1] > b[1];\n            return a[0] < b[0];\n        });\n        \n        vector<int> dp;\n        for (auto& env : envelopes) {\n            int h = env[1];\n            auto it = lower_bound(dp.begin(), dp.end(), h);\n            if (it == dp.end()) dp.push_back(h);\n            else *it = h;\n        }\n        return dp.size();\n    }\n};",
    "bugList": [
      {
        "id": 1,
        "description": "Sorts duplicate width envelopes in height-ascending order, allowing duplicate width envelopes to incorrectly count towards the nesting count.",
        "type": "wrong loop condition", 
        "lineRange": "12"
      }
    ],
    "primaryBugType": "wrong loop condition",
    "explanation": "If envelopes = [[3, 4], [3, 5]]. If we sort height ascending on tie, we get [[3, 4], [3, 5]]. The LIS height traversal sees heights [4, 5], yielding LIS = 2. But we can't nest [3, 4] inside [3, 5] because width is not strictly greater (3 is not > 3). Sorting height descending gets [[3, 5], [3, 4]]. LIS heights [5, 4] yields LIS = 1, which is correct.",
    "intendedApproach": "Sort height descending on width ties: 'if (a[0] == b[0]) return a[1] > b[1]'.",
    "constraints": ["1 <= envelopes.length <= 10^5", "envelopes[i].length == 2"],
    "visibleTestCases": [
      { "id": 1, "input": "5 4\n6 4\n6 7\n2 3", "expectedOutput": "3", "isHidden": False },
      { "id": 2, "input": "1 1\n1 1\n1 1", "expectedOutput": "1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "3 4\n3 5", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(n log n)", "space": "O(n)" },
    "tags": ["lis", "sorting", "dynamic-programming", "cpp", "hard"]
  },

  # 49. COIN CHANGE - Easy - C
  {
    "id": "q_coins_min",
    "title": "Coin Change Min Coins Overflow",
    "problemStatement": "You are given an integer array `coins` representing coins of different denominations and an integer `amount`. Return the fewest number of coins that you need to make up that amount. If that amount cannot be made up, return -1.",
    "language": "c",
    "topic": "coin-change",
    "subtopic": "coin-change",
    "difficulty": "easy",
    "buggyCode": "#include <stdlib.h>\n#include <string.h>\n\nint coinChange(int* coins, int coinsSize, int amount) {\n    int* dp = (int*)malloc((amount + 1) * sizeof(int));\n    dp[0] = 0;\n    for (int i = 1; i <= amount; i++) {\n        // Adding 1 (dp[i - coin] + 1) will cause integer overflow, wrapping back to negative numbers.\n        dp[i] = 1e9;\n    }\n    \n    for (int i = 1; i <= amount; i++) {\n        for (int j = 0; j < coinsSize; j++) {\n            if (i >= coins[j]) {\n                int sub = dp[i - coins[j]];\n                if (sub != 1e9 && sub + 1 < dp[i]) {\n                    dp[i] = sub + 1;\n                }\n            }\n        }\n    }\n    int result = (dp[amount] == 1e9) ? -1 : dp[amount];\n    free(dp);\n    return result;\n}",
    "correctCode": "#include <stdlib.h>\n#include <string.h>\n\nint coinChange(int* coins, int coinsSize, int amount) {\n    int* dp = (int*)malloc((amount + 1) * sizeof(int));\n    dp[0] = 0;\n    for (int i = 1; i <= amount; i++) {\n        dp[i] = amount + 1;\n    }\n    \n    for (int i = 1; i <= amount; i++) {\n        for (int j = 0; j < coinsSize; j++) {\n            if (i >= coins[j]) {\n                int sub = dp[i - coins[j]];\n                if (sub != amount + 1 && sub + 1 < dp[i]) {\n                    dp[i] = sub + 1;\n                }\n            }\n        }\n    }\n    int result = (dp[amount] == amount + 1) ? -1 : dp[amount];\n    free(dp);\n    return result;\n}",
    "bugList": [
      {
        "id": 1,
        "description": "Initializes DP table with a large magic constant (1e9) which runs the risk of integer overflows when adding offsets.",
        "type": "integer overflow",
        "lineRange": "9"
      }
    ],
    "primaryBugType": "integer overflow",
    "explanation": "If we use a massive placeholder like 1e9 or INT_MAX, expressions like sub + 1 can exceed standard integer bounds (if sub is INT_MAX) or represent risky magic numbers. A safer upper limit is 'amount + 1' since even with a coin of denomination 1, we can at most use 'amount' coins.",
    "intendedApproach": "Initialize the DP table with 'amount + 1' as the upper bound representation.",
    "constraints": ["1 <= coins.length <= 12", "1 <= coins[i] <= 2^31 - 1", "0 <= amount <= 10^4"],
    "visibleTestCases": [
      { "id": 1, "input": "3\n1 2 5\n11", "expectedOutput": "3", "isHidden": False },
      { "id": 2, "input": "1\n2\n3", "expectedOutput": "-1", "isHidden": False }
    ],
    "hiddenTestCases": [
      { "id": 3, "input": "1\n1\n0", "expectedOutput": "0", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(amount * n)", "space": "O(amount)" },
    "tags": ["coin-change", "dynamic-programming", "c", "easy"]
  },

  # 50. MATRIX DP - Hard - Java
  {
    "id": "q_matrix_square",
    "title": "Maximal Square Subproblem",
    "problemStatement": "Given an `m x n` binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.",
    "language": "java",
    "topic": "matrix-dp",
    "subtopic": "maximal-square",
    "difficulty": "hard",
    "buggyCode": "class Solution {\n    public int maximalSquare(char[][] matrix) {\n        if (matrix == null || matrix.length == 0) return 0;\n        int m = matrix.length;\n        int n = matrix[0].length;\n        int[][] dp = new int[m + 1][n + 1];\n        int maxSide = 0;\n        \n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (matrix[i - 1][j - 1] == '1') {\n                    // Fails to check the top-left diagonal cell (dp[i-1][j-1]), resulting in false square declarations.\n                    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;\n                    maxSide = Math.max(maxSide, dp[i][j]);\n                }\n            }\n        }\n        return maxSide * maxSide;\n    }\n}",
    "correctCode": "class Solution {\n    public int maximalSquare(char[][] matrix) {\n        if (matrix == null || matrix.length == 0) return 0;\n        int m = matrix.length;\n        int n = matrix[0].length;\n        int[][] dp = new int[m + 1][n + 1];\n        int maxSide = 0;\n        \n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (matrix[i - 1][j - 1] == '1') {\n                    dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;\n                    maxSide = Math.max(maxSide, dp[i][j]);\n                }\n            }\n        }\n        return maxSide * maxSide;\n    }\n}",
    "bugList": [
      {
        "id": 1,
        "description": "DP transition formula calculates min of left and top neighbors, ignoring the diagonal neighbor and misidentifying non-square dimensions.",
        "type": "incorrect DP state/transition",
        "lineRange": "14"
      }
    ],
    "primaryBugType": "incorrect DP state/transition",
    "explanation": "A square of side len at (i, j) requires squares of side len-1 at the left, top, and top-left diagonal cells. Min of all three is required: Math.min(Math.min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]). Ignoring the diagonal makes a shape like a 2x3 block with ones falsely report as a 3x3 square.",
    "intendedApproach": "Incorporate the diagonal cell dp[i-1][j-1] in the nested Math.min calculation.",
    "constraints": ["m == matrix.length", "n == matrix[i].length", "1 <= m, n <= 300", "matrix[i][j] is '0' or '1'"],
    "visibleTestCases": [
      { "id": 1, "input": "1 0 1 0 0\n1 0 1 1 1\n1 1 1 1 1\n1 0 0 1 0", "expectedOutput": "4" }
    ],
    "hiddenTestCases": [
      { "id": 2, "input": "0 1\n1 0", "expectedOutput": "1", "isHidden": True }
    ],
    "expectedComplexity": { "time": "O(m * n)", "space": "O(m * n)" },
    "tags": ["matrix-dp", "dynamic-programming", "java", "hard"]
  }
]

# Write out the JSON questions database file
with open("questions.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Generated {len(questions)} debugging questions successfully.")
