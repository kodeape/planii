from modules.fileToolbox import files_in_dir, read_file_lines
from modules.timeToolbox import LabeledTime
from modules.scheduleToolbox import Schedule
print()
print("Welcome to Planii!")
print(files_in_dir("schedules"))

def lt_from_file(filename):
    lines = read_file_lines(filename)
    labeled_times = []
    for line in lines:
        time_label = line.split()
        labeled_times.append(LabeledTime(time_label[0], time_label[1]))
    return labeled_times


ic_times = lt_from_file("schedules/IC.txt")
ic_plan = Schedule("IC", ic_times)
ic_plan.player.play()