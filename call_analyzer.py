import process as p

calls = open("call_logs.txt", "r")

dates = []

for i in range(100):
    line = calls.readline()
    if p.isDateLine(line):
        dates.append(p.formatDate(line))


print(len(dates))