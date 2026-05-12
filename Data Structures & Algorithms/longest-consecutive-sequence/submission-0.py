class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       num_set=set(nums)
       longest=0
       for i in nums:
            if i-1 not in num_set:
                count=1
                current=i
                while current+1 in num_set:
                    current+=1
                    count+=1
                longest=max(longest,count)
       return longest
                

