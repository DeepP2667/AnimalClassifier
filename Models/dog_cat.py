from save_stats import main_save

import os
import pickle as pk
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import cv2

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve

from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray
#HOG, histogram of oriented gradients


local_path = os.path.dirname(__file__)

labels = ["Cat", "Dog"]     # Cats:0 , Dogs:1


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

#cat_path, dog_path = get_data()

cat_path = 'C:/Users/deepp/Desktop/PetImages/Cat'
dog_path = 'C:/Users/deepp/Desktop/PetImages/Dog'

data = []

for filename in os.listdir(cat_path):
    try:
        img = cv2.imread(os.path.join(cat_path, filename), 0)
    except AttributeError:
        print("Image not applicable. (No image)")
        print("Will not be included")
        continue

    except ValueError:
        print("Not a jpg file or filename not an index.png (Eg. cat.png instead of 0.png)")
        print("Will not be included")
        continue

    except Exception as e:
        print(e)
        print("Image not applicable")
        continue

    if img is None:
        print('None')
    else:
        resized_img = cv2.resize(img, (50, 50))
        flattened_img = resized_img.flatten()/255 
        flattened_img = np.append(flattened_img, 0)

        data.append(flattened_img)
        
        # plt.imshow(resized_img, cmap='gray')
        # plt.show()

print("dogs")

for filename in os.listdir(dog_path):
    try:
        img = cv2.imread(os.path.join(dog_path, filename), 0)

    except AttributeError:
        print("Image not applicable. (No image)")
        print("Will not be included")
        continue

    except ValueError:
        print("Not a jpg file or filename not an index.png (Eg. cat.png instead of 0.png)")
        print("Will not be included")
        continue

    except Exception as e:
        print(e)
        print("Image not applicable")
        continue
    
    if img is None:
        print('None')
    else:
        resized_img = cv2.resize(img, (50, 50))
        flattened_img = resized_img.flatten()/255
        flattened_img = np.append(flattened_img, 1)

        data.append(flattened_img)

data_path = os.path.join(local_path, 'DataMatrix.npy')

data = np.array(data, dtype='uint8')

np.save(data_path, data) 
data = np.load(data_path)

random.shuffle(data)

features = len(data[0])-1
X = data[:,:features]
y = data[:,features:].ravel()

print(X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

parameters = {'C': [1, 10, 100, 1000],
              'gamma': [10, 1, 1e-1, 1e-2, 1e-3, 1e-4],
              'kernel':['poly', 'rbf']}   

clf = SVC(C=100, kernel='rbf', gamma='auto')
clf.fit(X_train, y_train)

train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)

print(test_score)

main_save(test_score, clf, data)

model_path = os.path.join(local_path, 'BestStats', 'best_model.pkl')

with open(model_path, 'rb') as model:
    loaded_model = pk.load(model)



#ADD GUI

