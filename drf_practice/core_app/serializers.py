from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Snippet serializer for serialization and deserialization of the instances
    of our snippet model
    """
    
    # Setting the owner field to ReadOnlyField to only use it for displaying the
    # owner's username and is populated with the owner's username
    owner = serializers.ReadOnlyField(source="owner.username")
    
    class Meta:
        model = Snippet
        fields = [
            'url',
            'id',
            'title',
            'code',
            'language',
            'linenos',
            'style',
            'created_at',
            'owner'
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    UserSerializer for serialization and deserialization of the instances
    of the User model
    """
    
    # The snippets field to display the pk of all the snippets associated with 
    # the user
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
