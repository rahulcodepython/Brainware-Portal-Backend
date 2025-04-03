from datetime import datetime, timedelta
import random
import requests

# Define courses, modules, and lectures
defined_courses = ["BCA47111", "BCA40202", "BCA49112", "BCA47113"]
defined_modules = {
    "BCA47111": ["BCA47111-M1", "BCA47111-M2"],
    "BCA40202": ["BCA40202-M1", "BCA40202-M2"],
    "BCA49112": ["BCA49112-M1", "BCA49112-M2"],
    "BCA47113": ["BCA47113-M1", "BCA47113-M2"]
}
defined_lectures = {
    "BCA47111-M1": ["BCA47111-M1-L1", "BCA47111-M1-L2"],
    "BCA47111-M2": ["BCA47111-M2-L1", "BCA47111-M2-L2"],
    "BCA40202-M1": ["BCA40202-M1-L1", "BCA40202-M1-L2"],
    "BCA40202-M2": ["BCA40202-M2-L1", "BCA40202-M2-L2"],
    "BCA49112-M1": ["BCA49112-M1-L1", "BCA49112-M1-L2"],
    "BCA49112-M2": ["BCA49112-M2-L1", "BCA49112-M2-L2"],
    "BCA47113-M1": ["BCA47113-M1-L1", "BCA47113-M1-L2"],
    "BCA47113-M2": ["BCA47113-M2-L1", "BCA47113-M2-L2"]
}


def generate_lecture_plan(class_routine_schedules):
    lecture_plans = []
    # Assuming the semester starts on Sep 30, 2024
    base_date = datetime(2024, 9, 30)

    # Mapping weekdays to their corresponding dates
    weekday_map = {
        "Monday": base_date + timedelta(days=0),
        "Tuesday": base_date + timedelta(days=1),
        "Wednesday": base_date + timedelta(days=2),
        "Thursday": base_date + timedelta(days=3),
        "Friday": base_date + timedelta(days=4)
    }

    for schedule in class_routine_schedules:
        assigned_date = weekday_map[schedule["day"]]
        course_code = schedule["course"]

        # Fetch a lecture corresponding to the course
        if course_code in defined_modules:
            selected_module = random.choice(defined_modules[course_code])
            selected_lecture = random.choice(defined_lectures[selected_module])
        else:
            selected_lecture = "Unknown-Lecture"

        lecture_plan = {
            "id": selected_lecture + "-" + course_code + "-" + schedule["section"] + "-" + schedule["semester"],
            "lecture": selected_lecture,
            "section": schedule["section"],
            "course": course_code,
            "semester": schedule["semester"],
            "module": selected_module,
            "assigned_date": assigned_date.strftime("%Y-%m-%d"),
            "assigned_faculties": [schedule["faculty"]],
            "assigned_room": schedule["room"],
            "assigned_method": random.choice(["Chalk & Talk", "ICT", "Flip Class", "Hands-on Experience", "Presentation", "Quiz", "Interactive Learning"]),
            "accomplision_status": False,
            "accomplished_date": None,
            "accomplished_faculties": [],
            "accomplished_room": None,
            "accomplished_method": None
        }
        lecture_plans.append(lecture_plan)

    return lecture_plans


