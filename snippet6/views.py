from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth.models import User
from snippet6.permissions import IsOwnerOrReadOnly
from snippets.serializers import UserSerializer, SnippetSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from models import Snippet
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#This api_root fundtion can be omitted if we are using
# DefaultRouter in urls.py  

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })