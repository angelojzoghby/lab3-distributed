from fastapi import FastAPI
import requests
import time

app = FastAPI()

USER_SERVICE = "http://user-service:8000"
COURSE_SERVICE = "http://course-service:8000"

enrollments = {} 

@app.post("/enroll")
def enroll(data: dict):
    start = time.time()

    student = data["student_id"]
    course = data["course_id"]

    user_resp = requests.get(f"{USER_SERVICE}/users").json()
    if not any(u.get("id") == student for u in user_resp):
        return {"error": "student does not exist"}

    course_resp = requests.get(f"{COURSE_SERVICE}/courses/{course}").json()
    if "error" in course_resp:
        return {"error": "course does not exist"}

    enrollments.setdefault(student, [])
    enrollments[student].append(course)

    return {
        "msg": "enrolled",
        "time": time.time() - start
    }

@app.get("/students/{sid}/courses")
def get_student_courses(sid: int):
    return enrollments.get(sid, [])
