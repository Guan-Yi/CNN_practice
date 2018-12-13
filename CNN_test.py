# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
import os
from keras.models import Model
from keras.layers import Input, Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization

os.chdir('C://Users//Emily//Desktop//code//CNN_practice//training_data')
filelist = os.listdir()

LETTERSTR = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'

#input data
class input_data:
    def __init__(self, FL):
        self.file = FL
        
    def x(self):
        data = []
        for i in range(0, len(self.file)):
            img = Image.open(self.file[i])  
            img_array = np.asarray(img, dtype='float64')/256
            data.append(img_array)
        return data
    
    def y(self):
        label = []
        for i in range(0, len(self.file)):
            name = self.file[i][0:4]
            label.append(name)
        return label

def to_onehot(text):
    labellist = []
    for letter in text:
        onehot = [0 for _ in range(34)]
        num = LETTERSTR.find(letter)
        onehot[num] = 1
        labellist.append(onehot)
    return labellist

#------------------------------------------------------------------------------

# Create CNN Model
print("Creating CNN model...")
start = Input((90, 160, 3))
out = start
out = Conv2D(filters=32, kernel_size=(3, 3), padding='same', activation='relu')(out)
out = Conv2D(filters=32, kernel_size=(3, 3), activation='relu')(out)
out = BatchNormalization()(out)
out = MaxPooling2D(pool_size=(2, 2))(out)
out = Dropout(0.3)(out)
out = Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu')(out)
out = Conv2D(filters=64, kernel_size=(3, 3), activation='relu')(out)
out = BatchNormalization()(out)
out = MaxPooling2D(pool_size=(2, 2))(out)
out = Dropout(0.3)(out)
out = Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation='relu')(out)
out = Conv2D(filters=128, kernel_size=(3, 3), activation='relu')(out)
out = BatchNormalization()(out)
out = MaxPooling2D(pool_size=(2, 2))(out)
out = Flatten()(out)
out = Dropout(0.3)(out)
out = [Dense(34, name='digit1', activation='softmax')(out),\
       Dense(34, name='digit2', activation='softmax')(out),\
       Dense(34, name='digit3', activation='softmax')(out),\
       Dense(34, name='digit4', activation='softmax')(out)]
model = Model(inputs=start, outputs=out)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

#------------------------------------------------------------------------------

train = input_data(filelist)
train_x = train.x()
train_y = train.y()

data_list = []
label_list = []
for i in range(0, len(filelist)):
    img = Image.open(filelist[i])  
    img_array = np.asarray(img, dtype='float64')/256
    label = filelist[i][0:4]
    data_list.append(img_array)
    label_list.append(label)

#build label
train_label = []
for i in range(0, len(filelist)):
    onehot = to_onehot(label_list[i])
    train_label.append(onehot)

new_train_label = [[] for _ in range(4)]

for arr in train_label:
    for index in range(4):
        new_train_label[index].append(arr[index])

new_train_label = [arr for arr in np.asarray(new_train_label)]

data_list = np.stack(data_list)

#train
model.fit(data_list, new_train_label, batch_size=40, epochs=1, verbose=2)






    
    
    