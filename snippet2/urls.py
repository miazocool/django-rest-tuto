from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippet2 import views

urlpatterns = [
    path('snippet2/', views.snippet_list),
    path('snippet2/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)