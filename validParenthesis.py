# https://leetcode.com/problems/valid-parenthesesentheses/


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        print("s\t", s)
        count = 0

        for p_curr in s:
            count += 1
            print("Step %s: p_curr %s stack %s \t" % (count, p_curr, stack))
            if stack == []:
                stack.append(p_curr)
                print("Step %s: p_curr %s stack was empty, now is %s \t" % (count, p_curr, stack))
                continue

            p_last = stack[-1]

            # print("Step %s: p_last %s p_curr %s expected parentheses[p_last] %s" % (count, p_last, p_curr, parentheses[p_last]))
            # print("Step %s: p_last %s p_curr %s parentheses[p_last] %s" % (count, p_last, p_curr))

            if(p_last in parentheses.keys() and p_curr == parentheses[p_last]):
                stack.pop()
                print("Step %s: %s == %s\tstack %s\t" % (count, p_curr, parentheses[p_last], stack))
            else:
                stack.append(p_curr)
                print("Step %s: p_curr %s p_last %s\tstack %s\t" % (count, p_curr, p_last, stack))

        if stack != []:
            print("Step %s: stack not empty\t%s" % (count, stack))
            return False
        return True

test = []
test.append("([)]")
test.append("()")
test.append("()[]{}")

test.append("(]")
test.append("{[]}")


for p_curr in test:
    solution = Solution()
    sol = solution.isValid(p_curr)

    print("Output test %s\t%s" % (p_curr, sol))