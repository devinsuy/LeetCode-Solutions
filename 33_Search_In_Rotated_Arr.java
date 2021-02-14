class Solution {
    public int getInflection(int[] a, int left, int right){
        if(a[left] < a[right]) return left;
        
        int mid;
        while(left < right){
            mid = (left + right) / 2;
            if(a[mid] > a[mid+1])           // Next element is first to decrease, mid+1 is inflection
                return mid+1;
            if(a[mid] < a[mid-1])           // Element to left and right of mid are both larger
                return mid;
            
            // Determine which half to search next
            if(a[left] < a[mid])
                left = mid+1;
            else
                right = mid;
        }
        return left;
    }
    
    public int searchUtil(int[] a, int target, int l, int r){
        int left, right, mid;
        int inflection = this.getInflection(a, l, r);
        if(a[inflection] == target)                     // Base case
            return inflection;    
        
        // Determine whether to search before or after the inflection
        if(target > a[inflection] && target <= a[r]){ 
            left = inflection;
            right = r;
        } else{
            left = l;
            right = inflection-1;
        }
        
        // Elements within bounds are fully sorted, run binary search
        while(left < right){
            mid = (left + right) / 2;
            if(a[mid] == target) 
                return mid;
            // Determine which half to continue search in
            if(target < a[mid])
                right = mid;
            else
                left = mid+1;
        }
        return a[left] == target ? left : -1;    
    }
    
    public int search(int[] nums, int target) {
        return this.searchUtil(nums, target, 0, nums.length-1);    
    }
}