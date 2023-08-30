def quickSort(v):
    if len(v) <= 1:
        return v
    else:
        pivot = v.pop()
    
    left = []
    right = []
    
    for item in v:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    
    return quickSort(left) + [pivot] + quickSort(right)

print(quickSort([1,3,4,5,1,2,52]))