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


## Manual Testing

  | Feature | Description     | Expected Result |    Actual Result   | Pass/Fail | Comments |
|----------|-----------|-----------|----------------|---------|----------|
|Navbar| Login button navigates to Signin page   |    On click user Sign in Page is shown   |      As expected     |   PASS  |   N/A   |
|Navbar| Sign in Page renders succesfully   |    User can enter in login details  |      As expected     |   PASS  |   N/A   |
|Sign in| Onced signed in User is directed tot he home page   |    Home page renders successfully |      As expected     |   PASS  |   N/A   |
|Navbar| Logout button navigates to sign out page   |    Log out page renders successfully   |      As expected     |   PASS  |   N/A   |
|Sign out| Sign out warning modal requires user to confirm sign out  |    Signout modal and button renders succesfully |      As expected     |   PASS  |   N/A   |
|Sign out| Sign out buttons signs user out and redirects to home page  |    User is signed out and redirected to home page |      As expected     |   PASS  |   N/A   |
|Home page (Logged out)| Home page is rendered as a logged out user with prompts to sign up/sign in  |    Home page displays all features for a logged out user   |      As expected     |   PASS  |   N/A |
|Home Page| Sing up button directs user to a page to register as a site user  |    Sign up page rendered successfully   |      As expected     |   PASS  |   N/A   |
|Home Page| Log in button directs user to a page to sign in Page   |    Sign in page rendered successfully   |      As expected     |   PASS  |   N/A   |
|Sign up Page| Form to register as a site user is displayed and working  |    Sign up Form renders successfully and creates a user account   |      As expected     |   PASS  |   N/A   |


|Navbar| Login button navigates to login page   |    On click user is directed to Login page   |      As expected     |   PASS  |   N/A   |


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