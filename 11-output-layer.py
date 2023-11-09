# Add the output layer
# In this project, the number of target classes which is 7 

model.add(tf.keras.layers.Dense(7, activation="softmax"))
