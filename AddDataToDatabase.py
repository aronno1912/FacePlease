import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceplease-71d8d-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "1111":
        {
            "name": "Alia Bhatt",
            "major": "Film and Production",
            "starting_year": 2018,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1112":
        {
            "name": "Anupama Ghose",
            "major": "Bangla",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1113":
        {
            "name": "Debjany Ghosh",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "1114":
        {
            "name":"Deepika Padukone",
            "major":"Liberal Studies",
            "starting_year":2022,
            "total_attendance": 0,
            "standing":"F",
            "year":4,
            "last_attendance_time":"2022-12-11 00:54:34"
        },

    "1115":
        {
            "name": "Steve Jobs",
            "major": "EEE",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "1116":
        {
            "name": "Mark Zuckerberg",
            "major": "Data Science",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-10-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)