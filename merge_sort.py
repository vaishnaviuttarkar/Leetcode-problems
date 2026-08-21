def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Dividing recursively
    left_hand = merge_sort(left_arr)
    right_hand = merge_sort(right_arr)

    return merge(left_hand,right_hand)

def merge(left,right):
    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i]) 
            i+=1
        else:
            sorted_array.append(right[j]) 
            j+=1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array


unsorted_array = [4, 2, 0, 6, 7, 8, 5]
print(merge_sort(unsorted_array))