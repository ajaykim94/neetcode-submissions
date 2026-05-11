class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_Open = {")" : "(" , "]" : "[" , "}" : "{"}

        for i in s:
            if i in close_Open:
                if stack and stack[-1] == close_Open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False