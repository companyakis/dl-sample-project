# scale all of the values between the 0 and 1 range
# features in different units or ranges can be problematic

# Normalize the features dataset and assign it to a variable
X_scaled = minmax_scale(X)

# Create a DataFrame using the new variable
X = pd.DataFrame(X_scaled)

# Look at the newly created DataFrame
X.head()
