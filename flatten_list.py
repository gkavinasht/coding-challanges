def flattenList(nestedList):
    res = []
    for ele in nestedList:
        if type(ele) == list:
            res.extend(flattenList(ele))
        else:
            res.append(ele)

    return res

nestedList = [[1,[1, 10, 3]],[2, 5, 4],[1,1]]
print(flattenList(nestedList))