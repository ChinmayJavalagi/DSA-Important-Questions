class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        flag = 0
        if len(s) == 1 and (s == '}' or s == ']' or s == ')'):
            return False
        for char in s:
            if char == '(' or char == '{' or char == '[':
                arr.append(char)
            else:
                if arr and ((char ==  ']' and arr[-1] == '[') or (char ==  '}' and arr[-1] == '{')or (char ==  ')' and arr[-1] == '(')):
                    arr.pop()

                else:
                    return False
        return True if not arr else False
