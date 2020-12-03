def dollar(str1):
    a=str1[0]
    result=str1.replace(a,'$')
    str1=a+result[1:]
    return str1
print(dollar("agan"))
