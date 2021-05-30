print('Setting up dependencies for data processing...', end='\r')
import csv
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import shuffle

raw = []
train_samples = []
train_labels = []
scaled_train_samples = []

print('Collecting data...                            ', end='\r')
with open('Data/MNIST.csv') as file:
    csv_data = csv.reader(file, delimiter=',')
    
    for row in csv_data:
        raw.append(row)


print('Parsing data...   ', end='\r')
raw.pop(0)  # Remove headers from the dataset


for image in raw:                     # Iterate through each image
    train_labels.append([image[0]])   # Add label to label list
    image.pop(0)                      # Remove from list of the image

for image in raw:
    train_samples.append(image)

for image in range(len(train_samples)):
    for pixel in range(len(train_samples[image])):
        train_samples[image][pixel] = int(train_samples[image][pixel])

for label in range(len(train_labels)):
    for i in range(len(train_labels[label])):
        train_labels[label][i] = int(train_labels[label][i])


print('Shaping data...', end='\r')


print('Data preprocessed!')