
class Solution:
    '''
    How can we know which machine is optimal?
    Brute-force
    
    for machine in range(k):
        price = [composition[machine][i]*cost[i] for i in range(n)]
    cheap_idx = price.index(min(price))
    count = budget//price[cheap_idx]
    rest = budget - count*price[cheap_idx]
    while True:
        stock = stock - composition[cheap_idx]
    '''
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        res = 0
        for machine in range(k):
            # if answer < current res, the answer is meaningless
            left = res
            # all budget is used to fixing the shortcomings of the bucket/stock
            # close lower upper-boundary
            right = min(stock)+budget//min(cost)
            while left <= right:
                #guess stock and budget money can create mid alloys
                mid = left + (right-left)//2
                rest = budget + sum([min(stock[type_i]- mid * composition[machine][type_i] ,0)*cost[type_i] for type_i in range(n)])
                if rest >= 0:
                    left = mid+1
                else:
                    right = mid-1
            res = max(res,right)
        return res

        
