from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from vendor import views_api

router = DefaultRouter()

router.register(r'vendor', views_api.VendorViewSet)

urlpatterns = [
    url(r'^v0.1/', include(router.urls)),
]