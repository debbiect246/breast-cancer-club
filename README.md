# Breast Cancer Club 

![AmIResponsive Mockup Screenshot](docs/mockup.jpg "AmIResponsive Mockup Screenshot")

## Project Summary

This app was created by Team Pink Ribbon.

The theme was to create an app to utilize technology to create awareness and support around breast cancer

In line with this theme we decided to create an app to encourage meet up events between breast cancer patients, for peer to peer support, and which provide them a space to blog about their experiences and raise awareness.

## Contents
- [1. User experience design](#1-user-experience-design "1. UX design")
  - [1.1 Strategy Plane](#11-strategy-plane "1.1 Strategy Plane")
  - [1.2 Scope plane](#12-scope-plane "1.2 Scope plane")
  - [1.3 User Stories](#13-user-stories "1.3 User Stories")
  - [1.4 Structure plane](#14-structure-plane "1.4 Structure plane")
  - [1.5 Skeleton plane](#15-skeleton-plane "1.5 Skeleton plane")
  - [1.6 Surface plane](#16-surface-plane "1.6 Surface plane")
- [2. Code design](#2-code-design "2. Code design")
- [3. Features Left to Implement](#3-features-left-to-implement "3. Features Left to Implement")
- [4. Technologies and Tools Used](#4-technologies-and-tools-used "4. Technologies and Tools Used")
- [5. Issues](#5-issues "5. Solved and Known issues")
- [6. Testing](#6-testing "6. Testing")
- [7. Deployment](#7-deployment "7. Deployment")
- [8. Credits](#8-credits "8 Credits")

## 1. User Experience design
As a team we met online to discuss how we would design an app that would bring together breast cancer patients using meet up events. Aside from providing a safe space, and a potentially cheerful and social one, this meet up app would raise an important kind of awareness. Meet ups between patients at different stages in their cancer journey raise awareness about what to expect, how to adapt, good coping and recovery strategies, and good resources with the group that needs that specialist awareness most.

Key to this also was providing them a place to blog about their experiences, for users of the site, and new visitors.

## User Experience

#### User Goals

The first-time user is looking to:
- Browse meet up events with people going through the same disease, in their locality.
- Browse blog posts written about their disease by other people going through it.

The returning user is looking to:
- Create and share their own meet up events.
- Create and edit their own blog posts.

#### Site Developer Goals
The Developer is looking to:
- Create an inviting, community-drive application that acts as a support for people going through breast cancer.

### User Stories

- New Visitor

  - I want to a cheerful landing page that makes me feel positive about this community.
  - I'd like to be able to browse the site content before registration.

- Repeat users

  - I'd like a nice profile page, easy login, and a quick fix if I forget my password.
  - I want to be able to create and edit my own meet ups, and blog posts.

-  All Users

   - I'd like to get visual feedback on all my actions on this site.
   - I'd like to be able to contact the admin for any complaints/inappropriate content.

- Site Developer

  - I create a peer-to-peer support group, where people can meet up together locally, and share experiences virtually.
  - I want the ability as admin to delete/edit any content that is inappropriate.


### 1.1 Strategy Plane
Stakeholders of the website: 

- Breast cancer patients
- Breast cancer survivors
- Family, friends and allies
- Medical community

#### 1.1.1 Goals and Objectives of Stakeholders (users)
|User Type          |           Goals, Needs, Objectives                 |
|-------------------|----------------------------------------------------|
| Patients          |   Learn how disease affects day to day life        |
|                   |   Have fun, with people who get my restrictions    |
|                   |   Hear how things will get better                  |
|-------------------|----------------------------------------------------|
| Survivors         |   Help others through this journey                 |
|                   |   Blog about my story                              |
|                   |   Feel part of a process combating this disease    |
|-------------------|----------------------------------------------------|
| Allies            |   Learn about what to expect for loved ones        |
|                   |   Read blog posts to better understand experience  |
|                   |   Check meet up locations if chaperoning           |            
|-------------------|----------------------------------------------------|
| Medics            |   Be able to refer patients to a good resource     |
|                   |   Improve bedside manner by learning from patients |
|                   |   Attend some meet ups to chat with survivors      |            
|-------------------|----------------------------------------------------|

The app needs to enable all **users** to:

- Register/login to an account

- View Meet Ups with the following information:

    - Meet Up Type
    - Meet Up DateTime
    - Meet Up Location
    - Event Host
    - Attending

- Upload and edit their own meet ups

- Click attending on other peoples' meet ups

- Get in contact with site owner

The website needs to enable the **site developer** to:
- Provide a community-driven meet up app
- Edit/delete inappropriate content

With these goals in mind, a strategy table was created to determine the trade-off between importance and viability with the following results: 

### 1.2 Scope plane

- **Content Requirements**
     - The user will be looking for:
     - Cheerful, colourful landing page.
     - Easy navigation.
     - Meet Up cards with following info:
        - Meet Up Type
        - Meet Up DateTime
        - Meet Up Location
        - Event Host
        - Attending
     - Simple registration process
     - Customisable User Profile
        - Custom User Name/Password
     - Site Developer contact form

- **Functionality Requirements**
     - The user will be able to:
        - Register/Login to account
        - Customise their profile
            - Custom Username/Password
        - Navigate to the Meet Up Cards:
            - Sort the photos into either Popular or Recent
            - I'm Attending Page
        - Create Meet Up Events:
            - Meet Up Type
            - Meet Up DateTime
            - Meet Up Location
        - Interact with other users
            - Click attending on other users' events
        - Get in contact with the Developer

- **Further Considerations**
    - Responsive design is essential so that the app works on desktop and mobile devices.
    - User should be able to navigate with ease to each part of the app.
    - The logo should take the user back to the home page when clicked on.  There should not be any need for the user to press the back button in order to get to any page of the app.
    - Information on the onboarding page and the home page should give the user useful information about onboarding and the app itself.
    - Colour schemes on the site should be designed so as to encourage inclusive access to the site for people with visual and neurological disabilites as well as for non disabled people.

### 1.4 Structure plane
The information architecture was organized in order to ensure that users could navigate through the site with ease and efficiency, with the following results: 

**Information Architecture for Bird Friend:**
![Information Architecture for Bird Friend Web App](docs/bcc-sitemap.png "Breast Cancer Club Information Architecture") 

### 1.5 Skeleton plane
Wireframe mockups were created in a [Figma Workspace](https://www.figma.com/file/zRQC6meZBDCes1yt7ToGTM/Breast-Cancer-Club?node-id=59%3A0 "Breast Cancer Club Figma Workspace").

- Landing Page:

     ![Mobile Landing Page](docs/mobile-landing-page.png "Mobile Landing Page")

- Meet Up Cards Page:

     ![Mobile Cards Page](docs/mobile-cards-page.png "Mobile Cards Page")

- User Profile Page:

     ![User Profile Page](docs/mobile-cards-page.png "User Profile Page")


### 1.6 Surface plane

- <strong>Colour Scheme</strong>

     - The soft, pastel colour scheme was picked to offset the vibrant pink associated with breast cancer support services.


- ![#D258A3](https://via.placeholder.com/15/D258A3/000000?text=+) #D258A3 (Bandana Pink)
- ![#F7FFF7](https://via.placeholder.com/15/F7FFF7/000000?text=+) #F7FFF7 (Washed Green)
- ![#4ECDC4](https://via.placeholder.com/15/4ECDC4/000000?text=+) #4ECDC4 (Hospital Gown Green)
- ![#FFE66D](https://via.placeholder.com/15/FFE66D/000000?text=+) #FFE66D (Bright Button Yellow)


- <strong>Typography</strong>

     - The primary font chosen and used on the photo gallery, and bird / user profiles is [Lato](https://fonts.google.com/specimen/Lato "Link to Lato Google Fonts page"). Lato means summer in Polish, and the font reflects its namesake with warmth in its rounded design.

     - The Secondary fonts are [Dela Gothic ONe](https://fonts.google.com/specimen/Dela+Gothic+One "Link to Dela Gothic One Google Fonts page") and [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab "Link to Roboto Slab Google Fonts page"). 
     
     - Dela Gothic One is used on the site landing page, and for site headings. It pairs really well with Lato, because it is similarly rounded and warm.
    
    - Roboto Slab is used on site links, and for site buttons. Its bolded, thick look is perfect for call-to-action elements like links and buttons, but its curves match it well with Lato and Dela Gothic One.

- <strong>Imagery</strong>

     - The imagery used was purchased from a designer linked to the Mater Foundation, where one of our team works, and from a Canva Pro Account.

## 2. Code design
* utilizing the [Flask](https://flask.palletsprojects.com/) framework for handling REST API calls
  - The `run.py` file contains code related to Flask only, no database or form reference can appear in there.
  - The `db.py` file is a module and contains code related to the database.
* generating web pages from HTML templates with [Jinja](https://jinja.palletsprojects.com/) 
  - the `base.html` file contains the base HTML structure of all web pages generated in the app
  - the `index.html` extends the `base.html` into the Home page
  - the `events.html` file contains details of breast cancer events
  - the `blog.html` file contains blog details.
 
## 3. Features Left to Implement
As the hackathon had a time limit we did not have time to implement the following functionality but in future we could review the app and add the following:
- 
- 


## 4. Technologies and Tools Used
[Flask](https://flask.palletsprojects.com/en/2.0.x/) is a microframework used to build apps.
[Jinja](https://jinja.palletsprojects.com/) is a templating language within flask.
[python](https://www.python.org/)is a programming language widely used on the internet with web frameworks to create apps.
[html](https://devdocs.io/html/)stands for HyperText MarkUp Language and is used to put content and structure on a web page.
[CSS](https://devdocs.io/css/) stands for cascading style sheets and is used to style a webpage.


## 5. Issues
### Issues solved during development
- As a team we had some issues with working with github collaboratively.  These issues were resolved through user team members experience and [github docs](https://docs.github.com/en).
- Issues with pages displaying were resolved using team review and some pair programming when needed.
- Issues with logic and the backend appeared when trying to connect up the json file holding interview questions, interviewer and interviewee details with the questions page.  These were resolved during team discussions and some pair coding.

### Known issues

## 6. Testing
Testing was done by all members of the team.  Automated testing was not done but this is a future area for development.

## 7. Deployment
 
### Deployment in development environment

#### 7.1 Python and Git
Make sure, that [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads) are installed on your computer

#### 7.2 Clone the project's GitHub repository

1. Locate the repository here https://github.com/debbiect246/breast-cancer-club
2. Click the 'Code' dropdown above the file list
3. Copy the URL for the repository (https://github.com/debbiect246/breast-cancer-club.git)
4. Open a terminal on your computer
5. Change the current working directory to the one where the cloned folder will be located
6. Clone the repo onto your machine with the following terminal command
```
git clone https://github.com/debbiect246/breast-cancer-club.git
```

#### 7.3 Create local files for environment variables
Change working directory to the cloned folder and start your code editor
```
cd breast-cancer-club
code .
```
Create file `envWS.py` with the following content into the root of the project folder
```
import os
os.environ.setdefault("FLASK_SECRET_KEY", "<secret key>")
os.environ.setdefault("FLASK_IP",         "127.0.0.1")
os.environ.setdefault("PORT",             "5500")
os.environ.setdefault("FLASK_DEBUG",      "True") 
os.environ.setdefault(“MONGO_URI”, “mongodb+srv://Team09:setterret12@team09.3qais.mongodb.net/BreastCancerClub?retryWrites=true&w=majority”)
os.environ.setdefault(“MONGO_DBNAME”, “BreastCancerClub”)
```
The `<secret key>` can be any random character string from your keyboard.
 
#### 7.4 Set up the Python environment
In your development environment, upgrade `pip` if needed
```
pip install --upgrade pip
```
Install `virtualenv`:
```
pip install virtualenv
```
Open a terminal in the project root directory and run:
```
virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
#### 7.5 Start the web server:
```
python run.py
```

### Deployment on Heroku
[Heroku](https://www.heroku.com/) is a PaaS cloud service, you can deploy this project for free on it.

#### 7.6 Prerequisites:
- you forked or copied this project into your repository on GitHub.
- Heroku requires these files to deploy successfully, they are both in the root folder of the project:
- `requirements.txt`
- `Procfile`
- you already have a Heroku account, or you need to register one.

#### 7.7 Create a Heroku App
Follow these steps to deploy the app from GitHub to Heroku:
- In Heroku, Create New App, give it a platform-unique name, choose region, click on `Create App` button
- On the app/Deployment page select GitHub as Deployment method, underneath click on `Connect GitHub` button
- In the GitHub authorization popup window login into GitHub with your GitHub username and click on `Authorize Heroku` button
- Type in your repo name and click `search`. It lists your repos. Choose the one and click on `connect` next to it.
- either enable automatic deployment on every push to the chosen branch or stick to manual deployment
- go to app/Settings page, click on `Reveal Config Vars` and enter the following variables and their values from the `envWS.py` file:
  * FLASK_SECRET_KEY

## 8. Credits
- ### Team & Hosts
- A huge thank you to all of our team members! Christopher, Deborah, Tindy, Valerie and David put a lot of hours into building this project over 4 days.
- Thanks so much to Code Institute and IT Labs Hacakthon for hosting this Breast Cancer Awareness Hackathon by Women in Tech.

### Content
- All images used in our project were purchased on Canva Pro using a Canva Pro license that enables them to be reused in commercial and educational projects. This license is held by one of our team - David

