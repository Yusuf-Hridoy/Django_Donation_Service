from django.urls import path
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('signup/',Signup,name='signup'),
     path('signin/',Signin,name='signin'),
     path('logout/',logoutUser,name='logout'),

     path('becomevolunteer/',BecomeVolunteer,name='becomevolunteer'),


     path('dashboard',DonorDashboard,name='dashboard'),
     path('showzakat/', ShowZakat, name='showzakat'),
     path('showdonation/', ShowDonation, name='showdonation'),
     path('showrequest/', ShowRequestZakat, name='showrequest'),

     path('showsinglerequest/<int:pk>', ShowSingleRequest, name='showsinglerequest'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
