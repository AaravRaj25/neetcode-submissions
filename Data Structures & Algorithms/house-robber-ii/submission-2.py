class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if not nums:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp=[0]*(n-1)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n-1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        max1=dp[-1]
        dp1=[0]*(n-1)
        dp1[0]=nums[1]
        dp1[1]=max(nums[1],nums[2])
        for i in range(2,n-1):
            dp1[i]=max(dp1[i-1],dp1[i-2]+nums[i+1])
        max2=dp1[-1]
        return max(max1,max2)






        