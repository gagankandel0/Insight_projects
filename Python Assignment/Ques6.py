def notpoor(str):
    a=str.find('not')
    b=str.find('poor')
    if b>a and b>0 and a>0:
        result=str.replace(str[a:(b+4)],'good')
        return result
    else:
        return str
print(notpoor('my food is not that poor'))
print(notpoor('my gagan'))
    