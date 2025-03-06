
def binary_search(nums, target): #find first nums >= target
    # []closed interval
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return left

class Solution:
    '''
        binary search
        find first num > 0
        find last num < 0
    '''
    def maximumCount(self, nums: List[int]) -> int:
        #first index(num >= 0) -->
        #negative count = index -1(to last index) + 1(index starts from 0)
        neg = binary_search(nums,0)
        #first index (nun >= 1)
        #positive count = last index - index + 1 = n -1 -pos + 1 = len-pos
        pos = len(nums) - binary_search(nums, 1)
        print(neg,pos)
        return max(neg,pos)

        
