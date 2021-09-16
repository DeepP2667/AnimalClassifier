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

labels = ["Cat", "Dog"]


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

width = []
height = []


for filename in os.listdir(cat_path):

    try:
        img = imread(os.path.join(cat_path, filename))
        width.append(img.shape[0])
        height.append(img.shape[1])

    except AttributeError:
        print("Image not applicable. (No image)")
        print("Will not be included")

    except ValueError:
        print("Not a jpg file or filename not an index.png (Eg. cat.png instead of 0.png)")
        print("Will not be included")

    plt.imshow(img)
    plt.show()

mean_width = np.mean(np.array(width)))   #356 (mean width ran on colab)
mean_height = np.mean(np.array(height))  #410 (mean height ran on colab)


for filename in os.listdir(cat_path):
    test_img = imread(os.path.join(cat_path, filename))
    resized_img = resize(test_img, (mean_width, mean_height, 3), anti_aliasing=True)

    #NEXT: Unravel and create dataframe
    #REMEMBER: Make file to add store dimensions so I don't need to rerun finding mean width/height 


