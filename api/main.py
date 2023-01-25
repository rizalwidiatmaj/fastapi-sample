from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from typing import Union


app = FastAPI()

courses = {
    1: {
        "title": "Modern History",
        "teacher": "Ms. Doe",
        "students": ["Harry", "Frodo"],
        "level": "advanced"
    },
    2: {
        "title": "Mathematics",
        "teacher": "Mr.Davies",
        "students": ["John", "Bruce"],
        "level": "beginner"
    },
    3: {
        "title": "Geography",
        "teacher": "Ms. Apple",
        "students": ["Micheal", "Bruce"],
        "level": "advanced"
    }
}


@app.get("/api/hello")
def hello():
    return {"message": "Hello World"}


@app.get("/api/courses")
def get_courses(level: Union[str, None]):
    if level:
        level_courses = []
        for index in courses.keys():
            if courses[index]['level'] == level:
                level_courses.append(courses[index])
        return level_courses
    return courses


@app.get("/api/courses/{course_id}")
def get_course(course_id: int):
    if course_id in courses:
        return courses[course_id]
    else:
        raise HTTPException(status_code=404, detail="course not found")
