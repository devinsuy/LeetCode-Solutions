
def merge_sort_util(a, b):
    merged = []
    p_a = p_b= 0
    
    while p_a < len(a) and p_b < len(b):
        if a[p_a] < b[p_b]:
            merged.append(a[p_a])
            p_a += 1            
        else:
            merged.append(b[p_b])
            p_b += 1

    # B list is empty but A is not
    while p_a < len(a):
        merged.append(a[p_a])
        p_a += 1
    
    # A list is empty but B is not
    while p_b < len(b):
        merged.append(b[p_b])
        p_b += 1

    print(merged)
    return merged
    

def merge_sort(arr, start, end):
    # Base case
    if start >= end:
        return [arr[start]]
    
    # Recurse
    else:
        mid_index = start + int((end - start)/2)    
        # print(mid_index)
        a = merge_sort(arr, start, mid_index)
        b = merge_sort(arr, mid_index+1, end)

        return merge_sort_util(a,b)


input_a = [38, 27, 43, 3, 9, 82, 10]
length = len(input_a) - 1
print(merge_sort(input_a, 0, length))


# (0, 6, 3) 
# (0, 3, 1) (4, 6, 5)
# (