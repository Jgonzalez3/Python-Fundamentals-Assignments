# pylint: disable=print-statement


def Stars(x):
    for idx in range(0,len(x)):
        starlength = ""
        if type(x[idx]) == str:
            string = x[idx]
            for letter in string:
                starlength += string[0].lower()
            print starlength
            continue
        for val in range(0,(x[idx])):
            starlength += "*"
        print starlength

Stars([1,2,2,5,3])


