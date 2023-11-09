# Plot the the training loss
plt.plot(results.history['loss'], label="Train")

# Plot the the validation loss
plt.plot(results.history["val_loss"], label="Test")

# Name the x and y axises
plt.ylabel('Loss')
plt.xlabel('Epoch')

# Put legend table
plt.legend()

# Show the plot
plt.show()
