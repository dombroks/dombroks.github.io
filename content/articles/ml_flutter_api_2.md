---
title: "Building a REST API for a Machine Learning Model and Mobile App Integration: Part2"
date: 2024-02-11
image: "img/ml_flutter_api.webp"
context: "Machine learning | Flutter | API"
ReadingTime: 4
draft: false
brief: "Part 2 of how to build a REST API for your ML model and consume it from mobile client"
slug: "Building a REST API for a Machine Learning Model and Mobile App Integration: Part2"
---
Post's image designed by the author.

**Introduction**

In the previous post, we introduced the tech stack for our journey. Now, it’s time to delve into the process of preparing the machine learning model for seamless integration with Django. We’ll focus on three critical aspects:

1.  **Overview of the Pre-trained Machine Learning Model**: Understand what pre-trained models are and why they are a game-changer in the field of machine learning.
2.  **Introduction to the Model’s Architecture and Purpose:** Dive into the fascinating world of ResNet-50, a pre-trained deep learning model with a remarkable architecture, and discover its primary use cases.
3.  **Loading and Preparing the Model for Integration with Django**: Learn how to write the code that initializes the model and prepares it for use in Python.

Let’s embark on this journey of understanding and preparation.

**Overview of the pre-trained machine learning model**

A fundamental question to address is: what exactly is a pre-trained model, and why is it such a valuable asset in machine learning?

I got the answers for you, a pre-trained model has already been trained on a dataset and contains the weights and biases that represent the features of the dataset on which it was trained. Learned characteristics are frequently transferable to new data. A model trained on a big dataset of bird photos, for example, will contain learned features such as edges or horizontal lines that are transferable to your dataset. We benefit from pre-trained models for a variety of reasons. You save time by employing a pre-trained model. Someone else has already invested time and compute resources in learning a large number of features, and your model will most likely profit from it.

What does ResNet stand for? ResNet stands for Residual Network which is a specific type of CNN (Convolutional Neural Network). It was introduced in the 2015 paper “Deep Residual Learning for Image Recognition” by He Kaiming, Zhang Xiangyu, Ren Shaoqing, and Sun Jian. CNNs are commonly used to power computer vision applications.

ResNet-50 is a pre-trained deep learning model that consists of 50 layers and is trained on large-scale datasets. It has gained immense popularity in the computer vision community due to its exceptional performance in various tasks, including image classification and object detection. To save valuable time, computing resources, and effort, I chose to use this deep learning model to avoid creating one from scratch.

**Introduction to the Model’s Architecture and Purpose**

Before we explore the ResNet-50 architecture, let’s acquaint ourselves with its precursor, ResNet-34. ResNet-34 is a version of the original ResNet design, consisted of 34 weighted layers. By exploiting the idea of shortcut connections, it offered a creative solution to the vanishing gradient problem while adding more convolutional layers to a CNN. A residual network is created when a shortcut connection “Skips over” some levels of a conventional network.

