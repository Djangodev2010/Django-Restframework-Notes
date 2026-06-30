from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewset, basename='snippet')
router.register(r'users', views.UserViewset, basename='user')

urlpatterns = [
    path('', include(router.urls))
]

