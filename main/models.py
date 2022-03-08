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
