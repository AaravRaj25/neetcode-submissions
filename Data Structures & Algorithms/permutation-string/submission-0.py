class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        aa = {}
        for i in s1:
            aa[i] = aa.get(i, 0) + 1
        window = {}
        for i in s2[:len(s1)]:
            window[i] = window.get(i, 0) + 1
        if window == aa:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            
            l += 1

            if window == aa:
                return True

        return False


