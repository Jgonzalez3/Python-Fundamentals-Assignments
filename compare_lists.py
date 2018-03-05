# pylint: disable=print-statement
list1 = ['celery','carrots','bread','milk']
list2 = ['celery','carrots','bread','milk']
count = 0

for val in range(0, len(list1)):
    if list1[val] == list2[val]:
        count += 1
if count == len(list1) and count == len(list2):
    print "the lists are the same"
else: print "the lists are not the same" 