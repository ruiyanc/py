

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([25, 10, 29, 1, 8, 7, 13, 56, 23, 49, 20, 4, 6, 70, 29, 35, 6, 50]))
