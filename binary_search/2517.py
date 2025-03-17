
class Solution:
    '''
    K distinct candies
    tastiness is min(abs),
    tastiness - 1 is also tastiness --> monotomy --> bisect guess
    ordered baskedt basktet[i] <= basket[i+1] - tastiness
    '''
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def check(price, k, target):# ordered price
            curr_price = price[0]
            count = 1
            for i in range(1,len(price)):
                if price[i] >= curr_price + target:
                    curr_price = price[i]
                    count +=1
            return count
        left = 0
        # close upper-boundary
        right = (price[-1]-price[0])//(k-1) + 1
        while left<=right:
            #guess tastiness is mid
            mid = left + (right - left)//2
            if check(price, k , mid) >= k:
                left = mid +1
            else:
                right = mid -1
        return right

        
