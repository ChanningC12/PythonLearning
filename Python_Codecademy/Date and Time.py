#Date and Time
from datetime import datetime
now=4
now=datetime.now()
print (datetime.now())

current_year=now.year
current_month=now.month
current_day=now.day

print (now.year)
print (now.month)
print (now.day)

#The % operator will fill the %s placeholders in the string on the left with the strings in the parentheses on the right.
print ('%s/%s/%s' % (now.month,now.day,now.year))
print ('%s:%s:%s' % (now.hour,now.minute,now.second))
print ('%s/%s/%s %s:%s:%s' % (now.month,now.day,now.year,now.hour,now.minute,now.second))


