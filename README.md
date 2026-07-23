# 🐱🐶 Cats vs Dogs Image Classification

## Overview

This repository contains two deep learning approaches for binary image classification of cats and dogs using TensorFlow and Keras.

The first implementation builds a Convolutional Neural Network (CNN) from scratch to understand the fundamentals of image classification. The second implementation uses Transfer Learning with a pretrained ResNet50 model to achieve higher accuracy by leveraging knowledge learned from the ImageNet dataset.

This project demonstrates image preprocessing, data augmentation, model training, validation, prediction, and performance evaluation.

---
## Theoretical Learning

Before implementing the projects in this repository, I built a strong theoretical foundation in Artificial Intelligence and Deep Learning. The concepts studied include:

- Introduction to Artificial Intelligence
- Machine Learning vs Deep Learning
- Artificial Neural Networks (ANN)
- Convolutional Neural Networks (CNN)
- Image Classification
- Convolution and Feature Extraction
- Activation Functions
- Pooling Layers
- Forward Propagation
- Loss Functions
- Optimizers
- Backpropagation
- Overfitting and Regularization
- Dropout
- Data Augmentation
- Transfer Learning
- Pretrained Models (ResNet50)
- Model Evaluation using Accuracy and Loss

These concepts were then applied through practical implementations using TensorFlow and Keras, reinforcing both theoretical understanding and hands-on experience.

## Project Structure

```
Cats_Dogs_Classification/
│
├── cats_vs_dogs.py
├── README_CNN.md
│
├── cats_vs_dogs_pretrained.py
├── README_ResNet50.md
│
├── PetImages/
│   ├── train/
│   └── test/
│
└── README.md
```

---

## Models Implemented

### 1. Custom CNN

- Built from scratch using TensorFlow/Keras
- Convolution + Pooling architecture
- Binary classification using Sigmoid activation

### 2. Transfer Learning (ResNet50)

- Uses pretrained ResNet50
- ImageNet pretrained weights
- Frozen convolutional base
- Custom classification head

---

## Dataset

The project uses the Cats vs Dogs image classification dataset organized into separate training and testing folders.

Directory structure:

```
PetImages/
    train/
        cats/
        dogs/
    test/
        cats/
        dogs/
```

---

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

---

## Features

- Image preprocessing
- Data augmentation
- CNN implementation from scratch
- Transfer learning using ResNet50
- Binary image classification
- Accuracy and loss visualization
- Prediction on custom images

---

## Results

| Model | Validation Accuracy |
|--------|---------------------|
| Custom CNN | ~60–70% |
| ResNet50 Transfer Learning | ~90–92% |

---

## How to Run

Install dependencies:

```bash
pip install tensorflow matplotlib numpy
```

Run the CNN model:

```bash
python cats_vs_dogs.py
```

Run the ResNet50 model:

```bash
python cats_vs_dogs_pretrained.py
```

---

## Future Improvements

- Fine-tune ResNet50
- Add MobileNetV2 implementation
- Improve dataset diversity
- Deploy using Flask or Streamlit
- Convert model to TensorFlow Lite

---
