class Solution {
    public int trap(int[] height) {
        // Base case
        if (height.length == 0){ return 0; }

        // Keep track of the max height seen at each index
        // from left to right and right to left
        int[] left_max = new int[height.length];
        int[] right_max = new int[height.length];
        
        int l_max, r_max, l_curr, r_curr, r_index;
        l_max = r_max = Integer.MIN_VALUE;
        for(int i = 0; i < height.length; i++){
            r_index = height.length - 1 - i;
            l_curr = height[i];
            r_curr = height[r_index];
            if (l_curr > l_max){ l_max = l_curr; } 
            if (r_curr > r_max){ r_max = r_curr; }
            left_max[i] = l_max;
            right_max[r_index] = r_max;
        }

        // The amount of water at an index is the min
        // of the left and right heights minus displacement 
        int num_water = 0;
        int curr_height = 0;
        for(int i = 0; i < height.length; i++){
            l_curr = left_max[i];
            r_curr = right_max[i];
            curr_height = l_curr < r_curr ? l_curr : r_curr; 

            // There is only water when there is a gap formed below left 
            // and right heights (may also be non 0 height at this index)
            num_water += (curr_height - height[i]);             
        }

        return num_water;      
    }

    public static void main(String[] args){
        // Expected: 6
//        int[] height = new int[] {0,1,0,2,1,0,1,3,2,1,2,1};

        // Expected: 9
        int[] height = new int[] {4,2,0,3,2,5};
        
        Solution s = new Solution();

        System.out.println(s.trap(height));
    }
}