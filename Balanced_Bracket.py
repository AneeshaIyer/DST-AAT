def isBalanced(s):
    stack = []
    b={')':'(',']':'[','}':'{'}
    for char in s:
        if char in b.values():
            stack.append(char)
        elif char in b:
            if stack and stack[-1] == b[char] :
                stack.pop()
            else:
                return "NO"
    return "YES" if not stack else "NO"

n = int(input()) 
for i in range(n):
    s = input() 
    print(isBalanced(s))
