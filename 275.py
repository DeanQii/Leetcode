
class Solution:
    '''
    h = 0
    for i in range(n):
        h = max(h,min(minC, count))
    return h


    find a sub array
    2 variables: count(citations), min(citation)
    count = n - left
    minC = citations[left]
    h = min(count, minC)
    max h
    logarithmic --> bisect
    left enlarge minC
    right enlarge count

    n = len(citations)
        left = 0
        right = n - 1
        #h = 0
        while left <= right:
            mid = left + (right-left)//2
            #h = max(h, min(n-mid,citations[mid]))
            if citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid -1
        #return h
        return n-left

    '''
    def hIndex(self, citations: List[int]) -> int:
        # guess h
        # bisearch h [0,n-1]
        # max h, cuz h-1 also fullfill H index
        left = 1
        right = len(citations)
        while left <= right:
            mid = left + (right-left)//2
            # guess h is mid --> citation[-mid] >= mid
            # left enlarge h
            if citations[-mid] >= mid:
                left = mid+1
            else:
                right = mid-1
        # left is 1st h that does not fullfill h-index
        return right


