from django.db import models

# Create your models here.
class userTable(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.username)

class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return '{}'.format(self.name)

class Post(models.Model):
    title = models.CharField(max_length=255)
    post_img=models.ImageField(upload_to='images/',default='path/to/default/image.jpg')
    body = models.TextField()
    author=models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    def __str__(self):
        return '{}'.format(self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)