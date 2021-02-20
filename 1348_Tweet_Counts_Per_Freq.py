from typing import List
from collections import defaultdict
import bisect

class TweetCounts:

    def __init__(self):
        self.deltas = {
            "minute"    : 60,
            "hour"      : 3600,
            "day"       : 86400
        }
        # Maps tweets to a list of the recorded times
        self.tweets = defaultdict(list)
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        # Use bisect to maintain times in sorted ascending O(logn) insert
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:        
        tweetTimes = self.tweets[tweetName]

        # Determine the intervals
        delta = self.deltas[freq]
        start = startTime
        end = min(startTime + delta*(1), endTime+1)
        intervals = []
        
        i = 1
        while(start < end):
            intervals.append((start, end))
            start = startTime + delta*i
            end = min(startTime + delta*(i+1), endTime+1)
            i += 1
        if(len(tweetTimes) == 0):
            return [0] * len(intervals)
        
        # Build the frequency output list
        frequency = []
        for interval in intervals:
            start, end = interval
            start = start-1                                             # Start bound is inclusive
            numTweets = 0   
            low = 0
            
            # Search for values in sorted list using bisect O(k * logn) where k= # of valid values in interval
            while(True):
                currIndex = bisect.bisect_left(tweetTimes, start, low)
                # Exit if no value >= start was found or no value < end
                if(currIndex == len(tweetTimes) or tweetTimes[currIndex] >= end): 
                    break
                # Next pass should search only after this index
                low = currIndex+1
                numTweets += 1         
            frequency.append(numTweets)
            
        return frequency
        
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)