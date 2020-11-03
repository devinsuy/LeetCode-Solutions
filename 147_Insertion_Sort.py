# O(n) Space Complexity, we maintain a second sorted_list that will
# at most grow to the size of the original array of length n

# O(n^2) time complexity, we must iterate through each element in the original list O(n)
# and for each of these, we may require up to another O(n) pass to correctly place it
# into its correct position in sorted_list 
def insertion_sort(array):
    sorted_list = []                                      # Initially the sorted list is empty, each iteration will increase it's size by one
    
    for i in range(len(array)):                           # O(n) outer pass, iterate through each element in the given list
        unsorted_num = array[i]
        if not sorted_list:
            sorted_list.append(unsorted_num)              # The sorted list is empty, we can simply add this first element to it
        else:
            insert_made = False 
            for j in range(len(sorted_list)-1, -1, -1):   # Another O(n) inner pass starting from the end of the list
                sorted_num = sorted_list[j]
                if unsorted_num >= sorted_num:            # We are iterating in descending order, place our element in the correct position, shift elements accordingly
                    sorted_list.insert(j+1, unsorted_num)   
                    insert_made = True
                    break

            # We have iterated through the entire list, insert our element at index 0 and shift accordingly
            if not insert_made:
                sorted_list.insert(0, unsorted_num)       # Incurs addition cost + cost of resizing underlying structure/copying

    return sorted_list


input_1 = [4,2,1,3]
input_2 = [-1,5,3,4,0]
input_3 = [1,2,3,-4]
input_4 = [1,2,3,3,-4,-4]
print(insertion_sort(input_4))