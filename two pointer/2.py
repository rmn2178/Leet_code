# ==========================================================
# 2. LEETCODE 344: REVERSE STRING
# Description: Reverse an array of characters in-place with O(1) extra memory.
# Approach: Two pointers (Opposite Ends). Swap characters at
# left and right indices, then move inward.
# ==========================================================
class Solution344:
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

# --- CALLING PROBLEM 344 ---
sol2 = Solution344()
char_array = ["h","e","l","l","o"]
sol2.reverseString(char_array)
print(f"344. Reverse String: {char_array}")