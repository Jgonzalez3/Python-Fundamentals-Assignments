# pylint: disable=print-statement

x = "x   1   2   3   4   5   6   7   8   9   10  11  12"
string = ""
start = 1

print x
for row in range(1,13):
    if row == 1:
        string += str(start)
        string += "   "
    if row <= 9:
        string += str(row)
        string += "   "
    elif row > 9:
        string += str(row)
        string += "  "
start += 1
print string

for row in range(1,12):
    string = "" 
    for val in range(1,13):
        if val == 1 and val < 9:
            string += str(start)
            string += "   "
        if val == 1 and val > 9:
            string += str(start)
            string += "  "
        string += str(val * start)
        string += "  "
    start += 1
    print string