class_routine_schedules = [
    {"day": "Monday", "start_time": "09:00", "end_time": "10:00", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A", "course": "BCA49112", "faculty": "BWU/BCA/001", "room": "R101"},
    {"day": "Monday", "start_time": "10:15", "end_time": "11:15", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B", "course": "BCA49112", "faculty": "BWU/BCA/002", "room": "R102"},
    {"day": "Monday", "start_time": "11:30", "end_time": "12:30", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A", "course": "BCA47111", "faculty": "BWU/BCA/003", "room": "R103"},
    {"day": "Monday", "start_time": "14:00", "end_time": "15:00", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B", "course": "BCA47111", "faculty": "BWU/BCA/004", "room": "R104"},
    {"day": "Tuesday", "start_time": "09:00", "end_time": "10:00", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A", "course": "BCA47113", "faculty": "BWU/BCA/001", "room": "R101"},
    {"day": "Tuesday", "start_time": "10:15", "end_time": "11:15", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B", "course": "BCA47113", "faculty": "BWU/BCA/002", "room": "R102"},
    {"day": "Tuesday", "start_time": "11:30", "end_time": "12:30", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A", "course": "BCA40202", "faculty": "BWU/BCA/003", "room": "R103"},
    {"day": "Tuesday", "start_time": "14:00", "end_time": "15:00", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B", "course": "BCA40202", "faculty": "BWU/BCA/004", "room": "R104"},
    {"day": "Wednesday", "start_time": "09:00", "end_time": "10:00", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A", "course": "BCA49112", "faculty": "BWU/BCA/001", "room": "R101"},
    {"day": "Wednesday", "start_time": "10:15", "end_time": "11:15", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B", "course": "BCA49112", "faculty": "BWU/BCA/002", "room": "R102"},
    {"day": "Wednesday", "start_time": "11:30", "end_time": "12:30", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A", "course": "BCA47111", "faculty": "BWU/BCA/003", "room": "R103"},
    {"day": "Wednesday", "start_time": "14:00", "end_time": "15:00", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B", "course": "BCA47111", "faculty": "BWU/BCA/004", "room": "R104"},
    {"day": "Thursday", "start_time": "09:00", "end_time": "10:00", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A", "course": "BCA47113", "faculty": "BWU/BCA/002", "room": "R101"},
    {"day": "Thursday", "start_time": "10:15", "end_time": "11:15", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B", "course": "BCA47113", "faculty": "BWU/BCA/003", "room": "R102"},
    {"day": "Thursday", "start_time": "11:30", "end_time": "12:30", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A", "course": "BCA40202", "faculty": "BWU/BCA/004", "room": "R103"},
    {"day": "Thursday", "start_time": "14:00", "end_time": "15:00", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B", "course": "BCA40202", "faculty": "BWU/BCA/001", "room": "R104"},
    {"day": "Friday", "start_time": "09:00", "end_time": "10:00", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A", "course": "BCA49112", "faculty": "BWU/BCA/001", "room": "R101"},
    {"day": "Friday", "start_time": "10:15", "end_time": "11:15", "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B", "course": "BCA49112", "faculty": "BWU/BCA/002", "room": "R102"},
    {"day": "Friday", "start_time": "11:30", "end_time": "12:30", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A", "course": "BCA47111", "faculty": "BWU/BCA/003", "room": "R103"},
    {"day": "Friday", "start_time": "14:00", "end_time": "15:00", "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B", "course": "BCA47111", "faculty": "BWU/BCA/004", "room": "R104"},
]

# lecture_plan_data = generate_lecture_plan(class_routine_schedules)
# print(lecture_plan_data)

# for lp in lecture_plan_data[:]:
#     print(lp)


lecture_plan_schedules = [
    {
        "id": "BCA49112-M2-L2-BCA49112-BCA(H)-2023-A-BCA(H)-2023-1",
        "lecture": "BCA49112-M2-L2",
        "section": "BCA(H)-2023-A",
        "course": "BCA49112",
        "semester": "BCA(H)-2023-1",
        "module": "BCA49112-M2",
        "assigned_date": "2024-09-30",
        "assigned_faculties": [
            "BWU/BCA/001"
        ],
        "assigned_room": "R101",
        "assigned_method": "Quiz",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA49112-M1-L2-BCA49112-BCA(H)-2023-B-BCA(H)-2023-1",
        "lecture": "BCA49112-M1-L2",
        "section": "BCA(H)-2023-B",
        "course": "BCA49112",
        "semester": "BCA(H)-2023-1",
        "module": "BCA49112-M1",
        "assigned_date": "2024-09-30",
        "assigned_faculties": [
            "BWU/BCA/002"
        ],
        "assigned_room": "R102",
        "assigned_method": "Flip Class",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47111-M2-L2-BCA47111-BCA(H)-2024-A-BCA(H)-2024-1",
        "lecture": "BCA47111-M2-L2",
        "section": "BCA(H)-2024-A",
        "course": "BCA47111",
        "semester": "BCA(H)-2024-1",
        "module": "BCA47111-M2",
        "assigned_date": "2024-09-30",
        "assigned_faculties": [
            "BWU/BCA/003"
        ],
        "assigned_room": "R103",
        "assigned_method": "Hands-on Experience",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47111-M2-L2-BCA47111-BCA(H)-2024-B-BCA(H)-2024-1",
        "lecture": "BCA47111-M2-L2",
        "section": "BCA(H)-2024-B",
        "course": "BCA47111",
        "semester": "BCA(H)-2024-1",
        "module": "BCA47111-M2",
        "assigned_date": "2024-09-30",
        "assigned_faculties": [
            "BWU/BCA/004"
        ],
        "assigned_room": "R104",
        "assigned_method": "Flip Class",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47113-M2-L2-BCA47113-BCA(H)-2023-A-BCA(H)-2023-1",
        "lecture": "BCA47113-M2-L2",
        "section": "BCA(H)-2023-A",
        "course": "BCA47113",
        "semester": "BCA(H)-2023-1",
        "module": "BCA47113-M2",
        "assigned_date": "2024-10-01",
        "assigned_faculties": [
            "BWU/BCA/001"
        ],
        "assigned_room": "R101",
        "assigned_method": "Quiz",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47113-M1-L2-BCA47113-BCA(H)-2023-B-BCA(H)-2023-1",
        "lecture": "BCA47113-M1-L2",
        "section": "BCA(H)-2023-B",
        "course": "BCA47113",
        "semester": "BCA(H)-2023-1",
        "module": "BCA47113-M1",
        "assigned_date": "2024-10-01",
        "assigned_faculties": [
            "BWU/BCA/002"
        ],
        "assigned_room": "R102",
        "assigned_method": "Chalk & Talk",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA40202-M1-L1-BCA40202-BCA(H)-2024-A-BCA(H)-2024-1",
        "lecture": "BCA40202-M1-L1",
        "section": "BCA(H)-2024-A",
        "course": "BCA40202",
        "semester": "BCA(H)-2024-1",
        "module": "BCA40202-M1",
        "assigned_date": "2024-10-01",
        "assigned_faculties": [
            "BWU/BCA/003"
        ],
        "assigned_room": "R103",
        "assigned_method": "Presentation",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA40202-M2-L2-BCA40202-BCA(H)-2024-B-BCA(H)-2024-1",
        "lecture": "BCA40202-M2-L2",
        "section": "BCA(H)-2024-B",
        "course": "BCA40202",
        "semester": "BCA(H)-2024-1",
        "module": "BCA40202-M2",
        "assigned_date": "2024-10-01",
        "assigned_faculties": [
            "BWU/BCA/004"
        ],
        "assigned_room": "R104",
        "assigned_method": "Hands-on Experience",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA49112-M2-L2-BCA49112-BCA(H)-2023-A-BCA(H)-2023-1",
        "lecture": "BCA49112-M2-L2",
        "section": "BCA(H)-2023-A",
        "course": "BCA49112",
        "semester": "BCA(H)-2023-1",
        "module": "BCA49112-M2",
        "assigned_date": "2024-10-02",
        "assigned_faculties": [
            "BWU/BCA/001"
        ],
        "assigned_room": "R101",
        "assigned_method": "Quiz",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA49112-M1-L1-BCA49112-BCA(H)-2023-B-BCA(H)-2023-1",
        "lecture": "BCA49112-M1-L1",
        "section": "BCA(H)-2023-B",
        "course": "BCA49112",
        "semester": "BCA(H)-2023-1",
        "module": "BCA49112-M1",
        "assigned_date": "2024-10-02",
        "assigned_faculties": [
            "BWU/BCA/002"
        ],
        "assigned_room": "R102",
        "assigned_method": "Interactive Learning",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47111-M2-L2-BCA47111-BCA(H)-2024-A-BCA(H)-2024-1",
        "lecture": "BCA47111-M2-L2",
        "section": "BCA(H)-2024-A",
        "course": "BCA47111",
        "semester": "BCA(H)-2024-1",
        "module": "BCA47111-M2",
        "assigned_date": "2024-10-02",
        "assigned_faculties": [
            "BWU/BCA/003"
        ],
        "assigned_room": "R103",
        "assigned_method": "Hands-on Experience",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47111-M2-L1-BCA47111-BCA(H)-2024-B-BCA(H)-2024-1",
        "lecture": "BCA47111-M2-L1",
        "section": "BCA(H)-2024-B",
        "course": "BCA47111",
        "semester": "BCA(H)-2024-1",
        "module": "BCA47111-M2",
        "assigned_date": "2024-10-02",
        "assigned_faculties": [
            "BWU/BCA/004"
        ],
        "assigned_room": "R104",
        "assigned_method": "ICT",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47113-M1-L1-BCA47113-BCA(H)-2023-A-BCA(H)-2023-1",
        "lecture": "BCA47113-M1-L1",
        "section": "BCA(H)-2023-A",
        "course": "BCA47113",
        "semester": "BCA(H)-2023-1",
        "module": "BCA47113-M1",
        "assigned_date": "2024-10-03",
        "assigned_faculties": [
            "BWU/BCA/002"
        ],
        "assigned_room": "R101",
        "assigned_method": "Presentation",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47113-M2-L1-BCA47113-BCA(H)-2023-B-BCA(H)-2023-1",
        "lecture": "BCA47113-M2-L1",
        "section": "BCA(H)-2023-B",
        "course": "BCA47113",
        "semester": "BCA(H)-2023-1",
        "module": "BCA47113-M2",
        "assigned_date": "2024-10-03",
        "assigned_faculties": [
            "BWU/BCA/003"
        ],
        "assigned_room": "R102",
        "assigned_method": "Interactive Learning",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA40202-M1-L1-BCA40202-BCA(H)-2024-A-BCA(H)-2024-1",
        "lecture": "BCA40202-M1-L1",
        "section": "BCA(H)-2024-A",
        "course": "BCA40202",
        "semester": "BCA(H)-2024-1",
        "module": "BCA40202-M1",
        "assigned_date": "2024-10-03",
        "assigned_faculties": [
            "BWU/BCA/004"
        ],
        "assigned_room": "R103",
        "assigned_method": "Flip Class",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA40202-M2-L1-BCA40202-BCA(H)-2024-B-BCA(H)-2024-1",
        "lecture": "BCA40202-M2-L1",
        "section": "BCA(H)-2024-B",
        "course": "BCA40202",
        "semester": "BCA(H)-2024-1",
        "module": "BCA40202-M2",
        "assigned_date": "2024-10-03",
        "assigned_faculties": [
            "BWU/BCA/001"
        ],
        "assigned_room": "R104",
        "assigned_method": "Hands-on Experience",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA49112-M2-L2-BCA49112-BCA(H)-2023-A-BCA(H)-2023-1",
        "lecture": "BCA49112-M2-L2",
        "section": "BCA(H)-2023-A",
        "course": "BCA49112",
        "semester": "BCA(H)-2023-1",
        "module": "BCA49112-M2",
        "assigned_date": "2024-10-04",
        "assigned_faculties": [
            "BWU/BCA/001"
        ],
        "assigned_room": "R101",
        "assigned_method": "Presentation",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA49112-M2-L2-BCA49112-BCA(H)-2023-B-BCA(H)-2023-1",
        "lecture": "BCA49112-M2-L2",
        "section": "BCA(H)-2023-B",
        "course": "BCA49112",
        "semester": "BCA(H)-2023-1",
        "module": "BCA49112-M2",
        "assigned_date": "2024-10-04",
        "assigned_faculties": [
            "BWU/BCA/002"
        ],
        "assigned_room": "R102",
        "assigned_method": "ICT",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47111-M2-L1-BCA47111-BCA(H)-2024-A-BCA(H)-2024-1",
        "lecture": "BCA47111-M2-L1",
        "section": "BCA(H)-2024-A",
        "course": "BCA47111",
        "semester": "BCA(H)-2024-1",
        "module": "BCA47111-M2",
        "assigned_date": "2024-10-04",
        "assigned_faculties": [
            "BWU/BCA/003"
        ],
        "assigned_room": "R103",
        "assigned_method": "Quiz",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    },
    {
        "id": "BCA47111-M1-L1-BCA47111-BCA(H)-2024-B-BCA(H)-2024-1",
        "lecture": "BCA47111-M1-L1",
        "section": "BCA(H)-2024-B",
        "course": "BCA47111",
        "semester": "BCA(H)-2024-1",
        "module": "BCA47111-M1",
        "assigned_date": "2024-10-04",
        "assigned_faculties": [
            "BWU/BCA/004"
        ],
        "assigned_room": "R104",
        "assigned_method": "Presentation",
        "accomplision_status": False,
        "accomplished_date": None,
        "accomplished_faculties": [],
        "accomplished_room": None,
        "accomplished_method": None
    }
]


def fetch(config):
    try:
        if config['method'] == 'GET':
            response = requests.get(
                config['url'], headers=config.get('headers'))
        elif config['method'] == 'POST':
            response = requests.post(
                config['url'], json=config['data'], headers=config.get('headers'))

        return response.json()

    except Exception as e:
        print(f"Error: {e}")
        return None


BASE_URL = 'http://localhost:8000'
Token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0MjQ0NTg5LCJpYXQiOjE3NDM2Mzk3ODksImp0aSI6ImEyODhhM2U4ZTU5MTRmNzc5MWY4OTc1Njk1OWQ2MDY5IiwidXNlcl9pZCI6MX0.pqVEoZzlb7mBoE8dXLvc9mVZrkvDpirrUO2oq2WmqsA'

config = {
    "method": "POST",
    "url": f'{BASE_URL}/classes/add-lecture-plan/',
    "data": lecture_plan_schedules[:1][0],
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

response = fetch(config)
print(response)
