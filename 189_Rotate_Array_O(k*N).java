class Solution {
    public static void rotate(int[] nums, int k){
        int temp;
        int prev;

        // Move each element k times O(k * n)
        for(int i = 0; i < k; i++){
            // Move each element forward by 1 O(n)
            prev = nums[0];
            for(int j = 1; j < nums.length; j++){
                temp = nums[j];
                nums[j] = prev;
                prev = temp;
            }
            nums[0] = prev;  
        }
    }
}