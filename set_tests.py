
setLst = [{8, 5, 6}, {5, 7}, {8, 5, 6, 7}, {5, 7}]
print(setLst)
dupset = [s for s in setLst if setLst.count(s) == len(s)]

if dupset:
    dupset = dupset[0]
    for index, set_ in enumerate(setLst):
        if dupset != set_:
            pairNumLst = list(set_) + list(dupset)
            if dupset.issubset(set_):
                setLst[index] = set_ - dupset
            else:
                removenums = {num for num in pairNumLst 
                              if pairNumLst.count(num) == len(dupset)}
                if removenums:
                    setLst[index] = set_ - removenums
                    print("ooo", pairNumLst, removenums)
                    print(setLst[index])
print(setLst)
