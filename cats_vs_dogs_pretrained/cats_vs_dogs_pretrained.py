import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

train_ds=tf.keras.utils.image_dataset_from_directory("PetImages/train",
image_size=(180,180),
batch_size=32,
)
val_ds=tf.keras.utils.image_dataset_from_directory("PetImages/test",
image_size=(180,180),
batch_size=32,
)
class_names=train_ds.class_names
print(class_names)

plt.figure(figsize=(8,8))
for image,labels in train_ds.take(1):
    for i in range(9):
        plt.subplot(3,3,i+1)
        plt.imshow(image[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
plt.show()

data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
])
base_model=tf.keras.applications.ResNet50(
    input_shape=(180,180,3),
    include_top=False,
    weights="imagenet"
)
base_model.trainable=False
model=tf.keras.Sequential([
    data_augmentation,
    tf.keras.layers.Lambda(tf.keras.applications.resnet50.preprocess_input),
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1,activation="sigmoid") 
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

history=model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10
)
acc=history.history["accuracy"]
val_acc=history.history["val_accuracy"]
loss=history.history["loss"]
val_loss=history.history["val_loss"]
plt.plot(acc)
plt.plot(val_acc)
plt.title("Model Accuracy")
plt.legend(["Training","Validation"])
plt.show()

img=tf.keras.utils.load_img("my_dog.jpg", target_size=(180,180))
img_array=tf.keras.utils.img_to_array(img)
img_array=tf.expand_dims(img_array,0)
predictions=model.predict(img_array)
score=predictions[0][0]
print("Score:",score)
if score>0.5:
    print("Dog")
else:
    print("Cat")