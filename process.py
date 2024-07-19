
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


    if len(day) == 1:
        day = "0" + day


    # Format time to 24 hour time
    hour, minute = time.split(':')
    hour = int(hour)

    if not morning:
        hour += 12

    time = str(hour) + ":" + minute + ":00"

    return month, day, time




# Checks input for date (Just looking at the first word in a given line for a name of a month)
def isDateLine(line):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    l = line.split()

    if len(l) > 0 and l[0] in months:
         return True
    else:
         return False