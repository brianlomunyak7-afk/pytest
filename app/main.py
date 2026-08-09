from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Student Management API is running"}

@app.get("/students")
def get_students():
    return [
        {"id": 1, "name": "Brian", "course": "Computer Science"},
        {"id": 2, "name": "Alice", "course": "Software Engineering"},
    ]
