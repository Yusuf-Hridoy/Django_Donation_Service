from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Profile.decorators import unauthenticatedUser, allowed_users, admin_only
from django.db.models import Sum
# if login then user can view the page

from Donations.models import *
from Profile.models import *
from Track.models import *


def home(request):
    donationList = Donation.objects.all().order_by('firstName')
    projectList = ProjectDonation.objects.all().order_by('projectName')[:3]
    vl = Volunteer.objects.all().order_by('volunteerName')

    context = {
        'donationList': donationList,
        'projectList': projectList,
        'volunteerData': vl,
    }

    return render(request, 'index.html', context)


# @allowed_users(allowed_roles=['admin'])
def about(request):
    volunteer = Volunteer.objects.all().order_by('volunteerName')

    context = {
        'volunteerData': volunteer,
    }

    return render(request, 'mainTemplate/about.html', context)


def contact(request):
    return render(request, 'mainTemplate/contact.html')




def AllProjects(request):

    projectList = ProjectDonation.objects.all().order_by('projectName')

    context = {
        'projectList': projectList,
    }
    return render(request, 'mainTemplate/projects.html',context)

def SingleProjectShow(request, pk):

    projects = ProjectDonation.objects.get(id=pk)

    context= {

        'projectsData': projects
    }
    return render(request, 'mainTemplate/singleproject.html',context)


def Volunteerdata(request):
    volunteer = Volunteer.objects.all().order_by('volunteerName')

    context = {
        'volunteerData': volunteer,
    }

    return render(request, 'mainTemplate/volunteer.html', context)

def TestForm(request):
    return render(request, 'mainTemplate/surveyform.html')

def AdminDashboard(request):
    donorCount = Donor.objects.count()
    projectCount = ProjectDonation.objects.count()
    requestCount = DonationRequest.objects.count()
    donationMoney = Donation.objects.all().aggregate(Sum('donationMoney'))['donationMoney__sum']


    donationData=Donation.objects.all()
    ZakatData=Zakat.objects.all()
    requestData=DonationRequest.objects.all()

    organizationData=Organization.objects.all()
    trackData=TrackDonation.objects.all()

    context={
        'donorCount':donorCount,
        'projectCount':projectCount,
        'requestCount':requestCount,
        'donationMoney':donationMoney,

        'donationData':donationData,
        'ZakatData':ZakatData,
        'requestData':requestData,
        'organizationData':organizationData,
        'trackData':trackData,
    }
    return render(request,'admin/admin.html',context)


