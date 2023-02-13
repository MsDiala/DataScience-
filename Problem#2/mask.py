# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# import numpy as np
# import cv2

# # Load the dataset of images and labels
# def load_dataset(dataset_path):
#     X, y = [], []
#     with open(dataset_path, "r") as f:
#         for line in f:
#             line = line.strip().split(",")
#             image_path, label = line[0], int(line[1])
#             image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#             image = cv2.resize(image, (64, 64))
#             X.append(image)
#             y.append(label)
#     X = np.array(X) / 255.0
#     y = np.array(y)
#     return X, y

# # Split the data into training and testing sets
# def train_test_split(X, y, test_size=0.2):
#     indices = np.arange(X.shape[0])
#     np.random.shuffle(indices)
#     X = X[indices]
#     y = y[indices]
#     split = int(X.shape[0] * (1 - test_size))
#     X_train, X_test = X[:split], X[split:]
#     y_train, y_test = y[:split], y[split:]
#     return X_train, X_test, y_train, y_test

# # Define the CNN model
# def create_model(input_shape=(64, 64, 1)):
#     model = keras.Sequential([
#         Conv2D(32, (3, 3), activation="relu", input_shape=input_shape),
#         MaxPooling2D(pool_size=(2, 2)),
#         Conv2D(64, (3, 3), activation="relu"),
#         MaxPooling2D(pool_size=(2, 2)),
#         Flatten(),
#         Dense(64, activation="relu"),
#         Dense(1, activation="sigmoid")
#     ])
#     model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
#     return model

# # Load the dataset
# X, y = load_dataset("dataset.csv")

# # Preprocess the data
# X = np.expand_dims(X, axis=-1)

# # Split the data
# X_train, X_test, y_train, y_test = train_test_split(X, y)

# # Create the model
# model = create_model()

# # Train the model
# history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# # Evaluate the model
# test_loss, test_acc = model.evaluate(X_test, y_test)
# print("Test Loss:", test_loss)
# print("Test Accuracy:", test)
