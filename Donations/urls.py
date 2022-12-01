from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
# from ZakatService.settings import STATIC_ROOT,STATIC_URL,MEDIA_ROOT,MEDIA_URL,DEBUG

urlpatterns = [
    path('panel/', panel, name='panel'),


    path('zakat', Zakat, name='zakat'),
    path('donationRequest/', donationRequest, name='donationRequest'),
    path('donation/', donation, name='donation'),

    path('payment/', payment, name='payment'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)