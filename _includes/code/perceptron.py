import os
from PIL import Image
import random

# -----------------------------
# Read image as 1D vector
# -----------------------------
def read_as_1D(filename):
    image = Image.open(filename).convert('L')
    pixels_raw = list(image.getdata())
    
    # Convert to binary pixels (0 or 1)
    pixels = []
    for p in pixels_raw:
        if p > 0:
            pixels.append(1)
        else:
            pixels.append(0)
    return pixels


# -----------------------------
# Weighted sum (with bias)
# -----------------------------
def weighted_sum(pixels, weights):
    total = weights[-1]  # last element is bias
    for i in range(len(pixels)):
        total += pixels[i] * weights[i]
    return total


# -----------------------------
# Load dataset into memory
# -----------------------------
def load_dataset(root_folder):
    dataset = []
    for digit in range(10):
        folder = root_folder + '/' + str(digit)
        for filename in os.listdir(folder):
            image_path = folder + '/' + filename
            pixels = read_as_1D(image_path)
            dataset.append((pixels, digit))  # store as tuple
    return dataset


# -----------------------------
# Learn all weights together (multiclass perceptron)
# -----------------------------
def get_all_weights(dataset):
    # Initialize weights for 10 digits (+1 for bias)
    weights = []
    for _ in range(10):
        w = []
        for _ in range(28*28 + 1):
            w.append(0)
        weights.append(w)

    # Run multiple passes over data
    for epoch in range(5):
        print("Epoch", epoch + 1)
        random.shuffle(dataset)

        for pixels, true_digit in dataset:

            # Compute scores for all digits
            scores = []
            for d in range(10):
                s = weighted_sum(pixels, weights[d])
                scores.append(s)

            predicted_digit = 0
            max_score = scores[0]
            for i in range(1, 10):
                if scores[i] > max_score:
                    max_score = scores[i]
                    predicted_digit = i

            # Update only if prediction is wrong
            if predicted_digit != true_digit:
                # Reward correct digit
                for i in range(len(pixels)):
                    weights[true_digit][i] += pixels[i]
                weights[true_digit][-1] += 1  # bias update

                # Punish wrong digit
                for i in range(len(pixels)):
                    weights[predicted_digit][i] -= pixels[i]
                weights[predicted_digit][-1] -= 1  # bias update

    return weights


# -----------------------------
# Predict
# -----------------------------
def predict(image, all_weights):
    pixels = read_as_1D(image)

    max_score = float('-inf')
    predicted_digit = None

    for digit in range(10):
        score = weighted_sum(pixels, all_weights[digit])
        if score > max_score:
            max_score = score
            predicted_digit = str(digit)

    return predicted_digit


# -----------------------------
# Evaluate
# -----------------------------
def evaluate(test_folder, all_weights):
    correct = 0
    count = 0

    for digit in '0123456789':
        folder = test_folder + '/' + digit
        for file in os.listdir(folder):
            fullname = folder + '/' + file
            count += 1
            if predict(fullname, all_weights) == digit:
                correct += 1

    print('Accuracy:', correct / count * 100, '%')


# -----------------------------
# Main
# -----------------------------
training_data = load_dataset('digits/training')
all_weights = get_all_weights(training_data)
evaluate('digits/testing', all_weights)
