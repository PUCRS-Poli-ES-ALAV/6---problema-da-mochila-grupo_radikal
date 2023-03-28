import itertools
import time

cases = {
    0: ([(12, 4), (2, 1), (1, 1), (1, 2), (4, 10)], 
        15),
    
    1: ([(23,92), (31,57), (29,49), (44,68), (53,60), (38,43), (63,67), (85,84), (89,87), (82,72)], 
        165),
    
    2: ([(56,50), (59,50), (80,64), (64,46), (75,50), (17,5)], 
        190)
}

def brute_force(capacity:int, items: tuple[int,int]) -> int:
    max_price = max_weight = float('-inf')
    max_backpack = []
        
    for perms in itertools.permutations(items):
        backpack = []
        weight = price = 0
        for block in perms:
            if weight + block[0] > capacity:
                break
            
            weight += block[0]
            price += block[1]
            backpack.append(block[0])
                
        if price > max_price:
            max_price = price
            max_backpack = backpack
            max_weight = weight

def main():
    for i in cases:
        items, capacity = cases[i]
        
        start = time.time()
        print(f"\nMax price for case {i}: {brute_force(capacity, items)}")
        print(f"Time for case {i}: {time.time() - start} seconds")
        
if __name__ == "__main__":
    main()
