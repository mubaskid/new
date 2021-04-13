class Time:
    def __init__(self, hours, mins, secs):
        self.hours = hours
        self.mins = mins
        self.secs = secs

    def addTime(time2,time3):
        time1 = Time(0,0,0)
        if time2.mins+time3.mins > 60:
            time1.hours = (time2.mins+time3.mins)/60
        time1.hours = time1.hours+time3.hours+time2.hours
        time1.mins = (time2.mins+time3.mins)-(((time2.mins+time3.mins)/60)*60)
        time1.secs = (time2.mins+time3.mins)/60
        return time1

    def displayTime(self):
        print("Time is", self.hours, "hours and", self.mins, "minutes and", self.secs, "seconds.")


    def displayMinute(self):
        print((self.hours*60)+self.mins)

    def displaySecond(self):
        print((self.mins*60)+self.secs)

a = Time(2,5,3)
b = Time(1,2,1)
c = Time(5,4,3)
d = Time.addTime(a,b)
d.displayTime()
d.displayMinute()
d.displaySecond()
