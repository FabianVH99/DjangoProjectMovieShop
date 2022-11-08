# Django CineShop
A responsive video store made in combination with Django and Tailwind css.
Designed to be deployed on Heroku.
Made by Fabian Vanhaelen for the course 'web topics' followed at Odisee hogeschool.
## Requirements
Please make sure the following software is present before going through the installation instructions for the project.

- **Python (>=3.10.7):** https://www.python.org/downloads/
- **PostgreSQL**: https://www.postgresql.org/download/
- **Git**: https://git-scm.com/downloads
- **Heroku cli**: https://devcenter.heroku.com/articles/heroku-cli

## Installation
Follow the installation instructions exactly as described. In order for the various components that the project consists of to run smoothly, specific configuration is required. The readme assumes the reader has a basic knowledge of Python and Django.

### Git configuration
Start by forking the project to your own repository. You should then clone your project to a location of your choosing on your machine. If you are not using a UI such as Github Desktop you can do so by running the following command:
```
git clone your_repo
```

You should now have the following directory structure:

├── movieShop
│   ├── movieShop
│   ├── shop
│   ├── static
├── .gitignore
├── LICENSE
├── manage.py
├── procfile
├── README.md
├── requirements.txt
└── runtime.txt

Navigate to Heroku: https://dashboard.heroku.com/
Make an account if you do not have one set up yet and make a new app.
You really only need to concern yourself with two things to link to your app which are **Dynos** and a **Heroku-postgres** database.

Navigate to the **deploy** section of your app and link your repository to the app. You can set up other things like what branch to deploy and turning automatic deployment on or off.
![Github_connect](assets\git.PNG)

You can now use the deploy button to build and launch your application. This will fail at this point because the app is missing some crucial configuration which will be added later.

It should be noted that although a Github repository is used as an example, you can also use Heroku git to deploy your app. You can find more on that Here: https://devcenter.heroku.com/articles/git

As a final step, go to settings.py and change the line ALLOWED_HOSTS to your own app url as well as CSRF_TRUSTED_ORIGINS.

### Packages
Heroku will take care of installing the packages on its own but in order to properly work with the project locally you will need to install some things.

You can now set up your virtual environment and install the required packages with pip:
```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```
Make sure everything is downloaded and installed without issue. Every package specified in the requirements file is, of course, required.

The project itself was made in Python 3.10.7, this is also the version specified in **runtime.txt**. This file essentially tells Heroku what Python version to use when building the application. You can change this to your desired version.

If everything went fine up to this point then tailwind should also have been installed thanks to the **django-tailwind** package. This requires some configuration however. The shop app provided is already seen as a tailwind app by the package so you can skip the initiation part. You do have to install some dependencies however:
```
python manage.py tailwind install
```

The classes used in the templates for this project should now be correctly stylized. After you have made any adjustments make sure to run the following command:
```
python manage.py tailwind build
```
This will compile every class into a css stylesheet for you to use, which will be saved in the *movieShop/shop/static* folder.

### Configuration Variables 
In the settings.py file, various sensitive information has been hidden by environment variables. To use them, make a **.env** file at the root of your project and populate them with the following data:

```
SECRET_KEY=YOURVALUE
DBHOST=YOURVALUE
DBNAME=YOURVALUE
DBUSER=YOURVALUE
DBPASS=YOURVALUE
DBPORT=YOURVALUE
SENDGRID_API_KEY=YOURVALUE
```
Change the values of these variables accordingly as installation continues. 
You can already supply a SECRET_KEY. To generate your secret key, run the following commands from the python shell: 
```
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```

Make sure to make a config var in Heroku for every variable in your .env file.
### Database setup
For this step we have to do some configuration in Heroku. How you do this is up to you, you can either use the cli or the webInterface. For the purposes of this project using the web interface is more than enough. If you have not yet added the Heroku-postgres addon to your app you should do so now. Navigate to the settings -> credentials overview of your database and copy the values shown to their respective variables in both the .env file and config vars on Heroku.

![Database Credentials](assets\db.png)

The settings.py file should now point to the correct Database configuration. 
You can make and migrate required data to your new database:
```
python manage.py makemigrations
python manage.py migrate
```

### Mail configuration
One feature of this app is that it allows users to stay updated on various products if they happen to be out of stock. For this to work you either need your own smtp server or make use of third party services. Case in point, this project uses sendgrid to take care of mail traffic.
If you choose to use your own server or a different service, you can remove the SENDGRID_API_KEY from your environment variables. 

Set up a SENDGRID account: https://app.sendgrid.com/

Before you can use the service, you will have to set up a verified sender. Do so now.
After you have done that, navigate to settings -> API key and generate a key. Make note of it, you will not be able to see it again. Replace SENDGRID_API_KEY value in your .env file with the api key you just received and make a config var for it in Heroku. You do not need to change anything else, the rest has been configured for you by the project. 

You should now have everything configured in order for the app to run properly.

## How to use the app
Usage of the app is pretty straightforward, aside from the extra Tailwind and sendgrid functionality it is a pretty typical Django app. Manipulation of database objects can be done via the admin interface (your_url/admin)

On the index page you will find a list of all movies in the database sorted by popularity. You can filter the movies show by using 
- The sort button
- The Platform filter
- The Categories list in the navbar

On the product page you can find details for the selected movie, some suggested movies from the same genre which are selected randomly and the option to either add the movie to cart or subscribe if the movie is out of stock.
A feature of this app is that it allows users to stay updated on various products if they happen to be out of stock. Essentially, what happens is that every time the stock field in the database is changed from zero to a higher value an email will be sent to users subscribed to whatever movie that correlates with the field that was just updated. Neither the admin nor the users need to concern themselves with unsubscribing from these mails, once the client has been updated they are automatically unsubscribed.