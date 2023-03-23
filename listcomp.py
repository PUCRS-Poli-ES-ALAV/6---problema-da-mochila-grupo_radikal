import itertools

def backpack(capacity, weights_price):
    if capacity < 0:
        return

def main():
    weights_price = [(12,4),(2,1),(1,1),(1,2),(4,10)]
    capacity = 15
    
    backpack = []
    weight = price = 0
    for tuple in weights_price:
        backpack = [tuple[0]]
        weight = tuple[0] 
        price = tuple[1]
        
        for perms in itertools.permutations(weights_price):
            print (perms)
            # for perm in perms:
            #     print (perm)
            
            #     if weight + perm[0] > capacity:
            #         break
            #     weight += perm[0]
            #     price += perm[1]
            #     backpack.append(perm[0])
                
            # print ("\nbackpack: ", backpack, "price: ", price)
        

if __name__ == "__main__":
    main()
