class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = False if len(set(nums)) == len(nums) else True

        return duplicate
        
        
