from django.db.models import Sum
from django.shortcuts import render
from .models import *
from Profile.decorators import unauthenticatedUser, allowed_users, admin_only



def TrackZakat(request):

    ZakatTrack = TrackDonation.objects.filter(donorName__user_id=request.user.id)
    CONTEXT = {
        'zakatTrack': ZakatTrack,

    }
    return render(request, 'trackTemplate/trackZakat.html', CONTEXT)


def Recipient(request, pk):
    ZakatTrack = TrackDonation.objects.get(id=pk)

    CONTEXT = {
        'zakatTrack': ZakatTrack
    }
    return render(request, 'trackTemplate/recipient.html', CONTEXT)
