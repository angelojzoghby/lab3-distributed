from fastapi import FastAPI
import time

app = FastAPI()

courses = {}
next_id = 1

@app.post("/courses")
def create_course(course: dict):
    global next_id
    start = time.time()
    course["id"] = next_id
    courses[next_id] = course
    next_id += 1

    return {
        "msg": "course added",
        "course": course,
        "time": time.time() - start
    }

@app.get("/courses")
def get_all():
    return list(courses.values())

@app.get("/courses/{cid}")
def get_one(cid: int):
    return courses.get(cid, {"error": "course not found"})

@app.delete("/courses/{cid}")
def delete_course(cid: int):
    if cid in courses:
        del courses[cid]
        return {"msg": "course deleted"}
    return {"error": "not found"}
