import process as p
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

calls = open("call_logs.txt", "r")

dates = []

for i in calls:
    line = calls.readline()
    if p.isDateLine(line):
        dates.append(p.formatDate(line))


calls.close()

months, days, hours, minutes = p.splitDates(dates)

out = pd.DataFrame({'months': months,
                   'days': days,
                   'hours': hours,
                   'minutes': minutes})


print(out)