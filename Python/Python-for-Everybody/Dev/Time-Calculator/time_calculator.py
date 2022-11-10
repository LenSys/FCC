def add_time(start, duration, dayOfWeek = ""):
  
    if "AM" in start:
      startFormat = "AM"
      start = start.replace("AM", "").strip()
    elif "PM" in start:
      startFormat = "PM"
      start = start.replace("PM", "").strip()
    else:
      return False

    hours, minutes = start.split(":")
    durationHours, durationMinutes = duration.split(":")

    hours = int(hours)
    minutes = int(minutes)
    durationHours = int(durationHours)
    durationMinutes = int(durationMinutes)
  
    # print(startFormat, hours, minutes, ",", durationHours, durationMinutes)

    hoursOverflow = 0
    minutes = minutes + durationMinutes
    if minutes > 60:
      hoursOverflow = int(minutes / 60)
      minutes = minutes % 60

    hours = hours + durationHours + hoursOverflow

    days = int(hours / 24)
    hours = hours % 24
  
    if hours >= 12:
      if startFormat == "AM":
        startFormat = "PM"
      else:
        # new day
        startFormat = "AM"
        days = days + 1

    if hours > 12:
      hours = hours - 12
  
    new_time = str(hours) + ':' + str(minutes).rjust(2, '0') + ' ' + startFormat
  
    if dayOfWeek:
      # days of week
      daysOfWeekToNumber = dict()
      daysOfWeekToNumber["monday"] = 0
      daysOfWeekToNumber["tuesday"] = 1
      daysOfWeekToNumber["wednesday"] = 2
      daysOfWeekToNumber["thursday"] = 3
      daysOfWeekToNumber["friday"] = 4
      daysOfWeekToNumber["saturday"] = 5
      daysOfWeekToNumber["sunday"] = 6

      daysOfWeekNumberToDay = dict()
      daysOfWeekNumberToDay[0] = "Monday"
      daysOfWeekNumberToDay[1] = "Tuesday"
      daysOfWeekNumberToDay[2] = "Wednesday"
      daysOfWeekNumberToDay[3] = "Thursday"
      daysOfWeekNumberToDay[4] = "Friday"
      daysOfWeekNumberToDay[5] = "Saturday"
      daysOfWeekNumberToDay[6] = "Sunday"
      
      dayNumberOfWeek = daysOfWeekToNumber[dayOfWeek.lower()]
      newDayNumberOfWeek = (dayNumberOfWeek + days) % 7
            
      new_time = new_time + ", " + daysOfWeekNumberToDay[newDayNumberOfWeek]
  
    if days == 1:
      new_time = new_time + " (next day)"
    elif days > 1:
      new_time = new_time + " (" + str(days) + " days later)"

  
    return new_time