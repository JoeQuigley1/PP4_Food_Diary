# Cookbook
Cook book is a site where users can quickly find a tasty recipe to use in their day to day lives.
It is built with a sense of community in mind where users can share and interact with each other. 

# Live website
A link to the live website can be found [here](https://food-diary.herokuapp.com/)

### Site purpose:
The goal of this project was to create an onlie recipe blog.  Users of the blog can come together to use and share their recipe ideas. 

### Features

## Navbar 
 # Logged In View
  ![NavBar Logged In](docs/testing/Navbar-loggedin.png)


# Logged Out View
  ![NavBar Logged Out](docs/testing/Navbar-loggedout.png)



# Testing 

-  All testing documentation can be found [here](/TESTS.md)


# Deployment
The site was deployed to Heroku. The following steps were taken:
- Install Django & Gunicorn:
```pip3 install 'django<4' gunicorn```
- Install Django database & psycopg:
```pip3 install dj_database_url psycopg2```
- Install Cloudinary:
```pip3 install dj3-cloudinary-storage```
- Creating the requirements.txt file with the following command:
```pip3 freeze --local > requirements.txt```
- Django project created using:``
```django-admin startproject fooddiary```
- Django project created using:``
```django-admin startapp cookbook```
- the changes were then migrated using:
```python3 manage.py migrate```
- navigated to [Heroku](www.heroku.com) & created a new app called food-diary.
- added the Heroku Postgres database to the Resources tab.
- navigated to the Settings Tab, to add the following key/value pairs to the configvars:
1. key: SECRET_KEY | value: randomkey
2. key: PORT | value: 8000
3. key: CLOUDINARY_URL | value: API environment variable
4. key: DATABASE_URL | value: value supplied by Heroku
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file
- add an import os statement for the env.py file.
- added Heroku to the ALLOWED_HOSTS in settings.py
- created the Procfile
- pushed the project to Github
- connected my github account to Heroku through the Deploy tab
- connected my github project repository, and then clicked on the "Deploy" button

## Final Deployment

### Gitpod
- Ensure 'DEBUG = FALSE' in settings.py
- Add "X_FRAME_OPTIONS= 'SAME ORIGIN'" to settings.py, to ensure that summernote editor works in deployed project.
- Add, commit and push deployment commit to GitHub.

### Heroku
- Go to 'Settings' tab and reveal config vars. Remove COLLECT_STATIC environment variable.
- Go to 'Deploy' tab and scroll down to 'Deploy Branch' (ensure github repo is connected). Run deployment.
- Wait for confirmation that application has deployed.

Technologies Used 

## Languages 

+ [HTML](https://en.wikipedia.org/wiki/HTML "HTML") - Provided in the Code Institute template
+ [CSS](https://en.wikipedia.org/wiki/CSS "CSS") - Provided in the Code Institute template
+ [JavaScript](http://en.wikipedia.org/wiki/JavaScript "JavaScript") - Provided in the Code Institute template
+ [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")
+ [Django](https://www.djangoproject.com/ "Django")
+ [SQL- Postgres](https://www.postgresql.org/ "SQL - Postgres")


## Libraries and Frameworks
Python libraries and api used
- [Google auth](https://google-auth.readthedocs.io/en/master/index.html)
- [Heroku](https://www.heroku.com/)
- [Gitpod](https://www.gitpod.io/)
- [GitHub](https://github.com/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

## Credits

- [Martina Terlevic](https://github.com/SephTheOverwitch): Helped with addressing realistic goals for my project given my time and personal circumstances. 
- “I think therefore I blog” walkthrough: Provided initial steps for setting up the project and deployment. In addition the instructions provided in the walkthrough guided me in the structure and styling of the project. 
-  "I think therefore I blog" + "Hello Django" + Slack + Stackoverflow + fellow  [student](https://github.com/CluelessBiker) + [VeryAcademy](https://www.youtube.com/watch?v=pNVgLDKrK40) helped in creating basic CRUD functionality. 
- Scott Tutor Support: Help with the user submissions showing correct content. 
- Joshua and Ger Tutor Support: Help getting the submission functionality to render successfully and linking urls and using slugs correctly. 
- [Django documentation](https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/): Helped when using generic Django 
- [Stack Overflow](https://stackoverflow.com/questions/4526273/what-does-enctype-multipart-form-data-mean): Help with forms submitting and processing file data. 
- [Stack Overflow](https://stackoverflow.com/questions/37207742/django-redirect) Help with procesessing views.

