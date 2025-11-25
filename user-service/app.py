from fastapi import FastAPI
import time

app = FastAPI()

users = []

@app.post("/register")
def register(user: dict):
    start = time.time()
    users.append(user)
    return {
        "msg": "user registered",
        "time": time.time() - start
    }

@app.post("/login")
def login(creds: dict):
    start = time.time()
    for u in users:
        if u["email"] == creds["email"] and u["password"] == creds["password"]:
            return {
                "msg": "login successful",
                "time": time.time() - start
            }
    return {
        "error": "invalid credentials",
        "time": time.time() - start
    }

@app.get("/users")
def list_users():
    return users
