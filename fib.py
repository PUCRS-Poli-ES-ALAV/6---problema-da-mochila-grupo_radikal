def fibRec(n):
    if n <= 1:
        return n
    else:
        return fibRec(n-1) + fibRec(n-2)
def fibo(n):
    f = []
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def memoized_fibo(f,n):
    i = 0
    for i in range (i,n+1):
        f[i] = -1
    return lookup_fibo(f,n)

def lookup_fibo(f,n):
    if f[n] >= 0:
       return f[n]
    if n <= 1:
        f[n] = n
    else:
        f[n] = lookup_fibo(f,n-1) + lookup_fibo(f,n-2)
    return f[n]

 





def main():
    return




if __name__ == "__main__":
    main()

