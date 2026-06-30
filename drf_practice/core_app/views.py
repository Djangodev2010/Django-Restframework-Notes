from django.shortcuts import render
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions, renderers
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

# Create your views here.

class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides retrieve and list commands
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewset(viewsets.ModelViewSet):
    """
    This viewset will provide the default list and retrieve commands,
    along with the custom highlight method
    """
    
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
