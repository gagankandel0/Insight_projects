def sample(str1):
    a='ing'
    b='ly'
    if len(str1)>=3:
        if str1[-3:]!='ing':
            result=str1+a
        else:
            result=str1+b
    else:
        return str1
    return result
print(sample('sw'))
            