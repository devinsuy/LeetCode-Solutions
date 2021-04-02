from math import sqrt
import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
    
        # Maintain max heap of tuples (-dist, indexOfPoint) 
        distHeap = []
        for i, point in enumerate(points):
            x, y = point
            dist = sqrt(pow(x, 2) + pow(y, 2))
            distTuple = (-dist, i)
            
            # Evict the furthest point from the origin and replace with 
            # current distance iff the distance is closer than the furthest
            if(len(distHeap) >= k):
                
                # All distances are multiplied by -1 for use as max heap
                # the furthest distance will have the most negative distance
                furthestDist = distHeap[0][0]
                if(dist < -furthestDist):
                    heapq.heapreplace(distHeap, distTuple)   
            else:
                heapq.heappush(distHeap, distTuple)
        
        # The tuples of the k largest pointIndexes remain in the heap, build output list
        kClosest = []
        for distTuple in distHeap:
            pointIndex = distTuple[1]
            kClosest.append(points[pointIndex])
        
        return kClosest
            
        