import requests

BASE_URL = 'http://localhost:8000'
Token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0MDkyODM2LCJpYXQiOjE3NDM0ODgwMzYsImp0aSI6ImMxNDAxMzZjMGJkMTQ3NThhMTQwN2JjNTQwNGNjNWQ0IiwidXNlcl9pZCI6MX0.gS1f9jUP5YMnq9Yh0-WDIZTsKKF5stgicGtfxnTm4yw'


# Get access token
get_access_token = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/login/',
    "data": {
        "code": "406",
        "password": "admin"
    },
}

# Add department
add_department = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-department/',
    "data": {
        "id": "BCA(H)",
        "name": "Bachalore of Computer Application (Honors)"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add batch
add_batch_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-batch/',
    "data": {
        "id": "BCA(H)-2023",
        "name": "2023",
        "department": "BCA(H)"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_batch_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-batch/',
    "data": {
        "id": "BCA(H)-2024",
        "name": "2024",
        "department": "BCA(H)"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add section
add_section_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-section/',
    "data": {
        "id": "BCA(H)-2023-A",
        "name": "A",
        "batch": "BCA(H)-2023"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_section_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-section/',
    "data": {
        "id": "BCA(H)-2023-B",
        "name": "B",
        "batch": "BCA(H)-2023"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_section_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-section/',
    "data": {
        "id": "BCA(H)-2024-A",
        "name": "A",
        "batch": "BCA(H)-2024"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_section_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-section/',
    "data": {
        "id": "BCA(H)-2024-B",
        "name": "B",
        "batch": "BCA(H)-2024"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add semester
add_semester_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-semester/',
    "data": {
        "id": "BCA(H)-2023-1",
        "name": "1",
        "batch": "BCA(H)-2023"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_semester_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-semester/',
    "data": {
        "id": "BCA(H)-2024-1",
        "name": "1",
        "batch": "BCA(H)-2024"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add sections to semester
add_section_to_semester_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-sections-to-semester/',
    "data": {
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_section_to_semester_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-sections-to-semester/',
    "data": {
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_section_to_semester_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-sections-to-semester/',
    "data": {
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_section_to_semester_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-sections-to-semester/',
    "data": {
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add New Student
add_student_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-student/',
    "data": {
        "code": "BWU/BCA/23/406",
        "password": "bwubca23406",
        "name": "Rahul Das",
        "email": "bwubca23406@brainwareuniversity.ac.in",
        "gender": "Male",
        "section": "BCA(H)-2023-A",
        "current_semester": "BCA(H)-2023-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_student_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-student/',
    "data": {
        "code": "BWU/BCA/23/407",
        "password": "bwubca23407",
        "name": "Rohit Das",
        "email": "bwubca23407@brainwareuniversity.ac.in",
        "gender": "Male",
        "section": "BCA(H)-2023-A",
        "current_semester": "BCA(H)-2023-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_student_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-student/',
    "data": {
        "code": "BWU/BCA/23/408",
        "password": "bwubca23408",
        "name": "Mohit Das",
        "email": "bwubca23408@brainwareuniversity.ac.in",
        "gender": "Male",
        "section": "BCA(H)-2023-B",
        "current_semester": "BCA(H)-2023-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_student_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-student/',
    "data": {
        "code": "BWU/BCA/23/409",
        "password": "bwubca23409",
        "name": "Jitesh Das",
        "email": "bwubca23409@brainwareuniversity.ac.in",
        "gender": "Male",
        "section": "BCA(H)-2023-B",
        "current_semester": "BCA(H)-2023-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_student_5 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-student/',
    "data": {
        "code": "BWU/BCA/24/410",
        "password": "bwubca24410",
        "name": "Ritesh Das",
        "email": "bwubca24410@brainwareuniversity.ac.in",
        "gender": "Male",
        "section": "BCA(H)-2024-A",
        "current_semester": "BCA(H)-2024-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_student_6 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-student/',
    "data": {
        "code": "BWU/BCA/24/411",
        "password": "bwubca24411",
        "name": "Nitesh Das",
        "email": "bwubca24411@brainwareuniversity.ac.in",
        "gender": "Male",
        "section": "BCA(H)-2024-A",
        "current_semester": "BCA(H)-2024-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_student_7 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-student/',
    "data": {
        "code": "BWU/BCA/24/412",
        "password": "bwubca24412",
        "name": "Nilesh Das",
        "email": "bwubca24412@brainwareuniversity.ac.in",
        "gender": "Male",
        "section": "BCA(H)-2024-B",
        "current_semester": "BCA(H)-2024-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_student_8 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-student/',
    "data": {
        "code": "BWU/BCA/24/413",
        "password": "bwubca24413",
        "name": "Milesh Das",
        "email": "bwubca24413@brainwareuniversity.ac.in",
        "gender": "Male",
        "section": "BCA(H)-2024-B",
        "current_semester": "BCA(H)-2024-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Faculty
add_faculty_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-faculty/',
    "data": {
        "code": "BWU/BCA/001",
        "password": "bwubca001",
        "name": "Prof. Rahul Das",
        "email": "bwubca001@brainwareuniversity.ac.in",
        "gender": "Male",
        "department": "BCA(H)"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_faculty_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-faculty/',
    "data": {
        "code": "BWU/BCA/002",
        "password": "bwubca002",
        "name": "Prof. Hitesh Das",
        "email": "bwubca002@brainwareuniversity.ac.in",
        "gender": "Male",
        "department": "BCA(H)"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_faculty_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-faculty/',
    "data": {
        "code": "BWU/BCA/003",
        "password": "bwubca003",
        "name": "Prof. Nitish Das",
        "email": "bwubca003@brainwareuniversity.ac.in",
        "gender": "Male",
        "department": "BCA(H)"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_faculty_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/auth/add-faculty/',
    "data": {
        "code": "BWU/BCA/004",
        "password": "bwubca004",
        "name": "Prof. Bitan Das",
        "email": "bwubca004@brainwareuniversity.ac.in",
        "gender": "Male",
        "department": "BCA(H)"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Course 1
batch_1_add_course_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-course/',
    "data": {
        "id": "BCA47111",
        "name": "Design and Analysis of Algorithm"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Module 1
batch_1_add_module_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-module/',
    "data": {
        "id": "BCA47111-M1",
        "name": "Module 1",
        "course": "BCA47111"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 1
batch_1_add_lecture_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA47111-M1-L1",
        "name": "Lecture 1",
        "course_outcome": "Course Outcome 1",
        "module": "BCA47111-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 2
batch_1_add_lecture_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA47111-M1-L2",
        "name": "Lecture 2",
        "course_outcome": "Course Outcome 2",
        "module": "BCA47111-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Module 1
batch_1_add_module_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-module/',
    "data": {
        "id": "BCA47111-M2",
        "name": "Module 2",
        "course": "BCA47111"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 1
batch_1_add_lecture_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA47111-M2-L1",
        "name": "Lecture 1",
        "course_outcome": "Course Outcome 1",
        "module": "BCA47111-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 2
batch_1_add_lecture_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA47111-M2-L2",
        "name": "Lecture 2",
        "course_outcome": "Course Outcome 2",
        "module": "BCA47111-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Course 2
batch_1_add_course_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-course/',
    "data": {
        "id": "BCA40202",
        "name": "Computer Network"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Module 1
batch_1_add_module_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-module/',
    "data": {
        "id": "BCA40202-M1",
        "name": "Module 1",
        "course": "BCA40202"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 1
batch_1_add_lecture_5 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA40202-M1-L1",
        "name": "Lecture 1",
        "course_outcome": "Course Outcome 1",
        "module": "BCA40202-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 2
batch_1_add_lecture_6 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA40202-M1-L2",
        "name": "Lecture 2",
        "course_outcome": "Course Outcome 2",
        "module": "BCA40202-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Module 2
batch_1_add_module_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-module/',
    "data": {
        "id": "BCA40202-M2",
        "name": "Module 2",
        "course": "BCA40202"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 1
batch_1_add_lecture_7 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA40202-M2-L1",
        "name": "Lecture 1",
        "course_outcome": "Course Outcome 1",
        "module": "BCA40202-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 2
batch_1_add_lecture_8 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA40202-M2-L2",
        "name": "Lecture 2",
        "course_outcome": "Course Outcome 2",
        "module": "BCA40202-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_1_add_lecture_to_module_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA47111-M1",
        "lecture": "BCA47111-M1-L1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_1_add_lecture_to_module_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA47111-M1",
        "lecture": "BCA47111-M1-L2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_1_add_lecture_to_module_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA47111-M2",
        "lecture": "BCA47111-M2-L1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_1_add_lecture_to_module_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA47111-M2",
        "lecture": "BCA47111-M2-L2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add module to course
batch_1_add_module_to_course_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-module-to-course/',
    "data": {
        "course": "BCA47111",
        "module": "BCA47111-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add module to course
batch_1_add_module_to_course_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-module-to-course/',
    "data": {
        "course": "BCA47111",
        "module": "BCA47111-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_1_add_lecture_to_module_5 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA40202-M1",
        "lecture": "BCA40202-M1-L1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_1_add_lecture_to_module_6 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA40202-M1",
        "lecture": "BCA40202-M1-L2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_1_add_lecture_to_module_7 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA40202-M2",
        "lecture": "BCA40202-M2-L1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_1_add_lecture_to_module_8 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA40202-M2",
        "lecture": "BCA40202-M2-L2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add module to course
batch_1_add_module_to_course_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-module-to-course/',
    "data": {
        "course": "BCA40202",
        "module": "BCA40202-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add module to course
batch_1_add_module_to_course_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-module-to-course/',
    "data": {
        "course": "BCA40202",
        "module": "BCA40202-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Course 1
batch_2_add_course_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-course/',
    "data": {
        "id": "BCA49112",
        "name": "PHP and MySQL Lab"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Module 1
batch_2_add_module_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-module/',
    "data": {
        "id": "BCA49112-M1",
        "name": "Module 1",
        "course": "BCA49112"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 1
batch_2_add_lecture_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA49112-M1-L1",
        "name": "Lecture 1",
        "course_outcome": "Course Outcome 1",
        "module": "BCA49112-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 2
batch_2_add_lecture_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA49112-M1-L2",
        "name": "Lecture 2",
        "course_outcome": "Course Outcome 2",
        "module": "BCA49112-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Module 1
batch_2_add_module_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-module/',
    "data": {
        "id": "BCA49112-M2",
        "name": "Module 2",
        "course": "BCA49112"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 1
batch_2_add_lecture_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA49112-M2-L1",
        "name": "Lecture 1",
        "course_outcome": "Course Outcome 1",
        "module": "BCA49112-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 2
batch_2_add_lecture_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA49112-M2-L2",
        "name": "Lecture 2",
        "course_outcome": "Course Outcome 2",
        "module": "BCA49112-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Course 2
batch_2_add_course_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-course/',
    "data": {
        "id": "BCA47113",
        "name": "Full-Stack Development-I"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Module 1
batch_2_add_module_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-module/',
    "data": {
        "id": "BCA47113-M1",
        "name": "Module 1",
        "course": "BCA47113"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 1
batch_2_add_lecture_5 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA47113-M1-L1",
        "name": "Lecture 1",
        "course_outcome": "Course Outcome 1",
        "module": "BCA47113-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 2
batch_2_add_lecture_6 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA47113-M1-L2",
        "name": "Lecture 2",
        "course_outcome": "Course Outcome 2",
        "module": "BCA47113-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Module 2
batch_2_add_module_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-module/',
    "data": {
        "id": "BCA47113-M2",
        "name": "Module 2",
        "course": "BCA47113"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 1
batch_2_add_lecture_7 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA47113-M2-L1",
        "name": "Lecture 1",
        "course_outcome": "Course Outcome 1",
        "module": "BCA47113-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add Lecture 2
batch_2_add_lecture_8 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/create-lecture/',
    "data": {
        "id": "BCA47113-M2-L2",
        "name": "Lecture 2",
        "course_outcome": "Course Outcome 2",
        "module": "BCA47113-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_2_add_lecture_to_module_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA49112-M1",
        "lecture": "BCA49112-M1-L1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_2_add_lecture_to_module_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA49112-M1",
        "lecture": "BCA49112-M1-L2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_2_add_lecture_to_module_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA49112-M2",
        "lecture": "BCA49112-M2-L1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_2_add_lecture_to_module_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA49112-M2",
        "lecture": "BCA49112-M2-L2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add module to course
batch_2_add_module_to_course_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-module-to-course/',
    "data": {
        "course": "BCA49112",
        "module": "BCA49112-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add module to course
batch_2_add_module_to_course_2 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-module-to-course/',
    "data": {
        "course": "BCA49112",
        "module": "BCA49112-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_2_add_lecture_to_module_5 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA47113-M1",
        "lecture": "BCA47113-M1-L1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_2_add_lecture_to_module_6 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA47113-M1",
        "lecture": "BCA47113-M1-L2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_2_add_lecture_to_module_7 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA47113-M2",
        "lecture": "BCA47113-M2-L1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add lecture to module
batch_2_add_lecture_to_module_8 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-lecture-to-module/',
    "data": {
        "module": "BCA47113-M2",
        "lecture": "BCA47113-M2-L2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add module to course
batch_2_add_module_to_course_3 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-module-to-course/',
    "data": {
        "course": "BCA47113",
        "module": "BCA47113-M1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add module to course
batch_2_add_module_to_course_4 = {
    "method": "POST",
    "url": f'{BASE_URL}/courses/add-module-to-course/',
    "data": {
        "course": "BCA47113",
        "module": "BCA47113-M2"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

# Add course to semester
add_course_1_semester_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-course-to-semester/',
    "data": {
        "course": "BCA47111",
        "semester": "BCA(H)-2023-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_course_2_semester_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-course-to-semester/',
    "data": {
        "course": "BCA40202",
        "semester": "BCA(H)-2023-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_course_3_semester_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-course-to-semester/',
    "data": {
        "course": "BCA49112",
        "semester": "BCA(H)-2024-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}
add_course_4_semester_1 = {
    "method": "POST",
    "url": f'{BASE_URL}/academics/add-course-to-semester/',
    "data": {
        "course": "BCA47113",
        "semester": "BCA(H)-2024-1"
    },
    "headers": {
        'Authorization': f"Bearer {Token}"
    }
}

class_routine_schedules = [
    {
        "day": "Monday",
        "start_time": "09:00",
        "end_time": "10:00",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A",
        "course": "BCA49112",
        "faculty": "BWU/BCA/001",
        "room": "R101"
    },
    {
        "day": "Monday",
        "start_time": "10:15",
        "end_time": "11:15",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B",
        "course": "BCA49112",
        "faculty": "BWU/BCA/002",
        "room": "R102"
    },
    {
        "day": "Monday",
        "start_time": "11:30",
        "end_time": "12:30",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A",
        "course": "BCA47111",
        "faculty": "BWU/BCA/003",
        "room": "R103"
    },
    {
        "day": "Monday",
        "start_time": "14:00",
        "end_time": "15:00",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B",
        "course": "BCA47111",
        "faculty": "BWU/BCA/004",
        "room": "R104"
    },
    {
        "day": "Tuesday",
        "start_time": "09:00",
        "end_time": "10:00",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A",
        "course": "BCA47113",
        "faculty": "BWU/BCA/001",
        "room": "R101"
    },
    {
        "day": "Tuesday",
        "start_time": "10:15",
        "end_time": "11:15",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B",
        "course": "BCA47113",
        "faculty": "BWU/BCA/002",
        "room": "R102"
    },
    {
        "day": "Tuesday",
        "start_time": "11:30",
        "end_time": "12:30",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A",
        "course": "BCA40202",
        "faculty": "BWU/BCA/003",
        "room": "R103"
    },
    {
        "day": "Tuesday",
        "start_time": "14:00",
        "end_time": "15:00",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B",
        "course": "BCA40202",
        "faculty": "BWU/BCA/004",
        "room": "R104"
    },
    {
        "day": "Wednesday",
        "start_time": "09:00",
        "end_time": "10:00",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A",
        "course": "BCA49112",
        "faculty": "BWU/BCA/001",
        "room": "R101"
    },
    {
        "day": "Wednesday",
        "start_time": "10:15",
        "end_time": "11:15",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B",
        "course": "BCA49112",
        "faculty": "BWU/BCA/002",
        "room": "R102"
    },
    {
        "day": "Wednesday",
        "start_time": "11:30",
        "end_time": "12:30",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A",
        "course": "BCA47111",
        "faculty": "BWU/BCA/003",
        "room": "R103"
    },
    {
        "day": "Wednesday",
        "start_time": "14:00",
        "end_time": "15:00",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B",
        "course": "BCA47111",
        "faculty": "BWU/BCA/004",
        "room": "R104"
    },
    {
        "day": "Thursday",
        "start_time": "09:00",
        "end_time": "10:00",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A",
        "course": "BCA47113",
        "faculty": "BWU/BCA/002",
        "room": "R101"
    },
    {
        "day": "Thursday",
        "start_time": "10:15",
        "end_time": "11:15",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B",
        "course": "BCA47113",
        "faculty": "BWU/BCA/003",
        "room": "R102"
    },
    {
        "day": "Thursday",
        "start_time": "11:30",
        "end_time": "12:30",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A",
        "course": "BCA40202",
        "faculty": "BWU/BCA/004",
        "room": "R103"
    },
    {
        "day": "Thursday",
        "start_time": "14:00",
        "end_time": "15:00",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B",
        "course": "BCA40202",
        "faculty": "BWU/BCA/001",
        "room": "R104"
    },
    {
        "day": "Friday",
        "start_time": "09:00",
        "end_time": "10:00",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-A",
        "course": "BCA49112",
        "faculty": "BWU/BCA/001",
        "room": "R101"
    },
    {
        "day": "Friday",
        "start_time": "10:15",
        "end_time": "11:15",
        "semester": "BCA(H)-2023-1",
        "section": "BCA(H)-2023-B",
        "course": "BCA49112",
        "faculty": "BWU/BCA/002",
        "room": "R102"
    },
    {
        "day": "Friday",
        "start_time": "11:30",
        "end_time": "12:30",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-A",
        "course": "BCA47111",
        "faculty": "BWU/BCA/003",
        "room": "R103"
    },
    {
        "day": "Friday",
        "start_time": "14:00",
        "end_time": "15:00",
        "semester": "BCA(H)-2024-1",
        "section": "BCA(H)-2024-B",
        "course": "BCA47111",
        "faculty": "BWU/BCA/004",
        "room": "R104"
    }
]


def add_class_routine_into_schedules_list(routines):
    schedules = []

    for routine in routines:
        schedules.append({
            "method": "POST",
            "url": f'{BASE_URL}/classes/add-class-routine/',
            "data": {
                "id": f"{routine['section']}-{routine['course']}-{routine['day']}"
            } | routine,
            "headers": {
                'Authorization': f"Bearer {Token}"
            }
        })

    return schedules


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


print(fetch(get_access_token))
# print(fetch(add_department))
# print(fetch(add_batch_1))
# print(fetch(add_batch_2))
# print(fetch(add_section_1))
# print(fetch(add_section_2))
# print(fetch(add_section_3))
# print(fetch(add_section_4))
# print(fetch(add_semester_1))
# print(fetch(add_semester_2))
# print(fetch(add_section_to_semester_1))
# print(fetch(add_section_to_semester_2))
# print(fetch(add_section_to_semester_3))
# print(fetch(add_section_to_semester_4))
# print(fetch(add_student_1))
# print(fetch(add_student_2))
# print(fetch(add_student_3))
# print(fetch(add_student_4))
# print(fetch(add_student_5))
# print(fetch(add_student_6))
# print(fetch(add_student_7))
# print(fetch(add_student_8))
# print(fetch(add_faculty_1))
# print(fetch(add_faculty_2))
# print(fetch(add_faculty_3))
# print(fetch(add_faculty_4))
# print(fetch(batch_1_add_course_1))
# print(fetch(batch_1_add_module_1))
# print(fetch(batch_1_add_lecture_1))
# print(fetch(batch_1_add_lecture_2))
# print(fetch(batch_1_add_module_2))
# print(fetch(batch_1_add_lecture_3))
# print(fetch(batch_1_add_lecture_4))
# print(fetch(batch_1_add_course_2))
# print(fetch(batch_1_add_module_3))
# print(fetch(batch_1_add_lecture_5))
# print(fetch(batch_1_add_lecture_6))
# print(fetch(batch_1_add_module_4))
# print(fetch(batch_1_add_lecture_7))
# print(fetch(batch_1_add_lecture_8))
# print(fetch(batch_1_add_lecture_to_module_1))
# print(fetch(batch_1_add_lecture_to_module_2))
# print(fetch(batch_1_add_lecture_to_module_3))
# print(fetch(batch_1_add_lecture_to_module_4))
# print(fetch(batch_1_add_module_to_course_1))
# print(fetch(batch_1_add_module_to_course_2))
# print(fetch(batch_1_add_lecture_to_module_5))
# print(fetch(batch_1_add_lecture_to_module_6))
# print(fetch(batch_1_add_lecture_to_module_7))
# print(fetch(batch_1_add_lecture_to_module_8))
# print(fetch(batch_1_add_module_to_course_3))
# print(fetch(batch_1_add_module_to_course_4))
# print(fetch(batch_2_add_course_1))
# print(fetch(batch_2_add_module_1))
# print(fetch(batch_2_add_lecture_1))
# print(fetch(batch_2_add_lecture_2))
# print(fetch(batch_2_add_module_2))
# print(fetch(batch_2_add_lecture_3))
# print(fetch(batch_2_add_lecture_4))
# print(fetch(batch_2_add_course_2))
# print(fetch(batch_2_add_module_3))
# print(fetch(batch_2_add_lecture_5))
# print(fetch(batch_2_add_lecture_6))
# print(fetch(batch_2_add_module_4))
# print(fetch(batch_2_add_lecture_7))
# print(fetch(batch_2_add_lecture_8))
# print(fetch(batch_2_add_lecture_to_module_1))
# print(fetch(batch_2_add_lecture_to_module_2))
# print(fetch(batch_2_add_lecture_to_module_3))
# print(fetch(batch_2_add_lecture_to_module_4))
# print(fetch(batch_2_add_module_to_course_1))
# print(fetch(batch_2_add_module_to_course_2))
# print(fetch(batch_2_add_lecture_to_module_5))
# print(fetch(batch_2_add_lecture_to_module_6))
# print(fetch(batch_2_add_lecture_to_module_7))
# print(fetch(batch_2_add_lecture_to_module_8))
# print(fetch(batch_2_add_module_to_course_3))
# print(fetch(batch_2_add_module_to_course_4))
# print(fetch(add_course_1_semester_1))
# print(fetch(add_course_2_semester_1))
# print(fetch(add_course_3_semester_1))
# print(fetch(add_course_4_semester_1))
# for schedule in add_class_routine_into_schedules_list(class_routine_schedules):
#     print(fetch(schedule))
