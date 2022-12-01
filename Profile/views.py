from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.db.models import Sum
from Track.models import *

# if login then user can view the page
# @login_required(login_url='signup')

from django.contrib.auth import authenticate, login, logout

from Donations.models import Donation, Zakat
from .decorators import allowed_users
from .forms import SignUp, BecomeVolunteerForm
from .models import *
from Donations.models import *


def Signup(request):
    form = SignUp()
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='donor')
            user.groups.add(group)

            Donor.objects.create(

                user=user,
            )
            messages.success(request, f'hi {username} , SignUp is Success')
            return redirect('signin')
    context = {
        'form': form
    }
    return render(request, 'loginTemplate/signup.html', context)


def Signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('admindashboard')
        else:
            messages.info(request, 'User Name is incorrect')
        return redirect('home')
    return render(request, 'loginTemplate/signin.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def BecomeVolunteer(request):
    form = BecomeVolunteerForm()
    if request.method == 'POST':
        form = BecomeVolunteerForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='volunteer')
            user.groups.add(group)

            Volunteer.objects.create(
                user=user,
            )

            messages.success(request, f'hi {user} , SignUp is Success')
            return redirect('signin')
    context = {
        'form': form
    }
    return render(request, 'loginTemplate/signup.html', context)


def ZakatRecipient(request):
    form = SignUp()
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='donor')
            user.groups.add(group)

            Zakatrecipient.objects.create(
                user=user,
            )
            messages.success(request, f'hi {username} , SignUp is Success')
            return redirect('signin')
    context = {
        'form': form
    }
    return render(request, 'loginTemplate/signup.html', context)


# profile data showing part



@login_required(login_url='signin')
# @allowed_users(allowed_roles=['donor'])
def DonorDashboard(request):
    donor = Donor.objects.filter(user_id=request.user.id)
    orgDonation = Donation.objects.filter(user__user_id=request.user.id)
    orgZakat = Zakat.objects.filter(user__user_id=request.user.id)
    sumOrganization, sumProject, zakatOrganization, total = 0.0, 0.0, 0.0, 0.0

    for obj in orgDonation:
        if obj.organizationDonation:
            sumOrganization += obj.donationMoney
        if obj.projectDonation:
            sumProject += obj.donationMoney
    for obj in orgZakat:
        if obj.organization:
            zakatOrganization += obj.zakatAmount
    totalDonation = Donation.objects.filter(user__user_id=request.user.id).aggregate(Sum('donationMoney'))[
        'donationMoney__sum']
    totalZakat = Zakat.objects.filter(user__user_id=request.user.id).aggregate(Sum('zakatAmount'))['zakatAmount__sum']

    total = totalZakat + totalDonation

    availableDonation = total - (sumOrganization + sumProject + zakatOrganization)

    if availableDonation < 0:
        availableDonation = 0

    spentMoney = TrackDonation.objects.filter(donorName__user_id=request.user.id).aggregate(Sum('receiptAmount'))[
        'receiptAmount__sum']
    donationleft = availableDonation - spentMoney


    if donationleft < 0:
        spentMoney = availableDonation
        donationleft = 0

    context = {
        'donor': donor,
        'totalDonation': totalDonation,
        'totalZakat': totalZakat,

        'Total': total,

        'orgDonation': sumOrganization,
        'proDonation': sumProject,
        'orgZakat': zakatOrganization,

        'availableDonation': availableDonation,
        'SpentMoney': spentMoney,
        'Donationleft': donationleft,

    }
    return render(request, 'profile/profilePages/dashboard.html', context)


# @login_required(login_url='signin')
# @allowed_users(allowed_roles=['donor'])
def ShowZakat(request):
    donor = Donor.objects.filter(user__id=request.user.id)
    ZakatData = Zakat.objects.filter(user__user_id=request.user.id)

    context = {

        'zakatdata': ZakatData,
        'donor': donor,
    }
    return render(request, 'profile/profilePages/showzakat.html', context)


def ShowDonation(request):
    donor = Donor.objects.filter(user__id=request.user.id)
    donationData = Donation.objects.filter(user__user_id=request.user.id)

    context = {
        'donationData': donationData,
        'donor': donor,
    }
    return render(request, 'profile/profilePages/showdonation.html', context)


def ShowRequestZakat(request):
    donor = Donor.objects.filter(user__id=request.user.id)
    requestData = DonationRequest.objects.filter(user__user_id=request.user.id)
    # requestData = DonationRequest.objects.filter(donation_request_user_id=request.user.id)

    CONTEXT = {

        'requestData': requestData,
        'donor': donor
    }

    return render(request, 'profile/profilePages/showrequest.html', CONTEXT)


def ShowSingleRequest(request, pk):
    requestData = DonationRequest.objects.get(id=pk)
    context = {
        'SingleRequest': requestData,
    }
    return render(request, 'profile/profilePages/singleZakatRequest.html', context)
