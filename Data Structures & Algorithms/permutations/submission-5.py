class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def backtracking(current):
            if len(current)==len(nums):
                res.append(current[:])
                

            for n in nums:
                if n not in current:
                    current.append(n)
                    backtracking(current)
                    current.pop()
        backtracking([])
        return res

      