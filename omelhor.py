import math

def printTotalValue(weights_price):
    soma  = 0
    for e in weights_price:
        soma = soma + e[1]
    print (soma)
def main():
    peso = 0
    weights_price =[(23,92), (31,57), (29,49), (44,68), (53,60), (38,43), (63,67), (85,84), (89,87), (82,72)]
    ratio = [0,0,0,0,0,0,0,0,0,0]
    for t in range((len(weights_price))):
        ratio[t] = ((weights_price[t][1])/(weights_price[t][0]))
        peso+=(weights_price[t][0])
#    print(ratio)
#    print(peso)
    capacity = 165
    while(peso > capacity):
        lowest = 1000
        
        for i in range((len(ratio))):
            print (ratio[i])
            if (ratio[i] < lowest):
                #print(ratio[i])
                lowest = ratio[i]
                print (lowest)
        a = ratio.index(lowest)
        #print(a)
        ratio.pop(a)
        weights_price.pop(a)
        peso = 0
        for i in range((len(weights_price))):
            peso = peso + (weights_price[i][0])
    print(weights_price)
    printTotalValue(weights_price)
    
if __name__ == "__main__":
    main()

