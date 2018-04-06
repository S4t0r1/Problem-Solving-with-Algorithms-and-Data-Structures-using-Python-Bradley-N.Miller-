from pythonds.basic.queue import Queue
import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return  False

    def setNextTask(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60/self.pagerate


class Task:
    def __init__(self, time, pages_per_task):
        self.timeStamp = time
        self.pagenum = random.randint(1, pages_per_task)

    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pagenum

    def waitTime(self, waitEndTime):
        return waitEndTime - self.timeStamp


def simulation(timeSpanSeconds, pagerate, studentnum, pages_per_task):
    labprinter = Printer(pagerate)
    waitQueue = Queue()
    waitTimes = []

    for nth_second in range(timeSpanSeconds):
        if nextTask(studentnum):
            task = Task(nth_second, pages_per_task)
            waitQueue.enqueue(task)
        if (not labprinter.busy()) and (not waitQueue.isEmpty()):
            newtask = waitQueue.dequeue()
            waitTimes.append(newtask.waitTime(nth_second))
            labprinter.setNextTask(newtask)
        labprinter.tick()

    average_wait_time = sum(waitTimes) / len(waitTimes)
    print("Average wait time = {:.4f}, tasks remaining = {:d}".format(average_wait_time, waitQueue.size()))
    return average_wait_time


def nextTask(studentnum):
    # supposing a student prints twice per hour
    randomrangeEquation = (60 / (studentnum * 2)) * 60
    num = random.randint(1, randomrangeEquation)
    if num == randomrangeEquation:
        return True
    else:
        return False


def get_simulations(cycles, timespan, pagerate, studentnum, taskpagesnum):
    averagesList = [simulation(timespan, pagerate, studentnum, taskpagesnum) for i in range(cycles)]
    total_average = sum(averagesList) / len(averagesList)
    print("*** total average wait time = {:.5f}".format(total_average))
    return averagesList


# ============================================= simulations =================================================
# base case..
print("\nBase case: (cycles=10, timespan=3600, pagerate=5, students=10, pages_per_task=20\n")
get_simulations(10, 3600, 5, 10, 20)

# doubled students case, pagerate doubled for balance..
print("\n\n2nd case: (cycles=10, timespan=3600, pagerate=10, students=20, pages_per_task=20\n")
get_simulations(10, 3600, 10, 20, 20)

# when the task length (pages per task) is cut in half, builds up on 2nd case..
print("\n\n3rd case: (cycles=10, timespan=3600, pagerate=10, students=20, pages_per_task=10\n")
get_simulations(10, 3600, 10, 20, 10)
