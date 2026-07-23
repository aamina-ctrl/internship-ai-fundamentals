# 🐱🐶 Cats vs Dogs Image Classification

## Overview

This project explores two deep learning approaches for binary image classification of cats and dogs using TensorFlow and Keras.

The first implementation builds a Convolutional Neural Network (CNN) from scratch to understand the fundamentals of image classification. The second implementation uses Transfer Learning with a pretrained ResNet50 model to achieve higher accuracy by leveraging knowledge learned from the ImageNet dataset.

This project demonstrates image preprocessing, data augmentation, model training, validation, prediction, and performance evaluation.

---

## Internship Context

This project was completed during my **Software Engineering & AI Internship** as part of my learning in Deep Learning and Computer Vision.

The objective was to understand both fundamental CNN architectures and modern Transfer Learning techniques by implementing and comparing two different image classification models.

---

## Theoretical Learning

Before implementing this project, I built a strong theoretical foundation in Artificial Intelligence and Deep Learning. The concepts studied include:

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

---

## Folder Structure

```
Cats_Dogs_Classification/
│
├── Dataset/
│   └── PetImages/
│       ├── train/
│       └── test/
│
├── cats_vs_dogs/
│   ├── cats_vs_dogs.py
│   └── README.md
│
├── cats_vs_dogs_pretrained/
│   ├── cats_vs_dogs_pretrained.py
│   └── README.md
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

This project uses the Cats vs Dogs image classification dataset organized into separate training and testing folders.

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
