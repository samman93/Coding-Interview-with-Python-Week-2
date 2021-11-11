class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ans1 = -1
        ans2 = -1
        start = 0
        end = len(nums) -1 
        
        def b_sort_left(nums,target,start,end):
            while start + 1 < end:
                mid = (start + end) // 2
                
                if nums[mid] < target:
                    start = mid
                else:
                    end = mid
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            return -1
        
        def b_sort_right(nums,target,start,end):
            while start + 1 < end:
                mid = (start + end) // 2
                
                if nums[mid] > target:
                    end = mid
                else:
                    start = mid
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
            return -1
       
        if len(nums) == 0:
            return [-1,-1]
        else:
            ans1 = b_sort_left(nums,target,start,end)
            if ans1 != -1:
                ans2 = b_sort_right(nums,target,start,end)
            else:
                ans2 = -1
        return [ans1,ans2]
    
            
            
            
        