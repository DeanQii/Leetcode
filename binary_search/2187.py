
class Solution:
    '''
    while time
    trips = sum(time//time[i])
    if trip < totalTrips
    time+=1
    else:
        break

    min time
    all time > time_target fullfill

    bisect

    left = 1
    right = totalTrips*min(time)
    '''
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = totalTrips*min(time)
        while left <= right:
            #guesss min time is mid
            mid = left + (right-left)//2
            trips = sum([mid//t for t in time])
            if trips < totalTrips:
                left = mid+1
            else:
                right = mid -1
        return left
        
