# ==========================================================
# 1. LEETCODE 125: VALID PALINDROME
# Description: Determine if a string is a palindrome, considering
# only alphanumeric characters and ignoring cases.
# Approach: Two pointers (Opposite Ends). Move pointers inward,
# skipping non-alphanumeric chars, and compare values.
# ==========================================================
class Solution125:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if s[l].lower() != s[r].lower(): return False
            l, r = l + 1, r - 1
        return True

# --- CALLING PROBLEM 125 ---
sol1 = Solution125()
print(f"Valid Palindrome: {sol1.isPalindrome('A man, a plan, a canal: Panama')}")