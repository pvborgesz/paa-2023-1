def countingSort(arr):
    aux = [0] * (max(arr) + 1) # create an auxiliary array with the size of the max value of the array

    for i in range(len(arr)):
        aux[arr[i]] += 1
    
    i = 0
    for j in range(len(aux)):
        while aux[j] > 0:
            arr[i] = j
            aux[j] -= 1
            i += 1
    
    return arr