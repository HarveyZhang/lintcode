class Solution:
    """
    @param: num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        mapping = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6'
        }
        left, right = 0, len(num) - 1
        while left <= right:
            if mapping.get(num[left], None) != num[right]:
                return False
            left += 1
            right -= 1
        return True
