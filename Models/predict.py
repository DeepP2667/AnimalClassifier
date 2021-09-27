import os
import pickle as pk
import cv2
import matplotlib.pyplot as plt
import numpy as np

from skimage.feature import hog

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
        img = cv2.resize(img, (64, 128))
        fd, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True)
        fd = fd.reshape(1,-1)
        prediction = int(loaded_model.predict(fd))

        print(prediction)

        return classes[prediction]
    
    # plt.imshow(img, cmap="gray")
    # plt.title(f"A {classes[prediction]}")
    # plt.show()
