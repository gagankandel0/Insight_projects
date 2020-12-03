def removal(str1,n):
    if len(str1)>n:
        result=str1[:n]+str1[n+1:]
        return result
    else:
        return 'Invalid input'
print(removal('google',6))