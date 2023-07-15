# api/urls.py
from django.urls import path, include
from rest_framework import routers

from api import views
from api.views import index

router = routers.DefaultRouter()
router.register(r'benefits', views.BenefitViewSet)
router.register(r'menu', views.MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('time', index)
]
