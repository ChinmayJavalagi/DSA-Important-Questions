#TC - Amortized O(n) for n calls for "next" method (O(1) amortized inside "next" method)

class StockSpanner(object):

    def __init__(self):
        self.stack = [] # pair: (price, span)

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1

        while self.stack and self.stack[-1][0]<=price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, span])
        return span
