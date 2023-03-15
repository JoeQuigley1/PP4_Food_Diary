# USER STORY TESTING

 ### As a Site User I can  access an individual post  so that I can see the details clearly

 ### As a Site User I can  create a post at the click of a button * so that I can easily contribute to the site

### As a Site User I can like or unlike posts so that I can interact with the content

### As a Site User I can comment on posts so that I can be involved in other users content

### As a Site User I can sign up with an email and password so that I can gain access to the blog site

### As a Site User I can logout of the site  so that I can ensure that my account is safe if I use multiple devices

### As a Site User I can login  so that I can have secure access to the site

### As a Site User I can view a list of recipes  so that I can choose one to open

### As a Site User/ Admin I can view the number of likes on each post so that I can see which posts are most popular.

### As a Site Admin I can ** approve or disapprove comments ** so that ** I can filter out objectionable comments**

### As a Site User/Admin I can view comments on an individual post so that I can read the conversation

### As a Site User I can create and save drafts so that I can submit them later

### As a Site Admin I can create, read, update and delete posts so that I can manage my blog content

## Validator Testing

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page                 | Logged Out | Logged In |
|----------------------|------------|-----------|
| submit_recipe.html   | N/A        | No errors |
| base.html            | No errors  | No errors |
| index.html           | No errors  | No errors |
| recipe_detail.html   | No errors  | No errors |
| edit_recipe.html     | N/A        | No errors |
| login.html           | No errors  | N/A       |
| logout.html          | N/A        | No errors |
| signup.html          | No errors  | N/A       |
| user_submissions.html| No errors  | No errors |


## Python

Pycodestyle was installed to validate the python code written.

- All code has been validated with no errors present.
- Settings.py file has 5 'line too long' errors which are constant with the use of django.

| App       | Models.py |    Forms.py    | Urls.py | Views.py |
|-----------|-----------|----------------|---------|----------|
| Cookbook  |    PASS   |      PASS      |   PASS  |   PASS   |
| FoodDiary |    PASS   |      PASS      |   PASS  |   PASS   |


## Lighthouse Performance

![Lighthouse Testing](docs/testing/Screenshot%202023-03-15%20202504.png)