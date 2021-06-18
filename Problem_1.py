"""
Time Complexity : O(N) where N is highest element in the nums array. 
Space Complexity : O(N) where N is highest element in the nums array. 
    
"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        max_ = max(nums)
        earn_ = [0]*(max_+1)
        
        for i in nums:
            earn_[i] += i
        
        skip = 0 
        take = earn_[0] 
        
        for i in range(len(earn_)):
            temp = skip
            skip = max(skip, take)
            take = temp + earn_[i]
            
        return max(skip, take)
        
        
        