from typing import Union, Dict, List, Callable
from datetime import datetime, timedelta
from collections import defaultdict
import requests
import json
import random

BASE_URL = 'http://localhost:8000'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0MDkyODM2LCJpYXQiOjE3NDM0ODgwMzYsImp0aSI6ImMxNDAxMzZjMGJkMTQ3NThhMTQwN2JjNTQwNGNjNWQ0IiwidXNlcl9pZCI6MX0.gS1f9jUP5YMnq9Yh0-WDIZTsKKF5stgicGtfxnTm4yw'


def pretty_print_json(data: Dict):
    """Pretty print JSON data."""
    print(json.dumps(data, indent=4, sort_keys=True))


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


# Get access token
def get_access_token():
    config = {
        "method": "POST",
        "url": f'{BASE_URL}/auth/login/',
        "data": {
            "code": "406",
            "password": "admin"
        },
    }
    response = fetch(config)

    print("Response: ", response.get('success'))
    print("Access Token: ", response.get('access'))
    print("Refresh Token: ", response.get('refresh'))


# Add department
DEPARTMENTS = [
    {
        "id": "BCA(H)",
        "name": "Bachalore of Computer Application (Honors)"
    }
]
BATCHES = [
    {
        "department": "BCA(H)",
        "id": "BCA(H)-2023",
        "name": "BCA(H)-2023"
    },
    {
        "department": "BCA(H)",
        "id": "BCA(H)-2024",
        "name": "BCA(H)-2024"
    }
]
SECTIONS = [
    {
        "batch": "BCA(H)-2023",
        "id": "BCA(H)-2023-A",
        "name": "BCA(H)-2023-A"
    },
    {
        "batch": "BCA(H)-2023",
        "id": "BCA(H)-2023-B",
        "name": "BCA(H)-2023-B"
    },
    {
        "batch": "BCA(H)-2024",
        "id": "BCA(H)-2024-A",
        "name": "BCA(H)-2024-A"
    },
    {
        "batch": "BCA(H)-2024",
        "id": "BCA(H)-2024-B",
        "name": "BCA(H)-2024-B"
    }
]
SEMESTERS = [
    {
        "batch": "BCA(H)-2023",
        "id": "BCA(H)-2023-1",
        "name": "BCA(H)-2023-1"
    },
    {
        "batch": "BCA(H)-2024",
        "id": "BCA(H)-2024-1",
        "name": "BCA(H)-2024-1"
    }
]
STUDENTS = [
    {
        "code": "BWU/BCA/23/406",
        "current_semester": "BCA(H)-2023-1",
        "email": "bwubca23406@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Rahul Das",
        "password": "bwubca23406",
        "section": "BCA(H)-2023-A"
    },
    {
        "code": "BWU/BCA/23/407",
        "current_semester": "BCA(H)-2023-1",
        "email": "bwubca23407@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Rohit Das",
        "password": "bwubca23407",
        "section": "BCA(H)-2023-A"
    },
    {
        "code": "BWU/BCA/23/408",
        "current_semester": "BCA(H)-2023-1",
        "email": "bwubca23408@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Mohit Das",
        "password": "bwubca23408",
        "section": "BCA(H)-2023-B"
    },
    {
        "code": "BWU/BCA/23/409",
        "current_semester": "BCA(H)-2023-1",
        "email": "bwubca23409@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Jitesh Das",
        "password": "bwubca23409",
        "section": "BCA(H)-2023-B"
    },
    {
        "code": "BWU/BCA/24/410",
        "current_semester": "BCA(H)-2024-1",
        "email": "bwubca24410@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Ritesh Das",
        "password": "bwubca24410",
        "section": "BCA(H)-2024-A"
    },
    {
        "code": "BWU/BCA/24/411",
        "current_semester": "BCA(H)-2024-1",
        "email": "bwubca24411@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Nitesh Das",
        "password": "bwubca24411",
        "section": "BCA(H)-2024-A"
    },
    {
        "code": "BWU/BCA/24/412",
        "current_semester": "BCA(H)-2024-1",
        "email": "bwubca24412@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Nilesh Das",
        "password": "bwubca24412",
        "section": "BCA(H)-2024-B"
    },
    {
        "code": "BWU/BCA/24/413",
        "current_semester": "BCA(H)-2024-1",
        "email": "bwubca24413@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Milesh Das",
        "password": "bwubca24413",
        "section": "BCA(H)-2024-B"
    }
]
FACULTY = [
    {
        "code": "BWU/BCA/001",
        "department": "BCA(H)",
        "email": "bwubca001@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Prof. Rahul Das",
        "password": "bwubca001"
    },
    {
        "code": "BWU/BCA/002",
        "department": "BCA(H)",
        "email": "bwubca002@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Prof. Hitesh Das",
        "password": "bwubca002"
    },
    {
        "code": "BWU/BCA/003",
        "department": "BCA(H)",
        "email": "bwubca003@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Prof. Nitish Das",
        "password": "bwubca003"
    },
    {
        "code": "BWU/BCA/004",
        "department": "BCA(H)",
        "email": "bwubca004@brainwareuniversity.ac.in",
        "gender": "Male",
        "name": "Prof. Bitan Das",
        "password": "bwubca004"
    }
]
ACADEMICS = {
    "Course": [
            {
                "id": "BCA47111",
                "name": "Design and Analysis of Algorithm"
            },
        {
                "id": "BCA40202",
                "name": "Computer Network"
            },
        {
                "id": "BCA49112",
                "name": "PHP and MySQL Lab"
            },
        {
                "id": "BCA47113",
                "name": "Full-Stack Development-I"
            }
    ],
    "Module": [
        {
            "course": "BCA47111",
            "id": "BCA47111-M1",
            "name": "Module 1"
        },
        {
            "course": "BCA47111",
            "id": "BCA47111-M2",
            "name": "Module 2"
        },
        {
            "course": "BCA40202",
            "id": "BCA40202-M1",
            "name": "Module 1"
        },
        {
            "course": "BCA40202",
            "id": "BCA40202-M2",
            "name": "Module 2"
        },
        {
            "course": "BCA49112",
            "id": "BCA49112-M1",
            "name": "Module 1"
        },
        {
            "course": "BCA49112",
            "id": "BCA49112-M2",
            "name": "Module 2"
        },
        {
            "course": "BCA47113",
            "id": "BCA47113-M1",
            "name": "Module 1"
        },
        {
            "course": "BCA47113",
            "id": "BCA47113-M2",
            "name": "Module 2"
        }
    ],
    "Lecture": [
        {
            "course_outcome": "Course Outcome 1",
            "id": "BCA47111-M1-L1",
            "module": "BCA47111-M1",
            "name": "Lecture 1"
        },
        {
            "course_outcome": "Course Outcome 2",
            "id": "BCA47111-M1-L2",
            "module": "BCA47111-M1",
            "name": "Lecture 2"
        },
        {
            "course_outcome": "Course Outcome 1",
            "id": "BCA47111-M2-L1",
            "module": "BCA47111-M2",
            "name": "Lecture 1"
        },
        {
            "course_outcome": "Course Outcome 2",
            "id": "BCA47111-M2-L2",
            "module": "BCA47111-M2",
            "name": "Lecture 2"
        },
        {
            "course_outcome": "Course Outcome 1",
            "id": "BCA40202-M1-L1",
            "module": "BCA40202-M1",
            "name": "Lecture 1"
        },
        {
            "course_outcome": "Course Outcome 2",
            "id": "BCA40202-M1-L2",
            "module": "BCA40202-M1",
            "name": "Lecture 2"
        },
        {
            "course_outcome": "Course Outcome 1",
            "id": "BCA40202-M2-L1",
            "module": "BCA40202-M2",
            "name": "Lecture 1"
        },
        {
            "course_outcome": "Course Outcome 2",
            "id": "BCA40202-M2-L2",
            "module": "BCA40202-M2",
            "name": "Lecture 2"
        },
        {
            "course_outcome": "Course Outcome 1",
            "id": "BCA49112-M1-L1",
            "module": "BCA49112-M1",
            "name": "Lecture 1"
        },
        {
            "course_outcome": "Course Outcome 2",
            "id": "BCA49112-M1-L2",
            "module": "BCA49112-M1",
            "name": "Lecture 2"
        },
        {
            "course_outcome": "Course Outcome 1",
            "id": "BCA49112-M2-L1",
            "module": "BCA49112-M2",
            "name": "Lecture 1"
        },
        {
            "course_outcome": "Course Outcome 2",
            "id": "BCA49112-M2-L2",
            "module": "BCA49112-M2",
            "name": "Lecture 2"
        },
        {
            "course_outcome": "Course Outcome 1",
            "id": "BCA47113-M1-L1",
            "module": "BCA47113-M1",
            "name": "Lecture 1"
        },
        {
            "course_outcome": "Course Outcome 2",
            "id": "BCA47113-M1-L2",
            "module": "BCA47113-M1",
            "name": "Lecture 2"
        },
        {
            "course_outcome": "Course Outcome 1",
            "id": "BCA47113-M2-L1",
            "module": "BCA47113-M2",
            "name": "Lecture 1"
        },
        {
            "course_outcome": "Course Outcome 2",
            "id": "BCA47113-M2-L2",
            "module": "BCA47113-M2",
            "name": "Lecture 2"
        }
    ]
}
COURSE_SEMESTER = [
    {
        "add_courses": [
            "BCA47111",
            "BCA40202"
        ],
        "semester": "BCA(H)-2023-1"
    },
    {
        "add_courses": [
            "BCA49112",
            "BCA47113"
        ],
        "semester": "BCA(H)-2024-1"
    }
]
ROOMS = [
    'Room 101',
    'Room 102',
    'Room 103',
    'Room 104',
    'Room 105',
]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
PER_DAY_TIMESLOTS = [
    ("10:00", "11:00"),
    ("11:00", "12:00"),
    ("12:00", "13:00"),
    ("13:00", "14:00"),
    ("14:00", "15:00"),
    ("15:00", "16:00"),
]
ROOMS = ["Room 101", "Room 102", "Room 103", "Room 104", "Room 105"]
FACULTY_COURSE = [
    {
        "code": "BWU/BCA/001",
        "courses": ["BCA47111", "BCA40202"],
    },
    {
        "code": "BWU/BCA/002",
        "courses": ["BCA47111", "BCA40202"],
    },
    {
        "code": "BWU/BCA/003",
        "courses": ["BCA49112", "BCA47113"],
    },
    {
        "code": "BWU/BCA/004",
        "courses": ["BCA49112", "BCA47113"],
    },
]
SECTIONS_DATA = [
    {
        "section_id": "BCA(H)-2023-A",
        "semester_id": "BCA(H)-2023-1",
        "courses": ["BCA47111", "BCA40202"]
    },
    {
        "section_id": "BCA(H)-2023-B",
        "semester_id": "BCA(H)-2023-1",
        "courses": ["BCA47111", "BCA40202"]
    },
    {
        "section_id": "BCA(H)-2024-A",
        "semester_id": "BCA(H)-2024-1",
        "courses": ["BCA49112", "BCA47113"]
    },
    {
        "section_id": "BCA(H)-2024-B",
        "semester_id": "BCA(H)-2024-1",
        "courses": ["BCA49112", "BCA47113"]
    }
]


