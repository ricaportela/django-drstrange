from django.contrib import admin
from django.conf.urls import include, url
from .bands.views import home, band_contact, band_detail, band_listing, BandContactForm, BandForm, MemberForm, protected_view, message


urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', home, name='home'),
    url(r'^bands/$', band_listing, name='bands'),
    url(r'^bands/(?P<pk>\d+)/$', band_detail, name='band_detail'),
    url(r'^bandform/$', BandForm.as_view(), name='band_form'),
    url(r'^memberform/$', MemberForm.as_view(), name='member_form'),
    url(r'^contact/$', band_contact, name='contact'),
    url(r'^protected/$', protected_view, name='protected'),
    url(r'^accounts/login/$', message),
]     