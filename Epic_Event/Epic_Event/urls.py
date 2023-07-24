"""
URL configuration for Epic_Event project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from contrats.views import ClientViewSet, ContratViewSet
from comptes.views import ComptesViewSet, ChangePasswordView
from évènements.views import EventViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register("clients", ClientViewSet, basename="clients")
router.register("comptes", ComptesViewSet, basename="comptes")
router.register("contrats", ContratViewSet, basename="contracts")
router.register("evenements", EventViewSet, basename="events")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/change_password/', ChangePasswordView.as_view(),
         name='change_password'),
    path("api/", include(router.urls)),
]
