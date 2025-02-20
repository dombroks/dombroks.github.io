---
title: "The right way to implement a search feature to filter a list using BLOC in Flutter"
date: 2022-05-25
image: "img/bloc.webp"
context: "Flutter | BloC"
ReadingTime: 5
draft: false
brief: "In this post, you will learn how Flutter Bloc could play a huge role in optimizing our ressources consumption so that we can have a better user experience and a better rationalization of how to use what we have"
slug: "The right way to implement a search feature to filter a list using BLOC in Flutter"
---

Hi there, in this post, you will learn how Flutter Bloc could play a huge role in optimizing our ressources consumption so that we can have a better user experience and a better rationalization of how to use what we have.

This post will also teaches you the difference between bloc and cubit, and will answer more of your questions, questions like why the two come in one library that called Bloc and when to use each one of them.

I will be straightforward, so, I will start directly with an example. Lets say you want to build a page that contains a text field and a button, the page allows the user to enter a text and click a button to perform a search operation. When the user clickes the button, a GET request containing the entered keyword will be sent to the server and this last one will filter the complete list of items and returns a response that contains list items that correspond to what the user wants to see.

Lets say you chose to implement this whole thing using cubit, you create a cubit and you put inside it a method called search that takes a string and sends a request to receive a response that contains a list and finally emits a state that contains the data that we want to display to our user. The UI part is much simpler, you call the search method from the search button’s onPressed callback and pass the search keyword that we got from the text field assingned controller. Till now, everything is simple, we just created a cubit that has a method in which the user can invoke and pass some inputs in order to receive a state. States are transmitted inside a stream which considred as a flow of data.

In order to display the data we got from the server, we create a listview and wrapped inside a blocBuilder widget, this widget enables us to subscribe to a stream and wait for states which we need to update our UI. Congratulations, you have finished implementing the search feature.

One day, you felt the need of removing the search button, the idea came when you were using Facebook and you discovred that removing the search button will make the user more comfortable. So, you removed it, and you tweaked the text field code a little bit so that cubit’s search method will be called when the entered keyword changes and of course you will use the onChanged callback like this:

![](https://cdn-images-1.medium.com/max/800/1*v0S9HojszdIoPRx-lEcXgQ.png)

You felt good and you thought everything is working perfectly and suddenly your back-end guy has called, he told you that he found a big issue, he noticed a lot of unnecessary requests that come from the app related to the search feature. Your friend grab a piece of paper and started explaning the problem to you, he directly put an example into action and Elon musk in involved :).

The example was about entering “Elon musk” as a search word, he typed “Elon” and you noticed the app has sent 4 requests to the server, one request for each of these strings: “E”, “El”, “Elo” and “Elon”. Also, this problem happens when you remove a letter, you will see that the app will sends another request, for example, if you remove “n” from “Elon”, then another request to the server will be send and you get new data as response to the word “Elo”, imagine if you are using Firebase Firestore where you will be charged by how much requests you performed :).

This is where Bloc comes handy, unlike cubit, Bloc recieves events as input and not functions and these events will be transmitted in a events stream, this way we can controll the execution time of our functions because we controll events sending in the stream.

How we fix this? the first thing you do is to convert you cubit to a bloc and make a new event called searchEvent, this way your text field onChanged callback will be like this :

![](https://cdn-images-1.medium.com/max/800/1*_Xef7dy4LY_UcNIFGj-1wg.png)

after that, you set your bloc to execute the search function when the search event comes, it could be done like this:

![](https://cdn-images-1.medium.com/max/800/1*DbuNDXUvPVMEFRDl17u5NA.png)

One last thing and you finish, you use the power of RxDart by applying the depounceTime so that you ignore any events that happen between a time range we define. The code will be something like this:

![](https://cdn-images-1.medium.com/max/800/1*T33kql3micqfBfYOVvBAIg.png)

You can modify the code to add more constraints. and this is it.

I like to conclude this article by answering some questions, such as:

*   Why Bloc and Cubit come in one library?
*   Could we use the two in the same project?
*   When to use what?

The answers are:

*   They come in one library because they share almost the same work mechanism, they share streams to update the UI.
*   Yes, we can use the two in the same project, but we apply them depending on the usecases.
*   We can use cubit when we have screens that don’t require a lot of events, this is up to the developer to choose what suits him/her better.

Thanks for reading this article ❤

Connect with me on [Linkedin](https://www.linkedin.com/in/younes-belouche-641bb3197/), [Instagram](https://www.instagram.com/younes_belouche/) and [Github](https://github.com/dombroks).

By [Younes Belouche](https://medium.com/@younes_belouche) on [April 25, 2022](https://medium.com/p/799969781fdb).

[Medium link](https://medium.com/@younes_belouche/the-right-way-to-implement-a-search-feature-to-filter-a-list-using-bloc-in-flutter-799969781fdb)

