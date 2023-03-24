import itertools

def main():
    weights_price = [(12,4),(2,1),(1,1),(1,2),(4,10)]
    capacity = 15    
    
    max_price = max_weight = float('-inf')
    max_backpack = []
        
    for perms in itertools.permutations(weights_price):
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
    
    print("\nbackpack:",max_backpack,"\nweight:",max_weight,"price:",max_price)
        
if __name__ == "__main__":
    main()
