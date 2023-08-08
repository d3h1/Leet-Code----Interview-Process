class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Since we are finding area of most water, we need to init a res which will be the max area 
        res = 0
        
        # Declare your pointers because we have to from left to right to understand 
        l, r = 0, len(height - 1)
        
        while l < r:
            area = min(height[r], height[l]) * (r - l)
            res = max(res, area)
            
            if height[r] > height[l]:
                l += 1
            
            elif height[r] <= height[l]:
                r -= 1
            
            
        return res