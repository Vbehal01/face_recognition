from deepface import DeepFace
# face_recognizer = DeepFace()
result = DeepFace.verify("dataset/img1.jpg", "dataset/img2.jpg")

print("Is verified: ", result["verified"])