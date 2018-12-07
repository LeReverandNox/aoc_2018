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
            if guard_id not in guards:
                guards[guard_id] = {"total_sleeped_time": 0, "sleepiest_minute": -1,
                                    "activities": [], "periodes": [], "visual_hour": []}
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


def compute_sleepiest_minute(guards):
    for k in guards:
        guard = guards[k]
        visual_hour = [0 for i in range(60)]
        for period in guard["periodes"]:
            fall_asleep_min = period[0].minute
            wake_up_min = period[1].minute
            for i in range(fall_asleep_min, wake_up_min):
                visual_hour[i] += 1
        guard["visual_hour"] = visual_hour


def get_sleepiest_guard_minute(guards):
    all_visual_hour = [{"minute": i, "id": -1, "times": 0} for i in range(60)]
    for k in guards:
        guard = guards[k]
        for i, v in enumerate(guard["visual_hour"]):
            if v > all_visual_hour[i]["times"]:
                all_visual_hour[i]["id"] = k
                all_visual_hour[i]["times"] = v

    return max(all_visual_hour, key=lambda minute: minute["times"])


inputs = sort_inputs(lines)
guards = treat_inputs(inputs)
compute_sleepiest_minute(guards)
sleepiest_guard_minute = get_sleepiest_guard_minute(guards)

print("La minute {} a ete dormie {} fois par le guard #{}. La reponse should be {}.".format(
    sleepiest_guard_minute["minute"], sleepiest_guard_minute["times"], sleepiest_guard_minute["id"], sleepiest_guard_minute["minute"] * sleepiest_guard_minute["id"]))
