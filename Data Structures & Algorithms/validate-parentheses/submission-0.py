class Solution:
    def isValid(self, s: str) -> bool:
        aa = {')':'(','}':'{',']':'['}
        stack =[]
        for i in s:
            if i in aa:
                if stack and stack[-1]==aa[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