def create_department(departments) -> None:
    department_structures = []

    for d in departments:
        department_structures.append({
            "method": "POST",
            "url": f'{BASE_URL}/academics/add-department/',
            "data": d,
            "headers": {
                'Authorization': f"Bearer {TOKEN}"
            }
        })

    for d in department_structures:
        pretty_print_json(d | fetch(d))


# Add batch
def create_batch(departments) -> None:
    data = []

    def generate_batchs_from_deparment(departments, base_url, token, start_year, end_year):
        batches = []
        for department in departments:
            dept_id = department["id"]
            for year in range(start_year, end_year + 1):
                batch = {
                    "method": "POST",
                    "url": f"{base_url}/academics/add-batch/",
                    "data": {
                        "id": f"{dept_id}-{year}",
                        "name": f"{dept_id}-{year}",
                        "department": dept_id
                    },
                    "headers": {
                        "Authorization": f"Bearer {token}"
                    }
                }
                batches.append(batch)
                data.append(batch["data"])

        return batches

    batchs = generate_batchs_from_deparment(
        departments=departments,
        base_url=BASE_URL,
        token=TOKEN,
        start_year=2023,
        end_year=2024
    )

    pretty_print_json(data)
    for b in batchs:
        pretty_print_json(b | fetch(b))


# Add section
def create_section(batches) -> None:
    data = []

    def generate_section_requests(batches, base_url, token, sections_config=2):
        """
        Generate section requests with flexible section counts per batch

        :param batches: List of batch dictionaries (must contain 'id' field)
        :param base_url: Base URL for API endpoints
        :param token: Authorization token
        :param sections_config: Can be:
            - Integer: Fixed number of sections for all batches
            - Dictionary: {batch_id: number_of_sections}
            - Callable: Function that takes batch and returns section count
        :return: List of section request dictionaries
        """
        sections = []

        for batch in batches:
            batch_id = batch['id']

            # Determine number of sections for this batch
            if callable(sections_config):
                num_sections = sections_config(batch)
            elif isinstance(sections_config, dict):
                num_sections = sections_config.get(
                    batch_id, 0)  # Default to 0 if not found
            else:
                num_sections = sections_config

            # Generate sections for this batch
            for i in range(num_sections):
                section_char = chr(65 + i)  # 65 is ASCII for 'A'
                section_data = {
                    "method": "POST",
                    "url": f"{base_url}/academics/add-section/",
                    "data": {
                        "id": f"{batch_id}-{section_char}",
                        "name": f"{batch_id}-{section_char}",
                        "batch": batch_id
                    },
                    "headers": {
                        "Authorization": f"Bearer {token}"
                    }
                }
                sections.append(section_data)
                data.append(section_data["data"])

        return sections

    sections = generate_section_requests(
        batches=batches,
        base_url=BASE_URL,
        token=TOKEN,
        sections_config=2
    )

    pretty_print_json(data)
    for s in sections:
        print(fetch(s))


