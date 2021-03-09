# Anthony Serrano
# Part C
from datetime import datetime
from pytz import timezone, utc

# This function converts the current time to military time
def get_mil_time(time12):
    time_format='%H:%M:%S'
    pstMilTime = time12.strftime(time_format)
    return pstMilTime


# Body 
# Get current time and convert from UTC to PST
now = datetime.now(tz=utc)
now = now.astimezone(timezone('US/Pacific'))
# Print current time in 12 hour format 
print ("Current time: ")
print (now.strftime("%I:%M:%S %p"))
# Print current time in Military time
print("Military Time: ")
print(get_mil_time(now))