# ==========================================================
# 5. LEETCODE 88: MERGE SORTED ARRAY
# Description: Merge two sorted arrays into nums1. nums1 has size m+n.
# Approach: Two pointers (Backwards). Compare elements from
# the end of both arrays to avoid overwriting nums1 data.
# ==========================================================
class Solution88:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# --- CALLING PROBLEM 88 ---
sol5 = Solution88()
n1, n2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
sol5.merge(n1, 3, n2, 3)
print(f"88. Merged Array: {n1}")