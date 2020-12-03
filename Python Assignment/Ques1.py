def str_freqency(str1):
    dict={}
    for a in str1:
        keys=dict.keys()
        if a in keys:
            dict[a] += 1
        else:
            dict[a]=1
    return dict
print(str_freqency('gagan.kandel@apexcollege.edu.np'))
