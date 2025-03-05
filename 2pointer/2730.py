
class Solution:
    '''
        find a substring
        sliding window --> 2 pointers
        only one adjacent pair of the same digit: one pointer ad s[ad] == a[ad-1] is True
        for right move from 1
            if adj same:
                if ad1
                    move left to ad
                else ad = right #init
            
            update res
    '''
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        ad= -1
        n = len(s)
        res = 1
        for right in range(1,n):
            if s[right-1] == s[right]:
                if ad != -1:
                    left = ad
                    ad = right
                else:
                    ad = right
            res = max(res, right-left+1)
        return res
            
