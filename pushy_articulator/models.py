from django.db import models

class PushyArticle(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def on_save():
        """
        publish to selected external sources
        """
        pass
    
    def auth_google():
        pass
        
    def auth_facebook():
        pass
        
    def auth_twitter():
        pass
        
    def __unicode__(self):
        return self.title
    