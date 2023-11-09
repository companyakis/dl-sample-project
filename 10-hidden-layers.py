# We need to add the hidden layers. 
# We'll add 4 hidden layers each with 4096 nodes

# Add the first hidden layer with 4096 nodes and relu activation function
model.add(tf.keras.layers.Dense(4096, activation="relu"))
# Add 0.5 dropout
model.add(tf.keras.layers.Dropout(0.5))

# Add the second hidden layer with 4096 nodes and relu activation function
model.add(tf.keras.layers.Dense(4096, activation="relu"))
# Add 0.5 dropout
model.add(tf.keras.layers.Dropout(0.5))

# Add the third hidden layer with 4096 nodes and relu activation function
model.add(tf.keras.layers.Dense(4096, activation="relu"))
# Add 0.5 dropout
model.add(tf.keras.layers.Dropout(0.5))

# Add the fourth hidden layer with 4096 nodes and relu activation function
model.add(tf.keras.layers.Dense(4096, activation="relu"))
# Add 0.5 dropout
model.add(tf.keras.layers.Dropout(0.5))
