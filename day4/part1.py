from datetime import datetime, timedelta
import re

INPUT = "./input.txt"
DATE_FORMAT = "%Y-%m-%d %H:%M"
lines = [line.rstrip('\n') for line in open(INPUT)]


def sort_inputs(inputs):
    return sorted(inputs, key=lambda e: datetime.strptime(e[1:17], DATE_FORMAT))


def treat_inputs(inputs):
    guards = {}
    guard_id = 0
    for i in inputs:
        if i[19:24] == "Guard":
            guard_id = int(re.search("#(\d+)", i).group(1))
            if not guard_id in guards:
                guards[guard_id] = {"total_sleeped_time": 0, "sleepiest_minute": -1,
                                    "activities": [], "periodes": []}
        elif i[19:24] == "falls":
            guards[guard_id]["activities"].append(i)
        elif i[19:24] == "wakes":
            guards[guard_id]["activities"].append(i)
            sleep_time = datetime.strptime(
                guards[guard_id]["activities"][-2][1:17], DATE_FORMAT)
            wake_up_time = datetime.strptime(
                guards[guard_id]["activities"][-1][1:17], DATE_FORMAT)
            guards[guard_id]["periodes"].append((sleep_time, wake_up_time))

            sleeped_time = (wake_up_time - sleep_time).seconds // 60
            guards[guard_id]["total_sleeped_time"] += sleeped_time

    return guards


def compute_sleepiest_minute(guard):
    visual_hour = [0 for i in range(60)]
    for period in guard["periodes"]:
        fall_asleep_min = period[0].minute
        wake_up_min = period[1].minute
        for i in range(fall_asleep_min, wake_up_min):
            visual_hour[i] += 1

    return visual_hour.index(max(visual_hour))


inputs = sort_inputs(lines)
guards = treat_inputs(inputs)

sleepy_id = sorted(guards, key=lambda k: guards[k]["total_sleeped_time"])[-1]
sleepy_guard = guards[sleepy_id]
sleepiest_min = compute_sleepiest_minute(sleepy_guard)
print("Sleepy (#{}) a dormi {} min total. La minute la plus dormie est {}. La reponse should be {}".format(
    sleepy_id, sleepy_guard["total_sleeped_time"], sleepiest_min, sleepy_id * sleepiest_min))
