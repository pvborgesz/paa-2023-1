<h1>Análise de complexidade</h1>

<h2>Notação Big O</h2>
Representa o Limite Superior. Quando dizemos que um algoritmo é O(f(n)) estamos dizendo que, no pior cenário possível, a complexidade do algoritmo não é pior do que f(n) para uma constante multiplicativa. 
Por exemplo, se um algoritmo tem uma complexidade de O(nˆ2). 
Isso significa que no pior caso o tempo (ou espaço) que ele leva é proporcional ao quadrado do tamanho da entrada.

<h2>Notação Theta Θ</h2>
Essa notação é mais precisa que a notação big O, pois ela representa ambos os limites superior e inferior.

<h2>Notação Omega Ω</h2>
Representa um limite inferior. Quando dizemos que um algoritmo é Ω(f(n)), estamos afirmando que no melhor cenário possível, a complexidade do algoritmo não é melhor do que f(n).Por exemplo, se um algoritmo é 
Ω(n), isso significa que mesmo no melhor cenário, ele ainda leva tempo proporcional a n.


<h1>Lista de Exercícios</h1>
<h2>Questão 2</h2>
primeiro laço -> até n
segundo laço -> até n-1
terceiro laço -> até n-i
O loop mais interno com a variável k vai de 1 até j - i. Para um valor fixo de i, o valor máximo de j - i é n - i. Portanto, este loop será executado no máximo n - i vezes. A soma total de vezes que este loop é executado para todos os ciclos do loop intermediário e do loop externo é uma soma dos primeiros n inteiros menos a soma dos primeiros i inteiros para cada i. Esta soma total é proporcional a n^2.

O número total de operações é, portanto, proporcional a n^2, e a complexidade de pior caso do algoritmo é Θ(n^2). Portanto, a função f(n) tal que T(n) é Θ(f(n)) é f(n) = n^2.

i = 1
j = i + 1 -> 2
k = j - i -> 1

i = 2
j = i + 1 -> 3
k = j - i -> 1

i = 3
j = 4
k = 4 - 3 -> 1

<h2>Questão 2</h2>

Dizemos que um vetor P[1..m] ocorre em um vetor T[1..n] se P[1..m] = T[s+1,..,s+m]

A questão está pedindo um algoritmo para encontrar todas as ocorrências do vetor P[1..m] no vetor T[1..n], ou seja, todos os índices s em T para os quais P[1..m] = T[s+1,..., s+m].

Esse problema pode ser solucionado com o algoritmo de pesquisa de strings de Knuth-Morris-Pratt (KMP), que pode ser facilmente adaptado para trabalhar com vetores. 
O algoritmo funciona da seguinte maneira: 
<!-- 
Crie uma tabela de prefixos-sufixos de P[1..m], que é um vetor de tamanho m que irá armazenar o maior sufixo próprio que também é um prefixo próprio para cada prefixo de P[1..m]. 
O valor da tabela para o índice i é o maior k tal que P[1..k] = P[i-k+1...i] e 0 <= k < i. 
Essa tabela será usada para evitar verificações desnecessárias quando procuramos P[1..m] em T[1..n].
Use a tabela de prefixos-sufixos para pesquisar P[1..m] em T[1..n] de forma eficiente. Comece comparando P[1..m] com T[1..m]. Se houver um descompasso em T[i] para algum i entre 1 e m, use a tabela de prefixos-sufixos para determinar o próximo índice em T a partir do qual você deve começar a comparar novamente. Isso permite que você pule várias comparações que seriam redundantes.

Outra explicação: -->
O algoritmo que estamos usando é chamado de Knuth-Morris-Pratt (KMP). O que ele faz é, basicamente, procurar todas as ocorrências de um vetor P[1..m] dentro de outro vetor T[1..n] de forma mais eficiente do que a busca normal.

A ideia principal é que quando o algoritmo encontra um descompasso entre os vetores P e T, ele utiliza uma tabela pré-computada para determinar onde deve continuar a busca, em vez de começar tudo de novo.

