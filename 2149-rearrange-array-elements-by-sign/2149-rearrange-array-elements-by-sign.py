class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        positive,negitive=0,1
        for num in nums:
            if num>=0:
                res[positive]=num
                positive+=2
            else:
                res[negitive]=num
                negitive+=2
            
        return res