# Add semester
def create_semester(batches) -> None:
    data = []

    def generate_semester(batches, base_url, token, semesters_config=1):
        """
        Generate semester requests with flexible semester counts per batch

        :param batches: List of batch dictionaries (must contain 'data' with 'id')
        :param base_url: Base URL for API endpoints
        :param token: Authorization token
        :param semesters_config: Can be:
            - Integer: Fixed number of semesters for all batches
            - Dictionary: {batch_id: number_of_semesters}
            - Callable: Function that takes batch and returns semester count
        :return: List of semester request dictionaries
        """
        semesters = []

        for batch in batches:
            batch_id = batch['id']

            # Determine number of semesters for this batch
            if callable(semesters_config):
                num_semesters = semesters_config(batch)
            elif isinstance(semesters_config, dict):
                num_semesters = semesters_config.get(batch_id, 1)
            else:
                num_semesters = semesters_config

            # Generate semesters for this batch
            for sem_num in range(1, num_semesters + 1):
                semester_data = {
                    "method": "POST",
                    "url": f"{base_url}/academics/add-semester/",
                    "data": {
                        "id": f"{batch_id}-{sem_num}",
                        "name": f"{batch_id}-{sem_num}",
                        "batch": batch_id
                    },
                    "headers": {
                        "Authorization": f"Bearer {token}"
                    }
                }
                semesters.append(semester_data)
                data.append(semester_data["data"])

        return semesters

    semesters = generate_semester(
        batches=batches,
        base_url=BASE_URL,
        token=TOKEN
    )

    pretty_print_json(data)
    for s in semesters:
        pretty_print_json(s | fetch(s))


