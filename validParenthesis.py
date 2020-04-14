class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_d = {'}':'{',']':'[',')':'('}
        if s == "": return True
        if len(s)<2: return False
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                top = stack.pop() if stack else '#' # to handle ccases where no open brackets come first
                if hash_d[c] == top:
                    continue
                else:
                    return False
        return len(stack) == 0
