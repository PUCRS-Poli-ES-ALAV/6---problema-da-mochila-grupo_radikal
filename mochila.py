import itertools

def backpack(capacity, weights_price, value=0, cache = {}, weights_used = []):

    #if (capacity,value) in cache:
    #    return cache[(weights_used,value)]
    if (capacity <= 0):
        print("hi2")
        cache [(weights_used,value)] = value
        return value
    else:
        
        for w in weights_price:
            if capacity >= w[0]:
                print ("hi")
                backpack(capacity - w[0], weights_price.pop(0),value + w[1],weights_used.append(w[0]))

            


      


def main():
 
    weights_price = [(12,4),(2,1),(1,1),(1,2),(4,10)]

    capacity = 15
    print(backpack(capacity, weights_price))

if __name__ == "__main__":
    main()
