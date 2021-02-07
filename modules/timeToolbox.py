from time import localtime as impure_localtime, sleep

class Time:
    def __init__(self, timeStr):
        try:
            if len(timeStr) != 5: raise ValueError("Attempted to initiate Time object with incorrect timeStr format (not 5 characters long)")
            self.timeStr = timeStr
            try:
                self.h = int(timeStr[:2])
                self.m = int(timeStr[3:])
                self.timeInt = int(timeStr[:2] + timeStr[3:])
            except ValueError:
                raise ValueError("Attempted to initiate Time object with incorrect timeStr format (integers are not in place)")
        except Exception as e:
            print("Error: " + str(e))
            print(len(timeStr))

    def __str__(self):
        return self.timeStr
    
    def __int__(self):
        return self.timeInt
    
    def __lt__(self, other):
        return self.timeInt < other.timeInt
    
    def __le__(self, other):
        return self.timeInt <= other.timeInt

    def __gt__(self, other):
        return self.timeInt > other.timeInt
    
    def __ge__(self, other):
        return self.timeInt >= other.timeInt

    def __eq__(self, other):
        return self.timeInt == other.timeInt

def localtime():
    now = impure_localtime()
    return Time(str(now.tm_hour).rjust(2, "0") + ":" + str(now.tm_min).rjust(2,"0"))

class LabeledTime(Time):
    def __init__(self, timeStr, label):
        Time.__init__(self, timeStr)
        self.label = label