
class Solution:
    '''
        positive int, positive int target
        monotony
        minimal len
        2 pointers:
        for right move
            s+=nums[right]
            while left move
                update res
            (s is smaller than target go back)
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = inf
        s = 0
        n = len(nums)
        left = 0
        # move right --> s is monotomily increasing
        for right, x in enumerate(nums):
            s += x
            # update res by keep s >= target and moving left
            while s >= target:
                res = min(res, right-left+1)
                s -= nums[left]
                left += 1
        # boundary setting
        return res if res < n+1 else 0
