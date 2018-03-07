# pylint: disable=print-statement

my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777",
}

def DictToTupe(dict):
    name = my_dict.keys()
    phone = my_dict.values()
    tupleout = zip(name, phone)
    print tupleout

DictToTupe(my_dict)
