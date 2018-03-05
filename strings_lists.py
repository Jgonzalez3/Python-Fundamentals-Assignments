# pylint: disable=print-statement
words = "It's thanksgiving day. It's my birthday,too!"
print words

print words.find("day")
print words.replace("day", "month")

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world!"]

print len(y)
print y[0]
print y[7]

z = [19,2,54,-2,7,12,98,32,10,-3,6]
sortedz = []
print sorted(z)
sortedz = sorted(z)
print z
print sortedz

newz = []

sortedzfirsthalf = sortedz[:len(sortedz)/2]
sortedzsecondhalf = sortedz[len(sortedz)/2:]
print "first half", sortedzfirsthalf
print 'secondhalf', sortedzsecondhalf

newz.append(sortedzfirsthalf)
newz.extend(sortedzsecondhalf)
print newz
