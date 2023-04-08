class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mini = float("infinity")
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append(val)
            self.mini = val
        elif val<self.mini:
            self.stack.append((2*val) - self.mini)
            self.mini = val
        else:
            self.stack.append(val)
            
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack: 
            return 
        val = self.stack.pop()
        if val<self.mini:
            self.mini = 2*self.mini - val

    def top(self):
        """
        :rtype: int
        """
        val = self.stack[-1]
        if val<self.mini:
            return self.mini
        return val

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini
