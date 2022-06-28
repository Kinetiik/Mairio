from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Dense
from keras.models import Sequential
from train_matrix_from_data import read_data
model = Sequential()

states, actions, rewards = read_data()
model.add(LSTM(224, input_shape=(224,)))
model.add(Dense(8))
nodel.compile(loss="mean_squared_error", optimizer="adam")


for state,action in zip(states,actions):
    model.fit()
