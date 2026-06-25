class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxar=0
        l=0
        r=len(height)-1
        while l<r:
            dist=r-l
            minarea=min(height[l],height[r])
            area=minarea*dist
            if area>maxar:
                maxar=area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxar