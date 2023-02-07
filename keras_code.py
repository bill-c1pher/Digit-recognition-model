from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Create the model: model
model = Sequential()

# Add the first hidden layer
input_shape=(784,)
model.add(Dense(50, activation='relu',input_shape=input_shape))

# Add the second hidden layer
model.add(Dense(50, activation='relu', input_shape=input_shape))

# Add the output layer
model.add(Dense(10, activation='softmax', input_shape=input_shape))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X, y ,validation_split=0.3, epochs=10)