# Add New Student
def create_student(sections) -> None:
    data = []

    def generate_student(
        sections: List[dict],
        students_per_section: Union[int, Dict[str, int], Callable[[dict], int]],
        base_url: str,
        token: str,
        starting_numbers: Dict[int, int] = None,
        first_names: List[str] = None,
        gender: str = "Male",
        last_name: str = "Das",
    ) -> List[dict]:
        """
        Generate student requests with configurable parameters

        :param sections: List of section dictionaries (must contain 'data' with 'id' and 'batch')
        :param students_per_section: Config for number of students per section (int, dict, or callable)
        :param base_url: Base URL for API endpoints
        :param token: Authorization token
        :param starting_numbers: Dictionary mapping years to starting student numbers
        :param first_names: List of first names to use cyclically
        :param gender: Default gender for students
        :param last_name: Default last name for students
        :return: List of student request dictionaries
        """
        # Initialize default values
        starting_numbers = starting_numbers or {}
        current_numbers = starting_numbers.copy()
        first_names = first_names or ["Rahul", "Rohit", "Mohit", "Jitesh",
                                      "Ritesh", "Nitesh", "Nilesh", "Milesh"]
        name_index = 0
        students = []

        for section in sections:
            section_id = section['id']
            batch_id = section['batch']
            year = int(batch_id.split('-')[-1])

            # Determine number of students for this section
            if callable(students_per_section):
                num_students = students_per_section(section)
            elif isinstance(students_per_section, dict):
                num_students = students_per_section.get(section_id, 0)
            else:
                num_students = students_per_section

            # Get starting number for this year
            current_number = current_numbers.get(year, 1)

            for _ in range(num_students):
                # Generate student code
                yy = f"{year % 100:02d}"
                code = f"BWU/BCA/{yy}/{current_number:03d}"

                # Create student data
                student = {
                    "method": "POST",
                    "url": f"{base_url}/auth/add-student/",
                    "data": {
                        "code": code,
                        "password": code.lower().replace('/', ''),
                        "name": f"{first_names[name_index % len(first_names)]} {last_name}",
                        "email": f"{code.lower().replace('/', '')}@brainwareuniversity.ac.in",
                        "gender": gender,
                        "section": section_id,
                        "current_semester": f"{batch_id}-1"
                    },
                    "headers": {
                        "Authorization": f"Bearer {token}"
                    }
                }
                students.append(student)
                data.append(student["data"])

                # Update counters
                current_number += 1
                name_index += 1

            # Update current numbers for the year
            current_numbers[year] = current_number

        return students

    students = generate_student(
        sections=sections,
        students_per_section=2,
        base_url=BASE_URL,
        token=TOKEN,
        starting_numbers={
            2023: 406,  # Starting number for 2023 batches
            2024: 410   # Starting number for 2024 batches
        }
    )

    pretty_print_json(data)
    for s in students:
        pretty_print_json(s | fetch(s))


# Add Faculty
def create_faculty(departments) -> None:
    data = []

    def generate_faculty_requests(
        departments: list,
        num_faculty: Union[int, Dict[str, int], Callable[[dict], int]],
        base_url: str,
        token: str,
        starting_numbers: Dict[str, int] = None,
        first_names: List[str] = None,
        last_name: str = "Das",
        gender: str = "Male",
        name_prefix: str = "Prof."
    ) -> List[dict]:
        """
        Generate faculty requests with configurable parameters

        :param departments: List of department dictionaries (must contain 'id' field)
        :param num_faculty: Can be:
            - Integer: Fixed number per department
            - Dictionary: {department_id: number_of_faculty}
            - Callable: Function that takes department and returns faculty count
        :param base_url: Base URL for API endpoints
        :param token: Authorization token
        :param starting_numbers: Dictionary of {department_id: starting_number}
        :param first_names: List of first names to use cyclically
        :param last_name: Common last name for faculty
        :param gender: Default gender for faculty
        :param name_prefix: Prefix for faculty names
        :return: List of faculty request dictionaries
        """
        starting_numbers = starting_numbers or {}
        current_numbers = defaultdict(int)
        first_names = first_names or ["Rahul", "Hitesh", "Nitish", "Bitan",
                                      "Amit", "Suman", "Rajesh", "Vikash"]
        name_index = 0
        faculties = []

        for department in departments:
            dept_id = department['id']
            dept_code = dept_id.split(
                '(')[0].strip()  # Extract department code

            # Determine number of faculty for this department
            if callable(num_faculty):
                n = num_faculty(department)
            elif isinstance(num_faculty, dict):
                n = num_faculty.get(dept_id, 0)
            else:
                n = num_faculty

            # Get starting number for this department
            start_num = starting_numbers.get(dept_id, 1)

            for i in range(n):
                code_num = start_num + i
                faculty_code = f"BWU/{dept_code}/{code_num:03d}"

                faculty = {
                    "method": "POST",
                    "url": f"{base_url}/auth/add-faculty/",
                    "data": {
                        "code": faculty_code,
                        "password": faculty_code.lower().replace('/', ''),
                        "name": f"{name_prefix} {first_names[name_index % len(first_names)]} {last_name}",
                        "email": f"{faculty_code.lower().replace('/', '')}@brainwareuniversity.ac.in",
                        "gender": gender,
                        "department": dept_id
                    },
                    "headers": {
                        "Authorization": f"Bearer {token}"
                    }
                }
                faculties.append(faculty)
                data.append(faculty["data"])

                name_index += 1

            # Update current number for the department
            current_numbers[dept_id] = start_num + n

        return faculties

    faculty_requests = generate_faculty_requests(
        departments=departments,
        num_faculty=4,
        base_url=BASE_URL,
        token=TOKEN,
        starting_numbers={"BCA(H)": 1}
    )

    pretty_print_json(data)
    for f in faculty_requests:
        pretty_print_json(f | fetch(f))


