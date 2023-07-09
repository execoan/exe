# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 23:24:52 2023

@author: yunus
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
import matplotlib.pyplot as plt

# Verileri tanımlayalım (hız ve zaman)
zaman = np.linspace(-100,100,1000)

def get_hiz(zaman):
    return 5*np.sin(0.05*zaman*np.pi + np.random.random(size=(len(zaman)))/2)
hiz = get_hiz(zaman)

plt.plot(zaman,hiz,'.')
plt.show()

# RNN modelini oluşturalım
model = Sequential()
#model.add(SimpleRNN(units=32, input_shape=(1, 1)))
model.add(Dense(units=50,activation='relu'))
model.add(Dense(units=25,activation='relu'))
model.add(Dense(units=10,activation='relu'))
model.add(Dense(units=1))

# Modeli derleyelim
model.compile(optimizer='adam', loss='mse')

model.fit(zaman.reshape(1000,1), hiz.reshape(1000,1), epochs=2000)

yeni_zaman = np.linspace(0,100,100)
tahmin_hiz = model.predict(yeni_zaman.reshape(-1, 1))

plt.plot(get_hiz(yeni_zaman),tahmin_hiz,'.')
plt.show()

plt.plot(yeni_zaman, get_hiz(yeni_zaman),label='olması gereken')
plt.plot(yeni_zaman, tahmin_hiz,label='tahmin edilen')
plt.legend()
plt.show()

