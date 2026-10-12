class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if char == "[" or char == "{" or char == "(":
                stk.append(char)
            else:
                if not stk:
                    return False 
                top = stk.pop()
                if char == ")" and top != "(":
                    return False
                if char == "]" and top != "[":
                    return False
                if char == "}" and top != "{":
                    return False
        return len(stk) == 0
            
            
            
                