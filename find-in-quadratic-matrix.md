A = 1 2 3 4
    2 3 4 5
    3 4 5 6
    4 5 6 7

i = 0
j = 1

O(n2) -> if A[i,j] == target : return target

O(n) -> 

def findTarget(target, A):
    n = len(A)
    i, j = 0, n - 1  # Começando do canto superior direito
    
    while i < n and j >= 0:
        if A[i][j] == target:
            return True
        
        if A[i][j] < target:
            i += 1  # Mover para baixo
        else:
            j -= 1  # Mover para a esquerda
            
    return False

# Exemplo de uso
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(findTarget(5, A))  # True
print(findTarget(10, A))  # False

    
Análise de Complexidade
No pior caso, você pode ter que mover-se ao longo de uma linha inteira e uma coluna inteira, o que resulta em uma complexidade de tempo de O(n).
A complexidade do espaço é constante O(1), já que você está usando apenas algumas variáveis auxiliares.

Você começa no canto superior direito da matriz.
Em cada passo do algoritmo, você se move para baixo ou para a esquerda.
O número máximo de passos para baixo que você pode dar é n, e o número máximo de passos para a esquerda também é n.
Portanto, o número máximo de passos que você pode dar no total é  n + n = 2n

A análise de Ω descreve o melhor cenário de tempo de execução para um algoritmo, ou seja, o limite inferior do tempo de execução. No caso do algoritmo apresentado para encontrar um elemento em uma matriz monotonicamente ordenada, o melhor cenário acontece quando o elemento que você está procurando está localizado na posição inicial da busca, ou seja, no canto superior direito da matriz.

Neste caso, você encontrará o elemento imediatamente, fazendo apenas uma comparação. Portanto, o melhor cenário de tempo de execução do algoritmo é Ω(1).

Entretanto, quando estamos interessados em classificar um algoritmo usando a notação Θ, estamos dizendo que o algoritmo tem o mesmo comportamento tanto no melhor quanto no pior cenário (até um fator constante). 
Assim, ao afirmar que o algoritmo tem uma complexidade de Θ(n), estamos dizendo que os limites superior e inferior são essencialmente os mesmos (até um fator constante), mesmo que o melhor cenário seja Ω(1).
Isso significa que o algoritmo é linear em relação ao tamanho n da matriz, tanto no melhor quanto no pior caso, até um fator constante.



Mostre como ordenar n inteiros no intervalo [1, n2] em tempo linear O(n).

def counting_sort(arr):
    n = len(arr)
    max_val = n * n  # O valor máximo que um elemento pode ter é n^2
    
    # Inicialize o array de contagem com zeros
    count = [0] * (max_val + 1)
    
    # Passo 1: Conte as ocorrências de cada elemento em arr
    for num in arr:
        count[num] += 1
    
    # Passo 2: Reconstrua o array arr com base no array de contagem
    i = 0  # Índice para arr
    for num in range(1, max_val + 1):
        while count[num] > 0:
            arr[i] = num
            i += 1
            count[num] -= 1

# Teste do algoritmo
arr = [4, 9, 2, 16]
print("Array antes da ordenação:", arr)
counting_sort(arr)
print("Array após a ordenação:", arr)


A = [1,2,3,4,5,6]

B = [2,3,4,5,6,7]

C = []

for i in range(len(n)):
    if (A[i] < B[i]):
        C.append(A[i])
    else:
        C.append(B[i])


As listas 
�
A e 
�
B estão ordenadas, e queremos mesclá-las em uma única lista 
�
C que também deve estar ordenada.

Vamos considerar o pior caso: no pior caso, sempre pegamos o menor elemento disponível entre as listas 
�
A e 
�
B a cada passo. Assim, no pior caso, alternamos entre elementos de 
�
A e 
�
B até que tenhamos percorrido todas as 
�
n posições em ambas as listas.

O pior caso ocorre quando, por exemplo, todos os elementos da lista 
�
A são menores do que todos os elementos da lista 
�
B ou vice-versa. Isso obriga a fazer uma comparação cada vez que um elemento é inserido na lista resultante 
�
C.

Para inserir 
�
1
a 
1
​
  em 
�
C, comparamos 
�
1
a 
1
​
  e 
�
1
b 
1
​
  (1 comparação).
Para inserir 
�
1
b 
1
​
  em 
�
C, comparamos 
�
2
a 
2
​
  e 
�
1
b 
1
​
  (1 comparação).
Para inserir 
�
2
a 
2
​
  em 
�
C, comparamos 
�
2
a 
2
​
  e 
�
2
b 
2
​
  (1 comparação).
...
Continuando dessa forma, cada elemento 
�
�
a 
i
​
  será comparado uma vez com um elemento 
�
�
b 
j
​
  e cada elemento 
�
�
b 
i
​
  será comparado uma vez com um elemento 
�
�
a 
j
​
 .

Temos 
�
n elementos em 
�
A e 
�
n elementos em 
�
B, resultando em 
2
�
2n elementos no total.

Cada um dos 
2
�
2n elementos requer uma comparação para ser colocado na lista 
�
C, exceto pelo último elemento. O último elemento não requer uma comparação porque, após a inserção do penúltimo elemento, ele é o único elemento restante e pode ser colocado em 
�
C sem comparação.

Portanto, o número total de comparações é 
2
�
−
1
2n−1 no pior caso.



Última questão:
```
def searchGate():
    step = 1
    position = 0  # Posição inicial
    while (True):
        for i in range(1, step+1):
            position += 1
            if verifica_porta_na_posicao(position):
                return "Porta encontrada na posição " + str(position)
        
        for i in range(1, step+1):
            position -= 1
            if verifica_porta_na_posicao(position):
                return "Porta encontrada na posição " + str(position)

        step += 1
```