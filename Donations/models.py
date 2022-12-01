from django.contrib.auth.models import User
# from django.db import models
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from Profile.models import *


class ProjectDonation(models.Model):

    projectName = models.CharField(max_length=20)
    projectTargetPrice = models.IntegerField()
    projectDescriptions = models.TextField(blank=False, default=None)
    projectImage = models.ImageField(
        upload_to='media/', null=False, default="")

    def __str__(self):
        return self.projectName


REQUEST_REASONS = (

    ('poor', 'Poor'),
    ('medicalEmergency', 'medical Emergency'),
    ('others', 'Others')
)


class DonationRequest(models.Model):

    user = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True)
    requesterFirstName=models.CharField(max_length=30,default=None,null=True)
    requesterLastName=models.CharField(max_length=30,default=None,null=True)
    requesterAddress=models.TextField(blank=False,default=None,null=True)
    requesterCity=models.TextField(blank=True,default=None,null=True)
    requesterZip=models.CharField(max_length=15,default=None,null=True)
    requesterNID=models.CharField(max_length=15,default=None)
    requestDescription = models.TextField(blank=True, default=None)
    requestReason = models.CharField(choices=REQUEST_REASONS, null=False, max_length=20, default=None)
    requestDocument=models.ImageField(upload_to='Verifications/',default=None,null=True,blank=True)
    requestedAmount = models.IntegerField(default=None, blank=False,)

    def __str__(self):
        return str(self.requesterFirstName)


class Donation(models.Model):

    user = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True)
    firstName = models.CharField(max_length=15, null=False)
    lastName = models.CharField(max_length=15)
    address = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=11, blank=False,)
    donationMoney = models.FloatField(blank=False, null=False)
    organizationDonation = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True,blank=True)
    projectDonation = models.ForeignKey(ProjectDonation, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.firstName


class Zakat(models.Model):
    user = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True)
    firstName = models.CharField(max_length=15, null=False)
    lastName = models.CharField(max_length=15)
    address = models.CharField(max_length=80, null=False)
    phone = models.CharField(max_length=11, blank=False,)
    zakatAmount = models.FloatField(blank=False, null=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.firstName

