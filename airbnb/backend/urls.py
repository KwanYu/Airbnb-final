from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from .views import AirbnbViewSet

router = routers.DefaultRouter()
router.register('airbnb',AirbnbViewSet)

from django.views.generic.base import TemplateView  # 1.

urlpatterns = [
    path('', include(router.urls)),
    # path(r'', TemplateView.as_view(template_name='index.html')),  # 2、
]
