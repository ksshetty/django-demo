from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from listing import views_api

router = DefaultRouter()

router.register(r'listing', views_api.ListingViewSet)

urlpatterns = [
    url(r'^v0.1/', include(router.urls)),
]