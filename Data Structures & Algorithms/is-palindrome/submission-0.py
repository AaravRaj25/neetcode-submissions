class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        l=0
        r=len(s)-1
        ans=True
        while l<r:
            if s[l]==s[r]:
                 ans=True
            else:
                 return False
            l+=1
            r-=1
        return ans
        