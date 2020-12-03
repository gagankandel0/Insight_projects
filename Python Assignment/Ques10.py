def odd_remove(str):
    even=" "
    for i in range(len(str)):
        if i%2==0:
            even=even+str[i]
    return even
print(odd_remove('kandel'))
            
