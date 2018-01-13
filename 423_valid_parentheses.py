class Solution:
    """
    @param: s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack = []
        parentheses = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if c in parentheses:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if c != parentheses[top]:
                    return False
        return len(stack) == 0
