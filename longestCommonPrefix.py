# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        min_length = len(min(strs, key=len))
        len_strs = len(strs)
        # print("\nstrs\t", strs)
        prefix = ""

        if(len_strs == 1): return strs[0]

        for l in range(min_length):
            for i in range(1, len_strs):
                if (strs[0][l] != strs[i][l]):
                    return prefix
                # print("strs[0][l] == strs[",i,"][",l,"]", strs[i][l])
            if(strs[0][l] == strs[-1][l]): prefix += strs[-1][l]
                
        return prefix



test = []
test.append(["flower","flow","flight"])
# test.append(["abca","aba","aaab"])
# test.append(["dog","racecar","car"])
# test.append(["ab", "ac"])
test.append(["ab", "a"])

test.append(["a"])
# test.append(["abca","aba","aaab","ccc"])

for i in test:
    solution = Solution()
    sol = solution.longestCommonPrefix(i)

    print("Output\t", sol)

