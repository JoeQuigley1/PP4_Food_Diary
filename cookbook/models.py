from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
DIFFICULTY = ((1, "Easy"), (2, "Moderate"), (3, "Difficult"))


class Recipe(models.Model):
    """Model for Recipe"""
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    method = models.TextField()
    difficulty = models.IntegerField(choices=DIFFICULTY)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """Comment Model"""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Submission(models.Model):

    submission_title = models.CharField(
        max_length=50, unique=True, null=False, blank=False
    )
    submission_slug = models.SlugField(max_length=50, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_submissions')
    method = models.TextField(blank=False,)
    ingredients = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder', blank=True)
    submission_status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        """Orders the submissions by most recent"""
        ordering = ['-created_on']

    def __str__(self):
        return self.submission_title

