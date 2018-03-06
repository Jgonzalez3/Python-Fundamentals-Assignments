# pylint: disable=print-statement

def EvenOdd():
    for count in range(1,2001):
        if count % 2 != 0:
            print "Number is ", count, ". " , "This is an odd number."
        elif count % 2 == 0:
            print "Number is ", count, ". ", "This is an even number."


def Multiply(a, mult):
    for num in range(0,len(a)):
        a[num] *= mult
    return a

a = [-5,10,3,9]
result1 = Multiply(a, 5)
print result1 



def layered_multiples(arr):
    array = []
    new_array = []
    for num in range(0,len(arr)):
        
        for val in range(0,(arr[num])):
            arr[num] = 1
            array.append(arr[num])
        new_array.append(array)
        array = []
    return new_array
x = layered_multiples(Multiply([2,4,5],3))
print x