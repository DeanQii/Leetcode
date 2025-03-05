class Solution:
    '''
        a hashmap to save num:frequency
        same as sybarray without repeat
        2 pointers
        for right move
            update hashmap with nums[right]
            while hashmap[nums[right]] > target(not good)
                move left and update hashmap
            update result (first good subarry(possible res))
    '''
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        left = 0
        res = 0
        for right, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                cnt[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
            
