## Testing

### Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in [WCAG 2.1 Reflow criteria for responsive design](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html) on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

1. Open browser and navigate to [findapub](https://find-a-pub-project-35ccdd2a93a3.herokuapp.com)
2. Open the developer tools (right click and inspect)
3. Set to responsive and decrease width to 320px
4. Set the zoom to 50%
5. Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched.
No horizontal scroll is present.
No elements overlap.

Actual:

Website behaved as expected.

Website was also opened on the following devices and no responsive issues were seen:

- Samsung A15
- iPad Pro
- Lenovo Ideapad S540

### Accessibility

Wave Accessibility tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs
- Color contrasts meet a minimum ratio as specified in WCAG 2.1 Contrast Guidelines
- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
- All not textual content had alternative text or titles so descriptions are read out to screen readers
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- WCAG 2.1 Coding best practices being followed
- Manual tests were also performed to ensure the website was accessible as possible and an accessibility issue was identified.

### Lighthouse Testing

#### __Home Page__

![Home](static/images/home-lighthouse.png)

#### __Pub Detail Page__

![Pub Detail](static/images/pub-detail-lighthouse.png)

#### __About Page__

![About](static/images/about-lighthouse.png)

#### __Contact Page__

![Contact](static/images/contact-lighthouse.png)

#### __Sign Up Page__

![Sign Up](static/images/signup-lighthouse.png)

#### __Sign Up Page__

![Sign In](static/images/signin-lighthouse.png)

#### __Sign Up Page__

![Sign Out](static/images/signout-lighthouse.png)



### Testing User Stories

| Goals                 | How are they achieved? |
| --------------------- | ---------------------- | 
| As a **new user** I can **create an account easily** so that **I can customise my website experience and be able to leave comments etc.** | With an email a user can register for an account, the user can sign in and out easily and the user can leave comments. |
| As an **admin** I can **create pub entries** so that **information can be displayed for users to consume**. | The admin can create a pub entry and the site displays these entries clearly and presentably. |
| As an **admin** I can **manage pub entries** so that **data can be edited and added to with ease**. | An admin can easily create, view, edit and delete entries. |
| As a **user** I can **view a list of pub entries easily** so that **I can see which pub best suits my needs** | A paginated list of pubs is show on the site homepage. |
| As a **user** I can **filter the list of pub entries by set criteria** so that **I can easily manipulate the information to see what best suits my needs**. | Users can filter pubs by set criteria and can use multiple filters at once. |
| As an **admin** I can **create draft entries** so that **I can finish them at a later date**. | An entry can be saved as a draft instead of published immediately, and can be accessed at a later date to continue creation. |
| As a **user** I can **easily leave and view comments/reviews** so that **I can view the opinions of others while making a choice of which pub to visit**. | Users can submit a comment or review on a pub’s detail page, submitted comments displayed under the pub entry, comments for a pub are shown in chronological order (newest first), showing the timestamp and commenter name. |
| As an **admin** I can **delete or hide comments/reviews** so that **I can retain a positive, clean and productive discourse on the site**. | The admin can delete/hide comments.
| As a **user** I can **edit or delete comments/reviews** so that **I can change typos etc. or delete the comment alltogether if I change my mind**. | The logged in user can edit and delete their comments. |
| As a **user** I can **visit an About and Contact page with a form** so that **I can learn about the site's goals and contact the creators in regard to any neccesary queries**. | There is an about page with information about the site and what it offers, the page also features a contact section with a form. |



### Functional Testing

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|------------------|-------------------|--------|-----------|
| `Navbar` | | | | |
| Home Page Nav Link | Home Page Loads | Clicked on Link | Taken to Page | Pass |
| About Page Nav Link | About Page Loads | Clicked on Link | Taken to Page | Pass |
| Contact Page Nav Link | Contact Page Loads | Clicked on Link | Taken to Page | Pass |
| Sign Up Page Nav Link | Sign Up Page Loads | Clicked on Link | Taken to Page | Pass |
| Sign In Page Nav Link | Sign In Page Loads | Clicked on Link | Taken to Page | Pass |
| Sign Out Page Nav Link | Sign Out Page Loads | Clicked on Link | Taken to Page | Pass |
| `Footer` | | | | |
| Facebook Link | Opens Facebook in New Tab | Clicked on Link | Opens Facebook in New Tab | Pass |
| YouTube Link | Opens YouTube in New Tab | Clicked on Link | Opens YouTube in New Tab | Pass |
| Instagram Link | Opens Instagram in New Tab | Clicked on Link | Opens Instagram in New Tab | Pass |
| `Home Page` | | | | |
| Filters | Filters Data | Clicked on Button | Filters Data | Pass |
| Pub Detail Link | Opens Pub Detail Page | Clicked on Button | Opens Pub Detail Page | Pass |
| `Pub Detail Page` | | | | |
| Comment Add | Comment is added and gives Success Message | Clicked on Button | Comment is added and gives Success Message | Pass |
| Comment Edit | Comment is edited and gives Success Message | Clicked on Button | Comment is edited and gives Success Message | Pass |
| Comment Delete | Comment is deleted and gives Success Message | Clicked on Button | Comment is deleted and gives Success Message | Pass |
| `Contact Page` | | | | |
| Send Button | Sends Form To Backend Admin Section and Gives Success Message | Clicked on Button | Sends Form To Backend Admin Section and Gives Succes Message | Pass |
| `404 Page` | | | | |
| Back to Homepage Link | Takes User Back to Home Page | Clicked on Link | Takes User Back to Home Page | Pass |



### Validator Testing 

HTML
  - No errors were returned when passing through the official [W3C Validator](https://validator.w3.org)

  ![Home HTML Validator Results](static/images//home-validation.png)

  ![About HTML Validator Results](static/images/about-validation.png)

  ![Contact HTML Validator Results](static/images/contact-validation.png)

CSS
  - No errors were found when passing through the official [Jigsaw Validator](https://jigsaw.w3.org)
  
  ![CSS Validator Results](static/images/css-validation.png)

JavaScript
 - No errors were found when passing through the official [JSHint Validator](https://www.jshint.com/)
  
  ![JavaScript Validator Results ](static/images/filters-validation.png)

  ![JavaScript Validator Results ](static/images/comments-validation.png)

Python
- No errors were found when passing through the Code Institute Python Linter [Python Validator](https://pep8ci.herokuapp.com/)



### Fixed Bugs

| Bug | Solution |
|------|-----------|
| .phone_number was not appearing in database and throwing errors | After many attempts the fix was deleting the migrations, caches and database data and starting again |
| Persisting overflow issue on certain pages | After many attempts at locating and fixing the cause, the issue was found to be simply that certain rows were not contained within containers, thus breaking the bootstrap structure and causing overflow. |
| Favicon not showing on all pages apart from home page | Changed href to href="{% static 'images/apple-touch-icon.png' %}" etc. |
| Had trouble targeting active page in navbar | First issue: Changed to {% if request.resolver_match.url_name == 'home' %} instead of {% if request.path == home_url %}
Second issue: Changed name to the correct "Pubs" instead of "home" |
| Unable to target socials using CSS | Was using "a .socials {}" instead of ".socials a {}" |


### Unfixed Bugs

* No known bugs.