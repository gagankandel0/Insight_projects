def longest(l):
    max=0
    for i in l:
        if len(i)>max:
            max=len(i)
    return max
print(longest(['gag','name','kandel']))