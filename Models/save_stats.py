import os
import pickle as pk
import numpy as np


local_path = os.path.dirname(__file__)

best_data_path = os.path.join(local_path, 'BestStats/best_data.npy')
best_score_path = os.path.join(local_path, 'BestStats', 'best_score.txt')
model_path = os.path.join(local_path, 'BestStats', 'best_model.pkl')

def save_best_model(clf):

    with open(model_path, 'wb') as best_model:
        pk.dump(clf, best_model)


def save_files(test_score, clf, data):

    with open(best_score_path, 'r+') as scores:

        best_score = scores.readline()

    try:
        if test_score > float(best_score):

            with open(best_score_path, 'w+') as stats:

                if test_score > float(best_score):
                    save_best_model(clf)
                    np.save(best_data_path, data)
                    stats.write(f"{test_score}")

    except ValueError:
        print("No value in file: Adding current score...")

        with open(best_score_path, 'w+') as stats:

            save_best_model(clf)
            np.save(best_data_path, data)
            stats.write(f"{test_score}")



def main_save(test_score, clf, data):

    save_files(test_score, clf, data)
    print("Files saved")