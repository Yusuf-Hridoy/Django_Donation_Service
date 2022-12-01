from django.db import models
# Create your models here.
from Profile.models import *
from Donations.models import *

# class TrackZakat(models.Model):
#
#
#     donarName = models.ForeignKey(Donor.donorName, on_delete=models.SET_NULL, null=True)
#
#     OrganizationName = models.ForeignKey(Organization.orgName,on_delete=models.CASCADE, null=True)
#     OrganizationPhone = models.ForeignKey(Organization.orgPhone,on_delete=models.CASCADE, null=True)
#     OrganizationDonationAmount = models.ForeignKey(Donation.organizationDonation,on_delete=models.CASCADE, null=True)
#
#     ProjectName = models.ForeignKey(Donation.firstName,on_delete=models.CASCADE, null=True)
#     ProjectAmount = models.ForeignKey(Donation.donationMoney,on_delete=models.CASCADE, null=True)
#
#     ZakatAmount = models.ForeignKey(Zakat.zakatAmount,on_delete=models.CASCADE, null=True)
#
#     recipientName = models.ForeignKey(Zakatrecipient.recipientName,on_delete=models.CASCADE, null=True)
#     recipientAddress = models.ForeignKey(Zakatrecipient.recipientAddress,on_delete=models.CASCADE, null=True)
#     recipientPhone = models.ForeignKey(Zakatrecipient.recipientPhone,on_delete=models.CASCADE, null=True)

class TrackDonation (models.Model):

    donorName = models.ForeignKey(Donor,max_length=20, on_delete=models.CASCADE,default="")
    recipientName = models.CharField(max_length=20,default="")
    recipientPhone = models.CharField(max_length=11,default="")
    recipientAddress = models.CharField(max_length=200,default="")
    recipientAvatar = models.ImageField(upload_to='recipients/',default="")
    receiptAmount = models.FloatField(null=False,default=None)

    def __str__(self):
        return str(self.recipientName)



