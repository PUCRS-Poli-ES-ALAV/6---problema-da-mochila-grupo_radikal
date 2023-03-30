menor = 100000
iteracoes = 0

def ED(s, t, i, j):
    global menor1, iteracoes
   
    iteracoes += 1
    if (i < 0 ):
        return j+1
    if (j < 0 ):
        return i+1
    if s[i] == t[j]:
        return ED(s, t, i -1, j -1)
    else:

        aux1 = (ED(s, t, i -1, j -1)) + 1
      
        aux2 = (ED(s, t, i -1, j)) + 1
       
        aux3 = (ED(s, t, i, j -1)) + 1
      
        menor = min(aux1, aux2, aux3)
        return menor
     
custoExtra = 0
def EDProgDin(s,t):
    global menor, iteracoes
    m = len(s)
    n = len(t)
    matriz = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m):
        #iteracoes += 1
        matriz[i][0] = matriz[i-1][0] + 1
    for j in range(n):
        #iteracoes += 1
        matriz[0][j] = matriz[0][j-1] + 1
    for i in range(1, m):
        for j in range(1, n):
            iteracoes += 1
            if s[i] == t[j]:
                custoExtra = 0
            else:
                custoExtra = 1
            matriz[i][j] = min(matriz[i-1][j] + 1, matriz[i][j-1] + 1, matriz[i-1][j-1] + custoExtra)
    return matriz[m-1][n-1]






def main():
    global menor, iteracoes
    
    s = "casamentoss"
    t = "paisagemfa"
    
    menor = ED(s, t, len(s)-1, len(t)-1)
    print("Menor : ", menor)
    print("Iteracoes: ", iteracoes)
    iteracoes = 0
    menor = EDProgDin(s, t)
    print("Menor : ", menor)
    print("Iteracoes: ", iteracoes)

    


if __name__ == "__main__":
    main()

