# 🐱🐶 Cats vs Dogs Classification using Custom CNN

## Objective

The objective of this project is to build a Convolutional Neural Network (CNN) from scratch for binary image classification between cats and dogs.

This implementation focuses on understanding the complete CNN pipeline without using pretrained models.

---

## Dataset

The project uses a dataset containing images of cats and dogs arranged into separate training and testing folders.

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

## Model Architecture

The CNN consists of the following layers:

- Data Augmentation
- Rescaling
- Conv2D (16 Filters)
- MaxPooling2D
- Conv2D (32 Filters)
- MaxPooling2D
- Conv2D (64 Filters)
- MaxPooling2D
- Flatten
- Dense (128 neurons)
- Dropout (0.3)
- Dense (1 neuron, Sigmoid)

---

## Data Augmentation

The following augmentation techniques are applied during training:

- Random Horizontal Flip
- Random Rotation
- Random Zoom

These techniques improve model generalization and reduce overfitting.

---

## Training Configuration

- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Batch Size: 32
- Image Size: 180 × 180
- Epochs: 10

---

## Prediction Pipeline

1. Load image
2. Resize to 180 × 180
3. Convert image to array
4. Expand dimensions
5. Predict using trained model
6. Apply sigmoid threshold
7. Display Cat or Dog prediction

---

## Output

The project displays:

- Training Accuracy
- Validation Accuracy
- Training Loss
- Validation Loss
- Accuracy Graph
- Prediction Results

---

## Results

The custom CNN successfully learns visual features from scratch and performs binary image classification with approximately **60–70% validation accuracy**.

---

## How to Run

Install dependencies:

```bash
pip install tensorflow matplotlib numpy
```

Run:

```bash
python cats_vs_dogs.py
```

---

## Future Improvements

- Increase dataset size
- Hyperparameter tuning
- Batch normalization
- Early stopping
- Transfer learning
