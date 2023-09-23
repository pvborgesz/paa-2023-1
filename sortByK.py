def insertion_sort_based_on_distance(A, x):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        
        # Enquanto j é válido e a distância de A[j] para x é maior que a distância de 'key' para x
        while j >= 0 and abs(A[j] - x) > abs(key - x):
            A[j + 1] = A[j]
            j -= 1
        
        A[j + 1] = key

    return A

def find_closest_subset(A, k, x):
    # Ordena A com base na distância de cada elemento para x
    insertion_sort_based_on_distance(A, x)
    
    # Retorna os primeiros k elementos
    return A[:k]

# Teste
A = [5, 2, 7]
x = 5
k = 2
print(find_closest_subset(A, k, x))  # Deve retornar [5, 7]


def partition(A, low, high, x):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if abs(A[j] - x) < abs(pivot - x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i + 1

def quickSelect(A, low, high, k, x):
    if low == high:
        return A[low]
    
    pivot_index = partition(A, low, high, x)
    
    if k == pivot_index:
        return A[:k]
    elif k < pivot_index:
        return quickSelect(A, low, pivot_index - 1, k, x)
    else:
        return quickSelect(A, pivot_index + 1, high, k, x)

def find_closest_subset(A, k, x):
    return quickSelect(A, 0, len(A) - 1, k, x)

# Teste
A = [5, 2, 7]
x = 5
k = 2
print(find_closest_subset(A, k, x))  # Deve retornar [5, 2] ou [2, 5] ou [5, 7] dependendo da partição
