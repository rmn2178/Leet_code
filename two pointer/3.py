# ==========================================================
# 3. LEETCODE 283: MOVE ZEROES
# Description: Move all 0's to the end while maintaining relative order.
# Approach: Two pointers (Same Direction). 'slow' tracks the
# position for non-zeros, 'fast' iterates through.
# ==========================================================
class Solution283:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

# --- CALLING PROBLEM 283 ---
sol3 = Solution283()
zeros_list = [0, 1, 0, 3, 12]
sol3.moveZeroes(zeros_list)
print(f"283. Move Zeroes: {zeros_list}")