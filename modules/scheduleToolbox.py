from modules.timeToolbox import Time, localtime, LabeledTime, sleep 
from winsound import PlaySound as play_sound

class SchedulePlayer:
    def __init__(self, schedule):
        self.schedule = schedule
        self.current = 0
    
    def skip_to_current(self):
        now = localtime()
        skipped = 0
        while self.schedule.times[self.current + 1] <= now:
            self.current += 1
            skipped += 1
        return skipped
    
    def wait_for_time(self, time, sleep_time = 10):
        while localtime() < time:
            print(".", end=".")
            sleep(sleep_time)
    
    def alarm(self):
        play_sound("./sounds/piano_notification.wav", True)

    def play(self, start_at = None):
        if start_at != None: self.current = start_at
        number_of_tasks = len(self.schedule.times)-1
        if self.current >= number_of_tasks:
            print("Tried to start schedule '%s' at its end or further." % self.schedule.name)
            return
        print("PLAYING SCHEDULE '%s'" % self.schedule.name)
        currentTime = self.schedule.times[self.current]
        print(currentTime.timeStr + ": " + currentTime.label)
        while self.current <= number_of_tasks-1:
            nextTime = self.schedule.times[self.current+1]
            print("Task lasts until " + nextTime.timeStr)
            print()
            self.wait_for_time(nextTime)
            #sleep(3)
            # input stuff here
            print()
            print("Beep beep! Task '%s' is over. Now onto the next one." % currentTime.label)
            print()
            self.alarm()
            currentTime = nextTime
            print(currentTime.timeStr + ": " + currentTime.label)
            self.current += 1
        print("Schedule '%s' is finished." % self.schedule.name)

class Schedule:
    def __init__(self, name, times):
        self.name = name
        self.times = times
        self.player = SchedulePlayer(self)
    

times = [LabeledTime("07:00", "Våkne"), LabeledTime("07:15", "Frokost"), LabeledTime("08:00", "Jobbe"), LabeledTime("09:00", "Ferdig")]

plan = Schedule("Jobbedag", times)

plan.player.play(1)