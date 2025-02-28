class Solution:
    '''
        volume of bucket = height.min * width
        two pointer: left right
        aim find max volume
        move one pointer each step:
            1. move --> width -1
            2. possible way to enlarge vol: height get bigger
                2.1 change height --> get small height pointer
                2.2 update res
                2.3 till left == right

    '''
    def maxArea(self, height: List[int]) -> int:
        n =  len(height)
        res = 0
        left = 0
        right = n-1
        max_h = max(height)
        while left < right:
            # init?end?
            # init res
            # end: right - left == 1, still update res, then move then break while
            vol = min(height[left], height[right]) * (right - left)
            res = max(res, vol)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            # cut branch: idea: ideal max vol = max.height * width
            if (right-left) * max_h <= res:
                return res

        return res
