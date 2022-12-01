from django.shortcuts import render, redirect
from Donations.models import *
from .forms import *
from .models import *


from django.contrib.auth.decorators import login_required


# Create your views here.


# @login_required(login_url='signin')
# def DonationRequest(request):
#
#     form = DonationRequestForm
#     if request.method == 'POST':
#         form = DonationRequestForm(request.POST,request.FILES)
#         if form.is_valid():
#             # form.save(commit=False)
#             form.save()
#             return redirect('showrequest')
#         else:
#             form = DonationRequestForm
#
#     context = {
#         'form':form
#     }
#
#     return render(request, "mainTemplate/request.html",context)


def panel(request):
    donation_requests = DonationRequest.objects.all().order_by('requestedAmount')
    projectDonation = ProjectDonation.objects.all().order_by('projectName')

    CONTEXT = {

        'DonationRequest': donation_requests,
        'ProjectDonation': projectDonation
    }
    return render(request, "profile/panel.html", CONTEXT)


@login_required(login_url='signin')
def donation(request):
    form = DonationForm
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.user=Donor.objects.get(user_id=request.user)
            temp.save()
            # return redirect('showdonation')
            return redirect('payment')
        else:
            form = DonationForm()
    context = {
        'form': form
    }
    return render(request, 'zakatTemplate/donationForm.html', context)


@login_required(login_url='signin')
def Zakat(request):
    form = ZakatForm
    if request.method == 'POST':
        form = ZakatForm(request.POST)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.user=Donor.objects.get(user=request.user)
            temp.save()
            # return redirect('showzakat')
            return redirect('payment')
        else:
            form = ZakatForm()
    context = {
        'form':form
    }
    return render(request, 'zakatTemplate/zakatForm.html', context)


def payment (request):
    return render(request,'mainTemplate/payment.html')


@login_required(login_url='signin')
def donationRequest(request):
    form = DonationRequestForm()
    if request.method == 'POST':
        form = DonationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = Donor.objects.get(user=request.user)
            temp.save()
            return redirect('showrequest')
        else:
            form=DonationRequestForm()
    context = {
        'form': form,
    }
    return render(request,"mainTemplate/request.html",context)

























 # firstName = request.POST['firstName'],
 #            lastName = request.POST['lastName'],
 #            address = request.POST['address'],
 #            phone = request.POST['phone'],
 #            donationMoney = request.POST['donationMoney'],
 #            organization = form.cleaned_data['organizationDonation'].id,
 #            project = form.cleaned_data['projectDonation'].id,
 #            user = Donor.objects.get(user_id=request.user.id),
 #
 #            Donation.objects.create(
 #                user_id=user,
 #                firstName=firstName,
 #                lastName=lastName,
 #                address=address,
 #                phone=phone,
 #                donationMoney=donationMoney,
 #                organizationDonation_id=organization,
 #                projectDonation_id=project,
 #            )