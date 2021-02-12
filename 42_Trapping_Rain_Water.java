class Solution {
    public int trap(int[] height) {
        // Build max height at each index from left to right
        int[] minHeight = new int[height.length];
        int max = 0;
        for(int i = 0; i < height.length; i++){
            if(height[i] > max) max = height[i];
            minHeight[i] = max;
        }
        
        // Update the height at each index to be the minimum of 
        // the max height from left and right vs right to left
        max = 0;
        for(int i = height.length-1; i > -1; i--){
            if(height[i] > max) max = height[i];
            if(max < minHeight[i]) minHeight[i] = max;
        }
        
        // The amount of water at any index is the minimum of the
        // max height from left to right and right to left - displacement
        // height at the given index
        int water = 0;        
        for(int i = 0; i < height.length; i++){
            water += (minHeight[i] - height[i]);
        }
        
        return water;
    }
}