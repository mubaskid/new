import time #useful for measuring code execution

class StopWatch:
    def __init__(self, startTime = 0, endTime = 0, elapsedTime = 0):
        self.__startTime = startTime
        self.__endTime = endTime

    def start(self):
        self.__startTime = time.clock()

    def stop(self):
        return self.getElapsedTime()


    def getstarttime(self):
        return self.__startTime

    def getendtime(self):
        return self.__endTime

    def getElapsedTime(self):
        elapsedTime = self.__elapsedTime
        elapsedTime +=((time.clock() - self.__startTime) * 1000)
        return elapsedTime

def main():
    x = StopWatch()
    x.start
    
    sum = 0 
    for i in range(1 , 10000000):
        sum += i
    x.stop
    print("Elapsed execution time is", x.getElapsedTime())
    print(sum)
    x.reset

    main()