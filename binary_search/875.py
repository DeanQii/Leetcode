
import math
class Solution:
    '''
    min K
    max K is max(piles)
    each pile takes math.ceil(pile[i]/k) h
    for K in range(1,max)
    if sum(time)<= h

    bisect
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            #guess k is mid
            mid = left + (right-left)//2
            time = sum([math.ceil(pile/mid) for pile in piles])
            if time > h:
                left = mid+1
            else:
                right = mid-1
        return left

