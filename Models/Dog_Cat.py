import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve

from sklearn.metrics import confusion_matrix

from sklearn.svm import SVC

from skimage.io import imread
#HOG, histogram of oriented gradients

classes = ["Cat", "Dog"]


def get_data():

    """ Search through user desktop and get cat/dog image folders

        Returns:
        -------
        cat_path: path to cat images folder
        dog_path: path to dog images folder
    """

    curr_path = os.getcwd()
    curr_path_split = curr_path.split('\\')
    desktop_index = curr_path_split.index("Desktop")
    desktop_path = "\\".join(curr_path_split[:desktop_index+1])

    for root, dirs, filename in os.walk(desktop_path):
        if "PetImages" in root:
            if "Cat" in dirs:
                cat_path = os.path.join(root, "Cat")

            if "Dog" in dirs:
                dog_path = os.path.join(root, "Dog")

    return cat_path, dog_path



# cat_path, dog_path = get_data()

cat_path = r'C:\Users\deepp\Desktop\PetImages\Cat'
dog_path = r'C:\Users\deepp\Desktop\PetImages\Dog'

for i in range(2):
    print(os.path.join(cat_path, f"{i}.png"))
    img = imread(os.path.join(cat_path, f"{i}.jpg"))
    
    plt.imshow(img)
    plt.show()

#NEXT: Figure out method to unravel image and match size for each image