# Add Course, Module, Lecture, and their associations
def create_course_module_lectures():
    data = {
        "Course": [],
        "Module": [],
        "Lecture": []
    }

    def generate_course_structures(courses: list, base_url: str, token: str) -> list:
        """
        Generate course, module, and lecture requests with consistent structure

        :param courses: List of course dictionaries with:
            - course_code: Unique course identifier (e.g., "BCA47111")
            - course_name: Full course name (e.g., "Design and Analysis of Algorithm")
            - semester: Associated semester (not used in this structure but included for reference)
        :param base_url: Base URL for API endpoints
        :param token: Authorization token
        :return: List of request dictionaries in order: course, modules, lectures
        """
        structures = []

        for course in courses:
            # Add course
            course_element = {
                "method": "POST",
                "url": f"{base_url}/courses/create-course/",
                "data": {
                    "id": course["course_code"],
                    "name": course["course_name"]
                },
                "headers": {
                    "Authorization": f"Bearer {token}"
                }
            }

            structures.append(course_element)
            data['Course'].append(course_element["data"])

            # Create modules (always 2 per course)
            for module_num in range(1, 3):
                module_id = f"{course['course_code']}-M{module_num}"

                # Add module
                module_element = {
                    "method": "POST",
                    "url": f"{base_url}/courses/create-module/",
                    "data": {
                        "id": module_id,
                        "name": f"Module {module_num}",
                        "course": course["course_code"]
                    },
                    "headers": {
                        "Authorization": f"Bearer {token}"
                    }
                }

                structures.append(module_element)
                data['Module'].append(module_element["data"])

                # Create lectures (always 2 per module)
                for lecture_num in range(1, 3):
                    # Add lecture

                    lecture_element = {
                        "method": "POST",
                        "url": f"{base_url}/courses/create-lecture/",
                        "data": {
                            "id": f"{module_id}-L{lecture_num}",
                            "name": f"Lecture {lecture_num}",
                            "course_outcome": f"Course Outcome {lecture_num}",
                            "module": module_id
                        },
                        "headers": {
                            "Authorization": f"Bearer {token}"
                        }
                    }

                    structures.append(lecture_element)
                    data['Lecture'].append(lecture_element["data"])

        return structures

    courses = [
        {
            "course_code": "BCA47111",
            "course_name": "Design and Analysis of Algorithm",
        },
        {
            "course_code": "BCA40202",
            "course_name": "Computer Network",
        },
        {
            "course_code": "BCA49112",
            "course_name": "PHP and MySQL Lab",
        },
        {
            "course_code": "BCA47113",
            "course_name": "Full-Stack Development-I",
        }
    ]

    # Generate the structure
    course_structures = generate_course_structures(
        courses=courses,
        base_url=BASE_URL,
        token=TOKEN
    )

    pretty_print_json(data)
    for structure in course_structures:
        pretty_print_json(structure | fetch(structure))


