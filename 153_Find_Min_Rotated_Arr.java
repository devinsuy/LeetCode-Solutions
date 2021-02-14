class Solution {
    // INPUT VALUES ARE DISTINCT => Strictly INCREASING
    public int findMinUtil(int[] a, int left, int right){
        // Base case, array is fully sorted
        if(a[left] < a[right]) 
            return a[left];
        
        int mid;
        while(left < right){
            // Check elements adjacent to the mid
            mid = (left + right) / 2;
            if(a[mid] > a[mid+1]) return a[mid+1];
            if(a[mid] < a[mid-1]) return a[mid];
            
            // Left half is sorted ascending, min must be on the right half 
            if(a[left] < a[mid])        
                left = mid+1;
            else                        // Right half is sorted
                right = mid;
        }
        return a[left];
    }
    
    public int findMin(int[] nums) {
        return findMinUtil(nums, 0, nums.length-1);
    }
}