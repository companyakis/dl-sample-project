# Artificial intelligence algorithms can't use string data when training a model because no mathematical operations can be performed on them

# Use the LabelEncoder of the Sklearn library to converting strings to integers

# Create an LabelEncoder object.
encoder = LabelEncoder()

# Convert string classes to integers using fit_transform() method
y = encoder.fit_transform(y)

# Print the y array
print(y)
