
class Solution:
'''
    1.a + b > c
    2.sorted nums
    3.c is longest, a is shortest
    4.for c in range, a is left, b is right
    5.aim: count(a+b > c)
        5.1 if left + right > c
                all left + right > c
            else:
                left += 1
'''
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        res = 0
        for i in range(2,n):
            left = 0
            right = i-1
            while left < right:
                if nums[left] + nums[right]>nums[i] :
                    # The most imortant one:
                    res = res + right -left
                    right -= 1
                else:
                    left += 1
                
        return res
            
