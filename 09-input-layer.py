# Construct an input layer and assign it to a variable
# The first argument is the number of nodes we want in that hidden layer

# Only for the input layer, we have to set the input_shape argument which is the number of columns (# of X columns)
# in this case, 24

# Create an input layer
input_layer = tf.keras.layers.Dense(4096, input_shape=(24,), activation="relu")

# Add input layer to model object
model.add(input_layer)
