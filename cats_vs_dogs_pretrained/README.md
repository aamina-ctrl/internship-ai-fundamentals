# 🐱🐶 Cats vs Dogs Classification using ResNet50 Transfer Learning

## Objective

The objective of this project is to improve image classification accuracy using Transfer Learning with a pretrained ResNet50 model.

Instead of training a CNN from scratch, the model utilizes knowledge learned from the ImageNet dataset and trains only the final classification layers.

---

## What is Transfer Learning?

Transfer Learning is a deep learning technique where a model pretrained on a large dataset is reused for a different but related task.

ResNet50 has already learned general image features such as:

- Edges
- Shapes
- Fur
- Eyes
- Textures
- Object Patterns

This allows the model to achieve higher accuracy with significantly less training.

---

## Dataset

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

The model consists of:

- Data Augmentation
- ResNet50 Preprocessing
- Pretrained ResNet50 (Frozen)
- GlobalAveragePooling2D
- Dropout (0.2)
- Dense (1 neuron, Sigmoid)

---

## Pretrained Model

ResNet50 is loaded using ImageNet weights.

```
include_top=False
weights="imagenet"
```

The original ImageNet classifier is removed and replaced with a custom binary classifier.

---

## Frozen Layers

```
base_model.trainable = False
```

All pretrained convolutional layers remain unchanged while only the custom classification layers are trained.

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
2. Resize image
3. Apply ResNet50 preprocessing
4. Extract image features using ResNet50
5. Global Average Pooling
6. Binary Classification using Sigmoid
7. Display Cat or Dog prediction

---

## Output

The model displays:

- Training Accuracy
- Validation Accuracy
- Training Loss
- Validation Loss
- Accuracy Graph
- Prediction Results

---

## Results

Transfer Learning significantly improves model performance.

Approximate validation accuracy:

**90–92%**

This demonstrates the effectiveness of using pretrained feature extractors compared to training a CNN entirely from scratch.

---

## How to Run

Install dependencies:

```bash
pip install tensorflow matplotlib numpy
```

Run:

```bash
python cats_vs_dogs_pretrained.py
```

---

## Future Improvements

- Fine-tune the final ResNet50 layers
- Experiment with EfficientNet
- Experiment with MobileNetV2
- Hyperparameter optimization
- Model deployment using Flask or Streamlit
