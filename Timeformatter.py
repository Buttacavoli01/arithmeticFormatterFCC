def add_time(start, duration, day=False):
    returnTime = ""
    day_array = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]
    day_index = {"sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6}


    duration_tpl = duration.partition(":")
    duration_hours = int(duration_tpl[0])
    duration_mins = int((duration_tpl[2]))

    start_tpl = start.partition(":")
    start_tpl_mins = start_tpl[2].partition(" ")

    start_am_pm = start_tpl_mins[2]

    start_hours = int(start_tpl[0])
    start_mins = int(start_tpl_mins[0])

    am_or_pm = str(start_tpl_mins[2])
    am_pm_flip = {"AM": "PM", "PM": "AM"}
    amount_of_days = int(duration_hours / 24)


    end_minutes = duration_mins + start_mins
    if end_minutes >= 60:
        start_hours += 1
        end_minutes = end_minutes % 60

    am_pm_flips = int((start_hours + duration_hours) / 12)
    end_hours = (start_hours + duration_hours) % 12

    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours

    if(am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
        amount_of_days += 1

    am_or_pm = am_pm_flip[am_or_pm] if am_pm_flips % 2 == 1 else am_or_pm

    returnTime = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm


    if(day):
        day = day.lower()
        index = int((day_index[day]) + amount_of_days) % 7
        new_day = day_array[index]
        returnTime += ", " + new_day

    if amount_of_days == 1:
        return returnTime + " " + "(next day)"
    elif amount_of_days > 1:
        return returnTime + " (" + str(amount_of_days) + " days later)"


    return returnTime

print(add_time("11:55 PM", "3:12", "Monday"))


