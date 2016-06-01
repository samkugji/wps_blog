from django.db  import models


class Post(models.Model):

    title = models.CharField(
        max_length=120,
    )
    
    content = models.TextField()

    def __str__():
        return self.title

class NaverPost(models.Model):

    title = models.CharField(
        max_length=120,
    )
    
    thumbnail_image_url =  models.URLField()
    original_url = models.URLField()
    content = models.TextField()

    def __str__():
        return self.title
