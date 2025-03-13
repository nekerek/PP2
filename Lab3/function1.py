def uniqueueue(lists):
    unique=[]
    for i in range(0,len(lists)):
        if lists[i] not in unique:
            unique.append(lists[i])

    return unique

