# ==========================================================
# 4. LEETCODE 26: REMOVE DUPLICATES FROM SORTED ARRAY
# Description: Remove duplicates in-place so each unique element
# appears once. Return the count of unique elements.
# Approach: Two pointers (Same Direction). 'slow' stays at the
# last unique element, 'fast' finds the next unique value.
# ==========================================================
class Solution26:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums: return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

# --- CALLING PROBLEM 26 ---
sol4 = Solution26()
dup_list = [1, 1, 2, 2, 3]
count = sol4.removeDuplicates(dup_list)
print(f"26. Unique Count: {count}, List: {dup_list[:count]}")