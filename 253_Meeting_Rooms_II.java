import java.util.Arrays;
import java.util.PriorityQueue;
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        // Base case
        if(intervals.length == 1){
            return 1;
        }
        
        // Sort intervals by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        int numRooms = 0;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        
        for(int[] interval : intervals){
            // There is a room that will become available before the current interval starts
            if(minHeap.size() > 0 && minHeap.peek() <= interval[0]){
                minHeap.poll();
            } 
            // Otherwise a new room must be allocated
            else{
                numRooms += 1;
            }
            
            // Add the end time of the current interval to the min heap
            // another interval may be able to use this room once finished
            minHeap.add(interval[1]);
        }
        
        return numRooms;
    }
}