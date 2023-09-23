# Given two arrays of integers, compute the pair of values
# (one value in each array) with the smallest (non-negative) difference. Return the difference.
# Example:
# Input: {1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
# Output: 3. That is, the pair (11,8)

arr1 = [1, 3, 15, 11, 2]
arr2 = [23, 127, 235, 19, 8]


def smallestDifQuadratic(arr1,arr2):
    left = 0
    right = len(arr1)
    smallestDif = float("inf")
    memo = {}
    n = len(arr1)

    for i in range(n):
        for j in range(n):
            smallestDif = min(smallestDif, abs(arr1[i] - arr2[j]))
            print("found the pair ({}, {}) with diff {}" .format(arr1[i], arr2[j], abs(arr1[i] - arr2[j])))
    
    return smallestDif

def smallestDif(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    # Considerando que arr2 pode ter um tamanho diferente de arr1
    n = len(arr1)
    m = len(arr2)  

    left = 0
    right = 0

    smallestDif = float('inf')

    while left < n and right < m: 
        curr = abs(arr1[left] - arr2[right])
        smallestDif = min(smallestDif, curr)
        
        if arr1[left] < arr2[right]:
            left += 1
        else:
            right += 1
    
    return smallestDif


def smallestDifHash(arr1, arr2):
    hashTable = set(arr1)
    
    smallestDif = float('inf')
    
    for num in arr2:
        # Verifique os números adjacentes em arr1 para encontrar a menor diferença
        if num in hashTable:
            return 0  
        if num + 1 in hashTable:
            smallestDif = min(smallestDif, 1)
        if num - 1 in hashTable:
            smallestDif = min(smallestDif, 1)
       
    
    return smallestDif


print(smallestDifQuadratic(arr1,arr2))
print(smallestDif(arr1,arr2))


import heapq

def smallestDifHeap(arr1, arr2):
    diffs = [] 
    
    for i in arr1:
        for j in arr2:
            diff = abs(i - j)
            heapq.heappush(diffs, (diff, (i, j)))
    
    smallestDif, (num1, num2) = heapq.heappop(diffs)
    return smallestDif

arr1 = [1, 3, 15, 11, 2]
arr2 = [23, 127, 235, 19, 8]
print(smallestDifHeap(arr1, arr2))  



def binarySearch(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return low

def smallestDifHeapBinarySearch(arr1, arr2):
    arr1.sort()
    diffs = []

    for num in arr2:
        idx = binarySearch(arr1, num)
        
        for i in range(idx-1, idx+2):
            if 0 <= i < len(arr1):
                diff = abs(arr1[i] - num)
                heapq.heappush(diffs, diff)
    
    return heapq.heappop(diffs)

print(smallestDifHeapBinarySearch(arr1, arr2))  



def BinSearch_diff(A, cont, x, old_dif):
    print(cont)
    # mid = (i + j)/2
    dif = x - A[cont]
    print(x, A[cont])
    # Caso da recurssão chegar em, alguma das extremidades
    # if cont == 0 or cont == len(A)
    #     return dif, (x, A[cont])
    
    # Busca um número menor quando a diferença atual é negativa
    if dif < 0:
        return BinSearch_diff(A, cont-1, x, dif)
    elif dif > 0:
        if old_dif < 0:
            # Achou a menor distancia atual positiva  depois de percorrer em ordem decrescente
            return dif, (x, A[cont])
        elif old_dif > 0: 
            if old_dif > dif:
                return BinSearch_diff(A, cont + 1, x, dif)
            if cont == len(A):
                return dif, (x, A[cont])
            
def SmallestDiff(A1, A2):
    A1.sort() #MergeSort
    A2.sort() #MergeSort
    print(A1)
    print(A2)

    res = []
    for a in A1:
        print(a)
        res.append(BinSearch_diff(A2, len(A2)//2, a, old_dif=float('inf')))
    
    return res
    

A1 = [1, 3, 15, 11, 2]
A2 = [23, 127, 235, 19, 8]
print(len(A2))
print(len(A2)//2)
print(A2[len(A2)//2])
res = SmallestDiff(A1, A2)
print(res)