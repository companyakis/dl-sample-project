# Train the model for 100 epochs
results=model.fit(X_train, y_train, epochs=100, validation_data=(X_val, y_val))
