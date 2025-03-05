
class Solution:
    '''
        each index can be seen as a bucket.
        each bucket vol is decided by left height [:i+1] max and right height[i:]

        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]
        for i in range(n):
            left_max[i] = max(height[:i+1])
            right_max[i] = max(height[i:])
        for i in range(n):
            res = res + min(left_max[i],right_max[i]) - height[i]
        return res
        --> time limite exceeded
        --> max(height[:i+1]) --> max(left_max[i-1],height[i])

        left_max = [0 for _ in range(n)]
        left_max[0] = height[0]
        right_max = [0 for _ in range(n)]
        right_max[-1] = height[-1]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])

        --> left_max, right_max are monotonically increasing
        --> each bucket always pick smaller one in list
        --> list -> variable by two pointers
        --> pointers move oppositely and update smaller one
        left = 0
        left_max = height[0]

        right = n-1
        right_max = height[-1]

        while left<=right: #bucket is each index
            res += min(left_max,right_max)
            if left_max <= right_max:
                left += 1
                if left > n-1:
                    break
                left_max = max(left_max, height[left])
            else:
                right -= 1
                if right < 0:
                    break
                right_max = max(right_max, height[right])
            
        res -= sum(height)

        --> without judge left and right range
        --> calculate first
        --> calculate max res

        left = 0
        left_max = 0

        right = n-1
        right_max = 0

        while left<=right: #bucket is each index
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            res += min(left_max,right_max)

            if left_max <= right_max:
                left += 1
            else:
                right -= 1
        -->  min(left_max,right_max) is unnecessary
        while left<=right: #bucket is each index
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max <= right_max:
                res += left_max
                left += 1
            else:
                res += right_max
                right -= 1
        
        
    '''
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        left = 0
        left_max = 0

        right = n-1
        right_max = 0

        while left<=right: #bucket is each index
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max <= right_max:
                res += left_max
                left += 1
            else:
                res += right_max
                right -= 1

            
        res -= sum(height)
        return res
