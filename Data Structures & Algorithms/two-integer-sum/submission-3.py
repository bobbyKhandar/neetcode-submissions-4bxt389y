class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining={}
        for i,n in enumerate(nums):
            if target-n in remaining:
                return [remaining.get(target-n),i]
            remaining[n]=i
        return [0,0]