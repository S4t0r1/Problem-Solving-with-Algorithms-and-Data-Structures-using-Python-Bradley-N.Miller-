
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getNextData(self):
        return None if self.next is None else self.next.getData()

    def getPrevious(self):
        return self.previous

    def getPreviousData(self):
        return None if self.previous is None else self.previous.getData()

    def setData(self, newitem):
        self.data = newitem

    def setNext(self, newitem):
        self.next = newitem

    def setPrevious(self, previtem):
        self.previous = previtem

class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.itemsDataDict = {}
        self.indexDataDict = {}

    def itemData(self, item):
        try:
            return self.itemsDataDict[item]
        except KeyError:
            return None

    def showDataDict(self):
        for key, value in sorted(self.itemsDataDict.items()):
            node, position = value
            prevnode, nextnode = node.getPreviousData(), node.getNextData()
            print("number {key} : prev={prevnode}, next={nextnode}, index={position}".format(**locals()))
        print("self.head {}\nself.tail {}\nlist size {}\n".format(
                 None if self.head is None else self.head.getData(),
                 None if self.tail is None else self.tail.getData(), self.length))

    def isEmpty(self):
        return self.head is None

    def search(self, item):
        return True if self.itemData(item) else False

    def size(self):
        return self.length

    def index(self, item):
        return self.itemData(item)[1] if self.itemData(item) else None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        position = 0
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
                position += 1

        prevnum = None if previous is None else previous.getData()
        if prevnum != item:
            temp = Node(item)
            temp.setPrevious(previous)
            if previous is None:
                temp.setNext(self.head)
                self.head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)
            self.itemsDataDict[item] = [temp, position]
            self.indexDataDict[position] = item
            self.length += 1
            self.__updateDataDictAdd(self.itemsDataDict[item])

    def __updateDataDictAdd(self, addedNodeData):
        addedNode = addedNodeData[0]
        addednum = addedNode.getData()
        for key in self.itemsDataDict.keys():
            [node, position] = self.itemsDataDict[key]
            num = node.getData()
            if self.length > 1 and position == (self.length - 1):
                self.tail = node
            if addednum < num:
                self.itemsDataDict[key] = [node, position + 1]
                if addedNode.getNext() == node:
                    node.setPrevious(addedNode)
            elif node.getNextData() == addednum > num:
                addedNode.setPrevious(node)

    def __updateDataDictPop(self, index):
        try:
            removenum = self.indexDataDict[index]
            self.__updateDataDictRemove(removenum)
            return removenum
        except KeyError:
            return

    def __updateDataDictRemove(self, removenum):
        for key in self.itemsDataDict.keys():
            [node, position] = self.itemsDataDict[key]
            num = node.getData()
            if self.head.getData() == removenum:
                self.head = self.head.getNext()
            if num > removenum:
                self.itemsDataDict[key] = [node, position - 1]
                if node.getPreviousData() == removenum:
                    node.setPrevious(node.getPrevious().getPrevious())
            elif num < removenum == node.getNextData():
                node.setNext(node.getNext().getNext())

    def remove(self, item):
        if self.itemData(item):
            if self.length > 1 and item  == self.tail.getData():
                self.pop(fromremove=True)
            else:
                self.__updateDataDictRemove(item)
                del self.itemsDataDict[item]
                self.length -= 1

    def pop(self, index=None, fromremove=None):
        assert self.length > 0, "Cannot pop() from empty linked-list !"
        if index is None or (index == self.length - 1):
            popitem = self.tail if self.tail is not None else self.head
            previtem, popnum = popitem.getPrevious(), popitem.getData()
            if popitem == self.tail:
                previtem.setNext(popitem.getNext())
            del self.itemsDataDict[popnum]
            self.length -= 1
            
            self.head = None if self.length == 0 else self.head
            self.tail = None if self.length < 2 else self.tail.getPrevious()
        else:
            assert (0 <= index < self.length), "Use only existing index positions !"
            popnum = self.__updateDataDictPop(index)
            if popnum is not None:
                del self.itemsDataDict[popnum]
                self.length -= 1
        if not fromremove:
            return popnum
