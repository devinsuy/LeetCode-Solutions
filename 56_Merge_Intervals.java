import java.util.Arrays;

class Solution {
    public int[][] merge(int[][] intervals) {
        // Base case
        if(intervals.length == 1){
            return intervals;
        }
        // Sort the intervals by ascending start time O(nlogn)
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));
        
        ArrayList<int[]> alOutput = new ArrayList<int[]>();
        int[] curr, next;
        int minStart, maxEnd;
        curr = intervals[0];
        
        // Merge overlapping intervals O(n)
        for(int i = 1; i < intervals.length; i++){
            next = intervals[i];
            // The two intervals overlap, merge their extremes
            if(curr[1] >= next[0]){
                minStart = curr[0] < next[0] ? curr[0] : next[0];
                maxEnd = curr[1] > next[1] ? curr[1] : next[1];
                curr = new int[] {minStart, maxEnd};
            } 
            else{
                alOutput.add(curr);
                curr = next;
            }
        }
        alOutput.add(curr);
        
        // Copy output into primitive 2D int array O(alOutput.size())
        int[][] output = new int[alOutput.size()][2];
        for(int i = 0; i < alOutput.size(); i++){
            output[i] = alOutput.get(i);
        }
        return output;
    }
}