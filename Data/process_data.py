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
    train_labels.append(image[0])     # Add label to label list
    image.pop(0)                      # Remove from list of the image

for image in raw:
    train_samples.append(image)       # Add each image's data to the samples

for image in range(len(train_samples)):
    for pixel in range(len(train_samples[image])):
        train_samples[image][pixel] = int(train_samples[image][pixel]) # Turn all samples into integers

# Turn all data and labels into integers
for label in range(len(train_labels)):
    
    if type(train_labels[label]) == list:
        
        for i in range(len(train_labels[label])):
            train_labels[label][i] = int(train_labels[label][i])
            
    elif type(train_labels[label]) == int or type(train_labels[label]) == str:
        train_labels[label] = int(train_labels[label])
    
    else: raise TypeError(f'Label data type {str(type(train_labels[label]))[8 : len(str(type(train_labels[label])))-2]} is not allowed.')

print('Shaping data...', end='\r')

train_samples = np.array(train_samples)
train_labels = np.array(train_labels)
train_labels, train_samples = shuffle(train_labels, train_samples)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_train_samples = scaler.fit_transform(train_samples)

print('Data preprocessed!')
print(train_samples)