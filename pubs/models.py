from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
YESORNO = ((0, "No"), (1, "Yes"))
PRICE = ((0, "£"), (1, "££"), (2, "£££"), (3, "££££"), (4, "£££££"))
WEEKDAYS = ((0, "Monday"), (1, "Tuesday"), (2, "Wednesday"), (3, "Thursday"), 
                    (4, "Friday"), (5, "Saturday"), (6, "Sunday"))
HOUR_OF_DAY_24 = [(i,i) for i in range(1,25)]


class Pub(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    address = models.CharField(max_length=500, unique=True)
    price = models.IntegerField(choices=PRICE, default=0)
    food = models.IntegerField(choices=YESORNO, default=0)
    craft_Beer = models.IntegerField(choices=YESORNO, default=0)
    beer_Garden = models.IntegerField(choices=YESORNO, default=0)
    dog_Friendly = models.IntegerField(choices=YESORNO, default=0)
    pool_Table = models.IntegerField(choices=YESORNO, default=0)
    dart_Board = models.IntegerField(choices=YESORNO, default=0)
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    author = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name="pub_listing")
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Comment(models.Model):
    post = models.ForeignKey(
        Pub, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
