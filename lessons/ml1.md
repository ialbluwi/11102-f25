---
layout: page
title:  ML 1
nav_exclude: true
author: Ibrahim Albluwi
---

<style>
h2 {
    font-weight: 400;           /* normal weight, not bold */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #3b7dc0ff;             /* optional: different color */
}

h3 {
    font-weight: 500;           /* bold weight */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #9c0101ff;             /* optional: different color */
}

.img-soft {
    width: 75%;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);  
}

.figure-soft {
    text-align: center;
    margin: 20px 0;
}

table thead th {
    background-color: #293150; /* dark blue */
    color: white;
    text-align: left;           /* optional: align text */
}

table td {
    vertical-align: top;       /* keep row heights compact */
}
</style>


# Machine Learning (Part 1)
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview
 
This is the first part of the lessons on Machine Learning (ML). The goal of these lessons is to give you an introduction to ML concepts through a hands-on application. Machine learning is a subfield of artificial intelligence (AI) that can be considered as the most important and widely used AI technique today.

In this part, we will introduce the ML application along with some naive solutions. The goal is to illustrate key ML concepts and pave the way for more advanced solutions in the next parts.

## The Problem

We are given a dataset of images of handwritten digits (0-9) and are asked to use it to build a system that can take an image of a handwritten digit (0-9) and predict which digit it is.

<img src="/11102-f25/lessons/images/digits1.png" style="display:block; margin: 20px auto; width: 80%">

This problem is a classical example of what is called **classification** in ML, where the goal is to assign an input (e.g., an image) to one of several categories (e.g., the digits 0-9). Other examples of classification problems include classifying emails as spam or not spam, classifying product reviews as positive or negative, and classifying medical images as showing signs of a disease or not.

In a classification problem, we have a dataset of **examples** that are already classified (labeled) that the system can **learn** from.

<img src="/11102-f25/lessons/images/ml.png" style="display:block; margin: 20px auto; width: 80%">


## The Dataset

