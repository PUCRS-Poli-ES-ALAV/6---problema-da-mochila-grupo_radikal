import sys
import time
iterations = 0
cases = [4,8,16,32,128,1000,10000]

def fibRec(n):
    global iterations
    iterations = iterations + 1
    if n <= 1:
        return n
    else:
        return fibRec(n-1) + fibRec(n-2)
    
def fibo(n):
    global iterations
    f = [0 for i in range(n+1)]
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        iterations = iterations + 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

def memoized_fibo(f,n):
    for i in range (0,n+1):
        f[i] = -1
    return lookup_fibo(f,n)

def lookup_fibo(f,n):
    global iterations
    iterations += 1
    
    if f[n] >= 0:
       return f[n]
    if n <= 1:
        f[n] = n
    else:
        f[n] = lookup_fibo(f,n-1) + lookup_fibo(f,n-2)
    return f[n]

def main():
    global iterations
    sys.setrecursionlimit(10000000)
    
    for alg in range (1,4):
        for idx in range(len(cases)):
            iterations = 0
            start = time.time()
            
            if (alg == 1 and idx < 4):
                print("\n\nRecursive")
                res = fibRec(cases[idx])
            
            elif (alg == 2):
                print("\n\nIterative")
                res = fibo(cases[idx])
                
            elif (alg == 3):
                print("\n\nMemoized")
                res = memoized_fibo([0]*(cases[idx]+1),cases[idx])
            
            if (alg != 1 or idx < 4):
                print(f"\nCase: {cases[idx]}")
                print(f"Time for case: {time.time() - start} seconds")
                print(f"Iterations: {iterations}")
                print(f"Result: {res}")
      
if __name__ == "__main__":
    main()
