class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        position=0
        for i in nums:
            if i != val:
                nums[position]=i
                position+=1
         
        return position
         


