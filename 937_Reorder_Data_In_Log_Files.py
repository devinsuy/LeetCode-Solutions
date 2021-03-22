class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLogs = []
        letterLogs = []
        
        # A log is a digit-log if any section of the log contains a digit
        # letter-logs consist ONLY of lowercase letters
        def containsDigit(firstWord: str) -> bool:
            for char in firstWord:
                if(char.isdigit()):
                    return True
            return False
        
        # Seperate logs as either a digit or letter log
        for log in logs:
            currLog = log.split(" ")
            if(containsDigit(currLog[1])):
                digitLogs.append(currLog)
            else:
                letterLogs.append(currLog)
        
        # Sort the letter logs lexicographically first by contents, then by identifiers if necessary
        letterLogs.sort(key = lambda x : (x[1:], x[0]))
        
        # Rebuild the output logs in the correct order
        finalLogs = []
        for i in range(len(letterLogs)):
            finalLogs.append(" ".join(letterLogs[i]))
        for i in range(len(digitLogs)):
            finalLogs.append(" ".join(digitLogs[i]))
        
        return finalLogs