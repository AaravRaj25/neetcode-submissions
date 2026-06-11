class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitToChar = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(i, current):
            # base case: used all digits → save combination
            if i == len(digits):
                res.append("".join(current))
                return

            # try every letter mapped to digits[i]
            for ch in digitToChar[digits[i]]:
                current.append(ch)       # choose
                backtrack(i + 1, current) # explore next digit
                current.pop()             # unchoose

        backtrack(0, [])
        return res