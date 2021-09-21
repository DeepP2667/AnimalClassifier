import os
import pickle as pk
import cv2
import matplotlib.pyplot as plt
import numpy as np

classes = ["Cat", "Dog"]
local_path = os.path.dirname(__file__)
model_path = os.path.join(local_path, 'BestStats', 'best_model.pkl')

def predict_img(img_path):

    with open(model_path, 'rb') as model:
        loaded_model = pk.load(model)


    img = cv2.imread(img_path, 0)

    if img is None:
        print("Please try a different image")
    
    else:
        resized_img = cv2.resize(img, (50, 50))
        flattened_img = resized_img.flatten()/255 
        img_data = np.array(flattened_img).reshape(1,-1)

    prediction = int(loaded_model.predict(img_data))

    print(classes[prediction])
    
    plt.imshow(img, cmap="gray")
    plt.title(f"A {classes[prediction]}")
    plt.show()

