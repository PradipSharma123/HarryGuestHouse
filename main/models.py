from distutils.command.upload import upload
from django.db import models

# from django's db package importing models module

# Model class stores, read and delete the database which is already
# configured in Model class so Service class inherit the common characterstics
# that belongs to Model class


class Service(models.Model):
    Service_icon = models.CharField(max_length=25)
    Service_name = models.CharField(max_length=100)
    Service_desc = models.TextField()

    def __str__(self) -> str:
        return self.Service_name


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=False, blank=False)
    topic = models.CharField(max_length=30, default='Add topic here')

    def __str__(self) -> str:
        return self.topic


# class Contact(models.Model):
#     Contact_name = models.CharField(max_length=100)
#     Contact_email = models.CharField(max_length=100)
#     Contact_message = models.TextField()
