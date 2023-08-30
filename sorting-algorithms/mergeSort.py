def merge(v, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            v[k] = left[i]
            i += 1
        else:
            v[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        v[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        v[k] = right[j]
        j += 1
        k += 1
    
    return v

def mergeSort(v):
    n = len(v)//2
    if n > 0:
        left = v[:n]
        right = v[n:]
        mergeSort(left)
        mergeSort(right)
        merge(v, left, right)
    return v

print(mergeSort([1,3,4,5,1,2,52]))


