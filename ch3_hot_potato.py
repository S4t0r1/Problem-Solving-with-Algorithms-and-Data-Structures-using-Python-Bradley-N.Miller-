import random
from pythonds.basic.queue import Queue


def num_input():
    prompt = input("Do you want to submit counter manually?: ")
    if prompt in {"Y".lower(), "YES".lower()}:
        return int(input("Choose counter: "))
    return random.randint(1, 20)


def hot_potato(nameslst, num=None):
    circle = Queue()
    if not num:
        num = num_input()
    print("counter is %d" % (num))
    for name in nameslst:
        circle.enqueue(name)

    while circle.size() > 1:
        for i in range(num):
            circle.enqueue(circle.dequeue())
        circle.dequeue()
    return circle.dequeue()


nameslst = ["Jan", "Anna", "Peter", "Zuzana", "Martin", "Dominika"]
print(hot_potato(nameslst))
print(hot_potato(nameslst, 7))
