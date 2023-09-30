from fastapi import FastAPI, UploadFile, HTTPException
import os
from fastapi.responses import JSONResponse
from deepface import DeepFace

app = FastAPI()

@app.post("/Register/")
def register_face(file: UploadFile):
    try:
        destination_folder = "dataset"
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

@app.get("/Recognise/")
async def recognise_face():
    result = DeepFace.find(img_path="img4.jpg", db_path="/workspaces/face_recognition/dataset")
    ans=[]
    for i in result:
        path=i["identity"].tolist()
        for a in path:
            a=a.split("/")
            ans.append(a[len(a)-1])
    return ans
