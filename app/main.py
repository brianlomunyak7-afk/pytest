from fastapi import FastAPI

app = FastAPI()

@app.get("/")
  def root():
  return {"message":"Student Management API is running"}

@app.get("/students")
  def get_students():
  return[
    {"id":1,"name":"Brian","course":"Information Technology"},
    {"id":2,"name":"Leah","course":"Teaching"},
]
