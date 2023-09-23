# Seja A = {a1 < . . . < an} uma lista ordenada de números reais. A proximidade entre
# ai e aj é definida como |ai − aj|. Dados os inteiros j e k, encontre os k elementos de A
# mais próximos de aj em O(k).

# a = [1,2,3,4,5,6,7]
# j = 2
# k = 4
# a[j] = 3

def searchDistance(a, j, k):
    # a é ordenado
    n = len(a)
    el = []  # Lista para armazenar os k elementos mais próximos

    left = j - 1  # Ponteiro esquerdo inicializado para o elemento à esquerda de a[j]
    right = j + 1  # Ponteiro direito inicializado para o elemento à direita de a[j]

    # Contador para manter o controle do número de elementos mais próximos encontrados
    count = 0

    while count < k:
        left_diff = float('inf') if left < 0 else abs(a[j] - a[left])
        right_diff = float('inf') if right >= n else abs(a[j] - a[right])

        if left_diff <= right_diff:
            el.append(a[left])
            left -= 1
        else:
            el.append(a[right])
            right += 1

        count += 1

    return el


a = [1, 2, 3, 4, 5, 6, 7]
j = 3
k = 5

result = searchDistance(a, j, k)
print("Os {} elementos mais próximos de a[{}] são: {}".format(k, j, result))

