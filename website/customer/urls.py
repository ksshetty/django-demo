
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

from customer import views_api

router = DefaultRouter()

router.register(r'customer', views_api.CustomerViewSet)

urlpatterns = [
    url(r'^v0.1/', include(router.urls)),
]