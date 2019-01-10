import re

log = [
'[1518-11-01 00:00] Guard #10 begins shift',
'[1518-11-01 00:05] falls asleep',
'[1518-11-01 00:25] wakes up',
'[1518-11-01 00:30] falls asleep',
'[1518-11-01 00:55] wakes up',
'[1518-11-01 23:58] Guard #99 begins shift',
'[1518-11-02 00:40] falls asleep',
'[1518-11-02 00:50] wakes up',
'[1518-11-03 00:05] Guard #1056 begins shift',
'[1518-11-03 00:24] falls asleep',
'[1518-11-03 00:29] wakes up',
'[1518-11-04 00:02] Guard #99 begins shift',
'[1518-11-04 00:36] falls asleep',
'[1518-11-04 00:46] wakes up',
'[1518-11-05 00:03] Guard #99 begins shift',
'[1518-11-05 00:45] falls asleep',
'[1518-11-05 00:55] wakes up']

guardId = -1
timeTable = {'guard':[], 'min':[[0 for minutes in range(60)]]}
i = 0

for record in log:
	matchGuard = re.match(".*Guard #(\d*)", record )
	if matchGuard != None:
		guardId = matchGuard.group(1)
		if guardId not in timeTable['guard']:
			print( 'new guard', guardId )
			timeTable['guard'].append(guardId)
			i += 1
	matchstartSleep = re.match(".* 00:(\d*)] falls asleep", record )
	if matchstartSleep != None:
		print( 'start at:', matchstartSleep.group(1) )
	matchstopSleep = re.match(".* 00:(\d*)] wakes up", record )
	if matchstopSleep != None:
		print( 'stop at:', matchstopSleep.group(1) )

print( timeTable['min'][0] )