def add_course_to_semester():
    data = []

    def generate_course_semester_assignments(academics_data, semesters):
        """
        Generate course-semester assignments with even distribution of courses

        :param academics_data: Dictionary containing academic structure 
                            (must contain "Course" list with "id" fields)
        :param semesters: List of semester dictionaries (must contain "id" field)
        :return: List of course-semester assignment dictionaries
        """
        courses = academics_data["Course"]
        total_courses = len(courses)
        num_semesters = len(semesters)

        # Calculate distribution of courses per semester
        base, remainder = divmod(total_courses, num_semesters)

        assignments = []
        course_index = 0

        for i, semester in enumerate(semesters):
            # Determine number of courses for this semester
            num_courses = base + 1 if i < remainder else base

            # Get course IDs for this semester
            semester_courses = [
                course["id"]
                for course in courses[course_index:course_index + num_courses]
            ]

            config = {
                "method": "POST",
                "url": f"{BASE_URL}/academics/add-course-to-semester/",
                "data": {
                    "semester": semester["id"],
                    "add_courses": semester_courses
                },
                "headers": {
                    "Authorization": f"Bearer {TOKEN}"
                }
            }

            assignments.append(config)
            data.append(config["data"])

            course_index += num_courses

        return assignments

    course_semester = generate_course_semester_assignments(
        academics_data=ACADEMICS,
        semesters=SEMESTERS
    )

    pretty_print_json(data)
    for cs in course_semester:
        pretty_print_json(cs | fetch(cs))