Por exemplo, suponha que você está procurando o vetor P = [1, 2, 3] no vetor T = [1, 2, 4, 1, 2, 3]. 
Se você comparar P e T começando do índice 1, você terá 1=1 e 2=2, mas a terceira comparação será 3≠4.
Em vez de começar a comparar P e T do índice 2, o algoritmo KMP, com a ajuda da tabela pré-computada, sabe que pode pular direto para o índice 4 e continuar a busca a partir daí.

Desta forma, o algoritmo KMP consegue encontrar todas as ocorrências de P em T de forma mais rápida e eficiente.
A complexidade de tempo desse algoritmo é O(n + m), onde n é o tamanho do vetor T e m é o tamanho do vetor P.
Isso ocorre porque ele consegue aproveitar a informação das comparações anteriores para acelerar a busca.

public static void kmpSearch(int[] T, int[] P) {
        int m = P.length;
        int n = T.length;
        int[] lps = new int[m];
        computeLpsArray(P, m, lps);
        
        int i = 0; // Index for T[]
        int j = 0; // Index for P[]
        
        while (i < n) {
            if (P[j] == T[i]) {
                j++;
                i++;
            }
            if (j == m) {
                System.out.println("Pattern found at index " + (i - j));
                j = lps[j - 1];
            } else if (i < n && P[j] != T[i]) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
    }

public static void computeLpsArray(int[] P, int m, int[] lps) {
    int length = 0;
    int i = 1;
    lps[0] = 0;

    while (i < m) {
        if (P[i] == P[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = length;
                i++;
            }
        }
    }
}


<h2>Questão 3</h2>

Vetor A[1..n] de positivos e negativos.
Determinar os índices i e j com i <= j, tal que A[i] + ... + A[j] é maximo. 
Algoritmo com Complexidade O(nˆ3):

- Determinar o maior subarray contínuo.

A = [1,2,3,6,5,6,7,2,4,5,6,7,1,23,2,4]
aux = 0
biggest = 0

i, j

i = 0
j = i + 1

A[i] = 1
A[j] = 2


A[j] > A[i] ? aux++ : aux = 0  after -> i++
aux = 1
biggest = max(biggest, aux)


A[i] = 2
A[j] = 3

A[j] > A[i] ? aux++ : aux = 0  after -> i++
aux = 2
biggest = max(biggest, aux)

A[i] = 3
A[j] = 6

A[j] > A[i] ? aux++ : aux = 0  after -> i++
aux = 3
biggest = max(biggest, aux)

A[i] = 6
A[j] = 5

A[j] > A[i] ? aux++ : aux = 0  after -> i++
aux = 0
biggest = max(biggest, aux)

O código pode ser da seguinte forma:

def kadane(A):
    n = len(A)
    max_sum = float('-inf')
    max_ending_here = 0
    max_i = -1
    max_j = -1
    start = 0
    for i in range(n):
        max_ending_here += A[i]
        if max_ending_here > max_sum:
            max_sum = max_ending_here
            max_i = start
            max_j = i
        if max_ending_here < 0:
            max_ending_here = 0
            start = i + 1
    return max_sum, max_i, max_j

A complexidade dele é 0(n), uma vez que o algoritmo varre o vetor somente uma vez.


Implementação iterativa de um LIS.
def lis(A):
  i = 0
  j = 1
  aux = 1
  biggest = 0

  while j != len(A):
    if A[j] > A[i]:
      i += 1
      aux += 1
    else:
      aux = 1
      i = j
    j += 1
  return biggest


Questão 5:
import heapq

def k_closest_elements(A, j, k):
    aj = A[j-1]  # Indices são baseados em 1 na pergunta
    heap = []

    for ai in A:
        proximity = abs(ai - aj)
        heapq.heappush(heap, (proximity, ai))
        if len(heap) > k:
            heapq.heappop(heap)

    return [item[1] for item in heap]

# Exemplo
A = [1, 3, 5, 7, 9, 11, 13]
j = 3  # Elemento de índice 3 é 5
k = 2  # Queremos encontrar os 2 elementos mais próximos de 5
print(k_closest_elements(A, j, k))  # Output: [3, 7]


Questão 6:

