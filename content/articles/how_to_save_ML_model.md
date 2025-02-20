---
title: "How to save your trained machine learning model"
date: 2020-05-30
image: "img/pickle.webp"
context: "Machine learning | Python"
ReadingTime: 2
draft: false
brief: "Guide on how to save a trained model with ability to reload it"
slug: "How to save your trained machine learning model"
---

* * *

### Efficient Machine Learning Model Saving and Reloading in Python: A Guide to Pickle and Joblib for Machine Learning

Save a trained model with ability to reload it


Article image by Zan on Unsplash

We all know that training models process often takes the big part of our time. So, in this article we mention a way or two to save our trained model, therefore, you will save time by training the model once and reload it when you need it.

![](https://cdn-images-1.medium.com/max/800/1*REGnvwZmowvVdUIIKtd-2Q.jpeg)

Photo by [Christine](https://www.flickr.com/photos/spanginator/3414847568/), some rights reserved.

#### First, let me introduce you to pickle

Pickle module is a powerful algorithm for serializing and de-serializing a Python object structure. Serialization is the operation or the process of turning an object hierarchy into a byte stream, this process is called “Pickling” when we talk about Pickle, and “unpickling” is the inverse operation, meaning that the byte stream is converted back into an object hierarchy.

#### Let me give you a simple example:

#### 1.Saving the model

![](https://cdn-images-1.medium.com/max/800/1*taFWXqPQguRHHO13rKGjig.png)

Serializing and saving our trained model

#### 2.Reloading the model

![](https://cdn-images-1.medium.com/max/800/1*P4-5jjwTUm46dOPeW3dLzg.png)

Reloading our model

Running the example saves the model to “model.pkl” in your local working directory. Load the saved model and evaluating it provide an estimation of the accuracy of the model on an unseen data.

You can also use Joblib, it is like pickle and easy to use. Those two modules are used in Scikit-Learn machine learning models but don’t worry, you can save your Keras’s models like this:

![](https://cdn-images-1.medium.com/max/800/1*zov3ZqNFES2wc2p_S32IDA.png)

Keras model

### Summary

In this post you have discovered how to persist your machine learning algorithms in Python, if you want to contact me, this my [_LinkedIn_](https://www.linkedin.com/in/younes-belouche-641bb3197/) account, I hope you enjoyed.

By [Younes Belouche](https://medium.com/@younes_belouche) on [April 30, 2020](https://medium.com/p/a159455218f5).

[Medium Link](https://medium.com/@younes_belouche/how-to-save-your-trained-machine-learning-model-a159455218f5)

