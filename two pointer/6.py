# ==========================================================
# 349. INTERSECTION OF TWO ARRAYS
# Description: Given two integer arrays nums1 and nums2, return
# an array of their intersection. Each element in the result
# must be unique.
#
# Approach: Two Pointers. Sort both arrays first. Use two pointers
# (i and j) to traverse the arrays. If elements match and aren't
# already in the result, add them. If they don't match, move the
# pointer pointing to the smaller value.
# ==========================================================

class Solution(object):
    def intersection(self, nums1, nums2):
        num1 = set(nums1)
        num2 = set(nums2)
        return list(num1 & num2)


# --- CALLING PROBLEM 349 ---
sol349 = Solution()
print(f"349. Intersection: {sol349.intersection([4, 9, 5], [9, 4, 9, 8, 4])}")