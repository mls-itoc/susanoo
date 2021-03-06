import sys
import numpy as np
from skimage import io, feature, color
from glob import iglob
import pickle

def get_features(directory):
    features = []
    for fn in iglob('%s/*.png', % directory):
        image = color.rgb2gray(io.imread(fn))
        features.append(get_histogram(image).reshape(-1))
        features.append(get_histogram(np.fliplr(image)).reshape(-1))
    return features

def main():
    positive_dir = sys.argv[1]
    negative_dir = sys.argv[2]
    positive_sample = get_features(positive_dir)
    negative_sample = get_features(negative_dir)
    n_positives = len(positive_sample)
    n_negatives = len(negative_sample)
    # (2)
    X = np.array(positive_sample + negative_sample)
    # (3)
    y = np.array([1 for i in range(n_positives)] +
                 [0 for i in range(n_negatives)])
    # (4)
    pickle.dump((X, y), open(sys.argv[3], 'w'))
