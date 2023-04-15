from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            dif = target - nums[i]
            nums[i] = ''
            if dif in nums:
                return i, nums.index(dif)

test = dict()
# test[9] = [2,7,11,15]
# test[6] = [3,2,4]
# test[6] = [3,3]
test[0] = [0,4,3,0]

solution = Solution()
sol = solution.twoSum(test[i], i)

print(sol)



