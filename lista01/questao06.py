'''
Seja S = {a1, . . . , an} um conjunto de n n´umeros naturais distintos e um inteiro x.
Considere o problema P de determinar se existem trˆes n´umeros naturais distintos em
S cuja soma ´e x
'''
def searchDistinct(s, x):
    n = len(s)
    memo = {}  

    # Preencher o dicionário com as somas de pares de números
    for i in range(n):
        for j in range(i+1, n):
            memo[s[i] + s[j]] = (s[i], s[j])

    # Verificar se x - soma existe no conjunto S
    for num in s:
        target = x - num
        if target in memo:
            a, b = memo[target]
            if num != a and num != b:
                return True, (num, a, b)

    return False, ()

s = [1, 4, 45, 6, 10, 8]
x = 22
result, triplet = searchDistinct(s, x)
if result:
    print(f"Triplet found: {triplet}")
else:
    print("No triplet found")
