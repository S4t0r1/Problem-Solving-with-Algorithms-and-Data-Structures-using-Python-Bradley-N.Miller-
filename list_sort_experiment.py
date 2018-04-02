
# *** The aim in this experiment is to achieve list sorting without sorted() achieving O(n) ***
#**********************************************************************************************

# 1st example is an algorithm to sort a list without the sorted() function


lst = [11, 4, 0, 3, 15, 10, 17, 8, 1, 16, 14, 2, 13, 9, 7, 5, 12, 6]
def main():
    lstsort = []
    while lst:
        minimum = lst[0]
        for e in lst:
            if e < minimum:
                minimum = e
        lstsort.append(minimum)
        lst.remove(minimum)        
    print(lstsort)

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))


#-----------------------------------------------------------------------------
# 2nd example is sorting a list without sorted(), append() and remove() functions
# as it does not create a new list, but updates the same list, however its slower
# and less comprehensive as it uses more iterations overall


lst = [11, 4, 0, 3, 15, 10, 17, 8, 1, 16, 14, 2, 13, 9, 7, 5, 12, 6]
def main():
    magicnum, i = 0, 0
    first_cycle = True
    while magicnum >= 0:
        if i == len(lst) - 1:
            first_cycle = False
            i = 0
            magicnum -= 1
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            magicnum += 1 if first_cycle else 0
        i += 1
    print(lst)

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