We will be using the [MNIST dataset](https://drive.google.com/file/d/1As2Km6JNlwOqIvULO3kWojH55lJ204qO/view?usp=sharing), which is a well-known dataset of handwritten digits. The data is split into:

- **Training set**: $$60,000$$ images of handwritten digits along with their labels (the digit they represent). This is the data that our system is allowed to learn from.

- **Test set**: $$10,000$$ images of handwritten digits along with their labels. This is the data that we will use to evaluate how well our system performs on unseen data.

Each image in the dataset is a $$28 \times 28$$ pixel grayscale image, where each pixel has a value between 0 (black) and 255 (white).

The images are organized in folders, where each folder corresponds to a digit (0-9). The following screen recording shows the structure of the dataset:

<video controls style="display:block; margin: 20px auto; width: 80%">
  <source src="/11102-f25/lessons/images/mnist.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Before We Start

Before we start building our solution, let's define the main functions we will be using throughout this lesson:

**1. `read_as_1D(filename)`**

This function takes the name of an image file as input and returns a list of pixel values representing the image in a flattened 1D format (i.e., a list of $$784$$ values for a $$28 \times 28$$ image). Each pixel value is an integer between $$0$$ and $$255$$.

<img src="/11102-f25/lessons/images/flatten.png" style="display:block; margin: 20px auto; width: 80%">

Here is the implementation of the `read_as_1D` function:

```python
from PIL import Image

def read_as_1D(filename):
    # Open the image in grayscale
    # (using convert('L') makes each pixel a single value 0-255)
    image = Image.open(filename).convert('L')  

    # Get pixel values as a 1D list
    return list(image.getdata())             
```

In many cases, we want to perform operations on all the pixel values of an image regardless of their 2D position (e.g., computing the average pixel value). Having a list of pixel values makes writing the code for such operations easier.

**2. `predict(image)`** 

This function takes the name of an image file as input and returns the predicted label (digit) for that image. Most of our work will be focused on implementing this function.

**3. `evaluate(test_folder)`** 

This function takes the name (or full path) of the folder containing test data and produces an accuracy score indicating how well our `predict` function performs on the given test data. 

Here is the implementation of the `evaluate` function:

```python
import os

def evaluate(test_folder):
    correct = 0     # Number of correct predictions
    count = 0       # Total number of predictions
    
    # Loop over each folder (0-9)
    for digit in '0123456789':
        folder = test_folder + '/' + digit

        # Loop over each file in the folder
        for file in os.listdir(folder):
            fullname = folder + '/' + file
            print('Evaluating image:', fullname)

            if predict(fullname) == digit:
                correct += 1
            count += 1
            
    print('Accuracy:', correct / count * 100, '%')

# Dummy predict function: Always predicts '0'
# We will improve this function later
def predict(image):
    return '0'
```

Assuming the function is called as `evaluate('digits/testing')`, the outer loop goes over the folders named: 

```
digits/testing/0
digits/testing/1
digits/testing/2
...
digits/testing/9
``` 

For each folder, the inner loop goes over each image file in that folder and sends it to the `predict` function to get a prediction. 

If the prediction matches the folder name, we increment the `correct` counter.

{: .important-title }
> A PYTHON NOTE
>
> The `os.listdir(folder)` function returns a list of all files and directories in the specified folder. We use it here to loop over all image files in each digit folder.

If we run the above code with the dummy `predict` function that always returns `0`, we will get an accuracy of around 10% since only the images in the `0` folder will be predicted correctly (out of `~10,000` images, only `~1,000` are `0`s).


## Attempt # 1

### A Simplified Version

Before we attempt the full problem, let's first attempt a simplified version of it. We will assume that our test set only contains images of `0`s and `1`s and our goal is to build a `predict` function that can distinguish between these two digits only.

We can easily modify our `evaluate` function to only consider these two digits by changing the outer loop to be: 

```python
for digit in '01':
```
Instead of:
```python
for digit in '0123456789':
```

Running the code again with the dummy `predict` function that always returns `0` will now give us an accuracy of around $$50\%$$ since half of the images in the test set are `0`s and the other half are `1`s.

### A Simple Approach

How can we distinguish between `0`s and `1`s? One simple idea is to look at _how black_ or white the image is. Intuitively, `0`s might have more black pixels than `1`s since `0`s are a closed loop, while `1`s are a straight line.

Let's begin by writing a function that computes the **average pixel value** of an image.

```python
def average(pixels):
    return sum(pixels) / len(pixels)

# Example usage:
pixels = read_as_1D('digits/training/1/1.png')
print('Average:', average(pixels))
```

We can apply the above function to each image in the training set to compute the average pixel value for `0`s and `1`s separately. I.e., we want o **learn** the average pixel value for each digit from the training data.

```python
def learn_average(digit_folder):
    total = 0
    count = 0
    
    for file in os.listdir(digit_folder):
        pixels = read_as_1D(digit_folder + '/' + file)
        total += average(pixels)
        count += 1
        
    return total / count

print('Learning average for 0 ...')
avg0 = learn_average('digits/training/0')

print('Learning average for 1 ...')
avg1 = learn_average('digits/training/1')

print('Average for 0:', avg0)
print('Average for 1:', avg1)
```
    
Running the above code gives us the following average pixel values:

```
Average for 0: 44.21682790539817
Average for 1: 19.379653852789957
```

This confirms our intuition that `0`s tend to have more black pixels (lower average pixel value) than `1`s. Let's use this information to build our `predict` function:

```python
def predict(image):
    AVERAGES = [44.21682790539817,    # learned average for '0'
                19.379653852789957]   # learned average for '1'

    pixels = read_as_1D(image)
    avg = average(pixels)
    
    # Predict '0' if avg is closer to the average for '0'
    # Otherwise, predict '1'
    if abs(avg - AVERAGES[0]) < abs(avg - AVERAGES[1]):
        return '0'
    else:
        return '1'
```

Let's evaluate our `predict` function on the simplified test set containing only `0`s and `1`s:

```
>>> evaluate('digits/testing')
Accuracy:  92.72%
```

This is huge! We managed to achieve over 90% accuracy using a very simple approach! 🎉🎉

### Generalizing to All Digits

Let's apply the same approach for the full problem (digits `0-9`) by learning the average pixel value for each digit:

```python
print('Digit\t Average')
for digit in '0123456789':
    folder = 'digits/training/' + digit
    avg = learn_average(folder)
    print(digit, '\t', avg)
```

Running the above code gives us the following average pixel values for all digits:

```
Digit   Average
0       44.21682790539817
1       19.379653852789957
2       37.988657849846874
3       36.09018653946659
4       30.948225682775707
5       32.83109548467975
6       35.011952681545765
7       29.204562926527398
8       38.2897753828927
9       31.260435427322733
```

Let's update our `predict` function to handle all digits:

```python
def predict(image):
    AVERAGES = [
        44.21682790539817,
        19.379653852789957,
        37.988657849846874,
        36.09018653946659,
        30.948225682775707,
        32.83109548467975,
        35.011952681545765,
        29.204562926527398,
        38.2897753828927,
        31.260435427322733
    ]

    pixels = read_as_1D(image)
    avg = average(pixels)

    # Find the closest digit based on average pixel value
    min_diff = None
    closest_digit = None
    for i in range(10):
        diff = abs(avg - AVERAGES[i])
        if min_diff is None or diff < min_diff:
            min_diff = diff
            closest_digit = i
    
    return str(closest_digit)
```

We can now evaluate our `predict` function again to see how well it performs on the full dataset.

What do we get?

```
>>> evaluate('digits/testing')
Accuracy: 22.3 %
```

This is catastrophically bad! 🤦‍♂️🤦‍♂️

We should have been less optimistic about this simple approach. But why?

While it worked well for distinguishing between `0`s and `1`s, the average pixel value fails to capture the complexity of the other digits. For example, digits like `2`, `3`, and `5` have similar average pixel values.

One problem in our approach is that we completely ignore where pixels are. Two images can have the same average pixel value but look completely different. 

We need a better way to represent images that captures more information about the pixel values and their locations.

## A Closer Look at Our Approach

### Architecture

Our approach can be split into two phases:

- **Training phase**: In this phase, we learned from the training data by computing the average pixel value for each digit (0-9). The result of this phase is a set of learned averages that we used for prediction. We will refer to these learned averages as our **model**.

<img src="/11102-f25/lessons/images/training.png" style="display:block; margin: 20px auto; width: 80%">

- **Testing phase**: In this phase, we used our learned model to make predictions on new images. To check how well our model performs, we checked the accuracy of our predictions on the images in the test set and computed an accuracy score.

<img src="/11102-f25/lessons/images/testing.png" style="display:block; margin: 20px auto; width: 80%">

### Shortcomings of Our Approach

The problem with our approach is that the model we learned is too simplistic:

- First, it only captures a single **feature** of the image: the average pixel value.
- Second, it bases its predictions on a very simple rule: choosing the digit whose average pixel value is closest to that of the input image.

To improve our model, we might need to consider **more** (or better) features of the image, and use **a more sophisticated method** to combine these features to make predictions.

<img src="/11102-f25/lessons/images/weights.png" style="display:block; margin: 20px auto; width: 80%">

What features should we consider? And how should we combine them? This is the essence of machine learning, and we will explore these questions in the next parts of this lesson series.

<!-- a footnote with small fonts -->
<br>
<br>
<sub><sup>
** Some digit images used in this lesson are adapted from https://www.cs.princeton.edu/courses/archive/fall25/cos126/assignments/classifier/
</sup></sub>