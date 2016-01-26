import datetime

print "Input your birthday date"
y = raw_input('Year: ')
m = raw_input('Month: ')
d = raw_input('Day: ')

birth = datetime.date(int(y),int(m),int(d))
now = datetime.datetime.now().date()

diff = now - birth
print diff.days*24*60*60
