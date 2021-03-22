class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Edge case, every square in the grid has a cut
        if(len(horizontalCuts) == h and len(verticalCuts) == w):
            return 1
        
        # O(nlogn) where n = max(len(horizontalCuts), len(vertivalCuts))
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Initialize the window as distance from 0 to the first cut
        maxHorizWindow = prevHorizCut = horizontalCuts[0]
        maxVertWindow = prevVertCut = verticalCuts[0]
        
        # Calculate the window between each cut, determine the max windows
        for i in range(1, len(horizontalCuts)):
            currHorizCut = horizontalCuts[i]
            currHorizWindow = currHorizCut - prevHorizCut
            maxHorizWindow = max(maxHorizWindow, currHorizWindow)
            prevHorizCut = currHorizCut
            
        # Also consider the last window from the last cut to the end of the dimension
        maxHorizWindow = max(maxHorizWindow, h - horizontalCuts[-1])
        
        for i in range(1, len(verticalCuts)):
            currVertCut = verticalCuts[i]
            currVertWindow = currVertCut - prevVertCut
            maxVertWindow = max(maxVertWindow, currVertWindow)
            prevVertCut = currVertCut
          
        # Last window
        maxVertWindow = max(maxVertWindow, w - verticalCuts[-1])

        # Max square is the product of the two windows
        return (maxHorizWindow * maxVertWindow) % (pow(10,9) + 7)
        