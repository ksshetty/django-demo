from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from work_request import views_api

router = DefaultRouter()

router.register(r'work_request', views_api.WorkRequesViewSet)

urlpatterns = [
    url(r'^v0.1/', include(router.urls)),
]