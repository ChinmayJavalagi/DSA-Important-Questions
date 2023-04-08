def nextSmallerElement(arr,n):
    # Write your code here.
    stack = []
    res = [-1]*n
    stack.append(arr[n-1])
    for i in range(n-2,-1,-1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
            
        if stack:
            res[i] = stack[-1]
            stack.append(arr[i])
            
        else:
            stack.append(arr[i])
    return res
