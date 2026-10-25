import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0, 1],
              [1, 1],
              [1, 0],
              [0, 0]])

y = np.array([[1], [1], [0], [0]])

np.random.seed(1)
weights = 2 * np.random.random((2, 1)) - 1

for iteration in range(10000):
    input_layer = X
    outputs = sigmoid(np.dot(input_layer, weights))
    error = y - outputs
    adjustments = error * sigmoid_derivative(outputs)
    weights += np.dot(input_layer.T, adjustments)

print("Váhy po naučení:")
print(weights)
print("\nVýsledky AI po učení (predikcia):")
print(outputs)