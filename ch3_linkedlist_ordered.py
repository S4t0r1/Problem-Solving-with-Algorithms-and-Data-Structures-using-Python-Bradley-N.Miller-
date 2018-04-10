
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newitem):
        self.data = newitem

    def setNext(self, newitem):
        self.next = newitem


class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def size(self):
        current = self.head
        count = 0
        while current != None:
            current = current.getNext()
            count += 1
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    previous = current
                    current = current.getNext()
        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                current = current.getNext()
                previous.setNext(current)
        else:
            return

    def index(self, item):
        current = self.head
        found = False
        count = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count += 1
        if found:
            return count
        else:
            return

    def pop(self, index=None):
        assert self.length > 0, "Cannot pop() from empty linked-list !"
        current = self.head
        previous = None
        if not index:
            while current.getNext():
                previous = current
                current = current.getNext()
            self.tail = current
        else:
            assert (0 <= index < self.length), "Use only existing index positions !"
            i = 0
            while i < index:
                previous = current
                current = current.getNext()
                i += 1
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1
        return current.getData()
