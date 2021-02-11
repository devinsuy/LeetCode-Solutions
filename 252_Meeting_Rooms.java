import java.util.Arrays;
class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        // Base case
        if(intervals.length == 0){
            return true;
        }
        
        // Sort intervals by start time
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));
        
        for(int i = 0; i < intervals.length-1; i++){
            if(intervals[i][1] > intervals[i+1][0]){
                return false;
            }
        }
        return true;
    }
}