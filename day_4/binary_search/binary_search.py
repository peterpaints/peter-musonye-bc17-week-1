class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.array = [x for x in range(self.b, (self.a + self.b), self.b) if x]
        self.array = list.__init__(self, [x for x in xrange(self.b, (self.a + self.b), self.b) if x])
        self.length = len(self)
        # this could also work? Saw this on slack:
        # self.append(elem) or self.extend(list(range(b, (a * b) + 1, b)

    def search(self, num):
        result = {}
        result['count'] = 0
        lo = 0
        hi = self.length
        while lo < hi:
            # mid = lo + (hi - lo) // 2
            mid = (lo + hi) // 2
            midval = self[mid]
            result['count'] += 1
            if midval < num:
                lo = mid + 1
            elif midval > num:
                hi = mid
            else:
                result['index'] = mid
                return result
