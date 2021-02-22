'''
Input: Two lists of intervals of availability, a desired meeting duration
Output: The earliest intersection of the availabilities that is atleast length duration
            - [commonAvail, commAvail+duration]
            - [] if no commonAvail of duration found
            
Constraints:
    - For the same person, no timeslots overlap

Approach:
    - Sort both avails by start time
    - Iterate through the first min(slots1.len, slots2.len) intervals simultaneously
    - If leftInterval overlaps with right interval
        - if the overlap is of atleast length duration
        - Return overlap, 
        - Else advance
        
Overlap:

'''


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # Sort both avails by start time ascending O(L1logL1 + L2logL2)
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        
        # Compare the two availabilities, pointer is only advanced if the
        # last end time is shorter than the end time of the other
        # (since the next interval might still end before the other)
        i = j = 0
        while(i < len(slots1) and j < len(slots2)):         # O(l1 + l2)
            leftAvail = slots1[i]
            rightAvail = slots2[j]
            commonAvail = [max(leftAvail[0], rightAvail[0]), min(leftAvail[1], rightAvail[1])]

            # There is a valid overlapping availability
            if(commonAvail[0] < commonAvail[1]):                        
                if(commonAvail[1] - commonAvail[0] >= duration):            # The overlapping avail is long enough for a meeting
                    return [commonAvail[0], commonAvail[0] + duration]
                
            # Advance the pointer of the availabiltiy that ends sooner
            if(leftAvail[1] < rightAvail[1]):
                i += 1
            else:
                j += 1
         
        # No common availability was found
        return []       