class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.output:
            return self.output.pop()
        else:
            while self.input:
                self.output.append(self.input.pop())
            return self.output.pop()


    def peek(self):
        """
        :rtype: int
        """
        if self.output:
            return self.output[-1]
        else:
            while self.input:
                self.output.append(self.input.pop())
            return self.output[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.input) == 0 and len(self.output) == 0

