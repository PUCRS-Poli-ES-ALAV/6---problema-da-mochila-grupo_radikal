def main():
    peso = 0
    weights_price =[(12,4),(2,1),(1,1),(1,2),(4,10)]
    ratio = [0,0,0,0,0]
    for t in range((len(weights_price))):
        ratio[t] = (weights_price[t][1])/(weights_price[t][0])
        peso+=(weights_price[t][0])
#    print(ratio)
#    print(peso)
    capacity = 15
    while(peso > capacity):
        lowest = 1000
        for i in range((len(ratio))):
            if (ratio[i] < lowest):
                lowest = ratio[i]
        a = ratio.index(lowest)
        ratio.pop(a)
        weights_price.pop(a)
        for i in range((len(weights_price))):
            peso+=(weights_price[i][0])
    print(weights_price)
    

if __name__ == "__main__":
    main()