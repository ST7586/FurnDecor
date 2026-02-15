from django.db import models

# Create your models here.
class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
