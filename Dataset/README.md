# Dataset

## Overview

This folder contains the dataset used for the Cats vs Dogs image classification projects implemented in this repository.

The dataset is organized into separate training, testing, and prediction folders to support model development and evaluation.

---

## Folder Structure

```
Dataset/
│
├── PetImages/
│   ├── train/
│   │   ├── cats/
│   │   └── dogs/
│   │
│   ├── test/
│   │   ├── cats/
│   │   └── dogs/
│   │
│   └── final_Unseen/
│       └── my_dog.jpg
│
└── README.md
```

---

## Training Dataset

The `train` folder contains cat and dog images used to train both the custom CNN and the ResNet50 transfer learning model.

> **Note:** Due to GitHub file size limitations and extraction constraints, only a portion of the original training dataset has been included in this repository (approximately **150–180 images per class**). The complete dataset contains significantly more training images.
To reproduce the project using the complete dataset, download the original dataset from Kaggle:

**Dataset:** Cats and Dogs Image Classification  
https://www.kaggle.com/datasets/samuelcortinhas/cats-and-dogs-image-classification/data
---

## Testing Dataset

The `test` folder contains separate cat and dog images used to evaluate the trained models.

This folder includes the complete extracted testing dataset used during model validation.

---

## Final Unseen Image

The `final_Unseen` folder contains images that were **not part of the training or testing datasets**.

These images are used to evaluate how well the trained models generalize to completely unseen data.

Current file:

- `my_dog.jpg`

---

## Dataset Usage

This dataset is used for:

- Training the Custom CNN model
- Training the ResNet50 Transfer Learning model
- Model validation
- Prediction on unseen images
- Performance evaluation

---

## Image Specifications

- Image Format: JPG
- Image Size Used During Training: **180 × 180 pixels**
- Color Channels: RGB (3 Channels)

---

## Note

The dataset included in this repository is intended for educational and demonstration purposes. A reduced version of the training dataset has been uploaded to keep the repository lightweight while preserving the project structure and reproducibility.
