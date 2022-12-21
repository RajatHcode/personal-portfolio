from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

# Model for Blog Category
class Category(models.Model):
    category_name = models.CharField(_("Post Category"), max_length=20)

    def __str__(self):
        return self.category_name


# Model for Blog Post
class Post(models.Model):
    post_title = models.CharField(_("Post Title"), max_length=255)
    post_body = models.TextField(_("Post Body"))
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    categories = models.ManyToManyField(
        Category, verbose_name="Category", related_name='posts')

    def __str__(self):
        return self.post_title


# Model for adding comment to a post (user can add multiple comments to a post)
class Comment(models.Model):
    comment_author = models.CharField(_("Comment Author"), max_length=60)
    comment_body = models.TextField(_("Comment Body"))
    created_on = models.DateTimeField(_("Created On"), auto_now_add=True)
    post = models.ForeignKey(Post, verbose_name="Post",
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_author
