"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param: l1: top-left coordinate of first rectangle
    @param: r1: bottom-right coordinate of first rectangle
    @param: l2: top-left coordinate of second rectangle
    @param: r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):
        # left or right
        if l1.x > r2.x or r1.x < l2.x:
            return False
        # top or bottom
        if l1.y < r2.y or r1.y > l2.y:
            return False
        return True
