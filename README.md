# DanceZone Blog

(Developer: Simmi Keshri)

Am I Responsive

<img src="docs/readme_images/am i responsive page.PNG">

## Live website


## Purpose of the project

DanceZone began as a blog dedicated to exploring the vibrant and diverse world of dance. Due to the overwhelming interest from professional dancers and enthusiasts, it has grown into a full-fledged platform offering dance class bookings alongside its engaging blog content. This full-stack website, built using the Django web framework, aims to transform passionate readers into active participants by providing easy access to a variety of dance classes.

The DanceZone website offers a seamless experience for users, featuring a blog that covers various dance styles, tips for beginners and seasoned dancers alike, and cultural insights into dance traditions worldwide. Registered users can also enjoy the convenience of booking dance classes directly through the website. The app allows users to schedule classes for different styles—from classical forms like Bharatanatyam and Ballet to contemporary styles like Hip Hop and Salsa. 

DanceZone’s goal is to inspire, educate, and connect dance enthusiasts while offering a streamlined platform to learn and practice with expert instructors. Whether you're here to read, learn, or dance, DanceZone is your ultimate destination for everything dance!

## Table of contents

- [User experience (UX)](#user-experience-ux)
   * [Key project goals](#key-project-goals)
   * [Target audience](#target-audience)
   * [User requirements and expectations](#user-requirements-and-expectations)

- [Epics and user stories](#epics-and-user-stories)
   * [Epics](#epics)
   * [User stories](#user-stories) 

-[Features](#features)

- [Wireframes](#wireframes)
   * [Index page wireframes](#index-page-wireframes)

- [Database schema](#database-schema)
   * [Entity relationship diagram](#entity-relationship-diagram)

- [Testing](#testing)
- [Code validation](#code-validation)
   * [CSS](#css)
   * [JavaScript](#javascript)
   * [Python](#python)
- [Manual testing](#manual-testing)

- [Deployment](#deployment)
   * [Pre deployment](#pre-deployment)
   * [Deploying with heroku](#deploying-with-heroku)

## User experience (UX)

### Key project goals

-Increase awareness of the DanceZone brand through a feel-good and accessible website that offers information about all things dance, including various styles and techniques, through blog posts.
-Build a website that encourages and guides users to book dance lessons, or sign up for events directly through the platform.

### Target audience

-Users who are interested in current dance trends, techniques, and tutorials.
-Users who would like to book dance lessons, choreography, or dance performances for an upcoming event.

### User requirements and expectations

- An intuitively structured and visually appealing website that is easy to read on all screen sizes
- Navigation that is easy to use and understand whether using mobile, tablet or monitor
- Ability to quickly understand the purpose of the website
- An ability to register, login and logout
- An ability to interact with content by commenting
- An ability to read comments that have been made under blogs
- An ability to update and delete comments if desired
- An ability to find relevant information on the business and its services
- An ability to make a booking for a dance style
- An ability to see a list of their own bookings
- An ability to update and delete bookings if desired
- Easy ways to contact the dancezone
- An accessible website for all users



### Epics

1. Fully functioning home page
2. Database and admin setup
3. Register page and form
4. Login page and form
5. Navigation bar that looks different when logged in
6. Blog detail page that has different capabilities when logged in compared to when not logged 
   in
7. Log out page
8. Booking page for various dance styles, that can be only accessed when logged in. This 
   includes full front-end CRUD functionality for the user

### User stories

Open a post: As a Site User, I can click on a post so that I can read the full text.

AC1 When a blog post title is clicked on a detailed view of the post is seen.

View comments: As a Site User / Admin I can view comments on an individual post so that I can read the conversation

AC1 Given one or more user comments the admin can view them.
AC2 Then a site user can click on the comment thread to read the conversation.

Account registration: As a Site User I can register an account so that I can comment on a post.

AC1 Given an email a user can register an account.
AC2 Then the user can log in.
AC3 When the user is logged in they can comment.

Comment on a post: As a Site User I can leave comments on a post so that I can be involved in the conversation

AC1 When a user comment is approved
AC2 Then a user can reply
AC3 Given more than one comment then there is a conversation thread

Modify or delete comment on a post: As a Site User I can modify or delete my comment on a post so that I can be involved in the conversation

AC1 Given a logged in user, they can modify their comment
AC2 Given a logged in user, they can delete their comment

Booking of dance class: As a Site user I can book a class so that I can enjoy the dance style I want from the available dance style

AC1 As a user I should be able to choose from dance list available
AC2 As a user I Could choose from the date available to join the dance
AC3 As a user i could choose from the time slots available

Edit and delete dance class: As a SITE USER I can edit booking so that I Can change my choice accordingly

AC1 As a user I Can edit my preference
AC2 As a user I Can delete my booking if made mistake
AC3 As a user I Can view my bookings

Manage posts: As a Site Admin I can create, read, update and delete posts so that I can manage my blog content

AC1 Given a logged in user, they can create a blog post
AC2 Given a logged in user, they can read a blog post
AC3 Given a logged in user, they can update a blog post
AC4 Given a logged in user, they can delete a blog post

Create drafts: As a Site Admin I can create draft posts so that I can finish writing the content later

AC1 Given a logged in user, they can save a draft blog post
AC2 Then they can finish the content at a later time

Approve comments: As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

AC1 Given a logged in user, they can approve a comment
AC2 Given a logged in user, they can disapprove a comment

Link to my Github [Project Board](https://github.com/users/SIMMI-K/projects/3/views/1)

## Wireframes

### Index page wireframes

#### Mobile

<img src="docs/readme_images/wireframe of home phone view.PNG">

#### Tablet

<img src="docs/readme_images/wireframe home tablet.PNG">

#### Monitor

<img src="docs/readme_images/browser home wireframe.PNG">

### Entity relationship diagram

In the diagram below it can be seen that User has a relationship to Post, Comment and Booking. Comment has a relationship with both User and Post.

<img src="docs/readme_images/DanceZone ERD.png">

# Testing

## Code validation

### HTML

All HTML pages were tested with the [W3C HTML Validator](https://validator.w3.org/).

#### HTML Result
| page                   | validator                                                                                                                               | result |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| blog                   |  <details><summary>Blog Page</summary><img src="docs/readme_images/html validator 1.PNG"></details>                          | PASS   |
| booking              |  <details><summary>booking Page</summary><img src="docs/readme_images/html validator booking page.PNG"></details>             | PASS   |
| post detail logged out |  <details><summary>Post Detail Logged Out</summary><img src="docs/readme_images/post logout validation.PNG"></details> | PASS   |
| post detail logged in  |  <details><summary>Post Detail Logged In</summary><img src="docs/readme_images/post detail login validation.PNG"></details>   | PASS   |
| sign up page           |  <details><summary>Register</summary><img src="docs/readme_images/sign up validation.PNG"></details>                         | PASS   |
| sign in page           |  <details><summary>Sign In</summary><img src="docs/readme_images/post detail login validation.PNG"></details>                           | PASS   |
| logout page            |  <details><summary>Sign Out</summary><img src="docs/readme_images/post logout validation.PNG"></details>                         | PASS   |
| edit booking page      |  <details><summary>Edit Booking</summary><img src="docs/readme_images/edit booking validation.PNG"></details>                   | PASS   |
| delete booking page    |  <details><summary>Delete Booking</summary><img src="docs/readme_images/delete booking validation.PNG"></details>        | PASS   |
| delete comment page    |  <details><summary>Delete Comment</summary><img src="docs/readme_images/delete comment validation.PNG"></details>        | PASS   |

The info messages that were ignored appeared in validation, because I used the [Prettier](https://prettier.io/) plugin in VS code. Prettier is hardcoded to add trailing slashes. Since all of my attributes were quoted, there is no effect of the trailing slash. After some research and finding the following 2 links I decided that it is ok to ignore these info messages in this instance.

- [Stack overflow](https://stackoverflow.com/questions/77343449/using-of-trailing-slash-in-void-element) - information on trailing slash

### CSS

Custom CSS was put through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

#### CSS Result

Pass
<img src="docs/readme_images/css validation.PNG">

Explanation of 3 warnings
<img src="docs/readme_images/css validation2.PNG">

Warning 1: Imported style sheets are not checked in direct input and file upload modes. This warning can be ignored in this instance.

- [Stack overflow](https://stackoverflow.com/questions/25946111/importing-css-is-ending-up-with-an-error) - the google style sheet is not checked in the validator

Warning 2: -webkit-transform is a vendor extension. This warning can be ignored in this instance.

- [Stack overflow](https://stackoverflow.com/questions/30607832/w3c-css-validation-error-using-calc-and-vendor-extensions) - vendor-specific extensions (mostly) do adhere to the CSS 2.1 grammar, but since they are not defined in the CSS 2.1 specification, they are marked as invalid in the validator.

Warning 3: -moz-transform is a vendor extension. This warning can be ignored in this instance.

- [Stack overflow](https://stackoverflow.com/questions/30607832/w3c-css-validation-error-using-calc-and-vendor-extensions) - vendor-specific extensions (mostly) do adhere to the CSS 2.1 grammar, but since they are not defined in the CSS 2.1 specification, they are marked as invalid in the validator.

### JavaScript

JavaScript code in the comment.js file was put through the [JSHint Validator](https://jshint.com/).

#### JS Result

The js code passed. There is 1 undefined variable: bootstrap. However, this warning can be ignored in this instance because the variable is imported with the CDN connection in the base.html file.

<img src="docs/readme_images/js validation.PNG">

### Python

All python code was put through the [CI Python Linter](https://pep8ci.herokuapp.com/).

#### Python Result

| File            | Validator                                                                                                                | Result |
| --------------- | ------------------------------------------------------------------------------------------------------------------------ | ------ |
| Blog models     |  <details><summary>Blog Models</summary><img src="docs/readme_images/blog model.py validation.PNG"></details>        | PASS   |
| Blog views      |  <details><summary>Blog Views</summary><img src="docs/readme_images/blog views.py.PNG"></details>          | PASS   |
| Blog forms      |  <details><summary>Blog Forms</summary><img src="docs/readme_images/blog forms.py.PNG"></details>          | PASS   |
| Blog urls       |  <details><summary>Blog urls</summary><img src="docs/readme_images/blog urls.py.PNG"></details>            | PASS   |
| Blog admin      |  <details><summary>Blog Admin</summary><img src="docs/readme_images/blog admin.py.PNG"></details>          | PASS   |
## Manual testing

<img src="docs/readme_images/dancezone testing US - Sheet1.pdf">

## Deployment

All code for this project was written in visual studio integrated development environment. Github was used for version control and the application was deployed to heroku from github.

### Pre deployment

- To ensure successful deployment with heroku, it's good practice to make sure that the requirements.txt file is kept up to date so as that imported python modules are configured correctly.
- A Procfile is required to allow heroku deployment to be configured to a gunicorn web app.
- In settings.py configure the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost'], make sure all static files and directories are configured correctly.
- All environment variables on the env.py which gitignored on the repo must be configured correctly with the database url, cloundinary url and secret key.

### Deploying with heroku

After account setup, the steps were as follows:

- Click the "create new app" button on heroku
- Create a unique name for the app
- Select region (Europe was selected for this project)
- Click "create app"
- Select the deployment method (github was used for this project)
- Search for the github repository name (it was 1st-full-stack-project for this project)
- Click connect
- There is an option to use manual deployment or automatic deployment. Make sure main branch is selected
- In the settings tab select reveal config vars. Input the required hidden variables
- Select nodejs and python as the buildpack
- Deploy
- After the first deployment you will see a message saying "your app was successfully deployed" and there will be a "view" button to take you to your deployed application

The live link for this project can be found here - [DanceZone]()

### Fork this repository:

- Go to the GitHub repository
- Click on the Fork button in the upper right-hand corner

### Clone this repository:

- Go to the GitHub repository
- Click the Code button near the top of the page
- Select 'HTTPS', 'SSH', or 'Github CLI', depending on how you would like to clone
- Click the copy button to copy the URL to your clipboard
- Open Git Bash
- Change the current working directory to where you want the cloned directory
- Type git clone and paste the URL ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
- Press enter to create your clone locally

Note: The difference between clone and fork is, you need permissions to push back to the original from a clone, but not a fork because a fork will be completely your own new project.

## Credits

### Code

[CI walkthrough I think therefore I blog](https://github.com/Code-Institute-Solutions/blog/tree/main/12_views_part_3/05_edit_delete) - The CI walkthrough repo was relied upon heavily, however I additionally created 1 whole custom app with associated custom models to suit the dance theme of the website. The app I added was a booking for dance classes where the user could make a booking for dance styles they like if they were logged in. This custom app has full front end CRUD functionality.

[CI previous project on statement beauty blog] -The inspiration came from this beauty blog to make something customise to my favourite dances from around the world and some classical dances from India.

[CHATGPT for many fixes, errors, codes, post descriptions]

## Acknowledgements

Thank you to friends, family specially my 4yr son for showing a big cooperation during meetings.
Also thank you to my mentor and CI cohort facilitator specially ELAINE, MARK and JOHN