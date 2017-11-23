from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lotto_list, name="lotto_list"),
]
