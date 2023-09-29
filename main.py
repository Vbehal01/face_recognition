from fastapi import FastAPI, UploadFile, HTTPException

app = FastAPI()

@app.post("/Register/")
def register_face(file: UploadFile):
    return

@app.get("/Recognise")
def recognise_face():
    return
