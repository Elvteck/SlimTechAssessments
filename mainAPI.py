from fastapi import FastAPI

gyde = FastAPI()

professions = []

@gyde.get("/")
def root():
    return{"Hello" : "dear student. Are you ready to be guided"}

@gyde.post("/professions") 
def create_item(profession: str):
    professions.append(profession)
    return professions
