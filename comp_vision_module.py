from deepface import DeepFace
import numpy as np

models = [
  "VGG-Face",
  "Facenet",
  "Facenet512",
  "OpenFace",
  "DeepFace",
  "DeepID",
  "ArcFace",
  "Dlib",
  "SFace",
]

backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'fastmtcnn',
  'retinaface', 
  'mediapipe',
  'yolov8',
  'yunet',
  'centerface',
]


def compare_faces(img1,img2):
  result_list = []
  for i in backends:
    try:
      result = DeepFace.verify(img1_path=img1, img2_path=img2, detector_backend = i)
      #print(result)
      result_list.append(result['distance'])
    except Exception:
      pass
  return np.mean(result_list)