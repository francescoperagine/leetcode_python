# https://leetcode.com/problems/roman-to-integer/

class Solution:

    def romanToInt(self, s: str) -> int:
        
        total = 0

        numbers = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        if(len(s) == 1): 
            return numbers[s]

        while (len(s) > 0):
            if(s[0:2] in numbers):
                total += numbers[s[0:2]]
                s = s[2:]
            else:
                total += numbers[s[0]]
                s = s[1:]

        return total

test = []
test.append("III")
test.append("LVIII")
test.append("MCMXCIV")

for i in test:
    solution = Solution()
    sol = solution.romanToInt(i)

    print(sol)

