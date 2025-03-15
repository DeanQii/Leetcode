
def ifmake(nums,target):
    gap = 0
    for i in range(len(nums)-1,0,-1):
        gap = max(nums[i]+gap - target,0)
        '''if nums[i]+gap > target:
            gap = nums[i]+gap - target
        else:
            gap = 0'''
    return nums[0]+gap <= target
class Solution:
    '''
    brute force:
    while True
    find max i
    choose i and operate
    if new max > old max break

    it is like a water flow from n-1 to 0
    max is decreasing --> monotomy!
    bisect
    key: if nums max can be mid
    '''
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left = nums[0]
        right = max(nums)
        
        while left<= right:
            # guess res is mid
            mid = left + (right-left)//2
            if not ifmake(nums, mid):
                left = mid+1
            else:
                right = mid-1
        return left
            
            
