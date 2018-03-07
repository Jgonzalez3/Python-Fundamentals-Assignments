# pylint: disable=print-statement

myDemo = {"name": "Javier", "age": 27, "cob": "Mexico", "favoritelanguage": "Python"} # cob is county of birth

def ReadDict(myDemo):
    print "My name is " + myDemo["name"]
    print "My age is", myDemo["age"]
    print "My country of birth is " + myDemo["cob"]
    print "My favorite language is " + myDemo["favoritelanguage"]
ReadDict(myDemo)