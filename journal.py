import csv
import datetime as dt

now = dt.datetime.now()

print(str(now), " enter your input for today")
text = input()

created_at = str(now)
with open('journal.txt', 'a') as f:
    f.write(str(now))
    f.write(" ")
    f.write(text)
    f.write("\r\n")

print(str(now), " thanks")
