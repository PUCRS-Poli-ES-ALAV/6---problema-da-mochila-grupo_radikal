import math
import time

def TotalValue(weights_price):
    soma  = 0
    for e in weights_price:
        soma = soma + e[1]
    print (soma)

def TotalWeight(weights_price):
    soma  = 0
    for e in weights_price:
        soma = soma + e[0]
    return soma

def main():
    iterations = 0
    peso = 0
    lowstRemoved = (1000,1)
    weights_price =[(56,50), (59,50), (80,64), (64,46), (75,50), (17,5)]
    ratio = [0,0,0,0,0,0]

    start = time.time()
    for t in range((len(weights_price))):
        ratio[t] = ((weights_price[t][1])/(weights_price[t][0]))
        peso+=(weights_price[t][0])
#    print(ratio)
#    print(peso)
    capacity = 190
    while(peso > capacity):
        lowest = 1000  
        for i in range((len(ratio))):
            #print (ratio[i])
            iterations += 1
            if (ratio[i] < lowest):
                #print(ratio[i])
                lowest = ratio[i]
                #print (lowest)
        a = ratio.index(lowest)
        #print(a)
        if(lowstRemoved[0] > weights_price[a][0]):
            lowstRemoved = weights_price[a]
        ratio.pop(a)
        weights_price.pop(a)
        peso = 0
        for i in range((len(weights_price))):
            iterations += 1
            peso = peso + (weights_price[i][0])

    if(lowstRemoved[0] <= (capacity - TotalWeight(weights_price))):
        weights_price.append(lowstRemoved)

    print(f"Time for case: {time.time() - start} seconds")
    print(f"Iterations: {iterations}")
    print(f"Precos: {weights_price}")
    print(lowstRemoved)
    TotalValue(weights_price)
    print(f"Peso: {TotalWeight(weights_price)}")
    
if __name__ == "__main__":
    main()

