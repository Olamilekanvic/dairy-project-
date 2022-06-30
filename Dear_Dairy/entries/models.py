from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=False)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.text)

    class Meta:
        verbose_name_plural = 'entries'
    
    
#Entry.objects.filter(author=user.user)