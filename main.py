from fastapi import FastAPI, UploadFile, HTTPException
import os
from constants import DESTINATION_FOLDER_PATH
from deepface import DeepFace

app = FastAPI()

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
        pickle_file_path="/workspaces/face_recognition/dataset/representations_vgg_face.pkl"
        if os.path.exists(pickle_file_path):
            os.remove(pickle_file_path)

@app.get("/recognise/")
async def recognise_face(file: UploadFile):
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    result = DeepFace.find(img_path=file.filename, db_path="/workspaces/face_recognition/dataset")
    ans=[]
    for data in result:
        identites=data["identity"].tolist()
        for identity in identites:
            identity=identity.split("/")
            ans.append(identity[len(identity)-1])
    return ans
