---
title: "Building a REST API for a Machine Learning Model and Mobile App Integration: Part1"
date: 2024-02-11
image: "img/ml_flutter_api.webp"
context: "Machine learning | Flutter | API"
ReadingTime: 4
draft: false
brief: "Part 1 of how to build a REST API for your ML model and consume it from mobile client"
slug: "Building a REST API for a Machine Learning Model and Mobile App Integration: Part1"
---


Post's image designed by the author.

In 2020, I wrote two Medium posts about two important topics. The first one talks about how to save your trained machine learning model, in which you learn how to serialize/de-serialize your ML model so that you can load it whenever needed. The second post was about creating a simple Android application using Java that consumes a simple REST API built using Flask. These two posts complete each other because when you build an ML model, you need to deploy it and for that, you need to make it available by building an API for it so that users can use your model by consuming the API you built from a client whether it is mobile or web. These are the links associated with the two posts:

[**How to save your trained machine learning model**](https://medium.com/@younes_belouche/how-to-save-your-trained-machine-learning-model-a159455218f5?source=your_stories_page-------------------------------------)

[**How to make client android application with Flask for server side**](https://medium.com/@younes_belouche/how-to-make-client-android-application-with-flask-for-server-side-8b1d5c55446e?source=your_stories_page-------------------------------------)

After a while, these posts received positive feedback, and many people found them useful. The thing I like most is that many students benefit from these posts. I realized the need to write again about building an API to make a machine-learning model accessible to users, whether through mobile or web applications.

So now, after three years, I am writing a comprehensive guide about how to build a RESTful API for a machine learning model and deploy it to be consumable from a Flutter mobile application (or any front-end). For the machine learning model, I decided to go with a pre-trained model called **ResNet50**, that’s because training an ML model is out of our scope. I chose Django for the backend, and Flutter for mobile. If you noticed, I chose a different tech stack to use from the old one, now we will use Django instead of Flask and Flutter instead of Java. Don’t worry, I will tell you why. Next, we will dive into the tech stack we’ll be using.

**Tech Stack**

**1\. Django: Rapid Development, Robustness, and Extensive Ecosystem**

According to the official documentation, “Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source. “

![](https://cdn-images-1.medium.com/max/800/1*8a4re_Iz4_hxc6UtIbMU2A.png)

> _“Django makes it easier to build better web apps more quickly and with less code.”_

I chose Django for many reasons, one of them is that it is fast and encourages rapid development because it takes care of a lot of things for you, you will be surprised at how fast you can create API endpoints. Also, it is batteries included, which means that everything that you need to build a complete web application already comes with it. Flask is considered a micro-framework; it doesn’t have all that Django has but it provides some flexibility. I will not compare the two frameworks since comparing them is out of our scope.

**2\. Flutter: Cross-platform Development**

It is an open-source UI software development kit created by Google. It enables you to build cross-platform apps for mobile, web, and desktop using a single codebase. With Flutter, you can save development time by sharing code across different platforms. Its popularity has grown rapidly due to its performance and native-like user interfaces. While native Android development has its merits, Flutter’s cross-platform capabilities make it an ideal choice for this project.

![](https://cdn-images-1.medium.com/max/800/1*Dw1qUD5aCkIobxCNjS749A.jpeg)

**3\. ResNet50: Pre-trained Deep Learning Model**

We will use a pre-trained deep-learning model called ResNet50. ResNet50 is a widely adopted model with 50 layers, trained on extensive data. Leveraging a pre-trained model eliminates the need to gather and train on large amounts of data, making it an efficient choice for our demonstration.

![](https://cdn-images-1.medium.com/max/800/1*gquE5sMA0OJw8c3pDrU0Yg.jpeg)

[Source](https://miro.medium.com/v2/resize:fit:720/format:webp/0*tH9evuOFqk8F41FG.png)

In the upcoming parts of this series, we’ll dive into the implementation details, step-by-step instructions, and code examples to build the machine learning API with Django and consume it from a Flutter mobile application.

By [Younes Belouche](https://medium.com/@younes_belouche) on [February 11, 2024](https://medium.com/p/417a0d8c3df8).

[Medium link](https://medium.com/@younes_belouche/building-a-rest-api-for-a-machine-learning-model-and-mobile-app-integration-part1-417a0d8c3df8)

