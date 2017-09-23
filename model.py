import numpy as np

from keras.models import Sequential
from keras.layers import Dense, InputLayer, Flatten, Activation, Dropout, LSTM
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ReduceLROnPlateau

import h5py

# activation function used following every layer except for the output layers
activation = 'relu'

# model weight initializer
initializer = 'he_normal'

# shape of input data that is fed into the input layer
input_shape = (None, 1)

# number of filters used in the convolutional layers
num_filters = [4,16]

# length of the filters in the convolutional layers
filter_length = 8

# length of the maxpooling window 
pool_length = 4

# number of nodes in each of the hidden fully connected layers
num_hidden_nodes = [256,128]

# number of samples fed into model at once during training
batch_size = 64

# maximum number of interations for model training
max_epochs = 30

# initial learning rate for optimization algorithm
lr = 0.0007

# exponential decay rate for the 1st moment estimates for optimization algorithm
beta_1 = 0.9

# exponential decay rate for the 2nd moment estimates for optimization algorithm
beta_2 = 0.999

# a small constant for numerical stability for optimization algorithm
optimizer_epsilon = 1e-08

model = Sequential([
        Conv1D( kernel_initializer=initializer, activation=activation, padding="same", filters=num_filters[0], input_shape=input_shape, kernel_size=filter_length),
        MaxPooling1D(),     # Downsample the output of convolution by 2X.
        Conv1D(kernel_initializer=initializer, activation=activation, padding="same", filters=num_filters[1], kernel_size=filter_length),
        #MaxPooling1D(),
        Flatten(),
        Dense(1, activation='linear'), 
    ])




# compile model
loss_function = 'mean_squared_error'
early_stopping_min_delta = 0.0001
early_stopping_patience = 4
reduce_lr_factor = 0.5
reuce_lr_epsilon = 0.0009
reduce_lr_patience = 2
reduce_lr_min = 0.00008

optimizer = Adam(lr=lr, beta_1=beta_1, beta_2=beta_2, epsilon=optimizer_epsilon, decay=0.0)

early_stopping = EarlyStopping(monitor='val_loss',     min_delta=early_stopping_min_delta, 
                                   patience=early_stopping_patience, verbose=2, mode='min')

reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.5, epsilon=reuce_lr_epsilon, 
                              patience=reduce_lr_patience,     min_lr=reduce_lr_min, mode='min', verbose=2)

model.compile(optimizer=optimizer, loss=loss_function)

train_x = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81])
train_y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

model.fit(train_x, train_y, validation_data=None,
      epochs=max_epochs, batch_size=batch_size, verbose=2,
      callbacks=[reduce_lr,early_stopping])


predictions = model.predict(np.array([225, 300, 1600]))
print(predictions.tolist())

model.save('model_file.h5')