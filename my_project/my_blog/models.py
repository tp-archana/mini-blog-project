from django.db import models

# Create your models here.
class PostModel(models.Model):
    heading = models.CharField(max_length=300)
    content = models.TextField()

    def __str__(self):
        return self.heading
    
class Comments(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name='comments')
    author_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"Comment by {self.author_name}"