def swap(str):
    a=str[0]
    b=str[-1]
    a,b=b,a
    result=a+str[1:-1]+b
    return result
print(swap('kite'))