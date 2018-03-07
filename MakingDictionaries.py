# pylint: disable=print-statement

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def MakeDict(list1, list2):
    array1 = len(list1)
    array2 = len(list2)
    newdict = {}
    if array1 > array2:
        zippedlists = zip(list1, list2)
    # print zippedlists
    elif array2 > array1:
        zippedlists = zip(list2, list1)
    else: zippedlists = zip(list1, list2)
    newdict = dict(zippedlists)
    # print newdict
    return newdict
x = MakeDict(name, favorite_animal)
print x
