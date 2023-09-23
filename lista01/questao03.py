# Seja A[1..n] um vetor que pode conter numeros positivos e negativos.
# Projete um algoritmo com complexidade O(n3) para determinar os indices i e j, com
# i ≤ j, tal que A[i] + . . . + A[j] é maximo. Tente reduzir a complexidade para O(n2) e
# depois para O(n).

def aux(a):
    n = len(a)
    left = 0
    right = n - 1
    biggestSum = 0
    isNeigh = 0

    for i in range(n):
        for j in range(n):
            curr = sum(a[i:j+1])
            if curr > biggestSum:
                biggestSum = curr
                left = i
                right = j

    return biggestSum


a = [1,23,4,5,6,1,2]


def max_subarray_n3(A):
    n = len(A)
    max_sum = float('-inf')
    left_index = 0
    right_index = 0

    for i in range(n):
        for j in range(i, n):
            current_sum = sum(A[i:j+1])
            if current_sum > max_sum:
                max_sum = current_sum
                left_index = i
                right_index = j

    return left_index, right_index, max_sum


print(aux(a))


def kadane(A):
    n = len(A)
    max_sum = float('-inf')
    current_sum = 0
    left_index = 0
    right_index = 0
    temp_left = 0

    for i in range(n):
        current_sum += A[i]
        if current_sum > max_sum:
            max_sum = current_sum
            left_index = temp_left
            right_index = i
        if current_sum < 0:
            current_sum = 0
            temp_left = i + 1

    return left_index, right_index, max_sum

print(kadane(a))