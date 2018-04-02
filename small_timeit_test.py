# tests timing of list[index] and dict.__setitem__, dict.__getitem__#
# done in an online interpreter

import timeit
import random

lit_avg, sit_avg, git_avg = (), (), () 
for i in range(10000,1000001,100000):
    x = list(range(i))
    num = x.index(random.randint(0, 999))
    t1 = timeit.timeit(lambda: x.index(num), number=1000)
    d = {j: None for j in range(i)}
    t2 = timeit.timeit(lambda: d.__setitem__, number=1000)
    t3 = timeit.timeit(lambda: d.__getitem__, number=1000)
    lit_avg += (t1,)
    sit_avg += (t2,)
    git_avg += (t3,)
    print("list index time = %.5f" % (t1), end= '   ')
    print("set item time = %.5f" % (t2), end= '   ')
    print("get item time = %.5f" % (t3))

for item in (lit_avg, sit_avg, git_avg):
    avg = sum(item) / len(item)
    desc = ("\nlit_avg" if item == lit_avg               
       else "sit_avg" if item == sit_avg else "git_avg")
    print(desc, "= %.5f" % (avg), end= '\n')
    del item