def create_class_routine():
    routines = []

    def generate_routine():
        routine = defaultdict(lambda: defaultdict(list))

        # Track occupied faculty and rooms by day and slot
        # faculty_schedule[day][slot] = set(faculty_code)
        faculty_schedule = defaultdict(lambda: defaultdict(set))
        # section_schedule[day][slot] = set(section_id)
        section_schedule = defaultdict(lambda: defaultdict(set))

        for section in SECTIONS_DATA:
            section_id = section["section_id"]
            courses = section["courses"]

            for day in DAYS:
                slots = random.sample(PER_DAY_TIMESLOTS, 4)

                for slot in slots:
                    start, end = slot
                    course = random.choice(courses)

                    # Find available faculty for course
                    available_faculty = [
                        f["code"] for f in FACULTY_COURSE
                        if course in f["courses"] and f["code"] not in faculty_schedule[day][slot]
                    ]

                    if not available_faculty:
                        continue  # Skip if no faculty available

                    faculty = random.choice(available_faculty)
                    room = random.choice(ROOMS)

                    # Register the class
                    routine[section_id][day].append({
                        "time": f"{start} - {end}",
                        "course": course,
                        "faculty": faculty,
                        "room": room
                    })

                    # Update occupied faculty & section
                    faculty_schedule[day][slot].add(faculty)
                    section_schedule[day][slot].add(section_id)

        return routine

    CLASS_ROUTINE = generate_routine()

    for section_id, days in CLASS_ROUTINE.items():
        for day, slots in days.items():
            for slot in slots:
                course = slot["course"]
                faculty = slot["faculty"]
                room = slot["room"]

                routine_element = {
                    "method": "POST",
                    "url": f"{BASE_URL}/classes/add-class-routine/",
                    "data": {
                        "section": section_id,
                        "semester": section_id.split('-')[0] + '-' + section_id.split('-')[1] + "-1",
                        "day": day,
                        "start_time": slot["time"].split('-')[0].strip(),
                        "end_time": slot["time"].split('-')[1].strip(),
                        "course": course,
                        "faculty": faculty,
                        "room": room
                    },
                    "headers": {
                        'Authorization': f"Bearer {TOKEN}"
                    }
                }

                routines.append(routine_element)

    for index, routine in enumerate(routines[:]):
        response = fetch(routine)
        pretty_print_json(routine | response)
        routines[index]["id"] = response["id"]
    print("Total Classes Created:", len(routines))

    with open("class_routine.json", "w") as f:
        json.dump(routines, f, indent=4)
    print("Class Routine JSON file created.")


def create_lecture_routine():
    teaching_methods = ["Lecture", "Discussion", "Hands-on", "Presentation"]

    def get_next_weekday(start_date, weekday_name):
        days = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_index = days.index(weekday_name)
        current_index = start_date.weekday()
        delta_days = (weekday_index - current_index + 7) % 7
        return start_date + timedelta(days=delta_days)

    def generate_django_model_lecture_plan(routine_data, semester_start_date_str):
        semester_start_date = datetime.strptime(
            semester_start_date_str, "%d/%m/%Y")
        lecture_plans = []

        for entry in routine_data:
            data = entry["data"]
            course = data["course"]
            faculty = data["faculty"]
            section = data["section"]
            semester = data["semester"]
            room = data["room"]
            day = data["day"]

            base_date = get_next_weekday(semester_start_date, day)

            for module_num in range(1, 3):
                for lecture_num in range(1, 3):
                    plan = {
                        "method": "POST",
                        "url": f"{BASE_URL}/classes/add-lecture-plan/",
                        "data": {
                            "referrence_class_routine": entry["id"],
                            "course": course,
                            "module": f"{course}-M{module_num}",
                            "lecture": f"{course}-M{module_num}-L{lecture_num}",
                            "section": section,
                            "semester": semester,
                            "assigned_date": (base_date + timedelta(weeks=(module_num - 1) * 2 + (lecture_num - 1))).strftime("%Y-%m-%d"),
                            "assigned_faculties": [faculty],
                            "assigned_room": room,
                            "assigned_method": random.choice(teaching_methods),
                            "accomplision_status": False,
                            "accomplished_date": None,
                            "accomplished_faculties": [],
                            "accomplished_room": None,
                            "accomplished_method": None
                        },
                        "headers": {
                            'Authorization': f"Bearer {TOKEN}"
                        }
                    }
                    lecture_plans.append(plan)

        return lecture_plans

    class_routine = None

    with open("class_routine.json", "r") as file:
        class_routine = json.load(file)

    plans = generate_django_model_lecture_plan(class_routine, "01/01/2024")

    for p in plans[:]:
        print(json.dumps(fetch(p), indent=4))

    print(len(plans))


# get_access_token()
# create_department(DEPARTMENTS)
# create_batch(DEPARTMENTS)
# create_section(BATCHES)
# create_semester(BATCHES)
# create_student(SECTIONS)
# create_faculty(DEPARTMENTS)
# create_course_module_lectures()
# add_course_to_semester()
# create_class_routine()
# create_lecture_routine()
