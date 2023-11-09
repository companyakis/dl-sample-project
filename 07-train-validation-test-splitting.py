# split the dataset into training, validation and test datasets

# we can adjust the ratio for splitting...

# First, create X_train, y_train and X_temporary and y_temporary datasets from X and y.
X_train, X_temporary, y_train, y_temporary = train_test_split(X, y, train_size=0.8)

# Using the X_temporary and y_temporary dataset we just created create validaiton and test datasets.
X_val, X_test, y_val, y_test = train_test_split(X_temporary, y_temporary, train_size=0.5)

# Print the lengths of the X, X_train, X_val and X_test
print(len(X))
print(len(X_train))
print(len(X_val))
print(len(X_test))
