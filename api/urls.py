from django.urls import include, path
from rest_framework import routers
from api import api_views

router = routers.DefaultRouter()
router.register(r'company', api_views.CompanyViewSet)
router.register(r'category', api_views.CategoryViewSet)
router.register(r'contact', api_views.ContactViewSet)
router.register(r'branch', api_views.BranchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
