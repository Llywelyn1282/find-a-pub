.phone_number was not appearing in database and throwing errors

after many attempts the fix was deleting the migrations, caches and database data and starting again.


persisting overflow issue on certain pages

after many attempts at locating and fixing the cause, the issue was found to be simply that certain rows were not contained within containers, thus breaking the bootstrap structure and causing overflow.

Favicon not showing on all pages apart from home page

changed href to href="{% static 'images/apple-touch-icon.png' %}" etc.

Had trouble targeting active page in navbar.

First issue: Changed to {% if request.resolver_match.url_name == 'home' %} instead of {% if request.path == home_url %}
Second issue: Changed name to the correct "Pubs" instead of "home".

Unable to target socials using css

was using "a .socials {}" instead of ".socials a {}"