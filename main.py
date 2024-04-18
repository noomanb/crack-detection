import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import cv2
model = pickle.load(open("Crack_detection_Model.pkl", "rb"))


def predict_crack(image, model):
    image = cv2.imread(image)
    resize_image = cv2.resize(image, (100,100))
    resized_image_batch = np.expand_dims(resize_image, axis=0)
    crack = np.argmax(model.predict([resized_image_batch]))
    if crack == 0:
        return "No Crack"
    else:
        return "Crack"
    
# print(predict_crack(images, model))