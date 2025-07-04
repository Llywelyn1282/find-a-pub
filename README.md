# findapub

findapub was created as my third milestone project for the Code Institutes Level 5 Diploma in Web Application Development.

Link to deployed site on Heroku: (https://find-a-pub-project-35ccdd2a93a3.herokuapp.com/)

![Welcome to findapub](static/images/mockup.png)

---

## CONTENTS

- [User Experience](#user-experience)

  - [Project Goals](#project-goals)
  - [Target Audience](#target-audience)
  - [User Stories](#user-story-1)

- [Design](#design)

  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)

- [Features](#features)

  - [Elements Found on Each Page](#elements-found-on-each-page)
  - [Future Implementations](#future-implementations)

- [Technologies Used](#technologies-used)

  - [Languages Used](#languages-used)
  - [Databases Used](#databases-used)
  - [Frameworks Used](#frameworks-used)
  - [Libraries & Packages Used](#libraries--packages-used)
  - [Programs Used](#programs-used)

- [Testing](#testing)

- [Deployment & Local Development](#deployment--local-development)
  - [Deployment](#deployment)
  - [Local Development](#local-development)
    - [How to Clone](#how-to-clone)
- [Credits](#credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)

---

## User Experience

### Project Goals

My project goals are to create a **site where users can locate a pub they wish to visit in the town of Brecon, and find any important information related to that pub**.

### Target Audience

The target audience of the project are **people who like visiting pubs, but either have specific needs, or like to do research about where to go beforehand**.

### User Story 1

As a **new user** I can **create an account easily** so that **I can customise my website experience and be able to leave comments etc.**

#### Acceptance Criteria:

- Acceptance Criteria 1: With an email a user can register for an account.
- Acceptance Criteria 2: The user can sign in and out easily.
- Acceptance Criteria 3: The user can leave comments.

#### Tasks:

- Task 1: Design and implement a registration form with username, email and password.
- Task 2: Create login and logout functionality.
- Task 3: Allow signed in users to be able to leave comments.

### User Story 2

As an **admin** I can **create pub entries** so that **information can be displayed for users to consume**.

#### Acceptance Criteria:

- Acceptance Criteria 1: The admin can create a pub entry.
- Acceptance Criteria 2: The site displays these entries clearly and presentably.

#### Tasks:

- Task 1: Build an interface to add important information regarding each pub.
- Task 2: Save entries to a database.
- Task 3: Make sure entries are displayed clearly on the site.

### User Story 3

As an **admin** I can **manage pub entries** so that **data can be edited and added to with ease**.

#### Acceptance Criteria:

- Acceptance Criteria 1: An admin can easily create entries.
- Acceptance Criteria 2: An admin can easily view entries.
- Acceptance Criteria 3: An admin can easily edit entries.
- Acceptance Criteria 4: An admin can easily delete entries.

#### Tasks:

- Task 1: Create an admin interface listing all pub entries.
- Task 2: Ensure the interface includes edit and delete functionality for the entries.

### User Story 4

As a **user** I can **view a list of pub entries easily** so that **I can see which pub best suits my needs**.

#### Acceptance Criteria:

- Acceptance Criteria 1: A paginated list of pubs is show on the site homepage.
- Acceptance Criteria 2: The pub entries are written clearly and concisely.
- Acceptance Criteria 3: The pub entries are presented in an aesthetically pleasing manner.

#### Tasks:

- Task 1: Design a homepage layout with pagination of entry thumbnails.
- Task 2: The user is able to click each thumbnail to reveal the full entry.

### User Story 5

As a **user** I can **filter the list of pub entries by set criteria** so that **I can easily manipulate the information to see what best suits my needs**.

#### Acceptance Criteria:

- Acceptance Criteria 1: Users can filter pubs by set criteria.
- Acceptance Criteria 2: Users can combine multiple filters at once.

#### Tasks:

- Task 1: Add filter elements to the UI.
- Task 2: Implement query logic to filter pub entries.
- Task 3: Update list as filters are applied.

### User Story 6

As an **admin** I can **create draft entries** so that **I can finish them at a later date**.

#### Acceptance Criteria:

- Acceptance Criteria 1: An entry can be saved as a draft instead of published immediately.
- Acceptance Criteria 2: The draft can be accessed at a later date to continue creation.

#### Tasks:

- Task 1: Add a 'Save as Draft' option to the pub entry interface.
- Task 2: Mark these entries as drafts when displayed on the admin page.
- Task 3: Allow for continued editing of these entries and the option to then publish them.

### User Story 7

As a **user** I can **easily leave and view comments/reviews** so that **I can view the opinions of others while making a choice of which pub to visit**.

#### Acceptance Criteria:

- Acceptance Criteria 1: Users can submit a comment or review on a pub’s detail page.
- Acceptance Criteria 2: Submitted comments displayed under the pub entry.
- Acceptance Criteria 3: Comments for a pub are shown in chronological order (newest first), showing the timestamp and commenter name.

#### Tasks:

- Task 1: Implement a comment form for each entry page.
- Task 2: Comments are displayed under each entry.
- Task 3: Comments are displayed in chronological order.

### User Story 8

As an **admin** I can **delete or hide comments/reviews** so that **I can retain a positive, clean and productive discourse on the site**.

#### Acceptance Criteria:

- Acceptance Criteria 1: The admin can delete/hide comments.

#### Tasks:

- Task 1: Allow admin to be able to access and delete comments.

### User Story 9

As a **user** I can **edit or delete comments/reviews** so that **I can change typos etc. or delete the comment alltogether if I change my mind**.

#### Acceptance Criteria:

- Acceptance Criteria 1: The logged in user can edit their comments.
- Acceptance Criteria 2: The logged in user can delete their comments.

#### Tasks:

- Task 1: Add and edit and delete button to users comments.

### User Story 10

As a **user** I can **visit an About and Contact page with a form** so that **I can learn about the site's goals and contact the creators in regard to any neccesary queries**.

#### Acceptance Criteria:

- Acceptance Criteria 1: There is an about page with information about the site and what it offers.
- Acceptance Criteria 2: The page also features a contact section with a form.
- Acceptance Criteria 3: The user is able to easily find this within the UI and it looks aesthetically pleasing.

#### Tasks:

- Task 1: Create an informative about page.
- Task 2: Implement a contact form that submits to an email service.

---

## Design

### Colour Scheme

![Colour Scheme for findapub](static/images/color-scheme.png)

### Typography

I used Google Fonts to import the following fonts for use in the site:

##### Logo & Headings

[**Inter**](https://fonts.google.com/specimen/Inter)

![Sample](static/images/inter.png)

##### Paragraphs

[**Inter**](https://fonts.google.com/specimen/Inter)

![Sample](static/images/inter.png)

##### Icons

Icons were used from [Font Awesome](https://fontawesome.com/icons)

### Imagery

Favicon generated using [favicon.io](https://favicon.io/)

![Favicon](static/images/favicon.png)

### Wireframes

Wireframes were created for mobile and desktop using Balsamiq.

Home Page

![Home Page](static/images/wf-home.png)

Pub Detail Page

![Pub Detail Page](static/images/wf-pub-detail.png)

About Page

![About Page](static/images/wf-about.png)

Contact Page

![Contact Page](static/images/wf-contact.png)

Sign In Page

![Sign In Page](static/images/wf-signin.png)

### Database Layout

![Database Layout](static/images/database-layout.png)

---

## Features

The website is comprised of **8** pages:

- Home Page
- Pub Detail Page
- About Page
- Contact Page
- Register Page
- Sign In Page
- Sign Out Page
- 404 Page

### Site Wide

**Navbar**

- Navbar styled to have right sided margin and burger icon on smaller devices. Contains links to **Home Page**, **About Page**, **Contact Page**, **Register Page** and **Sign In Page** if you aren't signed in, and **Sign Out Page** if you are signed in.

  ![Navbar](static/images/header.png)

**Footer**

- Footer containing social media links is displayed on all pages of the website.

  ![Footer](static/images/footer.png)

### Home Page

- The home page is an index of all of the available pubs on the site with a title, location and a small excerpt of each one. 

![Home Page](static/images/home-page.png)

### About Page

- The about page displays a small bit of information about the site.

![About Page](static/images/about-page.png)

### Contact Page

- The Contact Page contains a form with name, email and message fields.

![Contact Page](static/images/contact-page.png)

### Sign Up Page

![Sign Up Page](static/images/signup-page.png)

### Sign In Page

![Contact Page](static/images/signin-page.png)

### Sign Out Page

![Contact Page](static/images/signout-page.png)

### 404 Error Page

- A 404 page is in place to display if a user navigates to a broken link. The page has a link that allows users to navigate back to the homepage.

![404 Error Page](static/images/404.png)

### Future Implementations

In future implementations I would like to:

- Add a favourites button and page for users to save their favourite pubs.
- Add a dropdown menu for filters on mobile sized screens.
- Add the ability for users to be able to submit their own pubs for review to be added to the site.
- Add more images to Pub Detail Pages.

---

## Technologies Used

### Languages Used

HTML, CSS, JavaScript, Python

### Databases Used

[PostgreSQL](https://www.postgresql.org/)

### Frameworks Used

[Django](https://www.djangoproject.com/)

### Programs Used

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[Github](https://github.com/) - To save and store the files for the website.

[Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

[Favicon.io](https://favicon.io/favicon-converter/) - To create the favicon files.

[Font Awesome](https://fontawesome.com/) - For the icons on the website.

[Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.

[Am I Responsive?](http://ami.responsivedesign.is/) - To show the website image on a range of devices.

---

## Testing

Testing is listed in a separate file which can be found here: [TESTING.md](TESTING.md)

---

## Deployment & Local Development

The following git commands were used throughout development to push code to the remote repo:

`git add <file>` - This command was used to add the file(s) to the staging area before they are committed.

`git commit -m “commit message”` - This command was used to commit changes to the local repository queue ready for the final step.

`git push` - This command was used to push all committed code to the remote repository on github.

### Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

### Heroku Deployment

The Wallet Tracker app was deployed using **Heroku** with **PostgreSQL** and necessary environment variables.

#### Deployment Steps

1. **Create a new Heroku app**

   - Go to [http://heroku.com](https://heroku.com)
   - Log in and click **New > Create new app**
   - Choose a unique app name and select the region

2. **Add PostgreSQL**

   - In the **Resources** tab, search for **Heroku Postgres**
   - Select the **Hobby Dev** plan and click **Add**

3. **Set Config Vars**

   - Go to **Settings > Reveal Config Vars**
   - Add the following:
     - `DATABASE_URL` _(automatically added by Heroku)_
     - `SECRET_KEY` _(your Django secret key)_
     - `DEBUG` = `False`
     - Any other environment variables required

4. **Create a Procfile**

   - In the root directory of your project, create a file named `Procfile` (no extension)
   - Add the following line:
     ```
     web: gunicorn findapub.wsgi
     ```

5. **Requirements and Dependencies**

   - Ensure the following are included in your `requirements.txt`:
     ```
     gunicorn
     dj-database-url
     psycopg2
     whitenoise
     ```

6. **Update `settings.py`**

   - Add PostgreSQL configuration:

     ```python
     import dj_database_url

     DATABASES = {
         'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
     }
     ```

   - Add WhiteNoise static file config:

     ```python
     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
     ```

7. **Connect GitHub Repo**

   - In the **Deploy** tab on Heroku:
     - Connect your GitHub account
     - Choose the repository
     - Select the branch (usually `main`)
     - Click **Deploy Branch**

8. **Collect Static Files**
   - Run the following from the terminal:
     ```bash
     heroku run pyhthon manage.py migrate
     heroku run python manage.py collectstatic --noinput
     ```

The live link can be found here - (https://find-a-pub-project-35ccdd2a93a3.herokuapp.com/)

#### How to Clone

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now of been cloned on your local machine for use.

---

## Credits

Many thanks to Gareth McGirr, Alice Dean and Nick Le Mesurier for their advice on this project.

### Content

Content for this project was written by Gwilym Llywelyn.

### Media

Pint glass image found on Unsplash and taken by Engin Akyurt:

https://unsplash.com/photos/a-person-holding-a-mug-of-beer-in-a-park-s4qBgZs7n7c

