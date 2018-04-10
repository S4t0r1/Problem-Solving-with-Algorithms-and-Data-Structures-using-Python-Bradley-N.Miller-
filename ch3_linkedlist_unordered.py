class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        while temp.getNext() is not None:
            temp = temp.getNext()
        self.tail = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        if self.tail:
            self.tail.setNext(temp)
            self.tail = temp
        else:
            temp.setNext(self.head)
            self.head = temp
        self.tail = temp


    def index(self, item):
        current = self.head
        found = False
        index = 0
        while not found:
            if not current:
                current = self.tail
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1
        return index

    def pop(self, index=None):
        current = self.head
        previous = None
        if not index:
            while current.getNext():
                previous = current
                current = current.getNext()
            self.tail = current
        else:
            i = 0
            while i < index:
                previous = current
                current = current.getNext()
                i += 1
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return current.getData()

    def insert(self, index, item):
        current = self.head
        previous = None
        i = 0
        while i < index:
            previous = current
            current = current.getNext()
            i += 1
        newitem = Node(item)
        if previous == None:
            self.head = newitem
        else:
            previous.setNext(newitem)
        newitem.setNext(current)
        current.setNext(current.getNext())
