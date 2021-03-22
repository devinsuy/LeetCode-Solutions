class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if(not instructions):
            return True
        
        '''
        Notation:
            0 : North
            1 : West
            2 : South
            3 : East
        '''
        direction = 0
        x_pos = y_pos = 0
        
        for instruct in instructions:
            # Advance the robots coordinates
            if(instruct == "G"):
                if(direction == 0): y_pos += 1
                elif(direction == 1): x_pos += 1
                elif(direction == 2): y_pos -= 1
                else: x_pos -= 1
            
            # Update the direction of the robot 
            else:
                if(instruct == "L"):
                    direction = direction - 1 if direction > 0 else 3
                else:
                    direction = direction + 1 if direction < 3 else 0
             
        # Robot's end position is the same as its start
        # or the robot is facting a different direction than it began
        if((x_pos == 0 and y_pos == 0) or direction != 0):
            return True
        else:
            return False