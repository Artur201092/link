
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^sign-up/', views.SignUpAPIView.as_view(), name='sign-up'),
]
