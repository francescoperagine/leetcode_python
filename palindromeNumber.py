import math


def get_number(x, n):
    return x // 10**n % 10

class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        digits = int(math.log10(x))+1
        digit_half = math.floor(digits/2)
        print("digits\t", digits)
        for i in range(digits):
            l = digits - i -1
            left_num = get_number(x, l)
            right_num = get_number(x, i)
            print("i\t", i, "\tdigit_half\t",digit_half, "\tl\t", l, '\tleft num\t',left_num, '\tright_num\t', right_num)
            if left_num != right_num: return False
        return True
    
x = 234

solution = Solution()
sol = solution.isPalindrome(x)

print(sol)
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.