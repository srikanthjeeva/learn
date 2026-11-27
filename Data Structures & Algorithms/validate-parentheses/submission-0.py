class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {"}": "{", "]": "[", ")": "("}
        for item in s:
            if item in parentheses_map:
                if stack and stack[-1] == parentheses_map[item]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(item)
            
        return not stack