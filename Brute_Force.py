import itertools
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

def brute_force(capacity:int, items: tuple[int,int]) -> int:
    global iterations
    max_price = float('-inf')
    
    for perms in itertools.permutations(items):        
        weight = price = 0
        for block in perms:
            iterations += 1
            
            if weight + block[0] > capacity:
                break
            weight += block[0]
            price  += block[1]
                
        if price > max_price:
            max_price = price            
    return max_price

def main():
    global iterations
    for i in cases:
        items, capacity = cases[i]
        iterations = 0
        
        start = time.time()
        max_price = brute_force(capacity, items)
        print(f"\nMax price for case {i}: {max_price}")
        print(f"Time for case {i}: {time.time() - start} seconds")
        print(f"Iterations for case {i}: {iterations}")
        
if __name__ == "__main__":
    main()
