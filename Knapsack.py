import time

iterations = 0
cases = {
    0: ([(12, 4), (2, 1), (1, 1), (1, 2), (4, 10)], 
        15),
    
    1: ([(23,92), (31,57), (29,49), (44,68), (53,60), (38,43), (63,67), (85,84), (89,87), (82,72)], 
        165),
    
    2: ([(56,50), (59,50), (80,64), (64,46), (75,50), (17,5)], 
        190)
}

def knapsack(N:int, C:int, items: tuple[int,int]) -> int:
    global iterations
    maxTab = [[0 for _ in range(C + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, C + 1):
            iterations += 1
            if items[i][0] <= j:
                maxTab[i][j] = max(maxTab[i - 1][j], 
                                   items[i][1] + 
                                   maxTab[i - 1][j - items[i][0]])
            else:
                maxTab[i][j] = maxTab[i - 1][j]
    
    return maxTab[N][C]

def main():
    global iterations
    
    for i in cases:
        items = [(0, 0)] + cases[i][0]
        capacity = cases[i][1]
        iterations = 0
        
        start = time.time()
        max_price = knapsack(len(items) - 1, capacity, items)
        print(f"\nMax price for case {i}: {max_price}")
        print(f"Time for case {i}: {time.time() - start} seconds")
        print(f"Iterations for case {i}: {iterations}")

if __name__ == "__main__":
    main()
