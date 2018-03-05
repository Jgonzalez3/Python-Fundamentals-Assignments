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
for count in range(0,len(a)-1):
    x += a[count]
print x # prints the sum of the list

#Average List
y = 0
for count in range(0,len(a)-1):
    y += a[count]
print y/len(a) #prints the average of the sum of list