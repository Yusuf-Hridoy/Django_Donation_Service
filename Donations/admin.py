from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Donation)
admin.site.register(DonationRequest)
admin.site.register(ProjectDonation)
admin.site.register(Zakat)

