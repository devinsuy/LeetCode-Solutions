# O(n) Time, O(s) additional space
def shift_arr(arr, s):
    temp = [None] * s
    temp_ptr = 0

    # Save the first s elements
    for i in range(s):
        temp[i] = arr[i]
        
    # Shift all elements in the current array forward by s
    for i in range(s, len(arr)):
        arr[i-s] = arr[i]

    # Append the saved elements back in
    for i in range(len(arr) - s, len(arr)):
        arr[i] = temp[temp_ptr]
        temp_ptr += 1
    
    return arr
    

    


a = [1,2,3,4,5,6,7,8,9,10,11,12]

print(shift_arr(a,3))
print(shift_arr(a,9))