![](https://cdn-images-1.medium.com/max/800/1*JEGNYy9rXMj_XN7W1Qjo9g.png)

Image source: [ResNet-34 | Kaggle](https://www.kaggle.com/datasets/pytorch/resnet34)

ResNet-50’s architecture is similar to the model shown above, but with one significant difference. The bottleneck design is used for the building block in the 50-layer ResNet. A bottleneck residual block employs 11 convolutions to limit the number of parameters and matrix multiplications. This allows for significantly faster layer training. It employs a three-layer stack rather than two levels.

The 50-layer ResNet architecture includes the following elements:

*   **A 7×7 kernel convolution** alongside 64 other kernels with a 2-sized stride.
*   **A max pooling layer** with a 2-sized stride.
*   **9 more layers** 3×3,64 kernel convolution, another with 1×1,64 kernels, and a third with 1×1,256 kernels. These 3 layers are repeated 3 times.
*   **12 more layers** with 1×1,128 kernels, 3×3,128 kernels, and 1×1,512 kernels, iterated 4 times.
*   **18 more layers** with 1×1,256 cores, and 2 cores 3×3,256 and 1×1,1024, iterated 6 times.
*   **9 more layers** with 1×1,512 cores, 3×3,512 cores, and 1×1,2048 cores iterated 3 times.

(Up to this point the network has 50 layers)

*   **Average pooling**, followed by a fully connected layer with 1000 nodes, using the softmax activation function.

![](https://cdn-images-1.medium.com/max/800/1*9SrzCTHIVgxzPu3VmvWmVw.png)

Despite the use cases of ResNet-50, we are going to use it for **_Image Classification_**.

Image classification is the task of providing a label or class to a complete image is known as image classification. Images are expected to have no more than one class. Image classification models accept an image as input and estimate which class the image belongs to.

![](https://cdn-images-1.medium.com/max/800/1*UkmLk__zZW1Wte80e4byhg.png)

[Source](https://raw.githubusercontent.com/floydhub/image-classification-template/master/images/classification.png)

**Loading and Preparing the Model for Integration with Django**

Now it is time to write some code and open your favourite IDE (I prefer Pycharm), then create an empty Python file and start coding.

```Python
import tensorflow as tf
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np

def initialize_model():
    # Initialize the model
    return tf.keras.applications.resnet50.ResNet50(
        include_top=True, weights='imagenet', input_tensor=None,
        input_shape=None, pooling=None, classes=1000
    )
def preprocess_image(image_sample):
    # Convert image into array
    transformed_image = image.img_to_array(image_sample)
    # Expand the dimension
    transformed_image = np.expand_dims(transformed_image, axis=0)
    # Preprocess the image
    transformed_image = preprocess_input(transformed_image)
    return transformed_image

def decode_prediction(prediction):
    prediction_label = decode_predictions(prediction, top=1)
    return prediction_label[0][0][1], prediction_label[0][0][2] * 100

def predict(image1):
    # Load the model
    model = initialize_model()
    # Process image
    transformed_image = preprocess_image(image1)
    # Predict and print the result
    prediction = model.predict(transformed_image)
    decoded_prediction, score = decode_prediction(prediction)
    print('%s (%.2f%%)' % (decoded_prediction, score))
    return decoded_prediction, score
```

As you can see, we have four functions, **initialize_model**, **preprocess_image**, **decode_prediction**, and **predict**. The initialize_model function Instantiates the ResNet50 architecture with the following arguments:

**_include_top:_** decides whether to use the fully-connected layer at the top of the network.

**_weights_**: path to the weights file to be loaded.

**_input_tensor_**: optional Keras tensor (i.e. output of layers.Input()) to use as image input for the model.

**_input_shape_**: optional shape tuple, only to be specified if include_top is set to False.

**_pooling_**: optional pooling mode for feature extraction when include_top is set to False.

**_classes_**: optional number of classes to classify images into, only to be specified if include_top is set to True and if no weights argument is specified.

After that, the preprocess_image function preprocesses a tensor or Numpy array encoding a batch of images. It takes an image and makes it ready for our model. If you want more details, check the documentation [here](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet50/preprocess_input).

Now the rest is simple, the decode_prediction function decodes the prediction for us and the predict function is the one that we are going to use to make the prediction.

**Conclusion**

In this post, we explored the pre-trained ResNet-50 model, discussed its architecture and purpose, and learned how to load and prepare the model for integration with Django. With the model ready, we can now proceed to the next part of the series, where we’ll focus on building the API endpoints in Django to expose the machine learning capabilities.

**Resources**

[ResNet-50: The Basics and a Quick Tutorial](https://datagen.tech/guides/computer-vision/resnet-50/#:~:text=ResNet-50%20is%20a%2050,networks%20by%20stacking%20residual%20blocks.%29)

By [Younes Belouche](https://medium.com/@younes_belouche) on [February 11, 2024](https://medium.com/p/fd40927fcdc2).

[Medium link](https://medium.com/@younes_belouche/building-a-rest-api-for-a-machine-learning-model-and-mobile-app-integration-part-2-fd40927fcdc2)

