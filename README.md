# Covid Colombia API

I created this simple api to show somethings I can do using python, alphanumeric and geospatial data.
 This api was created using django-rest-framework and real cases of coronavirus in Colombia.
 The api is hosted in heroku, so if you want to check the page it would take 30 secs aprox for the app to load, 
 this is according to heroku settings. Unfortunaly Heroku doesnt allow postgis on free accounts, the main idea was that the api
 was capable of process points and give some information of that point; thats something I will correct in the future, perphaps
 migrating to another PaaS.
 
 The data was migrated from csv's files to Postgres database using Spoon.
 
 The API is hosted on: https://covid-rote-drf.herokuapp.com/ for swagger docs or https://covid-rote-drf.herokuapp.com/redoc/
 for redoc docs.
 
If you wanna play with the api this are some of the users and passwords.


user|password
----|--------
user_one|user_one_password
user_two|user_two_password
user_three|user_three_password


## Features

* The API uses jwt token to access some resources, so login is required.
* It uses CBV's for easy resources generation.
* The Database Engine is PostgreSQL.
* The API also supports filtering, ordering, searching and pagination 
as query parameters in multiple resources.

### Disclaimer
I think Automated testing it´s really important, since I learn some basic
usage of Unittest I try to use it on regular bases, but this repository was
created with the main idea of learning some basic and intermediate usage of drf.
So with that in mind testing is a feature i will implemented in the future.


