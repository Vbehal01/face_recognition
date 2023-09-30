from fastapi import FastAPI, UploadFile, HTTPException
import os
from constants import DESTINATION_FOLDER_PATH
from deepface import DeepFace


app = FastAPI()

DATASET_FOLDER_PATH = os.path.join(os.getcwd(), 'dataset')
PKL_FILE_PATH = os.path.join(DATASET_FOLDER_PATH, 'representations_vgg_face.pkl')
print(f"PKL File Path {PKL_FILE_PATH}")

@app.post("/register/")
def register_face(file: UploadFile):
    try:
        destination_folder = DESTINATION_FOLDER_PATH
        os.makedirs(destination_folder, exist_ok=True)
        with open(os.path.join(destination_folder, file.filename), "wb") as f:
            f.write(file.file.read())
        return {"filename": file.filename}
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
    finally:
        if os.path.exists(PKL_FILE_PATH):
            os.remove(PKL_FILE_PATH)

@app.get("/recognise/")
async def recognise_face(file: UploadFile):
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    result = DeepFace.find(img_path=file.filename, db_path=DATASET_FOLDER_PATH)
    ans=[]
    for data in result:
        identites=data["identity"].tolist()
        for identity in identites:
            identity=identity.split("/")
            ans.append(identity[len(identity)-1])
    return ans

@app.get("/")
async def root():
    return "Hello world!!"
