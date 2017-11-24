from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.eng_today, name="eng_today"),
]
