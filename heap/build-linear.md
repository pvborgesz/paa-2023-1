```
Para entender por que o algoritmo é \(O(n)\), podemos analisar o tempo que ele leva para "heapificar" cada nível da árvore. O último nível da árvore tem aproximadamente \( \frac{n}{2} \) elementos, mas não precisamos "heapificar" esses nós porque eles são folhas. O penúltimo nível tem aproximadamente \( \frac{n}{4} \) elementos, e cada operação "heapify-down" leva \(O(1)\) tempo. O nível acima do penúltimo tem \( \frac{n}{8} \) elementos, e cada operação "heapify-down" leva \(O(2)\) tempo, e assim por diante. Portanto, o tempo total é:

\[
\sum_{i=0}^{\log n} \frac{n}{2^{i+1}} \times i = O(n)
\]

Portanto, é possível construir um heap em tempo \(O(n)\) usando o método de "heapificação" de baixo para cima.

```
Para entender por que o algoritmo é \(O(n)\), podemos analisar o tempo que ele leva para "heapificar" cada nível da árvore. O último nível da árvore tem aproximadamente \( \frac{n}{2} \) elementos, mas não precisamos "heapificar" esses nós porque eles são folhas. O penúltimo nível tem aproximadamente \( \frac{n}{4} \) elementos, e cada operação "heapify-down" leva \(O(1)\) tempo. O nível acima do penúltimo tem \( \frac{n}{8} \) elementos, e cada operação "heapify-down" leva \(O(2)\) tempo, e assim por diante. Portanto, o tempo total é:

\[
\sum_{i=0}^{\log n} \frac{n}{2^{i+1}} \times i = O(n)
\]

Portanto, é possível construir um heap em tempo \(O(n)\) usando o método de "heapificação" de baixo para cima.
