class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        from Queue import Queue
        self.size = size
        self._window = Queue()
        self.sum = 0.0

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        self.sum += val
        if self._window.qsize() == self.size:
            self.sum -= self._window.get()
        self._window.put(val)
        return self.sum / self._window.qsize()


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(3)
# print obj.next(1)
# print obj.next(10)
# print obj.next(3)
# print obj.next(5)

