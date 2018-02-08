from datetime import datetime
from pytz import timezone

etime = timezone('US/Eastern')
eastime = datetime.now(etime)
ptime = timezone('US/Pacific')
pactime = datetime.now(ptime)

def hours(time1, time2):
    time1hr = int(time1[:2])
    time1min = int(time1[2:])

    mins1 = (time1hr * 60) + time1min

    time2hr = int(time2[:2])
    time2min = int(time2[2:])

    mins2 = (time2hr * 60) + time2min

    dist = mins2 - mins1
    dishr = int(dist / 60)
    dismin = dist % 60

    print "%d hrs and %d mins to games" % (dishr, dismin)
    
def time_to_games(time):
    atime = pactime.strftime('%I%M')
    hours(str(atime), time)    

print "Channing's Time: ", eastime.strftime('%I:%M %p')

print "Alex's Time: ", pactime.strftime('%I:%M %p')

time = str(raw_input("When are games? \n"))

print "Games will be at %s" % (int(time) + 300)

time_to_games(time)
