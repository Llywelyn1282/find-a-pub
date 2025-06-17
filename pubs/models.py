from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
YESORNO = (("No", "No"), ("Yes", "Yes"))
PRICE = (("£", "£"), ("££", "££"), ("£££", "£££"),
         ("££££", "££££"), ("£££££", "£££££"))


DAYS_OF_WEEK = [
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday'),
    ]


class Pub(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default="placeholder")
    location = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=500, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    website = models.CharField(max_length=254, blank=True)
    email = models.CharField(max_length=254, blank=True)
    mon_opening = models.CharField(max_length=254, default="Closed")
    tues_opening = models.CharField(max_length=254, default="Closed")
    wed_opening = models.CharField(max_length=254, default="Closed")
    thurs_opening = models.CharField(max_length=254, default="Closed")
    fri_opening = models.CharField(max_length=254, default="Closed")
    sat_opening = models.CharField(max_length=254, default="Closed")
    sun_opening = models.CharField(max_length=254, default="Closed")
    price = models.CharField(choices=PRICE, default="£")
    food = models.CharField(choices=YESORNO, default="No")
    craft_beer = models.CharField(choices=YESORNO, default="No")
    beer_garden = models.CharField(choices=YESORNO, default="No")
    dog_friendly = models.CharField(choices=YESORNO, default="No")
    pool_table = models.CharField(choices=YESORNO, default="No")
    dart_board = models.CharField(choices=YESORNO, default="No")
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    author = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name="pub_listing")
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    pub = models.ForeignKey(
        Pub, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.body} by {self.author}"
