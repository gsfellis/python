## Converts military time, i.e. 0800, to standard time format, 12:00 AM

def isMilitaryTime(time):
    if (time.isdigit() == False
            or len(time) != 4
            or int(time[:2]) > 24
            or int(time[2:4]) > 59):
        return False
        
    return True

def convertMilToStandard(time):
    period = 'AM'
    
    if time.startswith('0'):
        hours = time[1:2]        
    else:        
        hours = time[:2]
        
    minutes = time[2:4]

    if 12 < int(hours) < 24:
        period = 'PM'
        hours = str(int(hours) - 12)
    elif int(hours) == 24 or int(hours) == 0:
        hours = '12'
    

    return "{0}:{1} {2}".format(hours, minutes, period)

def main():    
    mTime = ''

    while not isMilitaryTime(mTime):
        print('Enter a time in military format, i.e. 0800.')
        mTime = input('Enter military time: ')

    time = convertMilToStandard(mTime)
    print('{0} converted to standard time is {1}'.format(mTime, time))


main() ## Start program

