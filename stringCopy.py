import time
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
    
    s = "casablanca"
    t = "portentoso"
    
    start = time.time()
    menor = ED(s, t, len(s)-1, len(t)-1)
    print("Menor : ", menor)
    print("Iteracoes: ", iteracoes)
    print(f"Time for case ED1: {time.time() - start} seconds")
    
    iteracoes = 0
    start = time.time()
    menor = EDProgDin(s, t)
    print("Menor : ", menor)
    print("Iteracoes: ", iteracoes)
    print(f"Time for case EDPD: {time.time() - start} seconds")
    
    s = "Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to " + \
				"simplify the build processes in the Jakarta Turbine project. There were several" + \
				" projects, each with their own Ant build files, that were all slightly different." + \
				"JARs were checked into CVS. We wanted a standard way to build the projects, a clear "+ \
				"definition of what the project consisted of, an easy way to publish project information" + \
				"and a way to share JARs across several projects. The result is a tool that can now be" + \
				"used for building and managing any Java-based project. We hope that we have created " + \
				"something that will make the day-to-day work of Java developers easier and generally help " + \
				"with the comprehension of any Java-based project."
    t = "This post is not about deep learning. But it could be might as well. This is the power of " + \
				"kernels. They are universally applicable in any machine learning algorithm. Why you might" + \
				"ask? I am going to try to answer this question in this article." + \
			        "Go to the profile of Marin Vlastelica Pogančić" + \
			        "Marin Vlastelica Pogančić Jun"
           
    start = time.time()
    menor = EDProgDin(s, t)
    print("Menor : ", menor)
    print("Iteracoes: ", iteracoes)
    print(f"Time for case ED2: {time.time() - start} seconds")

if __name__ == "__main__":
    main()

