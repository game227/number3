from django.urls import path , include
from .views import MamlakatViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mamlakat', MamlakatViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]