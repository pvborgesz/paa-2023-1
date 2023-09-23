def quickSort(v):
    if len(v) <= 1: 
        return v
    else:
        pivot = v.pop() # n - 1
    
    left = []
    right = []
    
    for item in v: # n - 1
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    
    return quickSort(left) + [pivot] + quickSort(right) # 2 * n - 1 why 2? because we are calling the function twice




print(quickSort([1,3,4,5,1,2,52]))


'''
    - The complexity of quick sort is O(n log n) in the average case and O(n^2) in the worst case.
    - T(0) = 1
    - T(n) = 2 * n - 1 + T(n/2) + T(n/2) = 2 * n - 1 + 2 * T(n/2)
    - So, the complexity is O(n log n)
'''