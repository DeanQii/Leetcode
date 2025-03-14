
class Solution:
    # bisect()
    # j [1,n)
    # lower-nums[j]<= nums[i] <= upper-nums[j]
    # find idx : 2 bisect()
    # l and r
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        count = 0
        n = len(nums)
        nums.sort()
        for j in range(1,n):
            l = bisect_left(nums, lower-nums[j],0,j)
            r = bisect_right(nums, upper-nums[j],0,j)
            count += r-l
        return count

        
