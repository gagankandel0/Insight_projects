def sentence(str1):
    count=dict()
    words=str1.split()
    for a in words:
        if a in count:
            count[a] += 1
        else:
            count[a]=1
    return count
print(sentence('my name is gagan and gagan is my name'))