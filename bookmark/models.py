from django.db import models
from main.models import Donor

# Create your models here.


class Bookmark(models.Model):
    donor = models.OneToOneField("main.Donor", on_delete=models.CASCADE)
    client = models.ManyToManyField("main.User")

    def __str__(self):
        return self.donor.user.user_name


# def bookmarked_by(self):
#     return ",".join([str(person) for person in self.client.all()])
