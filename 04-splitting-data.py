# Preprocessing steps...

# let’s split the dataset into features and labels
# Create X and y datasets using .drop() and .loc() methods

# Create the features dataset
X = data.drop('Class', axis=1)

# Create the labels dataset
y = data.loc[:, 'Class']
