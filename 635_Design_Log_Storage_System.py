from typing import List

class LogSystem:

    def __init__(self):
        self.logs = {}
        self.granIndex = {
            "Year"  : 1,
            "Month" : 2,
            "Day"   : 3,
            "Hour"  : 4,
            "Minute": 5,
            "Second": 6
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs[id] = timestamp
    
    # Given a logID, the split start and stop timestamps, and the index of
    # the index of the timestamp (exclusive) to stop checking return whether the log is in bounds 
    def inBounds(self, logID: int, start: List[str], end: List[str], granStop: int):
        currLog = self.logs[logID].split(':')[:granStop]
        checkStart = checkEnd = True
        
        # Validate if the log is within bounds up until the specified granularity
        for i in range(granStop):
            # Both bounds have been validated
            if(not (checkStart or checkEnd)):
                return True
            
            currLogVal = int(currLog[i])
            startVal = int(start[i])
            endVal = int(end[i])
            
            if(checkStart):
                if(currLogVal < startVal):
                    return False
                # The log is validated as past the start range
                if(currLogVal > startVal):
                    checkStart = False
            if(checkEnd):
                if(currLogVal > endVal):
                    return False
                # The log is validated as before the stop range
                if(currLogVal < endVal):
                    checkEnd = False
            
        return True
        
    # Start and end are inclusive, retrieive the ids of the respctive logs
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        startParsed = start.split(':')
        endParsed = end.split(':')
        granStop = self.granIndex[granularity]
        filteredLogs = []
        
        for logId in self.logs:
            if(self.inBounds(logId, startParsed, endParsed, granStop)):
                filteredLogs.append(logId)
                
        return filteredLogs


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)