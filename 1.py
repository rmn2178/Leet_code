
"""
Problem 125: Valid Palindrome

Given a string s, return true if it is a palindrome, or false otherwise.
Constraints:
- We must ignore case (convert to lowercase).
- We must ignore non-alphanumeric characters.
- An empty string or string with only spaces is considered a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Problem 125: Valid Palindrome
        """
        # Initialize two pointers at the start and end of the string
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer forward if the character is not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer backward if the character is not alphanumeric
            while right > left and not s[right].isalnum():
                right -= 1

            # Compare the characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward
            left += 1
            right -= 1

        return True

# --- TO CALL THE FUNCTION ---
# 1. Create an instance of the Solution class
sol = Solution()

# 2. Define a test string
test_string = "A man, a plan, a canal: Panama"

# 3. Call the function and store the result
result = sol.isPalindrome(test_string)

# 4. Print the output
print(f"Is it a palindrome? {result}")