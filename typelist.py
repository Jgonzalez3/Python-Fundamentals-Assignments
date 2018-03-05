# pylint: disable=print-statement

test = ['magical unicorns',19,'hello',98.98,'world']
newstr = ""
total = 0
stringcount = 0
intcount = 0
analysis = ""
for element in range(0,len(test)):
    if type(test[element]) is int:
        total += test[element]
        stringcount += 1
    elif type(test[element]) is str:
        newstr += test[element]
        newstr += " "
        intcount += 1
if intcount > 0 and stringcount > 0:
    analysis += "mixed data types"
elif intcount > 0 and stringcount == 0:
    analysis += "integers only"
elif stringcount > 0 and intcount == 0:
    analysis += "Strings only"
print newstr, total, analysis, intcount, "integers", stringcount, "strings" 