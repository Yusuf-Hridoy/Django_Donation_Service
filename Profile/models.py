from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

GENDER_OPTIONS = (

    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others')
)


class Donor(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    donorName = models.CharField(max_length=20,null=True)
    donorGender = models.CharField(choices=GENDER_OPTIONS, max_length=20,null=True)
    donorPhone = models.IntegerField(blank=False,null=True)
    donorEmail = models.EmailField(blank=False,null=True)
    donorAddress = models.TextField(default=None,null=True)
    donorAvatar = models.ImageField(upload_to='donor',null=True)

    def __str__(self):
        return str(self.user)


class Volunteer(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    volunteerName = models.CharField(max_length=20, blank=False)
    volunteerGender = models.CharField(choices=GENDER_OPTIONS, null=True, max_length=20)
    volunteerPhone = models.IntegerField(blank=False)
    volunteerEmail = models.EmailField(blank=False)
    volunteerAddress = models.TextField(blank=False, default=None)
    volunteerImage = models.ImageField(upload_to='volunteers')

    def __str__(self):
        return str(self.user)


class Organization(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    orgName = models.CharField(blank=False, max_length=40)
    orgOwnerName = models.CharField(blank=False, max_length=20)
    orgPhone = models.CharField(blank=False, max_length=11)
    orgEmail = models.EmailField(blank=False)
    orgAddress = models.TextField(blank=False, default=None)
    orgDescription = models.TextField(default="")
    orgDocument = models.ImageField(upload_to='Verifications')

    def __str__(self):
        return str(self.user)


class Zakatrecipient(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    recipientName = models.CharField(max_length=20,null=True)
    recipientGender = models.CharField(choices=GENDER_OPTIONS, max_length=20,null=True)
    recipientPhone = models.IntegerField(blank=False,null=True)
    recipientEmail = models.EmailField(blank=False,null=True)
    recipientAddress = models.TextField(default=None,null=True)
    recipientAvatar = models.ImageField(upload_to='donor',null=True)

    def __str__(self):
        return str(self.user)