---
title: "How to make client android application with Flask server"
date: 2020-05-10
image: "img/android_flask.webp"
context: "Android | Flask"
ReadingTime: 5
brief: "How to connect an android client with a flask server"
slug: "How to make client android application with Flask server"
---
* * *

You will learn how to connect android studio with flask server.


We all know that mobile devices are not powerful compared to PCs, we can do a lot of things with our smart phones but with limited resources, most of us consider that like a weakness point.

So, from the previous paragraph, we can conclude that mobile devices are not the best choice for many things such as machine learning.When we say machine learning we must also mention deep learning, because this last one is included in it, and for the record, deep neural network needs a lot of samples to be trained with so we need a lot of resources On the other hand.

Today, we will learn how to connect a simple android client side application made with java to python flask server, after reading this article you will be able to deploy you machine learning models.You will need Android studio, The HTTP requests and responses are handled in Android using [OkHttp](https://square.github.io/okhttp/) and Pycharm IDE for python coding.

This tutorial will show you how to send a simple text in which the Android app just makes an HTTP POST message for sending it, in the other hand, the flask app will return a simple message to confirm that the connection is successful.

The implementation of this project is available on GitHub: [Click here](https://github.com/dombroks/Android_client-Flask_server/).

Enough talking, let’s get started…

* * *

![](https://cdn-images-1.medium.com/max/800/0*N4a0py813N5deD1o)

Credit to Hal Gatewood from unsplash

### Building the Layout of the Android App

Our app is designed to be simple, but this will not prevent you form improving it in the future.So I decided to make one button in the main UI, after you click this button, it will test the connection between the android app and the flask app, the message returned from the flask app will displayed as Toast notification.

You can see that we used only one button with ID = connect.

After building the app user interface (UI), the next step is to implement the postRequest`()` method, which is responsible for message sending.

But, for doing that we must go through a small process…

![](https://cdn-images-1.medium.com/max/800/0*PBftIsvvZZBZNw-V.png)

By [Sylvain Saurel](https://medium.com/u/a4963fa09f17)

First, before using OkHttp, the project must support using it.You can do that by including one line to the dependencies section of the build.gradle (app module), the line is:

implementation 'com.squareup.okhttp3:okhttp:4.5.0'

Second, you must activate the using of clear text traffic in your app, in you can do that by inserting a this line to your application section in the manifest file:

android:usesCleartextTraffic="true"

It will be like this:

![](https://cdn-images-1.medium.com/max/800/1*ep1PqFJFW9nv8ZqUaK1W6w.png)

But we don’t forget to add the next permission in the manifest file:

```XML
<uses-permission android:name="android.permission.INTERNET" />
```

without it, you application will crash.

### Writing the java code of the Android App

```Java
package com.dombroks.android_flask;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {
    private String url = "http://" + "10.0.2.2" + ":" + 5000 + "/";
    private String postBodyString;
    private MediaType mediaType;
    private RequestBody requestBody;
    private Button connect;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        connect = findViewById(R.id.connect);
        connect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                postRequest("your message here", url);

            }
        });


    }

    private RequestBody buildRequestBody(String msg) {
        postBodyString = msg;
        mediaType = MediaType.parse("text/plain");
        requestBody = RequestBody.create(postBodyString, mediaType);
        return requestBody;
    }


    private void postRequest(String message, String URL) {
        RequestBody requestBody = buildRequestBody(message);
        OkHttpClient okHttpClient = new OkHttpClient();
        Request request = new Request
                .Builder()
                .post(requestBody)
                .url(URL)
                .build();
        okHttpClient.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(final Call call, final IOException e) {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {


                        Toast.makeText(MainActivity.this, "Something went wrong:" + " " + e.getMessage(), Toast.LENGTH_SHORT).show();
                        call.cancel();


                    }
                });

            }

            @Override
            public void onResponse(Call call, final Response response) throws IOException {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            Toast.makeText(MainActivity.this, response.body().string(), Toast.LENGTH_LONG).show();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                });


            }
        });
    }
}
```

Now, we will move to java code.

When you start reading the code, you will notice that we use the IP@ 10.0.2.2, this is just the default local address of the android emulator, and 5000 is the port number that we will use with it.You will some words like mediaType and requestBody, mediaType is just type the data that we will send such as text or image…etc, requestBody is the object that holds our message.These are some methods in the code that you must understand them:

1.  `onFailure()`: Called when the request couldn’t be executed due to cancellation, a connectivity problem, or timeout.
2.  `onResponse()`: Called when the HTTP response is successfully returned by the remote server.

The rest of the code will be easy to understand, But if you run into some problems, you can always go back to the OkHttp documentation from [here](https://square.github.io/okhttp/).

Now, you can test the app but it will show an error message because the server is off.While we mentioned the server, let’s continue building the Python HTTP server using Flask.

### Building the server-side using Flask

**Flask** is a micro [web framework](https://en.wikipedia.org/wiki/Web_framework "Web framework") written in [Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29 "Python (programming language)"). It is classified as a [microframework](https://en.wikipedia.org/wiki/Microframework "Microframework") because it does not require particular tools or libraries.It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself.[_From Wikipedia, the free encyclopedia_](https://en.wikipedia.org/wiki/Flask_%28web_framework%29)_._

```Python
import flask


app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    return "Successful Connection"

app.run(host="0.0.0.0", port=5000, debug=True)
```

From the picture above, you see that we created a flask app as an instance of the `Flask()` class, The `app.route()` decorator function associates a URL with a callback function.The `/`indicates the homepage of the server because the Android app requests will be sent to there.

The `handle_request()` method is responsible for return a message that confirms the connection between the client and the server.

the `run()` method uses the `host` argument for specifying the IP address. When the `host` is set to `“0.0.0.0”`, this means use the current IPv4 address. And of course, `5000`as port number.

The `debug` argument is for giving the permission to server for restarting itself if the code changed, otherwise you will be obligated to restart it manually to apply the new changes.

### The last step: Testing

You will need an internet connection.

Now you will be able to test you app, you have to run the android app and also the python code, clicking the connect button and then you will see that it will return “Successful Connection”.

### Summary

In this post you discovered how to build a client android application with python flask server.You can read an article to learn how to save your machine learning model to deploy it later, you just have to click here, if you want to contact me, this my [_LinkedIn_](https://www.linkedin.com/in/younes-belouche-641bb3197/) account, I hope you enjoyed, don’t for forget to hit Clap to encourage me :)

By [Younes Belouche](https://medium.com/@younes_belouche) on [May 10, 2020](https://medium.com/p/8b1d5c55446e).

[Medium Link](https://medium.com/@younes_belouche/how-to-make-client-android-application-with-flask-for-server-side-8b1d5c55446e)

