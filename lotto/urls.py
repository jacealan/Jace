from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lotto', views.lotto_list, name="lotto_list"),
]
