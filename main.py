from fastapi import FastAPI
# from pydantic import BaseModel
# from database import *

# class Enrollment(BaseModel):
#     stdId: int
#     stdName: str
#     course_name: str
#     grade: float
#     unit: int

app = FastAPI()

@app.get("/")
def home():
    return {"hi": "ho"}

# @app.get("/{stdId}", response_model = Enrollment)
# def get_subject(stdId: int):
#     result = collection.find_one({"stdId": stdId})
#     return result