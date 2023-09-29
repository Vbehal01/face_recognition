from deepface import DeepFace
# face_recognizer = DeepFace()
result = DeepFace.verify("dataset/img1.jpg", "dataset/img3.jpg")

print("Is verified: ", result["verified"])