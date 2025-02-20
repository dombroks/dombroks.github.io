---
title: "How to get your exact user location (latitude, longitude) in Android"
date: 2020-05-20
image: "img/location_android.webp"
context: "Android | Location"
ReadingTime: 3
draft: false
brief: "Guide on how to get the exact user location in Android"
slug: "How to get your exact user location (latitude, longitude) in Android"
---
* * *


Image Credit: [Kelsey Knight](https://unsplash.com/@kelsoknight) in [Unsplash](https://unsplash.com/)

We all know that getting the users current location is an important thing for apps that provide services that need location like pizza ordering, transportation, health care applications and a lot more. Location is based on two metrics, latitude and longitude, these are angles that uniquely define points on a sphere, from those values you can determine the exact user location, Google made it easy and clear for us by providing an API called [Fused Location Provider](https://developers.google.com/android/reference/com/google/android/gms/location/FusedLocationProviderClient "Fused Location Provider"). This API provides high accuracy with ability to control the power consumption by choosing the most efficient way to access the location.

Let me show how to use this API

First, we will check that Google’s library is added in our project by verifying that this `google()` is existed in the **build.gradle** file in the repositories.

Then we must add this line into our dependencies.

`implementation 'com.google.android.gms:play-services-location:17.0.0'`

You can change the version from 17.0.0 to the latest version, you will know the latest one from [Google APIs for Android](https://developers.google.com/android/guides/releases "Google APIs for Android").

Second, in the manifest file, we must add the permissions that allow us to get the location, these permissions are:

```XML
<uses-permission android:name="android.permission.ACCESS\COARSE\LOCATION"/>

<uses-permission android:name="android.permission.ACCESS\FINE\LOCATION"/>
```

By doing that, with those two permissions, the API will return a location with an accuracy approximately equivalent to a city block and we will get most relevant location information.

For security reasons starting from Marshmallow (android 6.0), we should request permissions from the users for the necessary access in runtime.

Next, we well implement our first method, checkPermission(), from the method name you will figure out that it is used to check that the permissions are granted or not by returning true or false.

```Java
 private boolean checkPermissions(){
    if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED &&
            ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED){
        return true;
    }
    return false;
}
```

But, for checking if the permissions are granted or not we must first request them by this simple method.**PERMISSION_ID** which is an integer value that helps us to identify the user’s action with which permission request. Declare it in you Main Activity like this:

```Java
int PERMISSION_ID = 75;
```

Note that **75** is just a number, you can use any number you want.

```Java
private void requestPermissions(){
    ActivityCompat.requestPermissions(
            this,
            new String[]{Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_FINE_LOCATION},
            PERMISSION_ID
    );
}
```

Now, we need a method which is called when the user allows or denies our requested permissions and it will help us to continue when the permissions are granted.

```Java
@Override
public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    if (requestCode == PERMISSION_ID) {
        if(grantResults.length>0 && grantResults[0] == PackageManager.PERMISSION_GRANTED){
            //Permissions are granted.
        }
    }
}
```

After that you check if the user has turned on the location from his device or not, the next method does that.

```Java
private boolean isLocationEnabled(){
    LocationManager Manager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
    return Manager.isProviderEnabled(LocationManager.GPS_PROVIDER) || Manager.isProviderEnabled(
            LocationManager.NETWORK_PROVIDER
    );
}
```

It’s time to use the Fused Location Provider API to get the current location, first we need to declare it as a variable like this:

`**FusedLocationProviderClient mFusedLocationClient;**`

And also we need to initialize it like this:

`mFusedLocationClient = LocationServices.getFusedLocationProviderClient(this);`

We almost done.

In order to get the user’s position, we’ll create a new method and call it by `getLastLocation()`

This method provides the last record of device’s location information and of course we’ll use our previous methods here to check whether the permissions are granted or not and the location is turned on

```Java
SuppressLint("MissingPermission")
private void getLastLocation(){
    if (checkPermissions()) {
        if (isLocationEnabled()) {
            mFusedLocationClient.getLastLocation().addOnCompleteListener(
                    new OnCompleteListener<Location>() {
                        @Override
                        public void onComplete(@NonNull Task<Location> task) {
                            Location location = task.getResult();
                            if (location == null) {
                                requestNewData();
                            } else {
                                //Do your logic here
                             
                            }
                        }
                    }
            );
        } else {
            Toast.makeText(this, "Turn on your location service", Toast.LENGTH_LONG).show();
            Intent MyIntent = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
            startActivity(MyIntent);
        }
    } else {
        requestPermissions();
    }
}
```

When you read the code you will notice that I wrote “Do your logic here”, it means that you need to write a code to define what you do with both longitude and latitude there, for example, you may want to create an intent there and put those longitude and latitude values inside this intent to pass them to another activity where you will use them. You can do what ever you want.

At this point we can say that our job is finished, but we have one case left to handle it…

In some devices, the previous recorded location information will be cleared if you turn off the location and switch on again so the location can be null. Also, if the user never turned on the location before using the app, your data will be null too. In order to prevent those cases from happening, we’ll make a new method which saves the location information, this method called `requestNewData()`

```Java
@SuppressLint("MissingPermission")
private void requestNewData(){

    LocationRequest Request = new LocationRequest();
    Request.setPriority(LocationRequest.PRIORITY_HIGH_ACCURACY);
    Request.setInterval(0);
    Request.setFastestInterval(0);
    Request.setNumUpdates(1);

    mFusedLocationClient = LocationServices.getFusedLocationProviderClient(this);
    mFusedLocationClient.requestLocationUpdates(
            Request, mLocationCallback,
            Looper.myLooper()
    );

}
```

And we should not forget our **callBack** method

```Java
private LocationCallback mLocationCallback = new LocationCallback() {
    @Override
    public void onLocationResult(LocationResult locationResult) {
        Location mLastLocation = locationResult.getLastLocation();
        //Do your logic here.
    }
};
```

Finally, we call the **getLastLocation()** method from **onCreate()** method.

Main Activity

```Java
public class MainActivity extends AppCompatActivity {

    int PERMISSION_ID = 75;
    FusedLocationProviderClient mFusedLocationClient;
    

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        mFusedLocationClient = LocationServices.getFusedLocationProviderClient(this);

        getLastLocation();
    }

    @SuppressLint("MissingPermission")
    private void getLastLocation(){
        if (checkPermissions()) {
            if (isLocationEnabled()) {
                mFusedLocationClient.getLastLocation().addOnCompleteListener(
                        new OnCompleteListener<Location>() {
                            @Override
                            public void onComplete(@NonNull Task<Location> task) {
                                Location location = task.getResult();
                                if (location == null) {
                                    requestNewData();
                                } else {
                                    //Do your logic here.
                                }
                            }
                        }
                );
            } else {
                Toast.makeText(this, "Turn on your location service", Toast.LENGTH_LONG).show();
                Intent MyIntent = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
                startActivity(MyIntent);
            }
        } else {
            requestPermissions();
        }
    }


    @SuppressLint("MissingPermission")
    private void requestNewData(){

        LocationRequest Request = new LocationRequest();
        Request.setPriority(LocationRequest.PRIORITY_HIGH_ACCURACY);
        Request.setInterval(0);
        Request.setFastestInterval(0);
        Request.setNumUpdates(1);

        mFusedLocationClient = LocationServices.getFusedLocationProviderClient(this);
        mFusedLocationClient.requestLocationUpdates(
                mLocationRequest, mLocationCallback,
                Looper.myLooper()
        );

    }

    private LocationCallback mLocationCallback = new LocationCallback() {
        @Override
        public void onLocationResult(LocationResult locationResult) {
            Location mLastLocation = locationResult.getLastLocation();
            //Do your logic here.
        }
    };

    private boolean checkPermissions() {
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED &&
                ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
            return true;
        }
        return false;
    }

    private void requestPermissions() {
        ActivityCompat.requestPermissions(
                this,
                new String[]{Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_FINE_LOCATION},
                PERMISSION_ID
        );
    }

    private boolean isLocationEnabled() {
        LocationManager Manager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        return Manager.isProviderEnabled(LocationManager.GPS_PROVIDER) || Manager.isProviderEnabled(
                LocationManager.NETWORK_PROVIDER
        );
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == PERMISSION_ID) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                getLastLocation();
            }
        }
    }

    @Override
    public void onResume(){
        super.onResume();
        if (checkPermissions()) {
            getLastLocation();
        }

    }
}
```

### Summary

In this post you discovered how to get the current location of users with high accuracy, if you want to contact me, this my [_LinkedIn_](https://www.linkedin.com/in/younes-belouche-641bb3197/) profile, I hope you enjoyed. Credits goes to Mr. Ferdousur Rahman Sarker for his wonderful tutorials.

By [Younes Belouche](https://medium.com/@younes_belouche) on [May 20, 2020](https://medium.com/p/c23b2ae9d380).

[Medium Link](https://medium.com/@younes_belouche/how-to-get-the-current-location-latitude-longitude-in-android-c23b2ae9d380)
