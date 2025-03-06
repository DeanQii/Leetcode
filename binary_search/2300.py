def binary_search(spell, potions, success):
    left = 0
    right = len(potions) - 1
    while left <= right:
        mid = left + (right - left)//2
        if spell * potions[mid] < success :
            left = mid + 1
        else:
            right = mid - 1
    return left

def binary_search2(potions, success):
    left = 0
    right = len(potions) - 1
    success += 1
    while left <= right:
        mid = left + (right - left)//2
        if potions[mid] < success:
            left = mid + 1
        else:
            right = mid - 1
    return left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        res = []
        success -= 1
        m = len(potions)
        for spell in spells:
            res.append(m - binary_search2(potions, success//spell))
        return res
