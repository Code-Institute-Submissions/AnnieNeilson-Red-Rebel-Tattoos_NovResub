from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Model for Posts made in the admin site
class Post(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="artwork_post")
    caption = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    preview_image = CloudinaryField('preview_image', default='placeholder')
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.caption

    # Displays number of likes on a post
    def number_of_likes(self):  # noqa
        return self.likes.count()  


# Model for Comments, displayed underneath post.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    # Display the comment and username of commenter
    def __str__(self):
        return f"Comment {self.body} by {self.name}"
 