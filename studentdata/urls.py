from django.conf.urls import url
from studentdata.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='studentdata'),
]
