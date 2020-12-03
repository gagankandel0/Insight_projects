def sample(str1,str2):
    a=str1[:2]
    b=str2[:2]
    c=' '
    a,b=b,a
    result=a+str1[2:]+c+b+str2[2:]
    return result
print(sample('gagan','kandel'))
    