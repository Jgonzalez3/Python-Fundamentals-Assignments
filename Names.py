# pylint: disable=print-statement

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"}
]

def StudentName(students):
    for student in students:
        print student["first_name"], student["last_name"]
# StudentName(students)

usrs = {
    "Students": [
        {"first_name": "Michael", "last_name": "Jordan"},
        {"first_name": "John", "last_name": "Rosales"},
        {"first_name": "Mark", "last_name": "Guillen"},
        {"first_name": "KB", "last_name": "Tonel"}
    ],
    "Instructors": [
        {"first_name": "Michael", "last_name": "Choi"},
        {"first_name": "Martin", "last_name": "Puryear"},
    ]
}

def Users(users):
    for obj in users:
        print obj
        rank = 1
        for key in users[obj]:
            namelength = len(key["first_name"]) + len(key["last_name"])
            print rank, "-", key["first_name"], key["last_name"], "-", namelength
            rank += 1
Users(usrs)