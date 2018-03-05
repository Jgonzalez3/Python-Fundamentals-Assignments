# pylint: disable=print-statement

#Multiples Part I print 1 - 1000
# for count in range(1,1001):
#     print "looping -", count

#Multiples Part II
# for count in range(5,1000001):
#     if count % 5 == 0:
#         print count

#Sum List
a = [1,2,5,10,255,3]
x = 0
for count in range(0,len(a)):
    x += a[count]
print x # prints the sum of the list

#Average List
y = 0
average = 0
newlist = [0,5,20,8,90]
for count in range(0,len(newlist)):
    y += newlist[count]
average = y / len(newlist) #prints the average of the sum of list
print average