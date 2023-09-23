# . Dizemos que um vetor P[1..m] ocorre em um vetor T[1..n] se P[1..m] = T[s+1,.., s+m]
# para algum s. O valor de um tal s ´e um deslocamento v´alido. Projete um algoritmo
# para encontrar todos os deslocamentos v´alidos em um vetor e analise sua complexidade
# em fun¸c˜ao de m e n.

''' 
    -> T = [1,2,3,4,5,6,7,8,9]
    -> P = [3,4,5]
    -> S = 2
'''

def searchDeslocamento(t, p):
    deslocamentos = []  
    n = len(t)
    m = len(p)
    
    for s in range(n - m + 1):  #  subvetor p tem tamanho m, e o vetor t tem tamanho n.
        if t[s:s + m] == p:  
            deslocamentos.append(s)  
    
    return deslocamentos  


t =[1,2,1,2,3,1,2]
p = [1,2]

result = searchDeslocamento(t, p)
print("Deslocamentos válidos:", result)

# A complexidade deste algoritmo é O( ( n - m + 1 ) * m )
# No pior caso, vai ser O (n * m)