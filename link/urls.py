"""link URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenVerifyView

from apps.core.utils import generate_url

schema_view = get_schema_view(
   openapi.Info(
      title="Link API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    generate_url('auth-users/sign-in/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    generate_url('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    generate_url('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    generate_url('auth-users/', include('apps.users.urls'), name='auth-users'),
]
