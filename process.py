from datetime import datetime

# Formats date to make useable with datetime library
def formatDate(d):
    D = d.split()
    month = D[0]
    day = D[1]
    time = D[2]

    def isMorning(x):
            if x[0] == 'p':
                return False
            elif x[0] == 'a':
                return True

    morning = isMorning(D[3])


    # clean day value to ensure only int
    rm = []
    for i in range(len(day)):
        try:
            int(day[i])
        except ValueError:
            print(day[i])
            rm.append(day[i])

    for i in rm:
        day = day.replace(i,'')

    if len(day) == 1:
        day = "0" + day

    day = int(day)


    # Format time to 24 hour time
    hour, minute = time.split(':')
    hour = int(hour)
    minute = int(minute)

    if not morning and hour < 12:
        hour += 12
    elif morning and hour == 12:
        hour = 0


    #add minutes to hours as decimal
    hour = hour + round((minute/60), 2)

    return month, day, hour, minute




# Checks input for date (Just looking at the first word in a given line for a name of a month)
def isDateLine(line):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    l = line.split()

    if len(l) > 0 and l[0] in months:
         return True
    else:
         return False
    

# Splits dates into lists of months, days, and times to be used for graphing
def splitDates(dates):
    months = []
    days = []
    hours = []
    minutes = []

    for date in dates:
        months.append(date[0])
        days.append(date[1])
        hours.append(date[2])
        minutes.append(date[3])

    return months, days, hours, minutes
